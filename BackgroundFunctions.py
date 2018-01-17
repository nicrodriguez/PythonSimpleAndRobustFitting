def normalize(vector):
    mag = (vector[0]**2 + vector[1]**2 + vector[2]**2)**(1/2)
    return [vector[0]/mag, vector[1]/mag, vector[2]/mag]


def point_to_plane_distance(normal, x, y, z, D):
    n1 = normal[0]*x + normal[1]*y + normal[2]*z + D
    n2 = (normal[0]**2 + normal[1]**2 + normal[2]**2)**(1/2)
    return n1/n2
