import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import math

start_x = None
start = None
slide = None
dots = None
arrows = None
break_point = None
break_location = None
pins = None
exit = None

start_x = -15
start = 35
slide = 25
arrows = 15
break_point = 10
break_location = 45
pins = 18
exit = 22

b2i = lambda x: (42.0/39) * x - (0.5 * 42.0 / 39)

points = []

if slide is not None:
    points.append((0, b2i(slide)))

if dots is not None:
    points.append((12, b2i(dots)))

if arrows is not None:
    f = lambda x: float(-2/b2i(15)) * abs(arrows - b2i(20)) + 17
    points.append((f(arrows), b2i(arrows)))

if break_point is not None:
    break_location = break_location or 52.5
    points.append((break_location, b2i(break_point)))

if pins is not None:
    p = lambda x: abs((2*math.sqrt(3)/12.0) * b2i(pins) - (b2i(20) * 2 * math.sqrt(3)/12.0)) + 60
    points.append((p(pins), b2i(pins)))

x = np.array([x for (x, _) in points])
y = np.array([y for (_, y) in points])

X_Y_Spline = make_interp_spline(x, y)

X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

print(X_)
print(Y_)

#fig, ax = plt.subplots(figsize=(9.0, 1.68), dpi=100)
#fig = plt.figure()
#fig.set_size_inches(9.0, 1.68)


fig = plt.figure(figsize = [9.0,2.1], tight_layout = {'pad': 0})

plt.plot(X_, Y_, lw=4, color='yellow')

for (x, y) in points:
   plt.plot(x, y, 'o', color='black', markersize=8)

_pins = [None for _ in range(11)]
_pins[1] = (60, 21)

_pins[2] = (60 + (2 * 0.5 * math.sqrt(3)), 21 + 6)
_pins[3] = (60 + (2 * 0.5 * math.sqrt(3)), 21 - 6)

_pins[4] = (60 + (2 * 1.0 * math.sqrt(3)), 21 + 12)
_pins[5] = (60 + (2 * 1.0 * math.sqrt(3)), 21)
_pins[6] = (60 + (2 * 1.0 * math.sqrt(3)), 21 - 12)

_pins[7] = (60 + (2 * 1.5 * math.sqrt(3)), 21 + 18)
_pins[8] = (60 + (2 * 1.5 * math.sqrt(3)), 21 + 6)
_pins[9] = (60 + (2 * 1.5 * math.sqrt(3)), 21 - 6)
_pins[10] = (60 + (2 * 1.5 * math.sqrt(3)), 21 - 18)

for (px, py) in _pins[1:]:
    print(f'{px} - {py}')
    plt.plot(px, py, 'o', color='white', markersize=12, markeredgecolor='red', markeredgewidth=2)

_arrows = [None for _ in range(8)]

_arrows[1] = (15, b2i(35))
_arrows[2] = (15 + 2.0/3, b2i(30))
_arrows[3] = (15 + 4.0/3, b2i(25))
_arrows[4] = (17, b2i(20))
_arrows[5] = (15 + 4.0/3, b2i(15))
_arrows[6] = (15 + 2.0/3, b2i(10))
_arrows[7] = (15, b2i(5))

_arrow_l = 2.0/12

for (ax, ay) in _arrows[1:]:
    plt.arrow(ax-_arrow_l, ay, 2*_arrow_l, 0, shape='full', lw=3, length_includes_head=True, head_width=(21.0/39), color='maroon') 

for dot in [3, 5, 8, 11, 14]:
    plt.plot(6, b2i(dot), 'o', color='black', markersize=1)
    plt.plot(6, b2i(40-dot), 'o', color='black', markersize=1)

for dot in [5, 10, 15, 20, 25, 30, 35]:
    plt.plot(-15, b2i(dot), 'o', color='black', markersize=3)
    plt.plot(-12, b2i(dot), 'o', color='black', markersize=3)
    plt.plot(-0.5, b2i(dot), 'o', color='black', markersize=3)


if start and start_x and slide:
    x = [start_x, -1]
    y = [b2i(start), b2i(slide)]
    
    plt.plot(start_x, b2i(start), 'o', color='black', markersize=8)
    plt.arrow(start_x, b2i(start), -1-start_x, b2i(slide)-b2i(start), shape='full', lw=2, linestyle='--', length_includes_head=True, head_width=2, color='maroon')

plt.plot([0, 0], [0, 42], linestyle='-', color='black', lw=0.5)

if pins and exit:
    plt.arrow(60, b2i(pins), 9, b2i(exit)-b2i(pins), shape='full', lw=2, linestyle='-', length_includes_head=True, head_width=2, color='seagreen')

plt.plot([34, 37], [b2i(15), b2i(15)], linestyle='-', color='brown', lw=3)
plt.plot([34, 37], [b2i(40-15), b2i(40-15)], linestyle='-', color='brown', lw=3)

plt.plot([40, 43], [b2i(10), b2i(10)], linestyle='-', color='brown', lw=3)
plt.plot([40, 43], [b2i(40-10), b2i(40-10)], linestyle='-', color='brown', lw=3)








ax = plt.gca()
ax.set_facecolor('none')
#ax.set_aspect(2 * 42/(60*12))
ax.set_ylim(0, 42)
ax.set_xlim(-20, 70)
ax.set_axis_off()

fig.savefig('sample.png', bbox_inches='tight', dpi=100, pad_inches=0, transparent=True)

#plt.show()


