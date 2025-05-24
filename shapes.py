class Sphere:
    def __init__(self, center, radius, color, specular, reflective):
        self.center = center
        self.radius = radius
        self.color = color
        #specular exponent
        self.specular = specular
        #reflectiviy, 0 <= reflectivity <= 1
        self.reflective = reflective