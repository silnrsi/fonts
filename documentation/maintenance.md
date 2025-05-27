# Maintenance Processes

These processes require the [pysilfont](https://github.com/silnrsi/pysilfont) library to be installed. Use the following steps:
```
python3 -m venv venv
source venv/bin/activate
pip install silfont[git] git+https://github.com/silnrsi/pysilfont.git@master
pip install brotli
```

Here are the various processes:
[Adding a new hosted font](#adding-a-new-hosted-font-package), [updating a hosted font](#updating-a-hosted-font-package), [removing a hosted font](#removing-a-hosted-font-package), [adding information on a non-hosted font family](#adding-information-on-a-non-hosted-font-family), [updating information on a non-hosted font](#updating-information-on-a-non-hosted-font-family), [updating information on non-hosted Noto fonts](#updating-information-on-non-hosted-google-noto-families), [rebuilding the main families.json](#rebuilding-the-familiesjson-file-mandatory-final-step), [details about the helper scripts: checkmanifest and createdraftfile](#other-tools), [updating the FLO index.html based on README.md](#updating-the-flo-indexhtml-based-on-readmemd)



## Rebuilding the families.json file (mandatory final step)

Whenever a change is made to the fonts or font metadata the final step is always to rebuild the `families.json` file. Always run this command from the repo root before committing your changes:

```
python3 tools/updatefamilydata.py
```

**WARNING: Do not make changes to the `families.json` file directly - those changes will be wiped out when the file is rebuilt. Make all changes to either `familyid_base.json` or `fontmanifest.json` files, then rebuild `families.json`** as a final step.

## Adding a new hosted font package

_(hosted fonts are only from SIL and close partners, see below for non-hosted fonts)_

To add a new hosted font to GFR/FLO:

- Pull all changes to the GFR repository.
- Verify that the font has a free and open license, preferably the OFL.
- Determine the appropriate *familyid*, based on the common font family name, lowercased, and with spaces removed.
- Copy the complete font release package, unzipped, to the appropriate fonts folder, either `/fonts/sil/familyid` or `/fonts/other/familyid`.
- If the font package does not contain a `fontmanifest.json` file, create one in the root of the package folder based on those for other fonts and the [Additional Family Metadata](/documentation/manifests.md) spec.
- Create a `familyid_base.json` basefile in `/basefiles` containing all appropriate fields, but omitting *defaults*, *files*, and *version* as they are defined in `fontmanifest.json`.
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

Example of a new `fontmanifest.json` file for a hosted non-SIL family:

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
- Copy the complete contents of the updated font release package into the existing *familyid/* folder. Be careful to remove any files that are no longer part of the package but retain any handcrafted `fontmanifest.json` file.
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
- Download the font package to your local drive as a reference to its contents and to test the download link(s). Make a new folder under `local/datafiles/`. **IMPORTANT: Do not commit any of these files into the repository, the whole local/ folder should be ignored by git anyway but be careful**.
- Create a `familyid_base.json` basefile then place it into the `basefiles/` folder containing all appropriate fields. This should include *defaults*, *files*, and *version*, based on what is found in the download package. Although many of the fields in `families.json` are technically optional, please include as many of them as you can. See other basefiles for examples. (You can also use `tools/createdraftfile.py` as a helper, see the [tools section for more details](#other-tools)). _Make sure to review the file manually carefully. Some font projects may leave .ttf files you don't want with suffixes like `input.ttf` or `volt.ttf` inside their release zip and we don't want to offer these intermediary source files._  Unlike for hosted fonts the `defaults`, `files` fields are necessary and the `version` field should be provided unless it cannot be determined. 
Non-hosted fonts don't need a `fontmanifest.json` file.
- Rebuild the `families.json` file (using `tools/updatefamilydata.py`)
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

## Updating information on non-hosted Google Noto families

_Note that the following process does not add information on any new families that may have been added to the Noto fonts. It only updates the information for families that have existing base files._

- Pull all changes to the GFR repository.
- Run the `updatenotobasefiles.py` script to grab the latest state.json data and update the `noto*_base.json` files:

```
python3 tools/updatenotobasefiles.py
```

- Very carefully inspect the resulting changes in each affected base file. Most changes should be in version numbers.
- Manually check and fix changes to families in packages that contain more than one font family. Discard any changes to *defaults* unless you are very sure that the default should change. For example, the script may try to change the *defaults* in Noto Sans Devanagari to `NotoSansDevanagariUI-Regular.ttf`.
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

## Updating information on a non-hosted font family

- Pull all changes to the GFR repository.
- Edit the `familyid_base.json` basefile.
- Rebuild the `families.json` file.
- Check your changes carefully, then commit and push your changes.

## Other tools

Some of the scripts in `tools/` were written only for short-term use as the collection was assembled. However, there are some tools that may be useful in creating and maintaining font metadata:

### checkmanifest.py

Validates a font manifest file. For example:

```
python3 tools/checkmanifest.py fonts/other/bailey/fontmanifest.json
```
This is important so that filepaths match the information given to the system.


### createdraftfile.py

Creates a draft font manifest `fontmanifest.json` or basefile `familyid_base.json` based on the content of a folder. For example:

```
mdkir -p local/datafiles/
python3 tools/createdraftfile.py -t ttf -f my/path/familyid/ familyid
```
This creates a draft file `familyid_data.json` file in `local/datafiles/` that you can copy into a `fontmanifest.json` file. Then by removing the *defaults*, *files*, and *version* fields for hosted fonts (leave them in for non-hosted fonts) and filing in the *distributable*, *familyid*, *license*, *packageurl*, *siteurl*, *source*, *status* and *ziproot* fields you can create a `familyid_base.json` file.

## Updating the FLO index.html based on README.md

The single HTML page on FLO is derived from the README.md file. To regenerate the file run the following command (requires pandoc):

```
pandoc -s -f markdown-smart --template documentation/assets/html/template.html README.md -o index.html --metadata title="SIL Global"
```
