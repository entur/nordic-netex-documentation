"""Regression checks for the example-driven table generator (no network or XSD downloads)."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS
from rdflib.namespace import SH, XSD
from scripts import generate_tables as g


class GeneratorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def example(self, folder, body):
        folder.mkdir(parents=True, exist_ok=True)
        p = folder / 'Example_Test.xml'
        p.write_text('<PublicationDelivery xmlns="http://www.netex.org.uk/netex" xmlns:gml="http://www.opengis.net/gml/3.2">' + body + '</PublicationDelivery>', encoding='utf-8')
        return p

    def shape(self, graph, cls, path, rng=None, mn=None, mx=None, description=None):
        shape, prop = BNode(), BNode()
        graph.add((shape, SH.targetClass, cls))
        graph.add((shape, SH.property, prop))
        graph.add((prop, SH.path, path))
        if rng is not None:
            graph.add((prop, SH['class'], rng))
        if mn is not None:
            graph.add((prop, SH.minCount, Literal(mn)))
        if mx is not None:
            graph.add((prop, SH.maxCount, Literal(mx)))
        if description is not None:
            graph.add((prop, SH.description, Literal(description)))
        return prop

    def run_main(self, docs, args, ont=None):
        output = io.StringIO()
        with patch.object(g, 'REPO_ROOT', self.root), patch.object(g, 'documented_classes', return_value=docs), patch.object(g, 'load_ontology', return_value=ont or g.Ontology(base=Graph())), patch('sys.argv', ['generate_tables.py', *args]), contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            code = g.main()
        return code, output.getvalue()

    def test_shared_annotations_cannot_override_class_range(self):
        graph = Graph()
        self.shape(graph, g.NETEX.Block, g.NETEX.journeys, g.NETEX.journeyRefs_RelStructure, mx=1)
        self.shape(graph, g.NETEX.OtherOwner, g.NETEX.journeys, g.NETEX.otherRefs_RelStructure, mx=1)
        graph.add((g.NETEX.journeys, g.NETEX.xsdType, Literal('WrongGlobalType')))
        graph.add((g.NETEX.journeys, RDFS.comment, Literal('Comment about the other owner')))
        shapes = g.scoped_base_shapes(graph)
        info = shapes[g.NETEX.Block]['journeys']
        self.assertEqual('journeyRefs_RelStructure', info.type)
        self.assertIsNone(info.comment)
        self.assertEqual('otherRefs_RelStructure', shapes[g.NETEX.OtherOwner]['journeys'].type)

    def test_local_description_is_authoritative_for_shared_property(self):
        graph = Graph()
        self.shape(graph, g.NETEX.Block, g.NETEX.journeys, g.NETEX.journeyRefs_RelStructure, description='Journeys belonging to this block')
        self.shape(graph, g.NETEX.OtherOwner, g.NETEX.journeys, g.NETEX.otherRefs_RelStructure)
        graph.add((g.NETEX.journeys, RDFS.comment, Literal('Unrelated global text')))
        self.assertEqual('Journeys belonging to this block', g.scoped_base_shapes(graph)[g.NETEX.Block]['journeys'].comment)

    def test_choice_member_is_optional_not_the_collection_requirement(self):
        graph = Graph()
        self.shape(graph, g.NETEX.Block, g.NETEX.journeys, g.NETEX.JourneyCollection, mx=1)
        self.shape(graph, g.NETEX.JourneyCollection, g.NETEX.journeyRef, g.NETEX.Journey)
        self.shape(graph, g.NETEX.JourneyCollection, g.NETEX.journeyDesignator, g.NETEX.JourneyDesignatorStructure)
        graph.add((g.NETEX.journeyRef, g.NETEX.isReference, Literal(True)))
        graph.add((g.NETEX.journeyRef, g.NETEX.xsdType, Literal('JourneyRefStructure')))
        ont = g.Ontology(base=graph, base_shapes=g.scoped_base_shapes(graph))
        self.assertEqual('0..n', g.resolve('Block', 'entur', 'journeys/JourneyRef/@ref', ont)[0])
        # No XML substitution mapping is present: do not infer a requirement
        # for VehicleJourneyRef from the observed example or a generic JourneyRef.
        self.assertEqual('?', g.resolve('Block', 'entur', 'journeys/VehicleJourneyRef/@ref', ont)[0])

    def test_inherited_metadata_keeps_the_declaring_class_context(self):
        graph = Graph()
        graph.add((g.NETEX.TrainBlock, RDFS.subClassOf, g.NETEX.TrainBlock_VersionStructure))
        graph.add((g.NETEX.TrainBlock_VersionStructure, RDFS.subClassOf, g.NETEX.Block_VersionStructure))
        self.shape(graph, g.NETEX.Block_VersionStructure, g.NETEX.journeys, g.NETEX.journeyRefs_RelStructure, mx=1)
        ont = g.Ontology(base=graph, base_shapes=g.scoped_base_shapes(graph))
        self.assertEqual(g.NETEX.journeyRefs_RelStructure, g.base_lookup(ont, 'TrainBlock', ['journeys']).range)

    def test_profile_mapping_controls_xml_type_even_when_folder_differs(self):
        folder = self.root / 'objects' / 'FriendlyName'
        self.example(folder, '<ServiceJourneyInterchange id="NP:ServiceJourneyInterchange:1" version="1"><Guaranteed>true</Guaranteed></ServiceJourneyInterchange>')
        index = self.root / 'index.ttl'
        index.write_text('@prefix doc: <https://netex-cen.eu/doc#> . <https://netex-cen.eu/nordic#FriendlyName> doc:table "objects/FriendlyName/Table_FriendlyName.md" .', encoding='utf-8')
        profile = self.root / 'profile'
        profile.mkdir()
        (profile / 'profile.ttl').write_text('@prefix profile: <https://netex-cen.eu/profile#> . <https://netex-cen.eu/nordic#FriendlyName> profile:onClass <https://netex-cen.eu/ontology#ServiceJourneyInterchange> .', encoding='utf-8')
        with patch.object(g, 'REPO_ROOT', self.root), patch.object(g, 'DOC_TTL', index), patch.object(g, 'NORDIC_DIR', profile), patch.object(g, 'ENTUR_DIR', self.root / 'absent'):
            docs = g.documented_classes()
        self.assertEqual('ServiceJourneyInterchange', docs['FriendlyName'].target)
        self.assertIn('Guaranteed', g.collect('FriendlyName', docs).nodes)

    def test_missing_explicit_mapping_is_an_error_not_a_folder_guess(self):
        index = self.root / 'index.ttl'
        index.write_text('@prefix doc: <https://netex-cen.eu/doc#> . <urn:unknown> doc:table "objects/Friendly/Table_Friendly.md" .', encoding='utf-8')
        with patch.object(g, 'REPO_ROOT', self.root), patch.object(g, 'DOC_TTL', index), patch.object(g, 'NORDIC_DIR', self.root / 'absent'), patch.object(g, 'ENTUR_DIR', self.root / 'absent'):
            with self.assertRaisesRegex(ValueError, 'explicit'):
                g.documented_classes()

    def test_gml_prefix_is_retained(self):
        folder = self.root / 'geometry'
        self.example(folder, '<LinkSequenceProjection id="NP:LinkSequenceProjection:1"><gml:LineString srsName="EPSG:4326"><gml:posList>1 2 3 4</gml:posList></gml:LineString></LinkSequenceProjection>')
        rows = g.collect('Geometry', {'Geometry': g.Documentation('nordic', folder, 'LinkSequenceProjection')})
        self.assertIn('gml:LineString/@srsName', rows.nodes)
        self.assertIn('gml:LineString/gml:posList', rows.nodes)

    def test_preflight_prevents_partial_writes_for_empty_or_mismatched_examples(self):
        good = self.root / 'good'
        self.example(good, '<Good id="NP:Good:1"><Name>Good</Name></Good>')
        good_table = good / 'Table_Good.md'
        good_table.write_text('original good table', encoding='utf-8')
        bad = self.root / 'bad'
        bad.mkdir()
        bad_table = bad / 'Table_Bad.md'
        bad_table.write_text('original bad table', encoding='utf-8')
        docs = {'Good': g.Documentation('nordic', good, 'Good'), 'Bad': g.Documentation('nordic', bad, 'Bad')}
        for mismatched in [False, True]:
            with self.subTest(mismatched=mismatched):
                if mismatched:
                    self.example(bad, '<Different id="NP:Different:1"/>')
                code, output = self.run_main(docs, ['Good', 'Bad'])
                self.assertEqual(2, code)
                self.assertIn('refusing', output)
                self.assertEqual('original good table', good_table.read_text())
                self.assertEqual('original bad table', bad_table.read_text())

    def test_description_failure_does_not_write_prepared_table(self):
        folder = self.root / 'good'
        self.example(folder, '<Good id="NP:Good:1"/>')
        table, desc = folder / 'Table_Good.md', folder / 'Description_Good.md'
        table.write_text('original table', encoding='utf-8')
        desc.write_text('No structure section here', encoding='utf-8')
        code, _ = self.run_main({'Good': g.Documentation('nordic', folder, 'Good')}, ['Good'])
        self.assertEqual(2, code)
        self.assertEqual('original table', table.read_text())
        self.assertEqual('No structure section here', desc.read_text())

    def test_generation_is_idempotent_and_check_does_not_write(self):
        folder = self.root / 'good'
        xml = self.example(folder, '<Good id="NP:Good:1" version="1"><Name>Example</Name></Good>')
        docs = {'Good': g.Documentation('nordic', folder, 'Good')}
        code, _ = self.run_main(docs, ['Good', '--check'])
        self.assertEqual(1, code)
        self.assertFalse((folder / 'Table_Good.md').exists())
        self.assertEqual(0, self.run_main(docs, ['Good'])[0])
        snapshot = {p: p.read_bytes() for p in folder.iterdir()}
        self.assertEqual(0, self.run_main(docs, ['Good', '--check'])[0])
        self.assertEqual(0, self.run_main(docs, ['Good'])[0])
        self.assertEqual(snapshot, {p: p.read_bytes() for p in folder.iterdir()})

    def test_unprofiled_documentation_requires_an_explicit_target(self):
        index = self.root / 'index.ttl'
        index.write_text('@prefix doc: <https://netex-cen.eu/doc#> . <urn:unprofiled> doc:table "objects/Friendly/Table_Friendly.md" ; doc:forClass <https://netex-cen.eu/ontology#Organisation> .', encoding='utf-8')
        with patch.object(g, 'REPO_ROOT', self.root), patch.object(g, 'DOC_TTL', index), patch.object(g, 'NORDIC_DIR', self.root / 'absent'), patch.object(g, 'ENTUR_DIR', self.root / 'absent'):
            docs = g.documented_classes()
        self.assertEqual('Organisation', docs['Friendly'].target)

    def test_coverage_can_audit_empty_class_without_overwriting_it(self):
        folder = self.root / 'Empty'
        folder.mkdir()
        table = folder / 'Table_Empty.md'
        table.write_text('Retain existing documentation', encoding='utf-8')
        docs = {'Empty': g.Documentation('nordic', folder, 'Empty')}
        code, output = self.run_main(docs, ['Empty', '--coverage'])
        self.assertEqual(0, code)
        self.assertIn('generation would fail', output)
        self.assertEqual('Retain existing documentation', table.read_text())
        self.assertEqual(2, self.run_main(docs, ['Empty', '--check'])[0])
        self.assertEqual('Retain existing documentation', table.read_text())

    def test_coverage_without_class_arguments_audits_every_documented_folder(self):
        folder = self.root / 'OtherClass'
        folder.mkdir()
        docs = {'OtherClass': g.Documentation('nordic', folder, 'OtherClass')}
        code, output = self.run_main(docs, ['--coverage'])
        self.assertEqual(0, code)
        self.assertIn('OtherClass', output)
        self.assertNotIn('ServiceJourney', output)

    def test_other_xml_namespace_is_not_a_netex_object(self):
        folder = self.root / 'Good'
        self.example(folder, '<external:Good xmlns:external="urn:unrelated" id="other:Good:1"/>')
        docs = {'Good': g.Documentation('nordic', folder, 'Good')}
        code, output = self.run_main(docs, ['Good'])
        self.assertEqual(2, code)
        self.assertIn('no Good instances', output)
        self.assertFalse((folder / 'Table_Good.md').exists())

    def test_structure_update_preserves_prose_and_provenance(self):
        before = '# Example\n\n## 2. Structure Overview\n\n```text\nold\n```\n\n## 3. Explanation\n\nKeep this prose.\n\n| Observed | example.xml |\n'
        block = g.TREE_START + '\n```text\nnew\n```\n' + g.TREE_END
        updated = g.with_description_tree(before, block)
        self.assertEqual(before.split('## 3.')[1], updated.split('## 3.')[1])
        self.assertIn('new', updated)
        self.assertEqual(updated, g.with_description_tree(updated, block))
        with self.assertRaises(ValueError):
            g.with_description_tree(g.TREE_START + '\nmissing end marker', block)


if __name__ == '__main__':
    unittest.main()
