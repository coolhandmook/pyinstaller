# Copyright (C) 2007, Matteo Bertini
# Based on previous work under copyright (c) 2001, 2002 McMillan Enterprises, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

# Requires Python 2.5+

print "test_getfilesystemencoding"


import os
import sys
import subprocess
import email


if not type(email.Header) == email.LazyImporter:
    raise SystemExit('email.Header does not match.')


if hasattr(sys, 'frozen'):
    # In frozen mode current working directory is the path with final executable.
    pyexe_file = os.path.join('..', '..', 'python_exe.build')
else:
    pyexe_file = 'python_exe.build'


pyexe = open(pyexe_file).readline().strip()


frozen_encoding = str(sys.getfilesystemencoding())


# For various OS is encoding different.
if sys.platform.startswith('win'):
    encoding = subprocess.Popen([pyexe, '-c', 'import sys; print sys.getfilesystemencoding()'],
            stdout=subprocess.PIPE).stdout.read().strip()
# On Mac OS X the value should be still the same.
elif sys.platform.startswith('darwin'):
    encoding = 'utf-8'
# On Linux and other unixes it should be None.
# Please note that on Linux the value differs from the value
# in interactive shell.
else:
    encoding = 'None'


print('Encoding expected: ' + encoding)
print('Encoding current: ' + frozen_encoding)


if not frozen_encoding == encoding:
    raise SystemExit('Frozen encoding is not the same as unfrozen.')
