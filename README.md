FontRename
==========

This script attempts to rename TTF fonts according to the name stored in the TTF header. This is useful particularly with font packs which have poorly thought out naming (e.g. 1.ttf, 2.ttf, 3.ttf). It does this by brute force extraction of the font name.

Usage: ./font-rename.py [directory]

In the directory (if not provided, the current working directory), two new directories will be created "old/" and "renamed/".

Then, all files in that directory that end in ".ttf" will be renamed according to the data in the TTF header. Fonts will be moved unchanged to "old/{original\_name}.ttf" and renamed to "renamed/{new\_name}.ttf"

License
-------

Copyright (c) 2003, 2011 Samuel G. D. Williams. <http://www.oriontransfer.co.nz>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.