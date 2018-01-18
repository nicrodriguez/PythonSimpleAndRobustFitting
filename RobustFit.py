from BackgroundFunctions import *


def robust_fit(x_points, y_points, z_points):

    # Calculating the centroid of the points
    n = len(x_points)
    cent = [sum(x_points) / n, sum(y_points) / n, sum(z_points) / n]

    # Calculating the covariance matrix
    xx = yy = xy = xz = yz = zz = 0.0
    for i in range(0, len(x_points)):
        xx += (x_points[i] - cent[0]) * (x_points[i] - cent[0])
        yy += (y_points[i] - cent[1]) * (y_points[i] - cent[1])
        xy += (x_points[i] - cent[0]) * (y_points[i] - cent[1])
        xz += (x_points[i] - cent[0]) * (z_points[i] - cent[2])
        yz += (y_points[i] - cent[1]) * (z_points[i] - cent[2])
        zz += (z_points[i] - cent[2]) * (z_points[i] - cent[2])

    xx /= n
    yy /= n
    xy /= n
    xz /= n
    yz /= n
    zz /= n

    # Calculating determinants for each axis
    det_x = yy*zz - yz*yz
    det_y = xx*zz - xz*xz
    det_z = xx*yy - xy*xy

    weight_x = det_x*det_x
    weight_y = det_y*det_y
    weight_z = det_z*det_z

    w = [weight_x, weight_y, weight_z]
    nx = [det_x, xz*yz - xy*zz, xy*yz - xz*yy]
    ny = [xz*yz - xy*zz, det_y, xy*xz - yz*xx]
    nz = [xy*yz - xz*yy, xy*xz - yz*xx, det_z]

    wn = [nx, ny, nz]
    weighted_n = [0, 0, 0]
    for i in range(0, len(nx)):
        dot_prodx = weighted_n[0]*wn[i][0] + weighted_n[1]*wn[i][1] + weighted_n[2]*wn[i][2]

        if dot_prodx < 0:
            weight_x *= -1

        weighted_n[i] += wn[i][0] * w[i]
        weighted_n[i] += wn[i][1] * w[i]
        weighted_n[i] += wn[i][2] * w[i]

    normal = normalize(weighted_n)

    calculated_z = []
    for i in range(0, len(x_points)):
        calculated_z.append(-(normal[0]*x_points[i] + normal[1]*y_points[i])/normal[2])

    return [calculated_z, normal, cent]





