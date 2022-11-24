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

import inspect

import glfw
from OpenGL import GL

from Xg.Core import XgEnums, XgException
from Xg.Gui import Color, ColorPreset

_applicationInstance = None


def _hexColorToClampedRGB(hexColor):
    """Takes in a hexcolor object and returns the clamped rgb values.

    Parameters
    ----------
    hexColor: str
        The input HexColor value.

    Returns
    -------
    rgb_clamped: Tuple[float, float, float]
        RGB values clamped to range 0-1
    """
    stripped_hex = hexColor.lstrip('#')
    rgb_clamped = tuple(int(stripped_hex[i : i + 2], 16) / 255 for i in (0, 2, 4))
    return rgb_clamped


class Application:
    """Application instance of MyGUI. Only a sinlge instance of Application can be created"""

    def __init__(self):
        global _applicationInstance
        if not _applicationInstance:
            _applicationInstance = self
        else:
            raise Exception('Only single instane of Appplication can be created.')
        self._mainWindow = None

    def exec(self):
        """Application main event loop

        Returns
        -------
        None
        """
        if self._mainWindow:
            while not glfw.window_should_close(self._mainWindow._glfwWindow):
                glfw.poll_events()

                GL.glClearColor(*self._mainWindow.backgroundColor, 1)
                GL.glClear(GL.GL_COLOR_BUFFER_BIT)

                glfw.swap_buffers(self._mainWindow._glfwWindow)

                GL.glGetError()

            glfw.terminate()


class MainWindow:
    def __init__(self, title=inspect.stack()[-1].filename.split('/')[-1].rstrip('.py'), width=800, height=600):
        """The main window of the application

        Parameters
        ----------
        width: int
            Window width (default is 800)
        height :int
            Window height (default is 600)
        title: str
            Window title (default is File name of caller)

        Returns
        -------
        None

        Raises
        ------
        Exception
            When glfw cannot be initialized
        """
        global _applicationInstance
        if not _applicationInstance:
            raise Exception('Application instance is not created.')

        self._width = width
        self._height = height
        self._title = title

        self.backgroundColor = ColorPreset(XgEnums.BaseColor.GREY, XgEnums.Shade.LIGHTER).getRGBTupleClamped()

        # initializing glfw library
        if not glfw.init():
            raise Exception('glfw cannot be initialized')

    def setBackgroundColor(self, color):
        """Set the given color as the background color

        Parameters
        ----------
        color: Xg.Gui.Color | Xg.Core.HexColor | RGBClamped | RGBTuple
            The color to be set as background.

        Returns
        -------
        None

        Raises
        ------
        XgException.UnsupportedColor
            When passed argument is not a supported color object
        """
        if isinstance(color, Color):
            self.backgroundColor = color.getRGBTupleClamped()
        elif isinstance(color, str):
            self.backgroundColor = _hexColorToClampedRGB(color)
        elif isinstance(color, tuple) and all((isinstance(c, int) for c in color)):
            self.backgroundColor = tuple(c / 255 for c in color)
        elif isinstance(color, tuple) and all((isinstance(c, float) for c in color)):
            self.backgroundColor = color
        else:
            raise XgException.UnsupportedColor()

    def show(self):
        """Show the main window

        Returns
        -------
        None

        Raises
        ------
        Exception
            When glfw window cannot be created
        """
        global _applicationInstance

        self._glfwWindow = glfw.create_window(self._width, self._height, self._title, None, None)

        # check if window was created
        if not self._glfwWindow:
            glfw.terminate()
            raise Exception('glfw window can not be created')

        # make the context current
        glfw.make_context_current(self._glfwWindow)

        _applicationInstance._mainWindow = self
