# -*- coding: utf-8 -*-
#
# Copyright 2010-2014 The pygit2 contributors
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# In addition to the permissions in the GNU General Public License,
# the authors give you unlimited permission to link the compiled
# version of this file into combinations with other programs,
# and to distribute those combinations without any restriction
# coming from the use of this file.  (The General Public License
# restrictions do apply in other respects; for example, they cover
# modification of the file, and distribution when not linked into
# a combined executable.)
#
# This file is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA.

# Import from the future
from __future__ import absolute_import

# Import from the Standard Library
import inspect
import codecs
import os
from os.path import abspath, dirname

# Import from cffi
from cffi import FFI

# Import from pygit2
from libgit2 import get_libgit2_paths


ffi = FFI()

dir_path = dirname(abspath(inspect.getfile(inspect.currentframe())))
decl_path = os.path.join(dir_path, 'decl.h')
with codecs.open(decl_path, 'r', 'utf-8') as header:
    ffi.cdef(header.read())

libgit2_bin, libgit2_include, libgit2_lib = get_libgit2_paths()
C = ffi.verify("#include <git2.h>", libraries=["git2"],
               include_dirs=[libgit2_include], library_dirs=[libgit2_lib])
