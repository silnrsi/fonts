# Internal Webfont Service Info

*Note: This webfont service is only for use by SIL and partners. Use by anyone else is unsupported and may be disabled without notice at any time.*

The SIL Internal Webfont Service provides webfonts for SIL and partner web apps and websites from a high-performance, high-reliability cloud source - [fonts.languagetechnology.org](https://fonts.languagetechnology.org). It hosts all current SIL fonts and a handful of freely-available fonts from partners.

## Setup

Search the `families.json` file for information on the desired font family. If the *files* records contain *flourl* fields then those fonts are available from FLO. Three font formats are supported: TTF, WOFF, WOFF2. The WOFF2 fonts are best to use as they will give the best performance and are supported by all modern browsers.

Add `@font-face` declarations for each individual font file to your CSS, using the *flourl*. For example, to use Regular and Bold weights of Andika add the following CSS (the *font-family* names can be defined to be whatever you wish):

```
@font-face {
    font-family: AndikaR;
    font-weight: normal;
    src: url("https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Regular.woff2") format("woff2");
}
@font-face {
    font-family: AndikaB;
    font-weight: bold;
    src: url("https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Bold.woff2") format("woff2");
}
```

Refer to the fonts in your CSS styles using the *font-family* names you have defined:

```
p { font-family: AndikaR, serif; }
```

## Limitations

Unlike other webfont services, FLO provides webfonts only by direct filename, not using family name and CSS axis values. It does not do any dynamic subsetting.

## Adding fonts to the service

All current SIL fonts are available. If there is a freely distributable webfont from others that is not available on another webfont service (such as Google Fonts) but would be useful to you please contact us. We can easily add additional fonts on request.
