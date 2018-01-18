import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def normalize(vector):
    mag = (vector[0]**2 + vector[1]**2 + vector[2]**2)**(1/2)
    return [vector[0]/mag, vector[1]/mag, vector[2]/mag]


def point_to_plane_distance(normal, x, y, z, D):
    n1 = normal[0]*x + normal[1]*y + normal[2]*z + D
    n2 = (normal[0]**2 + normal[1]**2 + normal[2]**2)**(1/2)
    return n1/n2


def plane(normals, x, y):
    return -(normals[0]*x + normals[1]*y)/normals[2]


def plot_plane(normal, coordinates, grid_spacing, title):
    x_max = max(coordinates[0])
    x_min = min(coordinates[0])
    y_max = max(coordinates[1])
    y_min = min(coordinates[1])

    x = np.arange(x_min, x_max, grid_spacing)
    y = np.arange(y_min, y_max, grid_spacing)
    X, Y = np.meshgrid(x, y)
    z = np.array([plane(normal, x, y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = z.reshape(X.shape)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('X')
    ax.set_xlabel('Y')
    ax.set_xlabel('Z')
    ax.set_title(title)
    plt.show()
