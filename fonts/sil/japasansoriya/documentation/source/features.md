---
title: Japa Sans Oriya - Font Features
fontversion: 2.200
---

Japa Sans Oriya is an OpenType-enabled font family that supports the Oriya/Odia script. It includes a number of optional features that may be useful or required for particular uses or languages. This document lists all the available features.

These OpenType features are primarily specified using four-letter tags (e.g. 'cv10'). For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](http://software.sil.org/fonts/features).

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For detailed information see [Using SIL Fonts on Web Pages](http://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Complete feature list

### Character variants

#### Va for Kui
<span class='affects'>Affects: U+0B35</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Default | <span class='japa-R normal'>&#x0b35; &#x0b35;&#x0b4d;&#x0b30; &#x0b35;&#x0b4d;&#x0b5c;</span>| `cv10=0`
Kui     | <span class='japa-R normal' style='font-feature-settings: "cv10" 1'>&#x0b35; &#x0b35;&#x0b4d;&#x0b30; &#x0b35;&#x0b4d;&#x0b5c;</span>| `cv10=1`

### Stylistic sets

#### KaTaRa Alternate
<span class='affects'>Affects: U+0B15 U+0B4D U+0B24 U+0B4D U+0B30</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Default   | <span class='japa-R normal'>&#x0b15;&#x0b4d;&#x0b24;&#x0b4d;&#x0b30;</span>| 
Alternate | <span class='japa-R normal' style='font-feature-settings: "ss01" 1'>&#x0b15;&#x0b4d;&#x0b24;&#x0b4d;&#x0b30;</span>| `ss01`

#### Oriya to Latin Figures
<span class='affects'>Affects: U+0B66..U+0B6F</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Default   | <span class='japa-R normal'>&#x0B66;&#x0B67;&#x0B68;&#x0B69;&#x0B6A;&#x0B6B;&#x0B6C;&#x0B6D;&#x0B6E;&#x0B6F;</span>| 
Alternate | <span class='japa-R normal' style='font-feature-settings: "ss02" 1'>&#x0B66;&#x0B67;&#x0B68;&#x0B69;&#x0B6A;&#x0B6B;&#x0B6C;&#x0B6D;&#x0B6E;&#x0B6F;</span>| `ss02`

#### Latin to Oriya Figures Figures
<span class='affects'>Affects: U+0030..U+0039</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Default   | <span class='japa-R normal'>0123456789</span>| 
Alternate | <span class='japa-R normal' style='font-feature-settings: "ss03" 1'>0123456789</span>| `ss03`


<!-- PRODUCT SITE ONLY
[font id='japa' face='JapaSansOriya-Regular' bold='JapaSansOriya-Bold' size='150%']
-->
