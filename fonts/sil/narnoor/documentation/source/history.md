---
title: Narnoor - Version History
fontversion: 2.000
---

### 21 Feb 2023 (SIL International) Narnoor font version 2.000
- Redraw all Gunjala Gondi glyphs
- Resolve Font Bakery issues
- Remove Graphite shaping
- Improve OpenType shaping
- Improve Gunjala Gondi glyphs
- Replaced Latin characters with Source Sans Regular at 100%
- Some geometric characters (U+2423, U+F130, U+F131) are from Andika Regular at 90%

### 01 Oct 2019 (SIL International) Narnoor font version 1.000
- An extra attachment point class caused builds to be be non-deterministic,
  so that attachment point class is now excluded from the font build.

### 06 Jun 2019 (SIL International) Narnoor font version 0.100
- Added OpenType font smarts
- Extra Latin glyphs (mostly outside of ASCII) are from
  Charis SIL (https://software.sil.org/charis/) scaled 110%
- Fix test data and font to remove codepoints from
  - PUA
  - outside the Gunjala Gondi block
  - unassigned with the the Gunjala Gondi block
- Rename glyphs and encode correctly (hopefully)
- Convert glyphs to Postscript curves
- Added test data, build system, and Graphite font smarts
- Updated licensing for SIL additions and modifications

### 04 Apr 2017 (S. Sridhar Murthy) GunjalaGondi font version 1.002
- Initial release
