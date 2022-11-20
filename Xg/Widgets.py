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

from Xg.Core import XgEnums
from Xg.Gui import ColorPreset

_applicationInstance = None


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
        """Application main event loop"""
        if self._mainWindow:
            while not glfw.window_should_close(self._mainWindow._glfwWindow):
                glfw.poll_events()

                GL.glClearColor(*self._mainWindow.backgroundColor, 1)
                GL.glClear(GL.GL_COLOR_BUFFER_BIT)

                glfw.swap_buffers(self._mainWindow._glfwWindow)

            glfw.terminate()
        else:
            return


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
        """
        global _applicationInstance
        if not _applicationInstance:
            raise Exception('Application instance is not created.')

        self._width  = width
        self._height = height
        self._title  = title

        self.backgroundColor = ColorPreset(XgEnums.BaseColor.GREY, XgEnums.Shade.LIGHT).getRGBTuple()

        # initializing glfw library
        if not glfw.init():
            raise Exception('glfw cannot be initialized')
    
    def setBackgroundColor(self, color):
        self.backgroundColor = color.getRGBTuple()

    def show(self):
        """Show the main window"""
        global _applicationInstance

        self._glfwWindow = glfw.create_window(self._width, self._height, self._title, None, None)

        # check if window was created
        if not self._glfwWindow:
            glfw.terminate()
            raise Exception('glfw window can not be created')

        # set window position
        glfw.set_window_pos(self._glfwWindow, 400, 200)

        # make the context current
        glfw.make_context_current(self._glfwWindow)

        GL.glClearColor(*self.backgroundColor, 1)

        _applicationInstance._mainWindow = self
