#!/usr/bin/python3
__doc__ = '''Create ziproot entries in base.json files from packages'''
__url__ = 'http://github.com/silnrsi/fonts'
__copyright__ = 'Copyright (c) 2023 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Martin Hosken'

import os, json, re, io
import urllib.request as urllib2
from zipfile import ZipFile
from silfont.gfr import gfr_base, gfr_manifest, gfr_family, setpaths
from silfont.core import execute

argspec = [
    ('-l','--log' , {'help': 'Log file'}, {'type': 'outfile', 'def': 'createziproots.log'}),
    ('-F','--fresh', {'action': 'store_true', 'help': 'only process files with no ziproot already'}, {}),
    ('-f', '--family', {'help': "Single family to process"}, {})]

'''
This script iterates the base.json files. For each file with a packageurl, download the package and identify the root directory under which all the fonts, etc. are stored.
'''

def doit(args):
    logger = args.logger
    (repopath, silpath, otherpath, basespath) = setpaths(logger)

    for dp, dn, fn in os.walk(basespath):
        for f in fn:
            base = gfr_base(filename=os.path.join(dp, f), logger=logger)
            base.read()
            data=base.data
            logger.log(f"Working on {base.id}", "V")
            if args.family is not None and base.id != args.family:
                continue
            if args.fresh and 'ziproot' in data:
                continue
            purl = data.get('packageurl', None)
            if purl is None:
                continue    # no need to log this since many files will not have this
            for a in (silpath, otherpath):
                manifestpath = os.path.join(a, base.id, "fontmanifest.json")
                if os.path.exists(manifestpath):
                    manifest = gfr_manifest(filename=manifestpath, logger=logger)
                    manifest.read()
                    deffile = manifest.data['defaults']['ttf']
                    defppath = manifest.data['files'][deffile]['packagepath']
                    break
            else:
                if 'defaults' in data and 'files' in data:
                    deffile = data['defaults']['ttf']
                    defppath = data['files'][deffile]['packagepath']
                else:
                    logger.log(f'files or defaults missing from base file for {base.id}', "W")
                    continue
            logger.log(f"Downloading {purl}", "V")
            req = urllib2.Request(url=purl, headers={'User-Agent': 'Mozilla/4.0 (compatible; httpget)'})
            reqdat = urllib2.urlopen(req)
            zipdat = reqdat.read()
            zipinfile = io.BytesIO(initial_bytes=zipdat)
            zipf = ZipFile(zipinfile)
            for zf in zipf.namelist():
                if zf.endswith(defppath):     # found a font, assume we want it
                    ziproot = zf[:-len(defppath)-1] # strip trailing /
                    break
            else:
                logger.log(f"Can't find {defppath} in {purl}")
                ziproot = None
            if ziproot is not None:
                data['ziproot'] = ziproot
            (valid,logs) = base.validate()
            if valid:
                base.write()
            else:
                logger.log(f'Invalid base file {f}', "E")
                logger.log(logs, "E")
            zipf.close()
            zipinfile.close()


def cmd(): execute(None, doit, argspec)

if __name__ == "__main__": cmd()

