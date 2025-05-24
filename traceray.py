import math
import numpy as np
from shapes import Sphere
from scene import lights, BACKGROUND_COLOR

def intersect_check(O, D, shape):
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
    
    
def reflect_ray(N, R):
    return 2 * N * np.dot(R, N) - R
    
def compute_lighting(p, n, v, s, lights, shapes):
    i = 0.0
    for light in lights:
        if light.type == "ambient":
            i += light.intensity
        else: 
            if light.type == "point":
                l = light.position - p
                t_max = 1
            else:
                l = light.direction
                t_max = math.inf
                
            #Check if point should be in shadow
            shadow_sphere, shadow_t = closest_intersection(p, l, 0.01, t_max,
                                                           shapes)
            if shadow_sphere == None:
                continue
            
            #Diffuse
            n_dot_l = np.dot(n, l)
            if n_dot_l > 0:
                n_len = np.linalg.norm(n)
                p_len = np.linalg.norm(p)
                i += light.intensity * n_dot_l/(n_len * p_len)
                
            #Specular
            if s != -1:
                r = reflect_ray(n, l)
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

def closest_intersection(O, D, t_min, t_max, shapes):
    closest_t = math.inf
    closest_shape = None
    for s in shapes:
        t1, t2 = intersect_check(O, D, s)
        if (t_min <= t1 <= t_max) and t1 < closest_t:
            closest_t = t1
            closest_shape = s
        if (t_min <= t2 <= t_max) and t2 < closest_t:
            closest_t = t2
            closest_shape = s
    
    return closest_shape, closest_t

def trace_ray(camera, direction, t_min, t_max, shapes, recursion_depth):
    closest_shape, closest_t = closest_intersection(camera, direction, t_min,
                                                    t_max, shapes)
    if closest_shape == None:
        return BACKGROUND_COLOR
    
    #Point of intersection with sphere
    intersection = camera + closest_t * direction
    
    #Normal vector at intersection
    normal = intersection - closest_shape.center
    normal = normal / np.linalg.norm(normal)
    
    color_tuple = hex_to_rgb(closest_shape.color)
    s = closest_shape.specular
    v = -1 * direction
    lighting_scalar = compute_lighting(intersection, normal, v, s, lights, 
                                       shapes)
    lit_array = np.array([max(0.0, min(255.0, lighting_scalar * x)) 
                       for x in color_tuple])
    
    r = closest_shape.reflective
    if recursion_depth <= 0 or r <= 0.0:
        lit_tuple = tuple([int(y) for y in lit_array])
        return rgb_to_hex(lit_tuple)
    
    R = reflect_ray(-direction, normal)
    reflected_hex = trace_ray(intersection, R, 0.01, math.inf,
                                shapes, recursion_depth - 1)
    reflected_color = hex_to_rgb(reflected_hex)
    
    reflected_array = np.array([x for x in reflected_color])
    final_color = (lit_array * (1 - r)) + (reflected_array * r)
    
    color_tuple = tuple([max(0,min(255, int(x))) for x in final_color])
    return rgb_to_hex(color_tuple)
    