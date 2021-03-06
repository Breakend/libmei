
"""
    Copyright (c) 2012 Andrew Hankinson
    
    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:
    
    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
    OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from pymei import MeiElement


class barre_(MeiElement):
    def __init__(self):
        MeiElement.__init__(self, "barre")
    # <barre>

class chordDef_(MeiElement):
    def __init__(self):
        MeiElement.__init__(self, "chordDef")
    # <chordDef>

class chordMember_(MeiElement):
    def __init__(self):
        MeiElement.__init__(self, "chordMember")
    # <chordMember>

class chordTable_(MeiElement):
    def __init__(self):
        MeiElement.__init__(self, "chordTable")
    # <chordTable>

class f_(MeiElement):
    def __init__(self):
        MeiElement.__init__(self, "f")
    # <f>

class fb_(MeiElement):
    def __init__(self):
        MeiElement.__init__(self, "fb")
    # <fb>

class harm_(MeiElement):
    def __init__(self):
        MeiElement.__init__(self, "harm")
    # <harm>

