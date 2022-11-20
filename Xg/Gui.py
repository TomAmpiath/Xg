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

from Xg.Core import XgEnums, XgException


class Color:
    
    def __init__(self, red = 0, green = 0, blue = 0):
        """Initializes Color for given rgb values.

        Parameters
        ----------
        red: int
            Red value. (default is 0)
        green: int
            Green value. (default is 0)
        blue: int
            Blue value. (default is 0)
        
        Returns
        -------
        None.

        Raises
        ------
        XgException.UnsupportedColor
            When rgb values are not in range 0-255
        """
        if not all([color in range(0, 256) for color in (red, green, blue)]):
            raise XgException.UnsupportedColor('rgb values not in range 0-255')
        self.red   = red
        self.green = green
        self.blue  = blue

    def __add__(self, color):
        return Color(
            min(self.red   + color.red,   255),
            min(self.green + color.green, 255),
            min(self.blue  + color.blue,  255),
        )

    def __sub__(self, color):
        return Color(
            max(self.red   - color.red,   0),
            max(self.green - color.green, 0),
            max(self.blue  - color.blue,  0),
        )

    def __mul__(self, scalar):
        if scalar < 0:
            raise XgException.UnsupportedColorScalar(
                'Scalar should be greater than or equal to 0 for color multiplication'
            )
        return Color(
            min(int(self.red   * scalar), 255),
            min(int(self.green * scalar), 255),
            min(int(self.blue  * scalar), 255),
        )

    def __truediv__(self, scalar):
        if scalar <= 0:
            raise XgException.UnsupportedColorScalar(
                'Scalar should be greater than 0 for color division'
            )
        return Color(
            max(int(self.red   / scalar), 0),
            max(int(self.green / scalar), 0),
            max(int(self.blue  / scalar), 0),
        )


    def __repr__(self):
        return 'Xg.Gui.Color(red: %d, green: %d, blue: %d)' % (self.red, self.green, self.blue)

    def getHexColor(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)

    def getRGBTuple(self):
        return self.red, self.green, self.blue

    def getRGBTupleClamped(self):
        return self.red / 255.0, self.green / 255.0, self.blue / 255.0


class ColorPreset(Color):

    def __init__(self, base_color, shade):

        color = Color(0, 0, 0)

        if base_color   == XgEnums.BaseColor.GREY:
            color       += Color(127, 127, 127)
        elif base_color == XgEnums.BaseColor.RED:
            color       += Color(127, 0, 0)
        elif base_color == XgEnums.BaseColor.GREEN:
            color       += Color(0, 127, 0)
        elif base_color == XgEnums.BaseColor.BLUE:
            color       += Color(0, 0, 127)

        if shade        == XgEnums.Shade.EXTRA_DARK:
            color       /= 5.0
        elif shade      == XgEnums.Shade.DARKER:
            color       /= 2.22
        elif shade      == XgEnums.Shade.DARK:
            color       /= 1.33
        elif shade      == XgEnums.Shade.NORMAL:
            color       *= 1
        elif shade      == XgEnums.Shade.LIGHT:
            color       *= 1.25
        elif shade      == XgEnums.Shade.LIGHTER:
            color       *= 1.55
        elif shade      == XgEnums.Shade.EXTRA_LIGHT:
            color       *= 1.8

        super().__init__(*color.getRGBTuple())
