"""
A test of LinearNDInterpolator.
"""
from scipy.interpolate import LinearNDInterpolator
import numpy as np


def surface(x_value, y_value, z_value):
    "Prints out linear heatmap."
    return x_value + y_value + z_value

X_POINTS = np.linspace(0, 10, num=11, endpoint=True)
Y_POINTS = np.linspace(0, 10, num=11, endpoint=True)
Z_POINTS = np.linspace(0, 10, num=11, endpoint=True)

X_DATA = []
Y_DATA = []
Z_DATA = []
P_DATA = []

for i in X_POINTS:
    for j in Y_POINTS:
        for k in Z_POINTS:
            X_DATA.append(i)
            Y_DATA.append(j)
            Z_DATA.append(k)
            P_DATA.append(surface(i, j, k))

X_ARRAY = np.asarray(X_DATA)
Y_ARRAY = np.asarray(Y_DATA)
Z_ARRAY = np.asarray(Z_DATA)
P_ARRAY = np.asarray(P_DATA)

POINTS_ARRAY = np.column_stack((X_ARRAY, Y_ARRAY, Z_ARRAY))

print LinearNDInterpolator(POINTS_ARRAY, P_ARRAY)(0.1,0,0.51)

