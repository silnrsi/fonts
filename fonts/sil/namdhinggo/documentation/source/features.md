---
title: Namdhinggo - Font Features
fontversion: 3.200
---

Namdhinggo is a Unicode font for the Limbu writing system of Nepal. It includes a number of optional features that may be useful or required for particular uses. This document lists all the available features.

These OpenType features are specified using four-letter tags (e.g. 'ss18'). For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features).

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Namdhinggo as a web font see [Namdhinggo Webfont Example](../web/Namdhinggo-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Complete feature list

### Stylistic alternates

#### Special Hyphenation <a id="ss18"></a>

<span class='affects'>Affects: U+002D</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
Default | <span class='namdhinggo-R normal'>-</span> | `ss18=0`
Special Hyphenation | <span class='namdhinggo-R normal' style='font-feature-settings: "ss18" 1'>-</span> | `ss18=1`

#### Latin to Limbu Digits <a id="ss19"></a>

<span class='affects'>Affects: U+0030 U+0031 U+0032 U+0033 U+0034 U+0035 U+0036 U+0037 U+0038 U+0039</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
Default | <span class='namdhinggo-R normal'>0 1 2 3 4 5 6 7 8 9</span> | `ss19=0`
Latin to Limbu Digits | <span class='namdhinggo-R normal' style='font-feature-settings: "ss19" 1'>0 1 2 3 4 5 6 7 8 9</span> | `ss19=1`

#### Limbu to Latin Digits <a id="ss20"></a>

<span class='affects'>Affects: U+1946 U+1947 U+1948 U+1949 U+194A U+194B U+194C U+194D U+194E U+194F</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
Default | <span class='namdhinggo-R normal'>᥆ ᥇ ᥈ ᥉ ᥊ ᥋ ᥌ ᥍ ᥎ ᥏</span> | `ss20=0`
Limbu to Latin Digits | <span class='namdhinggo-R normal' style='font-feature-settings: "ss20" 1'>᥆ ᥇ ᥈ ᥉ ᥊ ᥋ ᥌ ᥍ ᥎ ᥏</span> | `ss20=1`

<!-- PRODUCT SITE ONLY
[font id='namdhinggo' face='Namdhinggo-Regular' bold='Namdhinggo-Bold' size='150%']
-->
