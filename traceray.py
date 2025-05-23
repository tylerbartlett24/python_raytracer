import math
import numpy as np
from shapes import Sphere
from scene import lights

def intersect_check(O, D, shape):
    if isinstance(shape, Sphere):
        CO = O - shape.center
        a = np.dot(D, D)
        b = 2*np.dot(CO, D)
        c = np.dot(CO, CO) - shape.radius**2
        discrim = b*b - 4*a*c
        if discrim >= 0:
            t1 = -b/2*a + math.sqrt(discrim)
            t2 = -b/2*a - math.sqrt(discrim)
            return t1, t2
        else:
            return math.inf, math.inf
    else:
        t1 = math.inf
        t2 = math.inf
        return t1, t2
    
def compute_lighting(p, n, v, s, lights):
    i = 0.0
    for light in lights:
        if light.type == "ambient":
            i += light.intensity
        else: 
            if light.type == "point":
                l = light.position - p
            else:
                l = light.direction
            
            #Diffuse
            n_dot_l = np.dot(n, l)
            if n_dot_l > 0:
                n_len = np.linalg.norm(n)
                p_len = np.linalg.norm(p)
                i += light.intensity * n_dot_l/(n_len * p_len)
                
            #Specular
            if s != -1:
                r = 2 * n *n_dot_l - l
                r_dot_v = np.dot(r, v)
                if r_dot_v > 0:
                    r_len = np.linalg.norm(r)
                    v_len = np.linalg.norm(v)
                    i += (light.intensity * 
                          math.pow(n_dot_l/(r_len * v_len), s))
            
    return i

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    
    #Create a list of floats out of the hex string
    color_tuple = tuple(float(int(value[i:i + lv // 3],
                                  16)) for i in range(0, lv, lv // 3))

    return color_tuple

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def trace_ray(camera, direction, t_min, t_max, shapes):
    closest_t = math.inf
    closest_shape = None
    for s in shapes:
        t1, t2 = intersect_check(camera, direction, s)
        if (t_min <= t1 <= t_max) and t1 < closest_t:
            closest_t = t1
            closest_shape = s
        if (t_min <= t2 <= t_max) and t2 < closest_t:
            closest_t = t2
            closest_shape = s
    if closest_shape == None:
        return "#ffffff"
    
    #Point of intersection with sphere
    intersection = camera + closest_t * direction
    
    #Normal vector at intersection
    normal = intersection - closest_shape.center
    normal = normal / np.linalg.norm(normal)
    
    color_array = hex_to_rgb(closest_shape.color)
    s = closest_shape.specular
    v = -1 * direction
    lighting_scalar = compute_lighting(intersection, normal, v, s, lights)
    lit_tuple = tuple([max(0, min(255, int(lighting_scalar * x))) 
                       for x in color_array])
    
    return rgb_to_hex(lit_tuple)