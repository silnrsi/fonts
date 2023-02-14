#!/usr/bin/python3
__doc__ = '''Update Noto base.json files'''
__url__ = 'http://github.com/silnrsi/fonts'
__copyright__ = 'Copyright (c) 2023 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Martin Hosken'

import os, json, re
import urllib.request as urllib2
from silfont.gfr import gfr_base, gfr_manifest, gfr_family, setpaths
from silfont.core import execute

argspec = [
    ('dir', {'help': 'Directory containing noto base files'}, {'def': 'basefiles'}),
    ('-f', '--family', {'help': "Single family to process"}, {}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': 'updatenoto.log'})]


'''
This script reads the state.json file from the Google noto project and updates all the noto*_base.json files with the information found in state.json
'''

weights = {
    'Thin': 100.,
    'ExtraLight': 200.,
    'Light': 300.,
    'Regular': 400.,
    'Medium': 500.,
    'SemiBold': 600.,
    'Bold': 700.,
    'ExtraBold': 800.,
    'Black': 900.
}

condensation = {
    'SemiCondensed': 300,
    'Condensed': 200,
    'ExtraCondensed': 100
}

def calc_axes(furl):
    fname = os.path.basename(furl)
    res = {'ital': 0, 'wght': 400.0 }
    if "-" not in fname:
        return res
    style = fname[fname.rfind("-")+1:]
    style = style[:style.rfind(".")]
    if style.endswith("Italic"):
        res['ital'] = 1
        style = style[:-6]
    for k, v in condensation.items():
        if style.startswith(k):
            # set appropriate axes if any
            style = style[len(k):]
            break
    if style in weights:
        res['wght'] = weights[style]
    return res

def doit(args):
    logger = args.logger
    req = urllib2.Request(url="https://raw.githubusercontent.com/notofonts/notofonts.github.io/main/state.json")
    reqdat = urllib2.urlopen(req)
    jsondat = json.load(reqdat)
    reqdat.close()
    allfamilies = {}
    for k, v in jsondat.items():
        fs = v.get('families', None)
        if fs is None:
            continue
        for fk, fv in fs.items():
            allfamilies[fk] = fv

    for dp, dn, fn in os.walk(args.dir):
        for f in fn:
            m = re.match(r"^noto(.*?)_base.json", f)
            if m is None:
                continue
            fid = m.group(1)
            if args.family is not None and fid != args.family:
                continue
            base = gfr_base(filename=os.path.join(dp, f), logger=logger)
            base.read()
            data=base.data
            family = data["family"]
            if family not in allfamilies:
                logger.log(f'"base file {f} skipped - not represented in current state.json')
                continue
            info = allfamilies[family]
            vs = info.get('latest_release', {}).get('url', None)
            if vs is not None:
                data['siteurl'] = vs
                pname = os.path.basename(vs)
                data['packageurl'] = vs.replace('/tag/', '/download/') + "/" + pname + ".zip"
                data['version'] = info['latest_release'].get('version', 'v').replace('v', '')
            files = {}
            for furl in info.get('files', []):
                if 'full/ttf' not in furl:
                    continue
                b = furl.split("/")
                i = b.index("full")
                ppath = "/".join(b[i-1:])
                frecord = {
                    'packagepath': ppath,
                    'url': 'https://github.com/notofonts/notofonts.github.io/raw/main/' + furl,
                    'axes': calc_axes(furl)
                }
                files[os.path.basename(furl)] = frecord
            if files:
                data['files'] = files
            else:
                logger.log(f'No font files found for {f}')
            defaults = [x for x in files.keys() if '-Regular' in x]
            if len(defaults):
                data['defaults'] = {'ttf': defaults[0]}
            (valid,logs) = base.validate()
            if valid:
                base.write()
            else:
                logger.log(f'Invalid base file {f}', "E")
                logger.log(logs, "E")

def cmd(): execute("", doit, argspec)

if __name__ == "__main__": cmd()


