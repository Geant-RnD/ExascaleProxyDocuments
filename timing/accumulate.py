#!/opt/local/bin/python3.6
#
# MIT License
#
# Copyright (c) 2018, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory (subject to receipt of any
# required approvals from the U.S. Dept. of Energy).  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

''' @file plotting.py
Plotting routines for TiMemory module
'''

from __future__ import absolute_import
from __future__ import division

__author__ = "Jonathan Madsen"
__copyright__ = "Copyright 2018, The Regents of the University of California"
__credits__ = ["Jonathan Madsen"]
__license__ = "MIT"
__version__ = "2.4.0"
__maintainer__ = "Jonathan Madsen"
__email__ = "jonrobm.programming@gmail.com"
__status__ = "Development"
__all__ = ['plot',
           'plot_maximums',
           'plot_timing',
           'plot_memory',
           'plot_generic',
           'read',
           'plot_data',
           'timemory_data',
           'echo_dart_tag',
           'add_plotted_files',
           'make_output_directory',
           'nested_dict',
           'plot_parameters',
           'plotted_files',
           'timemory_types']

import sys
import os
import imp
import copy
import json
import ctypes
import platform
import warnings
import importlib
import traceback
import collections

__dir__ = os.path.realpath(os.path.dirname(__file__))

if os.environ.get("DISPLAY") is None and os.environ.get("MPLBACKEND") is None:
    os.environ.setdefault("MPLBACKEND", "agg")

_matplotlib_backend = None
# a previous bug inserted wrong value for levels, this gets around it
_excess_levels = 64

#------------------------------------------------------------------------------#
# check with timemory.options
#
try:
    import timemory.options
    if timemory.options.matplotlib_backend != "default":
        _matplotlib_backend = timemory.options.matplotlib_backend
except:
    pass


#------------------------------------------------------------------------------#
# if not display variable we probably want to use agg
#
if (os.environ.get("DISPLAY") is None and
    os.environ.get("MPLBACKEND") is None and
    _matplotlib_backend is None):
    os.environ.setdefault("MPLBACKEND", "agg")


#------------------------------------------------------------------------------#
# tornado helps set the matplotlib backend but is not necessary
#
try:
    import tornado
except:
    pass


#------------------------------------------------------------------------------#
# import matplotlib and pyplot but don't fail
#
try:
    import matplotlib
    import matplotlib.pyplot as plt
    _matplotlib_backend = matplotlib.get_backend()
except:
    try:
        import matplotlib
        matplotlib.use("agg", warn=False)
        import matplotlib.pyplot as plt
        _matplotlib_backend = matplotlib.get_backend()
    except:
        pass


#------------------------------------------------------------------------------#
#
#
_default_timing_types = ['wall', 'sys', 'user', 'cpu', 'perc']
""" Default timing data to extract from JSON """

_default_memory_types = ['total_peak_rss', 'total_current_rss',
                         'self_peak_rss', 'self_current_rss']
""" Default memory data to extract from JSON """


_default_timing_fields = ['wall', 'sys', 'user']
""" Default fields for reducing # of timing plot functions displayed """

_default_memory_fields = ['total_peak_rss', 'total_current_rss',
                          'self_peak_rss', 'self_current_rss']
""" Default fields for reducing # of memory plot functions displayed """

_default_timing_min_percent = 0.05 # 5% of max
""" Default minimum percent of max when reducing # of timing functions plotted """

_default_memory_min_percent = 0.05 # 5% of max
""" Default minimum percent of max when reducing # of memory functions plotted """

_default_img_dpi = 75
""" Default image dots-per-square inch """

_default_img_size = {'w': 1600, 'h': 800}
""" Default image size """

_default_img_type = 'jpeg'
""" Default image type """

plotted_files = []
""" A list of all files that have been plotted """

timemory_types = _default_timing_types + _default_memory_types
""" Data fields stored in timemory_data """



#==============================================================================#
def make_output_directory(directory):
    """
    mkdir -p
    """
    if not os.path.exists(directory) and directory != '':
        os.makedirs(directory)


#==============================================================================#
def nested_dict():
    return collections.defaultdict(nested_dict)


#==============================================================================#
class timemory_data():
    """
    This class is for internal usage. It holds the JSON data
    """
    # ------------------------------------------------------------------------ #
    def __init__(self, func, types = timemory_types, extract_data=None):
        self.laps = 0
        self.types = types
        self.func = func
        self.data = nested_dict()
        self.sums = {}
        for key in self.types:
            self.data[key] = []
            self.sums[key] = 0.0
        # populate data and sums from existing data
        if extract_data is not None:
            self.laps = extract_data.laps
            for key in self.types:
                self.data[key] = extract_data.data[key]
                self.sums[key] = extract_data.sums[key]
        self.delim_below = False

    # ------------------------------------------------------------------------ #
    def process(self, denom, obj, nlap):
        """
        record data from JSON object
        """
        _wall = obj['wall_elapsed'] / denom
        _user = obj['user_elapsed'] / denom
        _sys = obj['system_elapsed'] / denom
        _cpu = obj['cpu_elapsed'] / denom
        _MB = (1.0)
        _tpeak = obj['rss_max']['peak'] / _MB
        _tcurr = obj['rss_max']['current'] / _MB
        _speak = obj['rss_self']['peak'] / _MB
        _scurr = obj['rss_self']['current'] / _MB
        _perc = (_cpu / _wall) * 100.0 if _wall > 0.0 else 100.0
        _dict = {
            'wall' : _wall,
            'sys' : _sys,
            'user' :_user,
            'cpu' : _cpu,
            'perc' : _perc,
            'total_peak_rss' : _tpeak,
            'total_current_rss' : _tcurr,
            'self_peak_rss' : _speak,
            'self_current_rss' : _scurr }
        self.append(_dict)
        self.laps += nlap

    # ------------------------------------------------------------------------ #
    def __lt__(self, other):
            return self.sums['wall'] > other.sums['wall']


    # ------------------------------------------------------------------------ #
    def plottable(self, _params):
        """
        valid data above minimum
        """
        # compute the minimum values
        t_min = (0.01 * _params.timing_min_percent) * _params.timing_max_value
        m_min = (0.01 * _params.memory_min_percent) * _params.memory_max_value

        # function for checking passes test
        def is_valid(key, min_value):
            if key in self.sums.keys():
                # compute it's "percentage" w.r.t. max value
                return abs(self.sums[key]) > min_value
            return False

        # check the timing fields
        for field in _params.timing_fields:
            if is_valid(field, t_min):
                return True
        # check the memory fields
        for field in _params.memory_fields:
            if is_valid(field, m_min):
                return True

        # all values below minimum --> do not plot
        return False

    # ------------------------------------------------------------------------ #
    def insert(self, key, val):
        self.sums[key] = val

    # ------------------------------------------------------------------------ #
    def wall(self):
        return self.sums['wall']

    # ------------------------------------------------------------------------ #
    def cpu(self):
        return self.sums['cpu']

    # ------------------------------------------------------------------------ #
    def get(self, key):
        return self.sums[key]

    # ------------------------------------------------------------------------ #
    def header(self):
        s = "| {:^40s} | ".format("ITEM")
        for key, value in self.sums.items():
            if key in _default_memory_types or key == 'sys' or key == 'perc' or key == 'user':
                continue
            s += "{:^12s} | ".format(key.upper())
        s += "{:^12s} |".format("LAPS")
        n = len(s)
        s = "{}\n{}".format('-'*n, s)
        s += "\n{}".format('-'*n)
        return s

    # ------------------------------------------------------------------------ #
    def __str__(self):
        s = "| {:40s} | ".format(self.func)
        for key, value in self.sums.items():
            if key in _default_memory_types or key == 'sys' or key == 'perc' or key == 'user':
                continue
            tmp = None
            if key == 'perc':
                tmp = (self.sums['cpu'] / self.sums['wall']) * 100.0
            else:
                tmp = value
            if 'perc' in key or 'agg' in key:
                s += "{:>12s}".format("{:10.3f} % | ".format(tmp))
            else:
                s += "{:12.3f} | ".format(tmp)
        s += "{:12} |".format(self.laps)
        if self.delim_below:
            n = len(s)
            s += "\n{}".format('-'*n)
        return s

    # ------------------------------------------------------------------------ #
    def append(self, _dict):
        """
        append data to dataset
        """
        for key in self.types:
            self.data[key].append(_dict[key])
            # add entry if not exist
            self.sums[key] += _dict[key]

    # ------------------------------------------------------------------------ #
    def __add__(self, rhs):
        """
        for combining results (typically from different MPI processes)
        """
        for key in self.types:
            self.data[key].extend(rhs.data[key])
            for k, v in rhs.data.items():
                if isinstance(v, list):
                    for _v in v:
                        self.sums[k] += _v
                else:
                    self.sums[k] += v
        self.laps += rhs.laps

    # ------------------------------------------------------------------------ #
    def __sub__(self, rhs):
        """
        for differencing results (typically from two different runs)
        """
        for key in self.types:
            # if the lengths are the same, compute difference
            if len(self.data[key]) == len(rhs.data[key]):
                for i in len(self.data[key]):
                    self.data[key][i] -= rhs.data[key][i]
            else: # the lengths are different, insert the entries as neg values
                for entry in rhs.data[key]:
                    self.data[key].append(-entry)
            # compute the sums
            for k, v in rhs.data.items():
                self.sums[k] += v
        # this is a weird situation
        if self.laps != rhs.laps:
            self.laps = max(self.laps, rhs.laps)

    # ------------------------------------------------------------------------ #
    def reset(self):
        """
        clear all the data
        """
        self.data = nested_dict()
        for key in self.types:
            self.data[key] = []
            self.sums[key] = 0.0

    # ------------------------------------------------------------------------ #
    def __getitem__(self, key):
        """
        array indexing
        """
        return self.data[key]

    # ------------------------------------------------------------------------ #
    def keys(self):
        """
        get the keys
        """
        return self.data.keys()

    # ------------------------------------------------------------------------ #
    def __len__(self):
        """
        length operator
        """
        _maxlen = 0
        for key in self.data.keys():
            _maxlen = max(_maxlen, len(self.data[key]))
        return _maxlen

    # ------------------------------------------------------------------------ #
    def get_order(self, include_keys):
        """
        for getting an order based on a set of keys
        """
        order = []
        sorted_keys = sorted(self.sums, key=lambda x: abs(self.sums[x]))
        for key in sorted_keys:
            if key in include_keys:
                order.append(key)
        return order


#==============================================================================#
def read(json_obj, functions = nested_dict()):
    """
    Read the JSON data -- i.e. process JSON object of TiMemory data
    """

    # some fields
    data0 = json_obj
    manager_tag = 'manager'

    # ------------------------------------------------------------------------ #
    # loop over ranks
    for i in range(0, len(data0['ranks'])):
        # shorthand
        data1 = data0['ranks'][i]

        # loop over timers
        for j in range(0, len(data1[manager_tag]['timers'])):
            data2 = data1[manager_tag]['timers'][j]
            # construct the tag
            tag = '{}'.format(data2['timer.tag'])
            tag = tag[4:]

            if tag == 'global_time':
                continue

            # create timemory_data object if doesn't exist yet
            if not tag in functions:
                #print('Tag {} does not exist'.format(tag))
                functions[tag] = timemory_data(func=tag)
            # get timemory_data object
            timemory_func = functions[tag]

            # process the function data
            timemory_func.process(data2['timer.ref']['to_seconds_ratio_den'],
                                  data2['timer.ref'],
                                  int(data2['timer.ref']['laps']))

    return functions


#==============================================================================#
def process(args):
    """
    A function to accumulate JSON data
    """
    functions = nested_dict()
    if len(args.input) > 0:
        for filename in args.input:
            print ('Reading {}...'.format(filename))
            f = open(filename, "r")
            functions = read(json.load(f), functions)
            f.close()

    _particles = []
    _processes = []

    def create_name(prefix, base):
        _ldash = base.rfind('/')
        if _ldash > 0:
            _ldash += 1
            return base[:_ldash] + prefix + base[_ldash:]
        else:
            return prefix + base

    def within_list(_key, _list):
        for _l in _list:
            if _l == _key or 'anti_{}'.format(_l) == _key:
                return True
        return False


    _out_particles = open(create_name("particles_", args.output), 'w')
    _out_processes = open(create_name("processes_", args.output), 'w')
    _filter = ['nu_e', 'nu_mu', 'eta_prime', 'proton', 'neutron', 'lambda', 'sigma+',
              'sigma-', 'sigma0', 'xi0']
    try:
        for key, val in functions.items():
            if "_" in key and not within_list(key, _filter):
                _processes.append(val)
            else:
                _particles.append(val)

        _particles.sort()
        _processes.sort()

        _part_wall = 0.0
        _part_cpu = 0.0
        _proc_wall = 0.0
        _proc_cpu = 0.0

        for _l in _particles:
            _part_wall += _l.wall()
            _part_cpu += _l.cpu()

        for _l in _processes:
            _proc_wall += _l.wall()
            _proc_cpu += _l.cpu()

        for _l in _particles:
            _l.insert("perc_wall", _l.wall() / _part_wall * 100)
            _l.insert("perc_cpu", _l.cpu() / _part_cpu * 100)

        for _l in _processes:
            _l.insert("perc_wall", _l.wall() / _proc_wall * 100)
            _l.insert("perc_cpu", _l.cpu() / _proc_cpu * 100)

        def print_info(_title, _list, _out, _verbose):
            if args.verbose > 0:
                print("\n{}:\n".format(_title))

            n = 0
            _wcum = 0.0
            _ccum = 0.0
            for _l in _list:
                if n + 1 == len(_list) or n % 5 == 4:
                    _l.delim_below = True
                _wcum += _l.get('perc_wall')
                _ccum += _l.get('perc_cpu')
                _l.insert("agg_wall", _wcum)
                _l.insert("agg_cpu", _ccum)
                if _verbose > 0:
                    if n == 0:
                        print("{}".format(_l.header()))
                    print("{}".format(_l))
                if n == 0:
                    _out.write("{}\n".format(_l.header()))
                _out.write("{}\n".format(_l))
                n += 1

        print_info("Particles", _particles, _out_particles, args.verbose)
        print_info("Processes", _processes, _out_processes, args.verbose)

    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback, limit=5)
        print ('Exception - {}'.format(e))

    _out_particles.close()
    _out_processes.close()

#==============================================================================#
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output file", default="out.txt", type=str)
    parser.add_argument("-i", "--input", help="Input files", nargs='*', type=str, required=True)
    parser.add_argument("-v", "--verbose", help="Verbose", type=int, default=0)
    args = parser.parse_args()

    ret = 0
    try:
        process(args)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(
            exc_type, exc_value, exc_traceback, limit=5)
        print('Exception - {}'.format(e))
        ret = 1

    sys.exit(ret)
