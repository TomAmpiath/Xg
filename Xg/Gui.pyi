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

from typing import Optional, Tuple, Union

import Xg.Core
import Xg.Gui

class Color:

    def __init__(self, red : Optional[int] = ..., green : Optional[int] = ..., blue : Optional[int] = ...) -> None: ...
    def __add__(self, color: Xg.Gui.Color) -> Xg.Gui.Color : ...
    def __sub__(self, color: Xg.Gui.Color) -> Xg.Gui.Color : ...
    def __mul__(self, scalar: Union[int, float]) -> Xg.Gui.Color : ...
    def __truediv__(self, scalar: Union[int, float]) -> Xg.Gui.Color : ...
    def __repr__(self) -> str : ...
    def getHexColor(self) -> str : ...
    def getRGBTuple(self) -> Tuple[int, int, int] : ...
    def getRGBTupleClamped(self) -> Tuple[float, float, float] : ...


class ColorPreset(Xg.Gui.Color):

    def __init__(self, base_color : Xg.Core.XgEnums.BaseColor, shade : Xg.Core.XgEnums.Shade) -> None : ...
