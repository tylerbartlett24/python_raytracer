import numpy as np
from scene import C_h, C_w, V_w, V_h, d

def x_transform(x):
    '''
    Transforms from intuitive x coordinate with origin at center and x 
    increasing to the right to machine coordinate with origin at upper left 
    corner and x increasing to the right.

    Parameters
    ----------
    x : Integer or float 
        Old x value such that -width/2 < x < width/2

    Returns
    -------
    Float
        New x value such that 0 < x < width

    '''
    return C_w//2 + x
def y_transform(y): 
    """
    Transforms from intuitive x coordinate with origin at center and y 
    increasing upwards to machine coordinate with origin at upper left 
    corner and y increasing downward.

    Parameters
    ----------
    x : Integer or float 
        Old y value such that -width/2 < y < width/2

    Returns
    -------
    Float
        New y value such that 0 < x < width

    """
    return C_h//2 - y

def canvas_to_viewport(x, y):
    """
    Transforms from canvas coordinates to viewport coordinates.
    
    Parameters
    ----------
    x, y: Integer or float
        Coordinates of a pixel on the canvas
        
    Returns 
    -------
    3D Numpy array
        Coordinates of a square on the viewport corresponding to the input 
        pixel on the canvas.
    
    """
    return np.array([x*(V_w/C_w), y*(V_h/C_h), d])