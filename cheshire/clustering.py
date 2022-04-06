"""
Project settings
"""     
import cv2
import numpy as np


class Clustering:
    """
    Project settings
    """
    @staticmethod
    def exec_kmeans(nb_cluster:int, Z):
        """
        Project settings
        """
        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
        # Set flags (Just to avoid line break in the code)
        flags = cv2.KMEANS_RANDOM_CENTERS
        ret, label, center = cv2.kmeans(Z, nb_cluster, None, criteria, 10, flags)
        # Now convert back into uint8, and make original image
        center = np.uint8(center)  # value of the color selected by algo
        res = center[label.flatten()]
        return res
