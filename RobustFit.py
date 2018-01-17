from BackgroundFunctions import *


def robust_fit(x_points, y_points, z_points):

    # for val in x_points:
    #     print(val)
    #     print()
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

    weight_x = det_x*det_x
    weight_y = det_y*det_y
    weight_z = det_z*det_z

    nx = [det_x, xz * yz - xy * zz, xy * yz - xz * yy]
    ny = [xz * yz - xy * zz, det_y, xy * xz - yz * xx]
    nz = [xy * yz - xz * yy, xy * xz - yz * xx, det_z]
    # weighted_det = [nx, ny, nz]

    dot_prodx = 0*nx[0] + 0*nx[1] + 0*nx[2]
    dot_prody = 0*ny[0] + 0*ny[1] + 0*nz[2]
    dot_prodz = 0*nz[0] + 0*nz[1] + 0*nz[2]

    if dot_prodx < 0:
        weight_x = -weight_x

    if dot_prody < 0:
        weight_y = -weight_y

    if dot_prodz < 0:
        weight_z = -weight_z

    weighted_nx = 0
    weighted_ny = 0
    weighted_nz = 0

    for i in range(0, len(nx)):
        weighted_nx += nx[i] * weight_x
        weighted_ny += ny[i] * weight_y
        weighted_nz += nz[i] * weight_z

    weighted_det = [weighted_nx, weighted_ny, weighted_nz]

    # print(weighted_det)
    normal = normalize(weighted_det)
    # print(normal)

    calculated_z = []
    for i in range(0, len(x_points)):
        calculated_z.append(-(normal[0]*x_points[i] + normal[1]*y_points[i])/normal[2])

    return [calculated_z, normal, cent]





