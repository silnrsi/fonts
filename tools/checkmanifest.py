#!/usr/bin/python3
__doc__ = '''Validate a font manifest file'''
__url__ = 'http://github.com/silnrsi/fonts'
__copyright__ = 'Copyright (c) 2023 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

from silfont.gfr import gfr_manifest
from silfont.core import execute

argspec = [
    ('file',{'help': 'Manifest file to check'}, {'type': 'filename'}),
    ('-v','--version',{'help': 'Font version value to check'},{}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': '_checkmanifest.log'})]

def doit(args) :
    logger = args.logger

    manifest = gfr_manifest(filename=args.file, logger=logger)
    manifest.read()
    logger.log(f'Checking {args.file} for {manifest.id}', 'P')
    (valid, logs) = manifest.validate(version=args.version)

    if not valid:
        for logmess in logs:
            logger.log(logmess[0], logmess[1])
        logger.log("Manifest invalid", "S") # Needs to be a severe error so bash scripts can detect a problem

    return

def cmd(): execute("", doit, argspec)

if __name__ == "__main__": cmd()

