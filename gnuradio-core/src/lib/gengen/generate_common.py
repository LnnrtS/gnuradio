#!/usr/bin/env python
#
# Copyright 2004,2006,2007,2008,2009 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from build_utils import expand_template, standard_dict
from build_utils_codes import *

import re


# sources and sinks
ss_signatures = ['s', 'i', 'f', 'c']

ss_roots = [
    'gr_vector_source_X',
    'gr_vector_sink_X',
    ]

# regular blocks
reg_signatures = ['ss', 'ii', 'ff', 'cc']

reg_roots = [
    'gr_moving_average_XX',
    ]

# other blocks
others = (
    ('gr_peak_detector_XX',         ('fb','ib','sb')),
    )


def expand_h_cc_i (root, sig):
    # root looks like 'gr_vector_sink_X'
    name = re.sub ('X+', sig, root)
    d = standard_dict (name, sig)
    expand_template (d, root + '.h.t')
    expand_template (d, root + '.cc.t')
    expand_template (d, root + '.i.t')


def generate ():
    expand_h_cc_i ('gr_vector_sink_X', 'b')
    expand_h_cc_i ('gr_vector_source_X', 'b')
    for r in ss_roots:
        for s in ss_signatures:
            expand_h_cc_i (r, s)
    for r in reg_roots :
        for s in reg_signatures:
            expand_h_cc_i (r, s)

    for root, sigs in others:
        for s in sigs:
            expand_h_cc_i (root, s)



if __name__ == '__main__':
    generate ()


