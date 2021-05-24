#!/usr/bin/python3

from __future__ import print_function

import sys
import numpy as np
import spatialmath.base as tr

import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class least_squares_method:
    def __init__(self,g_noise_gain=0.1,dist = 1.23,npts= 10):
        #decide how much noise to add to points; start with 0.0, and should get precise results
        self.g_noise_gain=g_noise_gain
        self.dist=dist
        """// define the plane to have this distance from the origin.  Note that if we care about positive/negative sides of a plane,
        // then this "distance" could be negative, as measured from the origin to the plane along the positive plane normal"""
        self.npts= npts #// create this many planar points
        self.normal_es=np.zeros((3,1))
    def generate_points(self):
        pass
    def least_squares_with_covariance(self,data,normal_vec):
        #// first compute the centroid of the data:
        #// here's a handy way to initialize data to all zeros; more variants exist
        #//add all the points together:
        pass

    def solve_AxequalB(self,data):
        pass
    def draw_plane(self,points_mat,points_mat_noise,normal_vec):
        pass

        plt.show()
def main():
    pass



if __name__ == "__main__":
    main()