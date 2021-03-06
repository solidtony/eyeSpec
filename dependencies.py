## This imports modules eyeSpec is dependent on and performs some checks
# PURPOSE:
#   This file has all the dependencies used throughout eyeSpec
#   This allows for the control of versions
#   
# CATEGORY:
#   eyeSpec core
#
# MODIFICATION HISTORY:
#    13, June 2013: Dylan Gregersen
#    3,  July 2013: Dylan Gregersen
#                   more notes about necessary functions
#

#==============================================================================#
# Modules
import math
import time
import os
import sys
from copy import deepcopy
import pdb
import operator
iget = operator.itemgetter
import threading
import Queue
import subprocess
import re

#==============================================================================#
# wxPython
found_wx = True
try: import wxversion
except: found_wx = False

if found_wx:
    wxversion.ensureMinimal('2.8')
    import wx
    from wx.lib.newevent import NewEvent
else:
    print "HeadsUp: Many of the programs written in eyeSpec rely on wxPython which did not import into your version of python (try >> import wx) many of the more advanced interactive data editing probably won't work"
    wx = None

def check_for_wx ():
    if not found_wx: raise ValueError("This program relies on wxPython and wxversion which weren't found")

#==============================================================================#
# pyfits
try: import pyfits
except: raise ValueError("module pyfits is required for reading in data")

#==============================================================================#
# pickle
try: import cPickle as pickle
except: raise ValueError("module cPickle is required")

#==============================================================================#
# numpy
try: import numpy
except: raise ValueError("module numpy is required: http://www.numpy.org/")
np = numpy
check_version = numpy.__version__.split(".")
meets_min = True
c1 = check_version[0]
c2 = check_version[1]
c3 = check_version[2]

if c1 < 1: meets_min = False
elif c1 == 1 and c2 < 6: meets_min = False
elif c1 == 1 and c2 == 6 and c3 < 1: meets_min = False
if not meets_min: print "Warning: Numpy version is less than minimum, may encounter errors. 1.6.1 > "+check_version

import numpy.lib.recfunctions as np_recfunc


#==============================================================================#
# scipy
import scipy
check_version = scipy.__version__.split(".")
meets_min = True
c1 = check_version[0]
c2 = check_version[1]
c3 = check_version[2]

if c1 < 0: meets_min = False
elif c1 == 0 and c2 < 10: meets_min = False
elif c1 == 0 and c2 == 10 and c3 < 1: meets_min = False
if not meets_min:  print "Warning: scipy version is less than minimum, may encounter errors. 0.10.1 > "+check_version


#==============================================================================#
# Matplotlib
import matplotlib # Must have matplotlib for any eyeSpec internal plotting
mpl = matplotlib
if matplotlib.rcParams['backend'] != 'WXAgg':
    if sys.platform == 'darwin': # on a Mac
        if sys.version.find('64-bit') != -1:
            print "DANGER WILL ROBINSON: on a Mac OSX the WxAgg backend for the 64-bit EPD version of python is currently unavailable. You can TRY to fix this, but I did and (I assume) the EPD folks did and neither of us have found a solution. That said, eventually wxPython will be working with the libsraries of the Mac 64-bit system. Until then I suggest running this on a system which supports wxPython (32-bit on Mac works and is the most thoroughly tested). For now I'm going ahead with switching to the WxAgg backend but it'll probably crash on you. Have a great day!"
            # the other option is to write a different program, similar to below.
            # this basically is an interactive way to output a list of x-points which are the overlaps for different orders, as well as delete parts of orders.
    matplotlib.rcParams['backend'] = 'WXAgg'
    
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
FigureCanvas = FigureCanvasWxAgg

from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

from matplotlib.widgets import Button
import matplotlib.pylab as plt
#from matplotlib.ticker import LinearLocator, MultipleLocator
from matplotlib.pylab import FormatStrFormatter, savefig
from matplotlib.path import Path


if __name__ != "__main__":
    #==============================================================================#
    # resampling
    import resampling


