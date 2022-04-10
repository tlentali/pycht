"""
Project settings
"""
import cv2
import numpy as np


class Clustering:
    """
    Compute clustering
    """

    @staticmethod
    def exec_kmeans(Z: np.ndarray, nb_clusters: int):
        """
        Project settings
        """
        _, label, center = cv2.kmeans(
            Z,
            nb_clusters,
            None,
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1),
            10,
            cv2.KMEANS_RANDOM_CENTERS,
        )
        # Now convert back into uint8, and make original image
        center = np.uint8(center)  # value of the color selected by algo
        res = center[label.flatten()]
        return res
