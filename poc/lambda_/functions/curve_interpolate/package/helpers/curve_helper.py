import numpy as np
from scipy.interpolate import make_interp_spline
import math

def draw_curve(slide=None, dots=None, arrows=None, break_point=None, break_location=None, pin_entry=None):

    # function to convert boards to inches
    b2i = lambda x: (42.0/39) * x - (0.5 * 42.0 / 39)

    # list of points to plot
    points = []

    if slide is not None:
        points.append((0, b2i(slide)))

    if dots is not None:
        points.append((12, b2i(dots)))

    if arrows is not None:
        # special V function so that when crossing the arrows the 
        # proper lane depth is used
        f = lambda x: float(-2/b2i(15)) * abs(arrows - b2i(20)) + 17
        points.append((f(arrows), b2i(arrows)))

    if break_point is not None:
        break_location = break_location or 52.5
        points.append((break_location, b2i(break_point)))

    if pin_entry is not None:
        # in the drawing the aspect ratio is condensed for legibility
        # the result is that the depth of pins from headpin to 7-10 pins
        # are exaggerated. this function is to plot the correct
        # lane depth
        p = lambda x: abs((2*math.sqrt(3)/12.0) * b2i(pin_entry) - (b2i(20) * 2 * math.sqrt(3)/12.0)) + 60
        points.append((p(pin_entry), b2i(pin_entry)))

    # will use all of the known points to generate a curve
    x = np.array([x for (x, _) in points])
    y = np.array([y for (_, y) in points])

    X_Y_Spline = make_interp_spline(x, y)

    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)

    return {
        'X': X_.tolist(),
        'Y': Y_.tolist()
    }

