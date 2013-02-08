#!/usr/bin/python3 -tt

# Copyright 2013 Jussi Pakkanen

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys, pickle

class InstallData():
    def __init__(self, src_dir, build_dir):
        self.src_dir = src_dir
        self.build_dir = build_dir

def do_install(datafilename):
    ifile = open(datafilename, 'rb')
    d = pickle.load(ifile)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Installer script for Builder. Do not run on your own, mmm\'kay?')
        print('%s [install info file]' % sys.argv[0])
    datafilename = sys.argv[1]
    do_install(datafilename)

