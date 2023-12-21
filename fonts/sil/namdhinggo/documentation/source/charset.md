---
title: Namdhinggo - Character Set Support
fontversion: 3.100
---

Namdhinggo supports the Limbu script, the double danda from Devanagari, and a basic set of Latin characters.
Inclusion of a basic Latin repertoire is provided as a convenience, e.g., for use in menus or for displaying markup in text files.
These fonts are not intended for extensive Latin script use.

## Supported characters

The following character ranges are supported by this font:

Unicode block | Namdhinggo support
------------- | ------------------
Basic Latin|U+0020..U+007E
Latin 1 Supplement|U+00A0..U+00FF
Latin Extended A|U+0131, U+0152..U+0153, U+0160..U+0161, U+0178, U+017D..U+017E
Latin Extended B|U+0192
Spacing Modifier Letters|U+02C6..U+02C7, U+02D0, U+02D8..U+02DD
Combining Diacritical Marks|U+034F
Greek And Coptic|U+03A9, U+03C0
Devanagari|U+0964..U+0965
Limbu|U+1900..U+191E, U+1920..U+192B, U+1930..U+193B, U+1940, U+1944..U+194F
General Punctuation|U+2000..U+200D, U+2010..U+2015, U+2018..U+201A, U+201C..U+201E, U+2020..U+2022, U+2026..U+2029, U+202F..U+2030, U+2039..U+203A, U+2044, U+2060
Superscripts And Subscripts|U+2074
Currency Symbols|U+20A8, U+20AC, U+20B9
Letterlike Symbols|U+2122, U+2126
Mathematical Operators|U+2202, U+2206, U+220F, U+2211..U+2212, U+2215, U+2219..U+221A, U+221E, U+222B, U+2248, U+2260, U+2264..U+2265
Control Pictures|U+2423
Geometric Shapes|U+25CA, U+25CC
Private Use Area|U+F130..U+F131
Alphabetic Presentation Forms|U+FB01..U+FB02
Variation Selectors|U+FE00..U+FE0F
Arabic Presentation Forms B|U+FEFF
Specials|U+FFFC..U+FFFD

The Devanagari "bit" is set in this font to prevent unwarranted font switching when U+0965 DEVANAGARI DOUBLE DANDA or U+0964 DEVANAGARI DANDA is used.
However, U+0964 and U+0965 are the only characters from the Devanagari block in this font.
