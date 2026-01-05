---
title: Idiqlat - Design
fontversion: 2.000
---

The Idiqlat font supports the East Syriac style of the Syriac script. The original font on which Idiqlat was based was an [OFL](https://openfontlicense.org/)-licensed typeface called **East Syriac Marcus**, designed as a revival of metal type. However, significant design changes have been made in order to modernize and opitimize the font for web and mobile use. Additionally, the font has been resized in order to match standard point sizes in modern fonts. It also includes other weights. The Latin letters are a subset of the [Crimson Pro](https://github.com/Fonthausen/CrimsonPro) font.

Three fonts from this typeface family are included in the *Idiqlat* release:

* Idiqlat ExtraLight
* Idiqlat Light
* Idiqlat Regular

## Type Samples

Type samples showing some of the inventory of glyphs can be found here: 
[Idiqlat Type Sample](sample.md).

Examples of some text is shown below. 

![Idiqlat Sample - Three weights](../assets/images/three-weights.png){.fullsize}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/idiqlat/wp-content/uploads/sites/76/2025/12/three-weights.png -->
<figcaption>Idiqlat Sample - Three weights</figcaption>

![Idiqlat Sample - Genesis 11](../assets/images/IdiqlatGen11.png){.fullsize}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/idiqlat/wp-content/uploads/sites/76/2025/12/IdiqlatGen11.png -->
<figcaption>Idiqlat Sample - Genesis 11</figcaption>

## Character Set

For a complete list of characters included in this font, see [Character Set Support](charset.md).

## Font Features

Alternate glyphs that are available through features are demonstrated in the [Features](features.md) document. 

## Alaph shape

The shape of U+0710 SYRIAC LETTER ALAPH varies, depending on context, the character that precedes it, and whether it has a diacritic or not. These are conventions, and there is no documented hard rules of how the shape is rendered. This font follows the _Khudra_ (the most widely used Syriac book in the church) convention.

![Alaph rules](../assets/images/alaph-rules.png){.fullsize}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/idiqlat/wp-content/uploads/sites/76/2025/12/alaph-rules.png -->
<figcaption>Alaph rules</figcaption>

1. 0715 SYRIAC LETTER DALATH followed by 0710 SYRIAC LETTER ALAPH or 072A SYRIAC LETTER RISH followed by 0710 SYRIAC LETTER ALAPH
Obligatory: 0710 is rendered as Glyph 1 
2. 0720 SYRIAC LETTER LAMADH followed by 0710 SYRIAC LETTER ALAPH and they end the word, then 0710 is rendered as Glyph 3. It can be a ligature with connecting and non-connecting form and be used universally. Glyph 3 is only used with 0720
3. All other contexts of 0710, follow the general rule of shaping, i.e. initial, middle, and end forms. 

SIL Global is the creator of the Idiqlat fonts, and is the owner of all proprietary rights therein.

*Idiqlat* is a trademark of SIL Global.
