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
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': 'updatenoto.log'}),
    ('-f', '--family', {'help': "Single family to process"}, {})]


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
    'SemiCondensed': 87.5,
    'Condensed': 75,
    'ExtraCondensed': 62.5
}

default_axes = {'ital': 0, 'wght': 400.0, 'wdth': 100 }

def calc_axes(furl):
    fname = os.path.basename(furl)
    res = default_axes.copy()
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
            res['wdth'] = v
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

    (repopath, silpath, otherpath, basespath) = setpaths(logger)
    for dp, dn, fn in os.walk(basespath):
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
            allaxes = set()
            for furl in info.get('files', []):
                if 'full/ttf' not in furl:
                    continue
                b = furl.split("/")
                i = b.index("full")
                data['ziproot'] = b[i-1]
                ppath = "/".join(b[i:])
                axes = calc_axes(furl)
                allaxes.update([k for k, v in axes.items() if v != default_axes.get(k, None)])
                frecord = {
                    'packagepath': ppath,
                    'url': 'https://github.com/notofonts/notofonts.github.io/raw/main/' + furl,
                    'zippath': b[i-1] + "/" + ppath,
                    'axes': axes,
                }
                files[os.path.basename(furl)] = frecord
            allaxes.update(['wght'])
            if files:
                for k, v in files.items():
                    v['axes'] = {x: y for x, y in v['axes'].items() if x in allaxes}
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


