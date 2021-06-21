#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A Study of the Utmost Gravity

A set of functions to calculate the effects of gravity.

Created on Mon Jun 17 18:28:40 2019

@author: aanderson
"""

def xy(t, xy0, v0):
    """This function calculates the trajectory of an object
    under the influence of Earth's gravity near its surface:

        xy(t, (x0,y0), (vx0,vy0))

    where xy, x0, and y0 are in meters and vx0 and vy0 are in meters/second."""
    g = 9.81
    # split tuples into components for vector addition and scalar multiplication
    (x0,y0) = xy0
    (vx0,vy0)= v0
    return x0 + vx0 * t, y0 + vy0 * t + 1./2 * g * t**2


