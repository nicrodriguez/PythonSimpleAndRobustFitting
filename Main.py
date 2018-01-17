from RobustFit import robust_fit
from SimpleFit import simple_fit
from BackgroundFunctions import point_to_plane_distance, plot_plane


def read_points_from_file(filename):
    x_points = []
    y_points = []
    z_points = []
    file = filename
    with open(file, 'r') as f:
        coordinates = f.readlines()
        f.seek(0)
        for point in coordinates:
            points = point.replace("\n", "")
            points = points.split(",")
            x_points.append(int(points[0]))
            y_points.append(int(points[1]))
            z_points.append(int(points[2]))
    return [x_points, y_points, z_points]


def rms_error(z_points_c, z_points_a):
    differences = []
    diff_sum = 0.0

    for i in range(0, len(z_points_c)):
        differences.append((z_points_c[i] - z_points_a[i])/z_points_a[i])
        differences[i] = differences[i]**2
        diff_sum += differences[i]

    mean_error = diff_sum/len(differences)
    return 100*(abs(mean_error))**(1/2)


def plane_to_point_rms(normal_ref, coordinates_c, centroid):
    x = coordinates_c[0]
    y = coordinates_c[1]
    z = coordinates_c[2]

    x_c = centroid[0]
    y_c = centroid[1]
    z_c = centroid[2]

    # calculating points relative to the normal of the plane
    # x_new = []
    # y_new = []
    z_new = len(x)*[None]

    for i in range(0, len(x)):
        D = -(normal_ref[0]*x_c + normal_ref[1]*y_c + normal_ref[2]*z_c)
        # print(D)
        d = point_to_plane_distance(normal_ref, x[i], y[i], z[i], D)
        if d < 0:
            x_new = x[i] + normal_ref[0]*d
            y_new = y[i] + normal_ref[1]*d

        else:
            x_new = x[i] - normal_ref[0]*d
            y_new = y[i] - normal_ref[1]*d

        z_new[i] = -(normal_ref[0]*x_new + normal_ref[1]*y_new)/normal_ref[2]

    return rms_error(z, z_new)


# Reading values from txt files
vals = read_points_from_file('points_on_plane.txt')
perfect_x_points = vals[0]
perfect_y_points = vals[1]
perfect_z_points = vals[2]

vals = read_points_from_file('noisy_points_on_plane.txt')
x_points_n1 = vals[0]
y_points_n1 = vals[1]
z_points_n1 = vals[2]

vals = read_points_from_file('noisy_points_on_plane2.txt')
x_points_n2 = vals[0]
y_points_n2 = vals[1]
z_points_n2 = vals[2]

vals = read_points_from_file('noisy_points_on_plane3.txt')
x_points_n3 = vals[0]
y_points_n3 = vals[1]
z_points_n3 = vals[2]


# Obtaining perfect plane normal and corresponding points
z_points, normal, cent = simple_fit(perfect_x_points, perfect_y_points, perfect_z_points)
rmsR = rms_error(z_points, perfect_z_points)

c_c = [perfect_x_points, perfect_y_points, perfect_z_points]
rmsNR = plane_to_point_rms(normal, c_c, cent)

# Simple fitting
simple_z_n1, normalS1, centS1 = simple_fit(x_points_n1, y_points_n1, z_points_n1)
simple_z_n2, normalS2, centS2 = simple_fit(x_points_n2, y_points_n2, z_points_n2)
simple_z_n3, normalS3, centS3 = simple_fit(x_points_n3, y_points_n3, z_points_n3)

rmsS1 = rms_error(simple_z_n1, perfect_z_points)
rmsS2 = rms_error(simple_z_n2, perfect_z_points)
rmsS3 = rms_error(simple_z_n3, perfect_z_points)

c_c1 = [x_points_n1, y_points_n1, simple_z_n1]
c_c2 = [x_points_n2, y_points_n2, simple_z_n2]
c_c3 = [x_points_n3, y_points_n3, simple_z_n3]

rmsNS1 = plane_to_point_rms(normal, c_c1, centS1)
rmsNS2 = plane_to_point_rms(normal, c_c2, centS2)
rmsNS3 = plane_to_point_rms(normal, c_c3, centS3)

# Robust Fitting
robust_z_n1, normalR1, centR1 = robust_fit(x_points_n1, y_points_n1, z_points_n1)
robust_z_n2, normalR2, centR2 = robust_fit(x_points_n2, y_points_n2, z_points_n2)
robust_z_n3, normalR3, centR3 = robust_fit(x_points_n3, y_points_n3, z_points_n3)
# for i in range(0, len(robust_z_n2)):
#     print("{0}   {1}".format(z_points[i], robust_z_n3[i]))

rmsR1 = rms_error(robust_z_n1, perfect_z_points)
rmsR2 = rms_error(robust_z_n2, perfect_z_points)
rmsR3 = rms_error(robust_z_n3, perfect_z_points)

c_c1 = [x_points_n1, y_points_n1, robust_z_n1]
c_c2 = [x_points_n2, y_points_n2, robust_z_n2]
c_c3 = [x_points_n3, y_points_n3, robust_z_n3]

rmsNR1 = plane_to_point_rms(normal, c_c1, centR1)
rmsNR2 = plane_to_point_rms(normal, c_c2, centR2)
rmsNR3 = plane_to_point_rms(normal, c_c3, centR3)

# plot_plane(normalR1, [x_points_n1, y_points_n1, robust_z_n1], 0.5, 'Robust Fit +/- 1 units of noise')
# plot_plane(normalR2, [x_points_n2, y_points_n2, robust_z_n2], 0.5, 'Robust Fit +/- 2 units of noise')
# plot_plane(normalR3, [x_points_n3, y_points_n3, robust_z_n3], 0.5, 'Robust Fit +/- 3 units of noise')
# plot_plane(normalS1, [x_points_n1, y_points_n1, simple_z_n1], 0.5, 'Simple Fit +/- 1 units of noise')
# plot_plane(normalS2, [x_points_n2, y_points_n2, simple_z_n2], 0.5, 'Simple Fit +/- 2 units of noise')
# plot_plane(normalS3, [x_points_n3, y_points_n3, simple_z_n3], 0.5, 'Simple Fit +/- 3 units of noise')

print()
print()
print("Perfect Plane RMS (For reference)")
print("   -----Z-difference RMS-----")
print("RMS Error no noise: {0:.5}%".format(rmsR))
print("   ----Point to Plane RMS----")
print("RMS Error no noise: {0:.5}%".format(rmsNR))
print()
print()
print("------------Simple Fit-------------")
print("Normal Vector with +/- 1 unit: {0}".format(normalS1))
print("Normal Vector with +/- 2 units: {0}".format(normalS2))
print("Normal Vector with +/- 3 units: {0}".format(normalS3))
print()
print("   -----Z-difference RMS-----")
print("RMS Error with +/- 1 unit: {0:.5}%".format(rmsS1))
print("RMS Error with +/- 2 units: {0:.5}%".format(rmsS2))
print("RMS Error with +/- 3 units: {0:.5}%".format(rmsS3))
print("   ----Point to Plane RMS----")
print("RMS Error with +/- 1 unit: {0:.5}%".format(rmsNS1))
print("RMS Error with +/- 2 unit: {0:.5}%".format(rmsNS2))
print("RMS Error with +/- 3 unit: {0:.5}%".format(rmsNS3))
print()
print()
print("------------Robust Fit-------------")
print("Normal Vector with +/- 1 unit: {0}".format(normalR1))
print("Normal Vector with +/- 2 units: {0}".format(normalR2))
print("Normal Vector with +/- 3 units: {0}".format(normalR3))
print()
print("   -----Z-difference RMS-----")
print("RMS Error with +/- 1 unit: {0:.5}%".format(rmsR1))
print("RMS Error with +/- 2 units: {0:.5}%".format(rmsR2))
print("RMS Error with +/- 3 units: {0:.5}%".format(rmsR3))
print("   ----Point to Plane RMS----")
print("RMS Error with +/- 1 unit: {0:.5}%".format(rmsNR1))
print("RMS Error with +/- 2 unit: {0:.5}%".format(rmsNR2))
print("RMS Error with +/- 3 unit: {0:.5}%".format(rmsNR3))



