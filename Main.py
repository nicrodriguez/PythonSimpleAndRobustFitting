from RobustFit import robust_fit


perfect_z_points = []


def rms_error(z_points_c, z_points_a):
    differences = []
    diff_sum = 0.0

    for i in range(0, len(z_points_c)):
        differences.append((z_points_c[i] - z_points_a[i])/z_points_a[i])
        differences[i] = differences[i]**2
        diff_sum += differences[i]

    mean_error = diff_sum/len(differences)
    return 100*(abs(mean_error))**(1/2)


def plane_to_point_rma(z_points_c, z_points_a):
    print("Hello")


# Reading from perfect plane file
file = 'points_on_plane.txt'
with open(file, 'r') as f:
    coordinates = f.readlines()
    f.seek(0)
    # print(coordinates.sp)
    for point in coordinates:
        points = point.replace("\n", "")
        points = points.split(",")
        perfect_z_points.append(int(points[2]))

# Reading from noisy plane file
x_points = []
y_points = []
z_points = []
file = 'noisy_points_on_plane.txt'
with open(file, 'r') as f:
    coordinates = f.readlines()
    f.seek(0)
    for point in coordinates:
        points = point.replace("\n", "")
        points = points.split(",")
        x_points.append(int(points[0]))
        y_points.append(int(points[1]))
        z_points.append(int(points[2]))

# Reading from noisy plane file
x_points2 = []
y_points2 = []
z_points2 = []
file = 'noisy_points_on_plane2.txt'
with open(file, 'r') as f:
    coordinates = f.readlines()
    f.seek(0)
    for point in coordinates:
        points = point.replace("\n", "")
        points = points.split(",")
        x_points2.append(int(points[0]))
        y_points2.append(int(points[1]))
        z_points2.append(int(points[2]))


robust_z_n1 = robust_fit(x_points, y_points, z_points)
rms1 = rms_error(robust_z_n1, perfect_z_points)

robust_z_n2 = robust_fit(x_points2, y_points2, z_points2)
rms2 = rms_error(robust_z_n2, perfect_z_points)

print("RMS Error with +/- 1 unit: {0:.4}%".format(rms1))
print("RMS Error with +/- 2 unit: {0:.4}%".format(rms2))

