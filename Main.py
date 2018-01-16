from PythonSimpleAndRobustFitting.RobustFit import robust_fit
from PythonSimpleAndRobustFitting.SimpleFit import simple_fit
from PythonSimpleAndRobustFitting.BackgroundFunctions import point_to_plane_distance


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


def plane_to_point_rms(normal_ref, coordinates_c):
    x = coordinates_c[0]
    y = coordinates_c[1]
    z = coordinates_c[2]
    d = []

    for i in range(0, len(x)):
        d.append(point_to_plane_distance(normal_ref, x, y, z))


# Reading values from txt files
vals = read_points_from_file('PythonSimpleAndRobustFitting/points_on_plane.txt')
perfect_x_points = vals[0]
perfect_y_points = vals[1]
perfect_z_points = vals[2]

vals = read_points_from_file('PythonSimpleAndRobustFitting/noisy_points_on_plane.txt')
x_points_n1 = vals[0]
y_points_n1 = vals[1]
z_points_n1 = vals[2]

vals = read_points_from_file('PythonSimpleAndRobustFitting/noisy_points_on_plane2.txt')
x_points_n2 = vals[0]
y_points_n2 = vals[1]
z_points_n2 = vals[2]

vals = read_points_from_file('PythonSimpleAndRobustFitting/noisy_points_on_plane3.txt')
x_points_n3 = vals[0]
y_points_n3 = vals[1]
z_points_n3 = vals[2]


# Obtaining perfect plane normal
z_points, normal = simple_fit(perfect_x_points, perfect_y_points, perfect_z_points)


# Simple fitting
simple_z_n1, normalS1 = simple_fit(x_points_n1, y_points_n1, z_points_n1)
rmsS1 = rms_error(simple_z_n1, perfect_z_points)

simple_z_n2, normalS2 = simple_fit(x_points_n2, y_points_n2, z_points_n2)
rmsS2 = rms_error(simple_z_n2, perfect_z_points)

simple_z_n3, normalS3 = simple_fit(x_points_n3, y_points_n3, z_points_n3)
rmsS3 = rms_error(simple_z_n3, perfect_z_points)

# Robust Fitting
robust_z_n1, normalR1 = robust_fit(x_points_n1, y_points_n1, z_points_n1)
rmsR1 = rms_error(robust_z_n1, perfect_z_points)

robust_z_n2, normalR2 = robust_fit(x_points_n2, y_points_n2, z_points_n2)
rmsR2 = rms_error(robust_z_n2, perfect_z_points)

robust_z_n3, normalR3 = robust_fit(x_points_n3, y_points_n3, z_points_n3)
rmsR3 = rms_error(robust_z_n3, perfect_z_points)

print("------------Simple Fit-------------")
print("Normal Vector with +/- 1 unit: {0}".format(normalS1))
print("Normal Vector with +/- 2 units: {0}".format(normalS2))
print("Normal Vector with +/- 3 units: {0}".format(normalS3))
print()
print("   -----Z-difference RMS-----")
print("RMS Error with +/- 1 unit: {0:.5}%".format(rmsS1))
print("RMS Error with +/- 2 units: {0:.5}%".format(rmsS2))
print("RMS Error with +/- 3 units: {0:.5}%".format(rmsS3))
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


