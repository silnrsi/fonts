# SIL Language Technology Font Collection

*This documentation is currently incomplete and is a work-in-progress. Some links may not work.*

This is a collection of fonts, font metadata, and related tools maintained by SIL International. This collection is managed as a [git repository on Github](https://github.com/silnrsi/fonts) and mirrored for faster performance at [fonts.languagetechnology.org](https://fonts.languagetechnology.org). See below for license information and terms of use.

## What is not here

This collection is not intended as a primary end-user source of SIL fonts or information on how to use them. Here are links to better sources of fonts and information:

- **If you are looking for SIL fonts to install and use or distribute** see our main font product sites at [software.sil.org/fonts](https://software.sil.org/fonts). Those sites contain:
  - Compressed font packages rather than individual files
  - All versions and variants - current and past
  - Full documentation, including graphics
  - Contact forms for making requests and reporting problems
- **If you need help with using SIL fonts** see our [Font Help Guides](https://software.sil.org/fonts/guides/) as well as individual font product sites.
- **If you want to develop fonts or contribute to SIL font projects** see [Font Development Best Practices](https://silnrsi.github.io/FDBP/en-US/Introduction.html) and [SIL Font Development Notes](https://silnrsi.github.io/silfontdev/en-US/index.html).
- **If you need a keyboard or keyboard software** see [Keyman](https://keyman.com/).
- **If you are a developer and want an API that will provide infomation on appropriate fonts for a writing system** see the [Language Font Finder Service (NEEDS LINK)](). This collection contains much of the font metadata used by that service but not the corresponding writing system information.

## What is here

This collection is mainly for use by websites, web apps, and desktop applications. It is also used for internal font testing by [SIL's Writing Systems Technology team](https://software.sil.org/wstech/). It contains:

- Current (only) versions of fonts from SIL and chosen partners (`/fonts`)
- Metadata on 300+ fonts from SIL and others (`/basefiles`, `families.json`)
- Internal webfont test files used by the SIL font production team (`/tests`)
- Internal tools for managing this collection (`/tools`)

## What you can do with this collection

Common uses for this collection are:

- **To look at metadata on fonts from SIL and others that may be useful for language communities,** including links to font sources and distribution information. This can be found in the `families.json` file. Details on what that file contains can be found in [Font Family Metadata](/documentation/families.md). Some example uses:
  - Find a direct link to a font file
  - Determine whether a font family can freely redistributed
  - Identify which font in a large family should be considered the default
  - Find a suitable alternative to a propretary or deprecated font family
- **To programmatically grab the latest version of individual SIL font files.** These are found in `/fonts/sil` and in individual font family folders. Each folder generally contains the same files that are in the main font distribution packages, but packages with multiple font families are split into separate folders. The `families.json` file and the `fontmanifest.json` files in most folders provide metadata on the fonts. For details of how this repo and FLO (fonts.languagetechnology.org) can be used to identify and obtain fonts see [Finding Fonts](/documentation/findingfonts.md).
- **As a live webfont service for SIL and partner websites and web apps.** *This service is not recommended for use by the general public. At some point we may, without notice, restrict webfont use from this site to only registered sites and users, at which point unregistered access will no longer work.* This service is, however, intended as a reliable, high-performance webfont source for SIL and partner use - see [Internal Webfont Service Info](/documentation/webfonts.md).

Internal processes:

- To test local, cloud, and third-party hosting of SIL webfonts. See [Internal Webfont Testing](/documentation/testing.md).
- Maintaining this collection. See [Maintenance Processes](/documentation/maintenance.md).

## Limitations, licenses, and terms of use

Fonts and related font software included in this collection are licensed according to the terms of the licenses included in individual font folders. In most cases this is the [SIL Open Font License](https://scripts.sil.org/ofl).

All other contents, except where noted, are Copyright (c) 2021-2023, [SIL International](http://www.sil.org) and released under the MIT license - see [LICENSE](license).

**SIL International makes no guarantees regarding the ongoing availability of the fonts and data on this site. Individuals and organizations use these fonts and data at their own risk. SIL International maintains this collection but does not provide any technical support except for use by SIL and partners.**

