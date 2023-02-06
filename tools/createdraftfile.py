#!/usr/bin/python3
__doc__ = '''Create a draft font manifest or base file based on content of folder'''
__url__ = 'http://github.com/silnrsi/fonts'
__copyright__ = 'Copyright (c) 2023 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

from silfont.gfr import gfr_manifest, setpaths
from silfont.core import execute, splitfn
import os

argspec = [
    ('fontid',{'help': 'ID for the font'}, {}),
    ('fontfamily',{'help': 'Font family name'},{}),
    ('version',{'help': 'Font version'},{}),
    ('-t','--filetype',{'help': 'Type of file - m or b', 'default': 'm'}, {}),
    ('-f','--fontpath',{'help': 'Path for the font - required for base files'},{}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': '_createmanifest.log'})]

def doit(args) :
    logger = args.logger
    fontid = args.fontid
    (repopath, silpath, otherpath, basespath) = setpaths(logger)

    # Find the folder for the font
    filetype = args.filetype.lower()
    if args.fontpath:
        fontpath = args.fontpath
    elif filetype == 'b':
        logger.log('--fontpath must be specified if filetype is b', 'S')
    elif filetype == 'm':
        if os.path.isdir(os.path.join(silpath, fontid)):
            fontpath = os.path.join(silpath, fontid)
        elif os.path.isdir(os.path.join(otherpath, fontid)):
            fontpath = os.path.join(otherpath, fontid)
        else:
            logger.log(f'{fontid} not found in {silpath} or {otherpath}', "S")
    else:
        logger.log('Type must be m or b', "S")

    # Set the output file name
    if filetype == "m": # Create a draft manifest in the font's folder
        outfile = os.path.join(fontpath, "fontmanifest_draft.json")
    else:
        outfile = os.path.join(repopath, "local/datafiles", f'{fontid}_data.json')

    print(outfile)

    # Now find the font files within the folder
    fontexts = ['.ttf', '.woff', '.woff2']
    dfilelist = {}
    for dirname, subdirs, filenames in os.walk(fontpath):
        for filen in filenames:
            (base, ext) = os.path.splitext(filen)
            if ext in fontexts:
                dfilelist[filen] = (os.path.relpath(os.path.join(dirname, filen), start=fontpath))

    if len(dfilelist) == 0: logger.log(f'No font files found in {fontpath}', "S")
    print(dfilelist)
    defaultweights = {
        'ExtraLight': 200,
        'Light': 300,
        'Regular': 400,
        'Italic': 400,
        'Medium': 500,
        'SemiBold': 600,
        'Bold': 700,
        'ExtraBold': 800,
        'ExtraLightItalic': 200,
        'LightItalic': 300,
        'MediumItalic': 500,
        'SemiBoldItalic': 600,
        'BoldItalic': 700,
        'ExtraBoldItalic': 800
    }
    weightlist = ['ExtraLight','Light','Regular','Italic','Medium','SemiBold','Bold','ExtraBold']
    unmatched = 0
    defaults = {}
    files = {}
    # Build up the data...
    for fontfile in dfilelist:
        (path,base,ext) = splitfn(fontfile)
        weightn = "unmatched"
        for weight in weightlist:
            if f'{weight}Italic' in base:
                weightn = f'{weight}Italic'
            elif f'{weight}' in base:
                weightn = f'{weight}'
        if weightn == "unmatched":
                unmatched += 1
                weightn = f'unmatched{unmatched}'
                logger.log(f'Unable to match weight for {fontfile}', "W")
        weight = 999 if weightn[0:9] == "unmatched" else defaultweights[weightn]

        ital = 1 if "Italic" in base else 0

        if weightn == "Regular": defaults[ext[1:]] = fontfile
        files[fontfile] = {'axes': {"ital": ital, "wght": float(weight),}, "packagepath": dfilelist[fontfile]}
    if defaults == {}:
        logger.log("No regular weights found so defaults not set", "W")
        defaults["ttf"] = "Dummy"
    data = {
        "defaults": defaults,
        "family": args.fontfamily,
        "files": files,
        "version": args.version
    }
    manifest = gfr_manifest(id = fontid, data = data, logger = logger)
    manifest.write(outfile)

    return

def cmd(): execute("", doit, argspec)

if __name__ == "__main__": cmd()

