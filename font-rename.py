#!/usr/bin/python

# This script attempts to rename TTF fonts according to the name stored in the TTF header. This is useful particularly with font packs which have poorly thought out naming (e.g. 1.ttf, 2.ttf, 3.ttf).

# Usage: ./font-rename.py [directory]
# In the directory (if not provided, the current working directory), two new directories will be created "old/" and "renamed/".
# Then, all files in that directory that end in ".ttf" will be renamed according to the data in the TTF header. Fonts will be moved unchanged to "old/{original_name}.ttf" and renamed to "renamed/{new_name}.ttf"

# Copyright (c) 2003, 2011 by Samuel Williams.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys, os, shutil, fnmatch, re
from struct import *;
import string

font_name_identifiers = ("Copyright Notice", "Font Family", "Font Subfamily",
"Unique Subfamily Identification", "Real Name", "Version", "PostScript Name",
"Trademark notice", "Manufacturer Name", "Designer", "Description", "Vendor URL",
"Designer URI", "License Description", "License Information URL", "Reserved",
"Preferred Family", "Preferred Subfamily", "Full Name", "Sample Text")

def ttf_getname(fname):
    f = open(fname, "r")
    version, tnum, searchrange, entryselector, rangeshift = unpack (">iHHHH", f.read(12))
    
    # Read TTF headers
    headers = {}
    for i in range(0, tnum):
        tag = f.read(4)
        headers[tag] = unpack (">LLL", f.read(12))
    
    # Find name header
    cs, ofs, len = headers['name'];
    f.seek (ofs);
    format, count, strofst = unpack(">HHH", f.read(6));
    
    # We open the file a second time because we will be seeking to different parts with +p+ 
    # while iterating over the addresses in +f+.
    p = open(fname, "r");
    fontname = ""
    for i in range(0, count):
        platform, encoding, language, name, length, offset = unpack(">HHHHHH", f.read(12));
        # print font_name_identifiers[name];
        if ((name == 4) | (name == 6)) & ((platform == 1) | (platform == 3)):
            p.seek(ofs + strofst + offset);
            fontname = p.read(length);
    
    f.close()
    p.close()
    
    return fontname;

def nicename(name):
    name = string.lower (name)
    rname = ""
    for c in name:
        if (ord (c) >= 97) & (ord (c) < 123):
            rname = rname + c
    return string.lower (rname)

if len(sys.argv) == 2:
    os.chdir(sys.argv[1])

try:
    os.mkdir("old")
except:
    pass

try:
    os.mkdir("renamed")
except:
    pass

ttfname = re.compile(".*\.ttf", re.I)

for origname in os.listdir("."):
    if ttfname.match(origname):
        new_name = nicename(ttf_getname(origname))
        print new_name
        if new_name != "":
            shutil.copy(origname, "renamed/" + new_name + ".ttf")
            shutil.move(origname, "old/" + origname)
