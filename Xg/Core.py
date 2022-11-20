# MIT License

# Copyright (c) 2022 Tom George Ampiath

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import enum


class XgEnums:

    class BaseColor(enum.Enum):

        GREY        : int = enum.auto()
        RED         : int = enum.auto()
        GREEN       : int = enum.auto()
        BLUE        : int = enum.auto()
    
    class Shade(enum.Enum):

        EXTRA_LIGHT : int = enum.auto()
        LIGHTER     : int = enum.auto()
        LIGHT       : int = enum.auto()
        NORMAL      : int = enum.auto()
        DARK        : int = enum.auto()
        DARKER      : int = enum.auto()
        EXTRA_DARK  : int = enum.auto()


class XgException:

    class UnsupportedColor(Exception): pass

    class UnsupportedColorScalar(Exception): pass