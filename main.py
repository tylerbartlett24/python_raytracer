#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:49:50 2023

@author: tyler
"""

import math
from tkinter import Tk, Canvas, mainloop
import numpy as np
from shapes import Sphere
from scene import *
from coordtransforms import x_transform, y_transform, canvas_to_viewport
from traceray import trace_ray
        
def main():
    window = Tk()
    canvas = Canvas(window, width=C_w, height=C_h, bg="white")
    canvas.pack()
    for x in range(-C_w//2, C_w//2):
        S_x = x_transform(x)
        for y in range(-C_h//2, C_h//2):
            S_y = y_transform(y)
            D = canvas_to_viewport(x, y)
            color = trace_ray(O, D, 1, math.inf, scene, 3)
            canvas.create_rectangle(S_x, S_y, S_x, S_y, outline=color)

    mainloop()

if __name__ == "__main__":
    main()
