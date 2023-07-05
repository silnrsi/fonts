# Font Family Metadata

All the metadata on font families in this collection is aggregated into one file - `families.json`. This is at the root of this repository - [families.json (Github link)](https://github.com/silnrsi/fonts/blob/main/fonts/families.json). It is also available on FLO - [families.json (FLO link)](https://fonts.languagetechnology.org/families.json). This data may be used to:

- Find a direct link to a font file
- Determine whether a font family can freely redistributed
- Identify which font in a large family should be considered the default
- Find a suitable alternative to a propretary or deprecated font family

The [Language Font Finder (LFF)](https://github.com/silnrsi/langfontfinder) service provides access to this data through an API.

This collection also contains related metadata files that are used as sources for compiling `families.json`. These are similar in format to `families.json` but contain no additional information:

- `fontmanifest.json` files in individual font family folders
- `familyid_base.json` files in `basefiles`

These are documented in [Additional Family Metadata](/documentation/manifests.md).

## familyids

Every separately-named font family has a unique *familyid* that is generally (not not necessarily always!) formed by taking the family name, removing spaces, and making it lowercase. For example "Lisu Bosa" has *familyid* "lisubosa". This *familyid* is used as the key for all font metadata and as folder names in `/fonts`.

## families.json


### Font family records

The metadata for a font family is in a *font family record* JSON object identified by *familyid*. The object contains the following fields, most of which are optional. Required fields are in bold:

| Field | Description |
| ----- | ----------- |
| altfamily | [opt] An alternative family name that may be used by Windows apps to refer to the font family in certain situations. If defined in the root of the record the family name applies to all fonts in the family. If a *files* field exists, then this field is ignored. *This field is not used in current records but is here for completeness. *altfamily* information is normally found in individual *files* records.* |
| defaults | [opt] A subobject indicating which *files* entries represent default fonts for the family. See *defaults* section below. |
| **distributable** | Boolean to indicate whether the font is likely to be freely distributable. |
| fallback | [opt] A *familyid* for an alternative font family to use instead. Two common cases of this are 1) when the font family is not distributable (e.g. Microsoft system fonts) or 2) if the font family is deprecated. |
| **family** | Common family name as seen by users, which may contain spaces (e.g. "Lisu Bosa"). Some Windows apps may display a different family name for individual members of a family in certain situations - see *altfamily*. |
| **familyid** | The unique identifier for the font family. |
| features | [opt] A CSS-style features string describing how the font features should be set to appropriately style text in this font for this language. This field is only returned by the [Language Font Finder (LFF)](https://github.com/silnrsi/langfontfinde) service, if at all.
| files | [opt] A subobject containing information about individual font files in the package. The object is keyed by filename with its own object of information.  See *files* section below. |
| googlefonts | [opt] This subobject contains information on how to access the font family via the Google Fonts service. See *defaults* section below. *This field is not used in current records pending further discussion.* |
| license | [opt] The name of the font license, if known (MIT, OFL, GPL-FE, etc.). This may instead indicate a type of license, such as "shareware" or "proprietary". |
| packageurl | [opt] URL for direct download of the complete font package, typically a .zip file. |
| siteurl | [opt] URL to a website where users can find out about the font package and download it. |
| source | [opt] The source of this font, if known, such as "SIL", "Google", "NLCI", "Microsoft", etc. |
| status | [opt] The current status of this font package: *current* (active), *archived* (no longer active), *deprecated* (another *familyid* is preferred). Defined for all SIL fonts, and others whose status is known. |
| version | [opt] The version of the font package being described. This is always current for SIL fonts. For non-SIL fonts the version number reflects the latest known version, although there may be updated versions available. |
| ziproot | [opt] The name of the folder created when a .zip package is decompressed. Used to form *zippath* fields in *files* records. |

#### *default* subobjects

The *default* field is an object whose keys are font file types.

| Field | Description |
| ----- | ----------- |
| ttf | [opt] Key in *files* subobjects to the default TTF font file. |
| woff | [opt] Key in *files* subobjects to the default WOFF font file. |
| woff2 | [opt] Key in *files* subobjects to the default WOFF2 font file. |

#### *files* subobjects

The *files* field is an object whose keys are filenames without any path. For each filename, there is an object of information with the following fields:

| Field | Description |
| ----- | ----------- |
| axes | [opt] A subobject keyed by font axis and a float value.  See *axes* section below. | 
| altfamily | [opt] An alternative family name if different from the *family* field in the main font family description. This is typically used by legacy RIBBI-only applications to provide access to multi-weight font families, particularly on Windows. |
| flourl | [opt] If the font file exists on FLO, this field gives the URL. |
| packagepath | [opt] The path to the font file inside the main *packageurl*, if defined. |
| url | [opt] A direct download URL to this font file, if available. |
| zippath | [opt] Most packages are distributed as a zip file with a top level directory within the zip. This field gives the complete path within the zip file to the font file (including that top level directory). |

#### *axes* subobjects

The *axes* field within *files* records is a subobject whose keys are four-letter axis identifiers. There are [five standard registered axes](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg) although custom axes can be defined. The keys and their values identify a single style contained in a font family (e.g. Bold Italic). SIL fonts typically define styles using only these two axes:

| Field | Description |
| ----- | ----------- |
| ital | [opt] 0 for upright, 1 for italic. |
| wght | [opt] Font weight. This is a number between 0 and 999. Each multiple of 100 signifies an industry-standard weight name from 100 to 900: Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black. |

For example, the normal Regular weight of a font family will always be indicated by `{ "ital": 0 "wght": 400.0 }` and the Bold Italic by `{ "ital": 1, "wght": 700.0 }`.

#### *googlefonts* subobjects

The *googlefonts* field will contain information on how to access the fonts via the Google Fonts service. *Currently undefined pending further discussion.*

## Example font family records

### An SIL font family with a single weight (Abysssinica SIL)

```
"abyssinicasil": {
    "defaults": {
        "ttf": "AbyssinicaSIL-Regular.ttf",
        "woff": "AbyssinicaSIL-Regular.woff",
        "woff2": "AbyssinicaSIL-Regular.woff2"
    },
    "distributable": true,
    "family": "Abyssinica SIL",
    "familyid": "abyssinicasil",
    "files": {
        "AbyssinicaSIL-Regular.ttf": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/abyssinicasil/AbyssinicaSIL-Regular.ttf", "packagepath": "AbyssinicaSIL-Regular.ttf", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/abyssinicasil/AbyssinicaSIL-Regular.ttf", "zippath": "AbyssinicaSIL-2.201/AbyssinicaSIL-Regular.ttf" },
        "AbyssinicaSIL-Regular.woff": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/abyssinicasil/web/AbyssinicaSIL-Regular.woff", "packagepath": "web/AbyssinicaSIL-Regular.woff", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/abyssinicasil/web/AbyssinicaSIL-Regular.woff", "zippath": "AbyssinicaSIL-2.201/web/AbyssinicaSIL-Regular.woff" },
        "AbyssinicaSIL-Regular.woff2": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/abyssinicasil/web/AbyssinicaSIL-Regular.woff2", "packagepath": "web/AbyssinicaSIL-Regular.woff2", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/abyssinicasil/web/AbyssinicaSIL-Regular.woff2", "zippath": "AbyssinicaSIL-2.201/web/AbyssinicaSIL-Regular.woff2" }
    },
    "license": "OFL",
    "packageurl": "https://software.sil.org/downloads/r/abyssinica/AbyssinicaSIL-2.201.zip",
    "siteurl": "https://software.sil.org/abyssinica/",
    "source": "SIL",
    "status": "current",
    "version": "2.201",
    "ziproot": "AbyssinicaSIL-2.201"
},
```

### An SIL font family with multiple weights and styles (Andika)

```
"andika": {
    "defaults": {
        "ttf": "Andika-Regular.ttf",
        "woff": "Andika-Regular.woff",
        "woff2": "Andika-Regular.woff2"
    },
    "distributable": true,
    "family": "Andika",
    "familyid": "andika",
    "files": {
        "Andika-Bold.ttf": { "axes": { "ital": 0, "wght": 700.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/Andika-Bold.ttf", "packagepath": "Andika-Bold.ttf", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/Andika-Bold.ttf", "zippath": "Andika-6.200/Andika-Bold.ttf" },
        "Andika-Bold.woff": { "axes": { "ital": 0, "wght": 700.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Bold.woff", "packagepath": "web/Andika-Bold.woff", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-Bold.woff", "zippath": "Andika-6.200/web/Andika-Bold.woff" },
        "Andika-Bold.woff2": { "axes": { "ital": 0, "wght": 700.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Bold.woff2", "packagepath": "web/Andika-Bold.woff2", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-Bold.woff2", "zippath": "Andika-6.200/web/Andika-Bold.woff2" },
        "Andika-BoldItalic.ttf": { "axes": { "ital": 1, "wght": 700.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/Andika-BoldItalic.ttf", "packagepath": "Andika-BoldItalic.ttf", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/Andika-BoldItalic.ttf", "zippath": "Andika-6.200/Andika-BoldItalic.ttf" },
        "Andika-BoldItalic.woff": { "axes": { "ital": 1, "wght": 700.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-BoldItalic.woff", "packagepath": "web/Andika-BoldItalic.woff", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-BoldItalic.woff", "zippath": "Andika-6.200/web/Andika-BoldItalic.woff" },
        "Andika-BoldItalic.woff2": { "axes": { "ital": 1, "wght": 700.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-BoldItalic.woff2", "packagepath": "web/Andika-BoldItalic.woff2", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-BoldItalic.woff2", "zippath": "Andika-6.200/web/Andika-BoldItalic.woff2" },
        "Andika-Italic.ttf": { "axes": { "ital": 1, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/Andika-Italic.ttf", "packagepath": "Andika-Italic.ttf", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/Andika-Italic.ttf", "zippath": "Andika-6.200/Andika-Italic.ttf" },
        "Andika-Italic.woff": { "axes": { "ital": 1, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Italic.woff", "packagepath": "web/Andika-Italic.woff", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-Italic.woff", "zippath": "Andika-6.200/web/Andika-Italic.woff" },
        "Andika-Italic.woff2": { "axes": { "ital": 1, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Italic.woff2", "packagepath": "web/Andika-Italic.woff2", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-Italic.woff2", "zippath": "Andika-6.200/web/Andika-Italic.woff2" },
        "Andika-Regular.ttf": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/Andika-Regular.ttf", "packagepath": "Andika-Regular.ttf", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/Andika-Regular.ttf", "zippath": "Andika-6.200/Andika-Regular.ttf" },
        "Andika-Regular.woff": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Regular.woff", "packagepath": "web/Andika-Regular.woff", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-Regular.woff", "zippath": "Andika-6.200/web/Andika-Regular.woff" },
        "Andika-Regular.woff2": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/sil/andika/web/Andika-Regular.woff2", "packagepath": "web/Andika-Regular.woff2", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/sil/andika/web/Andika-Regular.woff2", "zippath": "Andika-6.200/web/Andika-Regular.woff2" }
    },
    "license": "OFL",
    "packageurl": "https://software.sil.org/downloads/r/andika/Andika-6.200.zip",
    "siteurl": "https://software.sil.org/andika/",
    "source": "SIL",
    "status": "current",
    "version": "6.200",
    "ziproot": "Andika-6.200"
},
```

### A non-SIL font family hosted on FLO (Surma)

```
"surma": {
    "defaults": {
        "ttf": "Surma-Regular.ttf",
        "woff": "Surma-Regular.woff",
        "woff2": "Surma-Regular.woff2"
    },
    "distributable": true,
    "family": "Surma",
    "familyid": "surma",
    "files": {
        "Surma-Regular.ttf": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/other/surma/Surma-Regular.ttf", "packagepath": "Surma-Regular.ttf", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/other/surma/Surma-Regular.ttf", "zippath": "Surma-4.000/Surma-Regular.ttf" },
        "Surma-Regular.woff": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/other/surma/Surma-Regular.woff", "packagepath": "Surma-Regular.woff", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/other/surma/Surma-Regular.woff", "zippath": "Surma-4.000/Surma-Regular.woff" },
        "Surma-Regular.woff2": { "axes": { "ital": 0, "wght": 400.0 }, "flourl": "https://fonts.languagetechnology.org/fonts/other/surma/Surma-Regular.woff2", "packagepath": "Surma-Regular.woff2", "url": "https://github.com/silnrsi/fonts/raw/main/fonts/other/surma/Surma-Regular.woff2", "zippath": "Surma-4.000/Surma-Regular.woff2" }
    },
    "license": "OFL",
    "packageurl": "https://github.com/syltrans/surma/releases/download/v4.000/Surma-4.000.zip",
    "siteurl": "https://github.com/syltrans/surma",
    "source": "STAR",
    "status": "current",
    "version": "4.000",
    "ziproot": "Surma-4.000"
},
```

### A deprecated font family (ShiShan)

```
"shishan": {
    "distributable": true,
    "fallback": "shimenkan",
    "family": "ShiShan",
    "familyid": "shishan",
    "license": "OFL",
    "packageurl": "https://software.sil.org/downloads/r/shishan/ShiShan-HMD-1.100.zip",
    "siteurl": "https://software.sil.org/shishan/",
    "source": "SIL",
    "status": "deprecated",
    "version": "1.100"
},
```

### A proprietary font family with fallback (Arial)

```
"arial": {
    "distributable": false,
    "fallback": "andika",
    "family": "Arial",
    "familyid": "arial",
    "license": "proprietary",
    "source": "Microsoft"
},
```
