# PublicationDelivery

> *→ [Glossary definition](../../guides/Glossary/Glossary.md#publicationdelivery)*

## 1. Purpose

A **PublicationDelivery** is the root element of every NeTEx XML document. It is the envelope around the data: it says when the data was published and by whom, and wraps the frames in `dataObjects`. It is not a frame itself and has no `@id`, but every frame in a delivery sits inside it.

## 2. Structure Overview

<!-- generated:structure:start -->
```text
📄 @version (?)
📄 PublicationTimestamp (1..1)
📄 ParticipantRef (1..1)
📄 Description (0..1)
📁 dataObjects (0..1)
   └── 📄 CompositeFrame (?)
```
<!-- generated:structure:end -->

## 3. Contained Elements

- **@version** – Version of the NeTEx schema the document follows, e.g. `2.0`. It is not an object version.
- **PublicationTimestamp** – Date and time the delivery was produced, as an `xsd:dateTime`.
- **ParticipantRef** – Short identifier for the publishing system or organisation. It is free text and not checked against any register; see [ParticipantRef Convention](../../guides/NeTExConventions/NeTEx_Conventions.md#7-participantref-convention).
- **Description** – Optional human-readable description of what the delivery contains.
- **dataObjects** – Container for the data, normally one [CompositeFrame](../CompositeFrame/Table_CompositeFrame.md) that holds the other frames.

## 4. Frame Relationships

PublicationDelivery is the outermost element. It contains `dataObjects`, which in the Nordic Profile holds a [CompositeFrame](../CompositeFrame/Description_CompositeFrame.md); the CompositeFrame in turn holds ResourceFrame, SiteFrame, ServiceFrame, TimetableFrame and the other frames. Nothing references a PublicationDelivery, and no frame depends on its content.

For the full structural specification, see [Table — PublicationDelivery](Table_PublicationDelivery.md).
Example XML: [Example_PublicationDelivery_Constructed.xml](Example_PublicationDelivery_Constructed.xml)

## 5. Usage Notes

- **Header order is fixed by the XSD.** `PublicationTimestamp` comes before `ParticipantRef`, and both come before `Description` and `dataObjects`. A different order fails schema validation.
- **@version is the schema version, not the data version.** Object versions live on each object's own `@version`.
- **The Nordic Profile lists only the header fields.** The profile names `PublicationTimestamp` and `ParticipantRef`. The XSD also allows `PublicationRequest` and `PublicationRefreshInterval`, which the profile does not mention and the examples here do not use.

### Example provenance

**Observed** examples are abbreviated, anonymized extracts from real deliveries. **Constructed** examples are hand-written to illustrate NeTEx 2.0 syntax; they do not establish real-world usage or Nordic Profile requirements. Older examples remain **Not assessed**.

| Status | Example |
|--------|---------|
| **Constructed** | [Example_PublicationDelivery_Constructed.xml](Example_PublicationDelivery_Constructed.xml) |
| Not assessed | [Example_PublicationDelivery.xml](../Example_PublicationDelivery.xml) |
