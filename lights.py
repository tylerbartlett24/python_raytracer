import numpy as np

class Light:
    def __init__(self, intensity):
        self.intensity = intensity
        
class AmbientLight(Light):
    def __init__(self, intensity):
        self.intensity = intensity
        self.type = "ambient"
        
class DirectionalLight(Light):
    def __init__(self, intensity, l1, l2, l3):
        self.intensity = intensity
        self.type = "directional"
        self.direction = np.array([l1, l2, l3])
        
class PointLight(Light):
    def __init__(self, intensity, p1, p2, p3):
        self.intensity = intensity
        self.type = "point"
        self.position = np.array([p1, p2, p3])