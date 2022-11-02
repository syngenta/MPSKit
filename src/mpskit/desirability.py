import matplotlib.pyplot as plt
import numpy as np
import math
from functools import partial

x = np.arange(0.1, 800, 1)
shift=0.0
ll=50
ul=500
slope=10


def f(x,ll,ul,slope, shift):
    return 1/(1+math.exp((x-(ul+ll)/2) * slope/(ul-ll) )) *(1-shift) + shift

f1 = partial(f, ll=50, ul=300, slope=-100, shift=0.1)
f2 = partial(f, ll=300, ul=500, slope=100, shift=0.0)

y = np.array([f1(x=xi)*f2(x=xi) for xi in x ])
plt.plot(x, y)
plt.show()