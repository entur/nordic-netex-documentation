/**
 * docsify-glossary-tooltip.js
 * Parses the Glossary page and adds hover tooltips on first occurrence of each term.
 */
(function () {
  var GLOSSARY_PATH = 'Guides/Glossary/Glossary.md';
  var glossaryTerms = {};

  function parseGlossary(markdown) {
    var terms = {};
    var sections = markdown.split(/^## /m);
    sections.shift(); // remove content before first ##

    sections.forEach(function (section) {
      var lines = section.trim().split('\n');
      var term = lines[0].trim();
      if (!term) return;

      // Grab the first non-empty paragraph as definition
      var def = '';
      for (var i = 1; i < lines.length; i++) {
        var line = lines[i].trim();
        if (line === '' || line === '---') continue;
        if (line.startsWith('>') || line.startsWith('→')) continue;
        if (line) {
          def = line;
          break;
        }
      }
      if (def) {
        terms[term] = def;
      }
    });
    return terms;
  }

  function escapeRegExp(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function addTooltips(html, terms) {
    var used = {};
    var sortedTerms = Object.keys(terms).sort(function (a, b) {
      return b.length - a.length; // longest first
    });

    // Process one term at a time, re-splitting HTML each time so we never
    // match inside attributes of previously inserted tooltip spans.
    sortedTerms.forEach(function (term) {
      if (used[term]) return;
      var re = new RegExp('\\b(' + escapeRegExp(term) + ')\\b');
      var tooltip = terms[term].replace(/"/g, '&quot;');
      var found = false;
      html = html.replace(/([^<]+)|(<[^>]+>)/g, function (match, text, tag) {
        if (tag || found) return match;
        if (re.test(text)) {
          found = true;
          return text.replace(re,
            '<span class="glossary-tooltip" data-tooltip="' + tooltip + '">$1</span>'
          );
        }
        return match;
      });
      if (found) used[term] = true;
    });

    return html;
  }

  // Start fetching immediately so it's ready as soon as possible
  var glossaryReady = fetch(GLOSSARY_PATH)
    .then(function (res) { return res.ok ? res.text() : ''; })
    .then(function (md) {
      glossaryTerms = parseGlossary(md);
    })
    .catch(function () {});

  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = (window.$docsify.plugins || []).concat(function (hook, vm) {
    // Use async afterEach (with next callback) to wait for glossary fetch
    hook.afterEach(function (html, next) {
      glossaryReady.then(function () {
        if (Object.keys(glossaryTerms).length === 0) { next(html); return; }
        if (vm.route.path && vm.route.path.indexOf('Glossary') !== -1) { next(html); return; }
        next(addTooltips(html, glossaryTerms));
      });
    });
  });

  // Minimal tooltip CSS
  var style = document.createElement('style');
  style.textContent = [
    '.glossary-tooltip {',
    '  border-bottom: 1px dotted rgba(150,150,150,0.5);',
    '  cursor: help;',
    '  position: relative;',
    '}',
    '.glossary-tooltip:hover::after {',
    '  content: attr(data-tooltip);',
    '  position: absolute;',
    '  bottom: 100%;',
    '  left: 0;',
    '  background: #1a1a2e;',
    '  color: #e0e0e0;',
    '  padding: 6px 10px;',
    '  border-radius: 4px;',
    '  font-size: 13px;',
    '  max-width: 320px;',
    '  white-space: normal;',
    '  z-index: 1000;',
    '  box-shadow: 0 2px 8px rgba(0,0,0,0.3);',
    '}'
  ].join('\n');
  document.head.appendChild(style);
})();
