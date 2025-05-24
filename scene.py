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
O = np.array([0.0, 0.0, 0.0])

#The background colour of the scene
BACKGROUND_COLOR = "#000000"

#Create new light sources here and add them to the lights array
light_1 = AmbientLight(0.6)
light_2 = PointLight(0.8, 2.0, 1.0, 0.0)
light_3 = DirectionalLight(0.8, 1.0, 4.0, 4.0)
lights = [light_1, light_2, light_3]

#Create new shapes here and add them to the scene array
sphere_1 = Sphere(np.array([0.0, -1.0, 3.0]), 1.0, "#ff0000", 500, 0.5)
sphere_2 = Sphere(np.array([-2.0, 0.0, 4.0]), 1.0, "#00ff00", 500, 0.3)
sphere_3 = Sphere(np.array([2.0, 0.0, 4.0]), 1.0, "#0000ff", 10, 0.2)
#sphere_4 = Sphere(np.array([0, 1, 4]), 1, "#ffff00", 10)
scene = [sphere_1, sphere_2, sphere_3]
