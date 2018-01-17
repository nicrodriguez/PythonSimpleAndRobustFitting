from BackgroundFunctions import *


def simple_fit(x_points, y_points, z_points):

    # Calculating the centroid of the points
    cent = [sum(x_points) / len(x_points), sum(y_points) / len(y_points), sum(z_points) / len(z_points)]

    # Calculating the covariance matrix
    xx = 0
    yy = 0
    xy = 0
    xz = 0
    yz = 0
    zz = 0
    for i in range(0, len(x_points)):
        xx += (x_points[i] - cent[0]) * (x_points[i] - cent[0])
        yy += (y_points[i] - cent[1]) * (y_points[i] - cent[1])
        xy += (x_points[i] - cent[0]) * (y_points[i] - cent[1])
        xz += (x_points[i] - cent[0]) * (z_points[i] - cent[2])
        yz += (y_points[i] - cent[1]) * (z_points[i] - cent[2])
        zz += (z_points[i] - cent[2]) * (z_points[i] - cent[2])

    # Calculating determinants for each axis
    det_x = yy*zz - yz*yz
    det_y = xx*zz - xz*xz
    det_z = xx*yy - xy*xy

    # Determining max determinant
    det_m = max(det_x, det_y, det_z)

    if det_m == 0:
        print("Points don't span a plane")
        return [0, 0]
    else:
        if det_m == det_x:
            n = [det_m, xz * yz - xy * zz, xy * yz - xz * yy]

        elif det_m == det_y:
            n = [xz * yz - xy * zz, det_m, xy * xz - yz * xx]

        else:
            n = [xy * yz - xz * yy, xy * xz - yz * xx, det_m]

        # Calculating the plane normal
        normal = normalize(n)

        # calculating points on the plane
        calculated_z = []

        for i in range(0, len(x_points)):
            calculated_z.append(-(normal[0] * x_points[i] + normal[1] * y_points[i]) / normal[2])

        return [calculated_z, normal, cent]
