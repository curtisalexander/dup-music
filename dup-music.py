#!/usr/bin/env python

import os
import re

root_dir = os.path.join(os.path.expanduser('~'),
                        'Music/iTunes/iTunes Media/Music')

patt = re.compile(r'\s\d\.')

first_run = True

for _dir, _, _flist in os.walk(root_dir):
    if _flist:
        run_in_dir = False
        for fname in _flist:
            result = patt.search(fname)
            if result:
                if not run_in_dir:
                    if not first_run:
                        print()
                    print(_dir)
                    print('*'*len(_dir))
                    print()
                print(f'File: {fname}')
            first_run = False
        run_in_dir = True
