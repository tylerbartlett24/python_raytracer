from shapes import Sphere
import numpy as np
from lights import *

#The values in this file describe the scene to be rendered

#The size of the canvas in pixels
C_w = 720
C_h = 720

#The size of the viewport in meters (units are arbitrary)
V_w = 1
V_h = 1

#The distance from the viewport to the camera
d = 1

#Location of the camera
O = np.array([0, 0, 0])

#Create new light sources here and add them to the lights array
light_1 = AmbientLight(0.2)
light_2 = PointLight(0.6, 2, 1, 0)
light_3 = DirectionalLight(0.2, 1, 4, 4)
lights = [light_1, light_2, light_3]

#Create new shapes here and add them to the scene array
sphere_1 = Sphere(np.array([0, -1, 3]), 1, "#ff0000", 500)
sphere_2 = Sphere(np.array([-2, 0, 4]), 1, "#00ff00", 500)
sphere_3 = Sphere(np.array([2, 0, 4]), 1, "#0000ff", 500)
scene = [sphere_1, sphere_2, sphere_3]
