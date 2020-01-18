# Author: Wentao Yuan (wyuan1@cs.cmu.edu) 05/31/2018

import h5py
import numpy as np
import open3d as o3d

def read_pcd(filename):
    pcd = o3d.io.read_point_cloud(filename)
    return np.array(pcd.points)


def save_pcd(filename, points):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.io.write_point_cloud(filename, pcd)


def read_h5(path, verbose=False):
    if verbose:
        print("Loading %s \n" % path)
    f = h5py.File(path, 'r')
    cloud_data = np.array(f['data'])
    f.close()

    return cloud_data.astype(np.float64)