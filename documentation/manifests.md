# Additional Family Metadata

The data in `families.json` comes from two sources:

- `fontmanifest.json` files in individual font family folders in the `fonts/` folder
- `familyid_base.json` files in the `basefiles/` folder

## Font manifests

Font manifest files (`fontmanifest.json`) are now included in all SIL font releases. They provide metadata on the fonts in the package.

The format is similar, but not identical to, font family records in `families.json`. They contain a single record, keyed by *familyid*. There are fewer fields, although more of them are required (shown in bold):

| Field | Description |
| ----- | ----------- |
| **defaults** | A subobject indicating which *files* entries represent default fonts for the family. See *defaults* section below. |
| **family** | Common family name as seen by users, which may contain spaces (e.g. "Lisu Bosa"). Some Windows apps may display a different family name for individual members of a family in certain situations - see *altfamily* in *files* records. |
| **files** | A subobject containing information about individual font files in the package. The object is keyed by filename with its own object of information.  See *files* section below. |
| **version** | The version of the font package being described. |

#### *default* subobjects

The *default* field is an object whose keys are font file types.

| Field | Description |
| ----- | ----------- |
| **ttf** | Key in *files* subobjects to the default TTF font file. |
| woff | [opt] Key in *files* subobjects to the default WOFF font file. |
| woff2 | [opt] Key in *files* subobjects to the default WOFF2 font file. |

#### *files* subobjects

The *files* field is an object whose keys are filenames without any path. For each filename, there is an object of information with the following fields:

| Field | Description |
| ----- | ----------- |
| **axes** | A subobject keyed by font axis and a float value.  See *axes* section below. |
| altfamily | [opt] An alternative family name if different from the *family* field in the main font family description. This is typically used by legacy RIBBI-only applications to provide access to multi-weight font families, particularly on Windows. This is often found in *stylemapfamilyname* properties in designspace instances. |
| **packagepath** | [opt] The path to the font file inside the main package relative to the root. |

#### *axes* subobjects

The *axes* field within *files* records is a subobject whose keys are four-letter axis identifiers. There are [five standard registered axes](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg) although custom axes can be defined. The keys and their values identify a single style contained in a font family (e.g. Bold Italic). SIL fonts typically define styles using only these two axes, **both of which are required in all cases**:

| Field | Description |
| ----- | ----------- |
| **ital** | 0 for upright, 1 for italic. |
| **wght** | ont weight. This is a number between 0 and 999. Each multiple of 100 signifies an industry-standard weight name from 100 to 900: Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black. |

Here is an example of the font manifest for Abyssinica SIL:

```
{
"abyssinicasil": {
    "defaults": {
        "ttf": "AbyssinicaSIL-Regular.ttf",
        "woff": "AbyssinicaSIL-Regular.woff",
        "woff2": "AbyssinicaSIL-Regular.woff2"
    },
    "family": "Abyssinica SIL",
    "files": {
        "AbyssinicaSIL-Regular.ttf": { "axes": { "ital": 0, "wght": 400.0 }, "packagepath": "AbyssinicaSIL-Regular.ttf" },
        "AbyssinicaSIL-Regular.woff": { "axes": { "ital": 0, "wght": 400.0 }, "packagepath": "web/AbyssinicaSIL-Regular.woff" },
        "AbyssinicaSIL-Regular.woff2": { "axes": { "ital": 0, "wght": 400.0 }, "packagepath": "web/AbyssinicaSIL-Regular.woff2" }
    },
    "version": "2.201"
}
}
```

## Basefiles

Basefiles are used to define all information that ends up in `families.json` that is not included in `fontmanifest.json` files. The format is identical to `families.json` but without data that is present in a `fontmanifest.json` file for that *familyid*.

Every font family (*familyid*) included in `families.json` will have a corresponding `familyid_base.json` file in the `basefiles/` folder.

Here is an example of the basefile for Abyssinica SIL:

```
{
"abyssinicasil": {
    "distributable": true,
    "family": "Abyssinica SIL",
    "familyid": "abyssinicasil",
    "license": "OFL",
    "packageurl": "https://software.sil.org/downloads/r/abyssinica/AbyssinicaSIL-2.201.zip",
    "siteurl": "https://software.sil.org/abyssinica/",
    "source": "SIL",
    "status": "current",
    "ziproot": "AbyssinicaSIL-2.201"
}
}
```
