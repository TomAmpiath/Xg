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

from __future__ import annotations

from typing import Optional, Tuple

import Xg.Core
import Xg.Gui

class Color:
    
    def __init__(
        self  : Xg.Gui.Color,
        red   : Optional[int] = ...,
        green : Optional[int] = ...,
        blue  : Optional[int] = ...)                     -> None                    : ...

    def __add__(self: Xg.Gui.Color, color: Xg.Gui.Color) -> Xg.Gui.Color            : ...

    def __sub__(self: Xg.Gui.Color, color: Xg.Gui.Color) -> Xg.Gui.Color            : ...

    def __mul__(self: Xg.Gui.Color, scalar: int)         -> Xg.Gui.Color            : ...

    def __truediv__(self: Xg.Gui.Color, scalar: int)     -> Xg.Gui.Color            : ...

    def __repr__(self: Xg.Gui.Color)                     -> str                     : ...

    def getHexColor(self: Xg.Gui.Color)                  -> str                     : ...

    def getRGBTuple(self: Xg.Gui.Color)                  -> Tuple[int, int, int]    : ...


class ColorPreset(Xg.Gui.Color):

    def __init__(
        self       : Xg.Gui.ColorPreset,
        base_color : Xg.Core.XgEnums.BaseColor,
        shade      : Xg.Core.XgEnums.Shade)              -> None                     : ...

# class ShadedColor(Xg.Gui.Color):

#     def __init__(
#         self: Xg.Gui.Color,
#         red_shade: Xg.Core.XgEnums.Shade,
#         green_shade: Xg.Core.XgEnums.Shade,
#         blue_shade: Xg.Core.XgEnums.Shade)              -> None                   : ...
