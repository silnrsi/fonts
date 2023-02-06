#!/usr/bin/python3
__doc__ = '''Create draft base.json files'''
__url__ = 'http://github.com/silnrsi/fonts'
__copyright__ = 'Copyright (c) 2023 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

import os
from silfont.gfr import gfr_base, gfr_manifest, gfr_family, setpaths
from silfont.core import execute

argspec = [
    ('incsv',{'help': 'Input csv file'}, {'type': 'incsv'}),
    ('-t','--type', {'help': 'Font type(s) to process', 'action': 'append'}, {}),
    ('-f','--familyid', {'help': 'Familyid to process', 'action': 'append'}, {}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': 'createbase.log'})]

'''
This script is a short-term script for creating draft base.json files from a csv export of an internal WSTech spreadsheet.

By default it will run against all lines in the spreadsheet excluding those where the type is FLO-future or the status is future
If -type is specified it will just run against those matching the specific type(s) supplied
If -familyid is specified it will just run against that specific font(s) supplied

As well as writing to a log file it will write a summary out to local/createbasefilesresults.csv

If it determines the data for a specific font is in valid, it will still output the base file but add _invalid to the file name.

This script is designed to be run from the root folder of the repository locates other files relative to there
- The incsv is usually in  fonts/local/
- Manifest files for for FLO-SIL fonts with be in fonts/fonts/sil/<familyid>/ folders
- Manifest files for for FLO-other fonts with be in fonts/fonts/other/<familyid>/ folders
- The draft base.json files will be output to fonts/local/draftbases/
'''

headers = ['type', 'familyid', 'family', 'fallback', 'version', 'siteurl', 'packageurl', 'source', 'license', 'status', 'defaults/ttf', 'defaults/woff', 'defaults/woff2', 'hosturl', 'filesroot']
fields =          ['familyid', 'family', 'fallback', 'version', 'siteurl', 'packageurl', 'source', 'license', 'status', 'defaults',                                        'hosturl', 'filesroot']

def doit(args) :
    global headers
    logger = args.logger
    incsv = args.incsv

    # Read the first line and create index to column positions within the csv.
    fl = incsv.firstline
    colindex = {}
    missing = []
    for header in headers:
        col = fl.index(header) if header in fl else None
        if col is None:
            missing.append(header)
        else:
            colindex[header] = col
    if missing:
        logger.log(f'Headers missing from incsv {str(missing)}', 'S')

    # Set up paths to folders
    (repopath, silpath, otherpath, basespath) = setpaths(logger)
    outdir = os.path.join(repopath, "local/draftbases")
    if not os.path.isdir(outdir): os.mkdir(outdir)

    # Now process the csv and produce the base files
    resultssummary = []
    next(incsv.reader, None)  # Skip first line with headers in
    for line in incsv:
        fdata = fontdata(line, colindex)
        familyid = fdata.familyid
        ftype = fdata.type

        # If --type or --familyid used, only process matching records
        if args.type and ftype not in args.type: continue
        if args.familyid and familyid not in args.familyid: continue

        valid = True
        invalidreason = None # For recording why the data is invalid
        # create initial family data
        basedata = {}
        for field in fields:
            val = getattr(fdata, field)
            if val != "" and val != {} : basedata[field] = val

        basedata["distributable"] = True if ftype not in ("nodist", "nosource") else False

        # Now need to do further checks and add further data depending on record type
        if ftype in ("FLO-SIL", "FLO-other"): # Just works for FLO-SIL currently
            # Open the manifest file, if present
            mname = os.path.join(silpath, familyid, "fontmanifest.json")
            if os.path.isfile(mname):
                manifest = gfr_manifest(filename=mname, logger=logger)
                manifest.read()
                logger.log(f'Checking {mname} for {manifest.id}', 'P')
                (valid, logs) = manifest.validate(version=fdata.version)
                if not valid: invalidreason = f'Font manifest {mname} is not valid; check using checkmanifest.py for details'
                del basedata['version'] # The version is stored in the manifest so should not be in the base file
            else:
                valid = False
                invalidreason = f'Font manifest {mname} does not exist'
            #anything else to do to data for these types?

        # Now create the base file
        basefile = gfr_base(id=familyid, data=basedata, logger=logger)
        (bvalid, logs) = basefile.validate()
        if not bvalid:
            if not valid: # Already found to be invalid above, so log that first
                logger.log(invalidreason, "W")
            else:
                invalidreason = "Errors in the base file data - see log file"
            valid = False
            for logmess in logs:
                logger.log(logmess[0], logmess[1])

        if valid:
            summarymess = f'{familyid}, Valid'
        else:
            summarymess = f'{familyid}, Invalid: {invalidreason}'
        resultssummary.append(summarymess)

        # Write the base file out
        bext = ".json" if valid else ".json_invalid"
        bname = os.path.join(outdir, familyid + "_base" + bext)
        basefile.write(bname)

    # Write results summary to file
    filename = os.path.join(repopath, "local", "createbasefilesresults.csv")
    with open(filename, "w", encoding="utf-8") as outf:
        for line in resultssummary: outf.write(line + "\n")

    return

class fontdata(object):
    def __init__(self, csvline, colindex):
        global headers
        for header in headers:
            if "/" not in header: # Those with / in will be defaults which are handled differently below
                setattr(self, header, csvline[colindex[header]])
        self.defaults = {}
        for dtype in ("ttf", "woff", "woff2"):
            default = csvline[colindex[f'defaults/{dtype}']]
            if default != "": self.defaults[dtype] = default


def cmd(): execute("", doit, argspec)

if __name__ == "__main__": cmd()

