from PythonSimpleAndRobustFitting.RobustFit import robust_fit


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


def plane_to_point_rms(z_points_c, z_points_a):
    print("Hello")


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

robust_z_n1 = robust_fit(x_points_n1, y_points_n1, z_points_n1)
rms1 = rms_error(robust_z_n1, perfect_z_points)

robust_z_n2 = robust_fit(x_points_n2, y_points_n2, z_points_n2)
rms2 = rms_error(robust_z_n2, perfect_z_points)

robust_z_n3 = robust_fit(x_points_n3, y_points_n3, z_points_n3)
rms3 = rms_error(robust_z_n3, perfect_z_points)

print("RMS Error with +/- 1 unit: {0:.4}%".format(rms1))
print("RMS Error with +/- 2 unit: {0:.4}%".format(rms2))
print("RMS Error with +/- 3 unit: {0:.4}%".format(rms3))


