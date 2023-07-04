# Finding Fonts using GFR, LFO, and LFF

How the fonts and data in this collection is best used depends on the specific need. The data can come from three sources:

- **GFR** - the source [Github Font Repository](https://github.com/silnrsi/fonts)
- **FLO** - the high-performance mirror at [fonts.languagetechnology.org](https://fonts.languagetechnology.org)
- **LFF** - the [Language Font Finder service NEED LINK]()

Font families with information in `families.json` fall into categories that determine which fields the font family record contains:


| Category | Details |
| -------- | ------- |
| GFR/FLO Hosted | Fonts (TTF, WOFF, WOFF2) that are directly available from GFR & FLO, including all current SIL fonts and a handful of fonts from partners. Individual font file links are listed in the *url* (GFR) and *flourl* fields in *files* records. These will always be kept up to date. |
| Externally Hosted | Fonts that are available from a direct link but are not hosted on GFR/FLO. Individual font file links are listed in the *url* field in *files* records. We will try to keep these links current, however they may be changed by the host at anytime with notifying us. |
| Packaged | Fonts that are only available in full release packages, not individual files, and not from GFR/FLO. These will typically have a *packageurl* that can be used to get the package. The *packagepath* and *zippath* fields in *files* records will provide the direct paths to individual font files within the decompressed and compressed packages respectively.
| Deprecated | Fonts that we do not recommend. They may be subsetted versions, use outdated encodings, have technical problems, lack proper licensing, or have higher-quality alternatives. In almost all cases the *fallback* field provides the *familyid* for a reasonable alternative. In some cases *packageurl* and *siteurl* may be provided in case the original font must be used such as for archived documents.
| Not Distributable | Fonts that cannot be freely obtained or redistributed. These may be proprietary fonts, such as those from Microsoft, or fonts with no known current source. In almost all cases the *fallback* field provides the *familyid* for a reasonable alternative.

Here are a few scenarios that demonstrate how this collection can be used:

## Desktop app needs to find and download a specific font or family

- Grab `families.json` (from either GFR or FLO) and search for the font family record that contains the font family name in *family*, *altfamily*, or *files/altfamily* fields. This may be more successful than guessing at the *familyid*, and will find records where the font family name is only listed in *altfamily* fields.
- Check the *distributable* field. If this is false there is no free source for the font. Look at *fallback* to find a font family that may be a reasonable substitute.
- Check the *status* field. If this is "deprecated" then look at *fallback* to find a font family that may be a reasonable substitute. In many cases the deprecated fonts remain available though not recommended. See *siteurl* and *packageurl* (if defined) for sources.
- If you want the full package of fonts, use *packageurl* (if defined). The path to individual font files in a decompressed package is in *packagepath* in *files* records. The direct path within a .zip file is in *zippath* in *files*.
- If you want only specific fonts within a family, look at the *files* records and check if there is a direct link - either *url* or *flourl*.

## App or script wants to check to see if a font is the current version

- Grab `families.json` (from either GFR or FLO) and search for the font family record that contains the font family name in *family*, *altfamily*, or *files/altfamily* fields. This may be more successful than guessing at the *familyid*, and will find records where the font family name is only listed in *altfamily* fields.
- Check the *version* field. This is always current for SIL fonts. For non-SIL fonts the version number reflects the latest known version, although there may be updated versions available.

## App or service wants to maintain a local collection of relevant fonts

- Clone the GFR, either partially or as a complete repo.
- Pull changes whenever updates are desired.

## Website or web app wants to self-host a webfont

- Follow the process for finding and downloading a specific font or family above.
- Find all *files* records with keys that end in ".woff2", and use the *url* or *flourl* to obtain them.
- See [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts/) for details on how to load self-hosted webfonts.

## Website or web app wants to dynamically load a webfont

See [Internal Webfont Service Info](/documentation/webfonts.md).

## A font is needed for a specific language or writing system

This collection does not contain any information on the preferred fonts for languages or writing systems. The [Language Font Finder service NEED LINK]() manages that information and provides an API that links writing systems with specific font family information from this collection. 
