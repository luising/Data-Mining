# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

import unittest
import numpy as np
import KMeans
from Point import Point
from Cluster import Cluster


class MyTestCase(unittest.TestCase):
    global DATASET
    DATASET = "../dataSet/DSclustering/DS_3Clusters_999Points.txt"
    global point
    point = Point(np.array([2, 2]))
    global list_points
    list_points = [Point(np.array([1, 1])), Point(np.array([1, 3])),
                   Point(np.array([3, 1])), Point(np.array([3, 3]))]
    global cluster
    cluster = Cluster(list_points)

    # Check point dimension

    def testDimensionPoint(self):
        self.assertEqual(point.dimension, 2)
        self.assertNotEquals(point.dimension, 1)

    # Check cluster dimension
    def testDimensionCluster(self):
        self.assertEquals(cluster.dimension, 2)
        self.assertNotEquals(cluster.dimension, 3)

    # Check centroid calculation
    def testCentroideCluster(self):
        centroid = cluster.centroid
        self.assertEquals(centroid[0], 2)
        self.assertEquals(centroid[1], 2)

    # Check read data set file 
    def testReadFilePoints(self):
        points = KMeans.dataset_to_list_points(DATASET)
        self.assertTrue(len(points) > 0)
        self.assertTrue(points[0].dimension == 2)

    # Check nearest Clsuter
    def testGetNearestCluster(self):
        self.assertEquals(KMeans.get_nearest_cluster(
            [cluster, Cluster([Point(np.array([8, 8]))])], point), 0)

    # Check cluster's method
    def testCluster(self):
        cluster_test = Cluster([point])
        self.assertEquals(cluster_test.dimension, 2)
        self.assertFalse(cluster_test.converge)
        np.testing.assert_array_equal(cluster_test.centroid, np.array([2, 2]))
        cluster_test.update_cluster(list_points)
        self.assertEquals(cluster_test.dimension, 2)
        self.assertTrue(cluster_test.converge)
        np.testing.assert_array_equal(cluster_test.centroid, np.array([2, 2]))


if __name__ == '__main__':
    unittest.main()
