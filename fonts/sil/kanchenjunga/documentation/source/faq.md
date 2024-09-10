---
title: Kanchenjunga - Frequently Asked Questions
fontversion: 2.000
---

Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](https://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [The SIL Open Font License (OFL-FAQ)](https://openfontlicense.org/ofl-faq/)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.


#### *Where does the name Kanchenjunga come from?*

Kanchenjunga is the world’s third highest mountain, situated on the border between Sikkim state in northeast India and eastern Nepal. Etymology of this name is found in Britannica: The name Kanchenjunga is derived from four words of Tibetan origin, usually rendered Kang-chen-dzo-nga or Yang-chhen-dzö-nga and interpreted in Sikkim as the “Five Treasuries of the Great Snow.” This peak represents the geographical distribution of the Bantawa language quite well.

#### *How is this font different from v1.000 which was released before it was officially in the Unicode Standard?*

The Kirat Rai script was officially encoded in the Unicode Standard version 17.0. Kanchenjunga version 1.000 was released in 2023 with provisional codepoints. However, those codepoints did not change, so if you used Kanchenjunga version 1.000, no data conversion will be necessary. The only difference is that the font now includes a Medium and SemiBold weight in addition to the Regular and Bold that were released with version 1.000.

#### *I would like to use the variants defined in Character Variants. How do I type these using the Kanchenjunga font? How do I use these variants?*

Type the character the same way you would type its standard form (see "Keyboarding and character set support" in [Resources](resources.md) for a keyboard). Then select the variants to be displayed. If your application supports the OpenType Character Variant features, you can use these to access the font features built into the font. See [Font Features](features.md) page for more details.

If your application does not support the OpenType Character Variants, you can use TypeTunerWeb to customize the font with the variants you require. See [Font Features](features.md) page for more details. 

#### *I used a Kirat Rai font which was custom encoded. How can I convert my data from the custom encoding to Unicode?*

Data which was created with the a custom encoded font will not be automatically converted to Unicode by switching fonts. The data must be converted to Unicode using a data conversion routine. See "Text conversion" in [Resources](resources.md) for information on converting your data.

#### *I have text in Bantawa using the Devanagari script. How can I convert my data from Devanagari to Kirat Rai?*

A TECKit converter to convert text from Devanagari script to Kirat Rai is available. See "Text conversion" in [Resources](resources.md) for information on converting your data.
