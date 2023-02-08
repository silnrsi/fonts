#!/usr/bin/python3
__doc__ = '''Create a draft font manifest or base file based on content of folder'''
__url__ = 'http://github.com/silnrsi/fonts'
__copyright__ = 'Copyright (c) 2023 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

import re

from silfont.gfr import gfr_manifest, setpaths, getttfdata
from silfont.core import execute, splitfn
import os

argspec = [
    ('fontid',{'help': 'ID for the font'}, {}),
    #('fontfamily',{'help': 'Font family name','nargs': '?'},{}),
    #('version',{'help': 'Font version','nargs': '?'},{}),
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
        outfile = os.path.join(fontpath, "fontmanifest_draft2.json")
    else:
        outfile = os.path.join(repopath, "local/datafiles", f'{fontid}_data.json')

    # Now find the font files within the folder
    fontexts = ['.ttf', '.woff', '.woff2']
    dfilelist = {}
    for dirname, subdirs, filenames in os.walk(fontpath):
        for filen in filenames:
            (base, ext) = os.path.splitext(filen)
            if ext in fontexts:
                dfilelist[filen] = (os.path.relpath(os.path.join(dirname, filen), start=fontpath))

    if len(dfilelist) == 0: logger.log(f'No font files found in {fontpath}', "S")

    defaults = {}
    files = {}
    regulars = {".ttf": {}, ".woff": {}, ".woff2": {}}
    # Build up the data...
    for fontfile in dfilelist:
        (path,base,ext) = splitfn(fontfile)
        ttfdata = getttfdata(os.path.join(fontpath, dfilelist[fontfile]), logger)
        regular = True if ttfdata["subfamily"] == "Regular" else False
        if regular:
            regulars[ext][fontfile] = {
                "family": ttfdata["family"],
                "version": ttfdata["version"],
                "wght": ttfdata["wght"]
            }

        files[fontfile] = {'axes': {"ital": ttfdata["ital"], "wght": float(ttfdata["wght"]),}, "packagepath": dfilelist[fontfile]}

    # Of the fonts with a subfamily of "Regular" determine the default regular
    for ext in fontexts:
        regs = regulars[ext]
        if len(regs) == 0:
            regular = None
        elif len(regs) == 1:
            regular = list(regs)[0] # Key for only item in dict
        else: # Multiple, so which is the default...
            regular = None
            w400 = None
            for regn in regs:
                reg = regs[regn]
                if "Regular" in regn:
                    regular = regn
                elif int(reg["wght"]) == 400:
                    regular = regn
        if regular:
            defaults[ext[1:]] = regular
            if ext == ".ttf": # Take version and family from regular ttf
                reg = regulars[ext][regular]
                version = reg["version"]
                family = reg["family"]

    if defaults == {}:
        logger.log("No regular weights found so defaults, version and family not set", "W")
        defaults["ttf"] = ".ttf"
        defaults["woff"] = ".woff"
        defaults["woff"] = ".woff2"
        version = 0.0
        family = ""

    if not re.match("^[0-9]\.[0-9][0-9][0-9]$", version):
        logger.log('Version not of form n.nnn so will need checking/editing', "W")

    data = {
        "defaults": defaults,
        "family": family,
        "files": files,
        "version": version
    }
    manifest = gfr_manifest(id = fontid, data = data, logger = logger)
    manifest.write(outfile)

    return

def cmd(): execute("", doit, argspec)

if __name__ == "__main__": cmd()

