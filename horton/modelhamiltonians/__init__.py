# -*- coding: utf-8 -*-
# Horton is a development platform for electronic structure methods.
# Copyright (C) 2011-2013 Toon Verstraelen <Toon.Verstraelen@UGent.be>
#
# This file is part of Horton.
#
# Horton is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# Horton is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
#--
'''Input and output routines

   All input routines begin with ``load_``. All output routines begin with
   ``dump_``.

   This package also contains a ``Molecule`` class to facilitate reading from
   and writing to different file formats. It contains the methods ``from_file``
   and ``to_file`` that automatically determine the file format based on the
   prefix or extension of the filename.
'''


from horton.modelhamiltonians.physmodham import Hubbard
