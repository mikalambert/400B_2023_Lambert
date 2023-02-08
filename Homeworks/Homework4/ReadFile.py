#!/usr/bin/env python
# coding: utf-8

# imports
import numpy as np
import astropy.units as u


def Read(filename):
    '''
    This function reads in a file line by line to extract information
    like time, total number of particles, and the data
    inputs: the name of the file
    outputs: the time in Myrs, the total number of particles, and
    and array of the data with columns type, mass, x,y,z coordinates, and
    the velocity in x,y,and z in km/s
    '''
    
    file = open(filename, 'r')
    line1 = file.readline() # reading the first line in the file
    label, value = line1.split() # splitting the label and value of the line
    time = float(value)*u.Myr # the time in Mega years
    
    line2 = file.readline() # reading the second line
    label2, value2 = line2.split() # splitting the label and value of the line
    total_particles = float(value2)
    file.close()

    # the rest of the data in the file with columns
    # type, mass, x,y,z coords, and x,y,z velocities
    data = np.genfromtxt(filename, dtype=None, names=True, skip_header=3)
    
    return time*u.Myr, total_particles, data


