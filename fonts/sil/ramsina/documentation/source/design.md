---
title: Ramsina - Design
fontversion: 2.000
---

Ramsina is a font family for the East Syriac script. The font was designed as a revival, or facsimile, of metal type cut in India from around 1920. This font was initially designed by Esho Marcus and named East Syriac Marcus. The font is used according to the terms of the [SIL Open Font License](https://openfontlicense.org/). The Latin letters are a subset of the [Crimson Pro](https://github.com/Fonthausen/CrimsonPro) font.

One font from this typeface family is included in the *Ramsina* release:

* Ramsina Regular

## Type Samples

Type samples showing some of the inventory of glyphs can be found here: 
[Ramsina Type Sample](sample.md).

![Ramsina Sample - Genesis 11](../assets/images/RamsinaGen11.png){.fullsize}
<figcaption>Ramsina Sample - Genesis 11</figcaption>

## Character Set

For a complete list of characters included in this font, see [Character Set Support](charset.md).

## Font Features

Alternate glyphs that are available through features are demonstrated in the [Features](features.md) document. 

## Alaph shape

The shape of U+0710 SYRIAC LETTER ALAPH varies, depending on context, the character that precedes it, and whether it has a diacritic or not. These are conventions, and there is no documented hard rules of how the shape is rendered. This font follows the _Khudra_ (the most widely used Syriac book in the church) convention.

![Alaph rules](../assets/images/alaph-rules.png){.fullsize}
<figcaption>Alaph rules</figcaption>

1. 0715 SYRIAC LETTER DALATH followed by 0710 SYRIAC LETTER ALAPH or 072A SYRIAC LETTER RISH followed by 0710 SYRIAC LETTER ALAPH
Obligatory: 0710 is rendered as Glyph 1 
2. 0720 SYRIAC LETTER LAMADH followed by 0710 SYRIAC LETTER ALAPH and they end the word, then 0710 is rendered as Glyph 3. It can be a ligature with connecting and non-connecting form and be used universally. Glyph 3 is only used with 0720
3. All other contexts of 0710, follow the general rule of shaping, i.e. initial, middle, and end forms. 

SIL Global is the creator of the Ramsina fonts, and is the owner of all proprietary rights therein.

*Ramsina* is a trademark of SIL Global.
