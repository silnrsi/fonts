---
title: Kanchenjunga - Font Features
fontversion: 2.001
---

Kanchenjunga is an OpenType-enabled font family that supports the Kirat Rai script. It includes a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The sections below enumerate the details of these features. Whether these features are available to users will depend on both the application and the rendering technology being used. Some applications let the user control certain features such as Character Variants to turn on the rendering of variant characters. However, at this point, most applications do not make use of those features.

See [Using Font Features](https://software.sil.org/fonts/features/). That page provides a comprehensive list of applications that make full use of the OpenType font technology.

This page uses web fonts (WOFF) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Kanchenjunga as a web font see *Kanchenjunga-webfont-example.html* in the font package web folder. 

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Customizing with TypeTuner

For applications that do not make use of the OpenType Character Variant features, you can now download fonts customized with the variant glyphs you choose. Read the [Font Features](features.md) page, visit [TypeTuner Web](https://scripts.sil.org/ttw/fonts2go.cgi), then to choose the variants and download your font.

### Character variants

There are some character shape differences which can be accessed by using OpenType Character Variants.

#### Ca 

<span class='affects'>Affects: U+16D49</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='Kanchenjunga-R normal'>&#x16D49;</span>| `cv05=0`
Alternate | <span class='Kanchenjunga-R normal' style='font-feature-settings: "cv05" 1'>&#x16D49;</span>| `cv05=1`

#### Ta 

<span class='affects'>Affects: U+16D52</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='Kanchenjunga-R normal'>&#x16D52;</span>| `cv15=0`
Alternate | <span class='Kanchenjunga-R normal' style='font-feature-settings: "cv15" 1'>&#x16D52;</span>| `cv15=1`

#### Ma 

<span class='affects'>Affects: U+16D5B</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard  | <span class='Kanchenjunga-R normal'>&#x16D5B;</span>| `cv25=0`
Alternate | <span class='Kanchenjunga-R normal' style='font-feature-settings: "cv25" 1'>&#x16D5B;</span>| `cv25=1`

#### Ha 

<span class='affects'>Affects: U+16D62</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='Kanchenjunga-R normal'>&#x16D62;</span>| `cv35=0`
Alternate | <span class='Kanchenjunga-R normal' style='font-feature-settings: "cv35" 1'>&#x16D62;</span>| `cv35=1`



<!-- PRODUCT SITE ONLY
[font id='Kanchenjunga' face='Kanchenjunga-Regular' bold='Kanchenjunga-Bold' size='150%']

-->


