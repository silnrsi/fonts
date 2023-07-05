# Maintenance Processes

These processes require the [pysilfont](https://github.com/silnrsi/pysilfont) library to be installed.

## Rebuilding the families.json file

Whenever a change is made to the fonts or font metadata the final step is always to rebuild the families.json file. Run this command from the repo root before committing your changes:

```
python3 tools/updatefamilydata.py
```

## Adding a new hosted font package

To add a new hosted font to GFR/FLO:

- Pull all changes to the GFR repository.
- Verify that the font has a free and open license, preferably the OFL.
- Determine the appropriate *familyid*, based on the common font family name, lowercased, and with spaces removed.
- Copy the complete font release package, unzipped, to the appropriate fonts folder, either `/fonts/sil/familyid` or `/fonts/other/familyid`.
- If the font package does not contain a `fontmanifest.json` file, create one in the root of the package folder based on those for other fonts and the [Additional Family Metadata](/documentation/manifests.md) spec.
- Create a `familyid_base.json` basefile in `/basefiles` containing all appropriate fields, but omitting *defaults*, *files*, and *version* as they are defined in `fontmanifest.json`.
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

Example of a new `fontmanifest.json` file for a hosted non-SIl family:

```
{
"bailey": {
    "defaults": {
        "ttf": "Bailey-Regular.ttf",
        "woff2": "Bailey-Regular.woff2"
    },
    "family": "Bailey",
    "files": {
        "Bailey-Bold.ttf": { "axes": { "ital": 0, "wght": 700.0 }, "packagepath": "Bailey-Bold.ttf" },
        "Bailey-Bold.woff2": { "axes": { "ital": 0, "wght": 700.0 }, "packagepath": "web/Bailey-Bold.woff2" },
        "Bailey-Regular.ttf": { "axes": { "ital": 0, "wght": 400.0 }, "packagepath": "Bailey-Regular.ttf" },
        "Bailey-Regular.woff2": { "axes": { "ital": 0, "wght": 400.0 }, "packagepath": "web/Bailey-Regular.woff2" }
    },
    "version": "0.202"
}
}
```

And the accompanying basefile:

```
{
"bailey": {
    "distributable": true,
    "family": "Bailey",
    "familyid": "bailey",
    "license": "OFL",
    "packageurl": "https://github.com/nlci/mlym-font-bailey/releases/download/v0.202/Bailey-0.202.zip",
    "siteurl": "https://github.com/nlci/mlym-font-bailey",
    "source": "NLCI",
    "status": "current",
    "ziproot": "Bailey-0.202"
}
}
```

## Updating a hosted font package

To update a hosted font package:

- Pull all changes to the GFR repository.
- Copy the complete contents of the updated font release package into the existing *familyid* folder. Be careful to remove any files that are no longer part of the package but retain any handcrafted `fontmanifest.json` file.
- Check the `fontmanifest.json` file and update the info if necessary, particularly the *version*.
- Update the `familyid_base.json` basefile, and carefully check data that may change between versions, such as *packagepath* and *ziproot*.
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

## Removing a hosted font package

- Pull all changes to the GFR repository.
- Remove the *familyid* folder in `/fonts/sil/` or `/fonts/other`.
- Change the `familyid_base.json` basefile as needed to reflect the new status of the font. If the font is no longer available then be sure to provide a *fallback*. **Do not remove the basefile altogether!**
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

## Adding information on a non-hosted font family

- Pull all changes to the GFR repository.
- Double-check that there is no info on the font family already in `families.json`.
- Determine the appropriate *familyid*, based on the common font family name, lowercased, and with spaces removed.
- Download the font package to your local drive as a reference to its contents and to test the download link(s). Do not copy this into the repository.
- Create a `familyid_base.json` basefile in `/basefiles` containing all appropriate fields. This should include *defaults*, *files*, and *version*, based on what is found in the download package. Although may of the fields in `families.json` are technically optional, please include as many of them as you can. See other basefiles for examples.
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

Here is an example of the basefile for a non-hosted font:

```
{
"dukor": {
    "defaults": {
        "ttf": "Dukor.ttf"
    },
    "distributable": true,
    "fallback": "wakor",
    "family": "Dukor",
    "familyid": "dukor",
    "files": {
        "Dukor.ttf": { "axes": { "ital": 0, "wght": 400.0 }, "packagepath": "Dukor-1.0.7/Dukor.ttf" },
        "DukorItalic.ttf": { "axes": { "ital": 1, "wght": 400.0 }, "packagepath": "Dukor-1.0.7/DukorItalic.ttf" }
    },
    "license": "OFL",
    "packageurl": "https://www.evertype.com/fonts/vai/dukorfont.zip",
    "siteurl": "https://www.evertype.com/fonts/vai/",
    "source": "Evertype",
    "version": "1.0.7",
    "ziproot": ""
}
}
```

## Updating information on a non-hosted font family

- Pull all changes to the GFR repository.
- Edit the `familyid_base.json` basefile.
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

## Other tools

Some of the scripts in `/tools` were written only for short-term use as the collection was assembled. However, there are some tools that may be useful in creating and maintaining font metadata:

### checkmanifest.py

Validates a font manifest file. (needs documentation and example)

### createdraftfile.py

Creates a draft font manifest or basefile based on the content of a folder. (needs documentation and example)

### updatenotobasefiles.py

This script reads the state.json file from the Google noto project and updates all the noto*_base.json files with the information found in state.json. (needs documentation and example?)

## Updating the FLO index.html based on README.md

The single HTML page on FLO is derived from the README.md file. To regenerate the file run the following command (requires pandoc):

```
pandoc -s -f markdown-smart --template documentation/assets/html/template.html README.md -o index.html --metadata title="SIL International"
```