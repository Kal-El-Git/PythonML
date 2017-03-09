import numpy as np

# time a command
a = np.random.randn(100,100)
%timeit np.dot(a,a)

import time 
start = time.time()# returns the current time


# start a PyQt console
ipython qtconsole --pylab=inline


# history of input
%hist
# loggging input/output
%logstart / %logstop / %logstate
%logoff / %logon

#interact with the OS
!cmd # run "cmd" in system shell

# magic cmd alias (alias will be kept until a session is over)
%alias ll ls -ls # give "ls -l" an alias "ll"

# Interactive debugger
%debug # envoke debugger after any exception
%run -d
# in debugger, "s"-step in, "u/d"-up/down, "c"-continue 

# after modifying a module "some_lib", reload the updated version
import some_lib
reload(some_lib)
