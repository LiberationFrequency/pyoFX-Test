# pyoFX-Test

A few code snippets to build a live digital audio effect rack based on python and pyo, nothing fancy, just to get an idea how pyo works.

Requirements:
* Python 2.x (https://www.python.org/downloads/)
* pyo (http://ajaxsoundstudio.com/software/pyo/)
* PyAudio (https://people.csail.mit.edu/hubert/pyaudio/)
** or Jack (http://jackaudio.org/)
* wxPython (http://www.wxpython.org/)
* Windows: ASIO4all (http://www.asio4all.com/)



== Installation ==

Windows:
---------
* Install the ASIO4all binary
* Install the python 2.7 32-bit binary
* Install PyAudio with "pip install pyaudio" - If that failed download a wheel from http://www.lfd.uci.edu/~gohlke/pythonlibs/ and use "pip install filename.whl"
* Install the wxPython 2.7 32-bit binary
* Install the pyo 32-bit binary

Linux:
---------
I am pretty sure you know what to do. 
* For ArchLinux there is a pyo AUR-PKGBUILD available (https://aur.archlinux.org/packages/python2-pyo/) 
> yaourt python2-pyo

* on Debian and forks there are definitely apt-packages available


MacOS:
----------
Sorry, I don't know in detail. You maybe have to adjust the server setting from portaudio to coreaudio.

For example:
> s = Server(sr=44100, buffersize=128, audio=coreaudio nchnls=1)



 
You maybe have to adjust the Server settings manually.

>python
>> from pyo import *

>> pa_list_devices()

Choose the input/output-device (with the lowest latency) and assign the number to the script.

Plug in your mic, guitar, bass, keyboard, whatever, play around, have fun, rock on, find your settings and build a preset.



License: 
pyoFX is published under the same conditions as pyo distributed.

pyoFX is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

pyoFX is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with pyoFX.  If not, see <http://www.gnu.org/licenses/>.




... work in progress.... please stand by
