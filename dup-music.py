#!/usr/bin/env python

import os
import re

root_dir = '/Users/calex/Music/iTunes/iTunes Media/Music'
patt = re.compile(r'\s1\.')

for _dir, _, _flist in os.walk(root_dir):
    if _flist:
        has_run = False
        for fname in _flist:
            result = patt.search(fname)
            if result != None:
                if not has_run:
                    print()
                    print(_dir)
                    print('*'*len(_dir))
                    print()
                print(f'File: {fname}')
        has_run = True
