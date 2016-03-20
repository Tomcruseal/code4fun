k = 3.0
c = 0.2
m = 0.1
f = lambda t: 10.0
init = 5.0, 0.0

def mass_dump_spring(status, t):
    x, v = status
    dx = v
    dv = (f(t) - k*x - c*v)/m
    return dx, dv

import numpy as np
from scipy.integrate import odeint
import pylab as pl

def solve_by_odeint(time, h):
    t = np.arange(0, time, h)
    result = odeint(mass_dump_spring, init, t)
    return t, result[:, 0], result[:, 1]

print solve_by_odeint(2,0.1)
