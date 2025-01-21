# SIL Webfont Testing

These files are used for internal testing of SIL's webfonts. They test the fonts as provided by three sources:

- [This repository](https://github.com/silnrsi/fonts) - using local path references (LPR)
- [fonts.languagetechnology.org](https://fonts.languagetechnology.org) - SIL's internal font source (FLO)
- [Google Fonts](https://fonts.google.com) - only for those fonts available through the service (GF)

## Viewing the tests

The tests are in HTML files, generated from markdown and FTML data, and stored in folders that reflect the font family name. They can be viewed either from a local clone of the [Github repository](https://github.com/silnrsi/fonts) or directly on [fonts.languagetechnology.org](https://fonts.languagetechnology.org).

**To get an accurate view of how the fonts look from these three sources the HTML files must be viewed on a machine that does not have the specific fonts installed.** Otherwise some browsers will allow locally installed fonts to be used in place of the other three sources.

## Preparing and updating markdown tests

The markdown tests in each folder are transformed into HTML files using pandoc and a general test template (assets/testtemplate.html). The HTML is styled using a general test theme (assets/css/testtheme.css) and webfont definitions in individual folders (*fontFamilyID*/webfonts.css).

These tests are intended to test the webfonts as they would be used - using real language texts, all weights, all styles, and any language-specific features.

## Making new tests

To make a new set of tests for a font family:

- Clone this repo to your local drive
- Copy the contents of the release package in full (unzipped) to the *fonts* folder in the root of the repo (fonts/sil/*fontFamilyID*/)
    - If the version of the font being tested is not the current one, then it may be necessary to name the folder with a version number, as in *fonts/sil/andika6.000*.
- Duplicate the tests folder of a similar family (e.g. *tests/andika* for LCG fonts)
- Rename the folder to reflect the appropriate *fontFamilyID*
- Change the CSS in *tests/fontFamilyID/webfonts.css* to point to the new folder
- Change the gfhref in the header of the .md file(s) to use the appropriate Google Fonts href for the font family and all its styles
- Customize the .md file(s) for your particular project
- Add your files to the `tests/maketests` script based on the examples there
- Run the script with `./maketests` (in the `tests` folder) to generate the HTML files
- Pull any changes to the repo since you cloned (important!) in case others have made changes
- Commit your changes to your local repository and push them to the origin `main` branch

## Updating existing tests

To update the tests later:

- Pull any changes to the repo (important!)
- Make your changes to the .md files (and any others, such as the css)
- Rebuild all the test HTML docs with `./maketests`
- Commit your changes to your local repository and push them to the origin `main` branch

## Preparing and updating FTML tests

(to be added)

## Acknowledgements

Test contents, unless another source is named, are copyright (c) 2022-2025, SIL Global (http://www.sil.org) and released under the MIT license.
