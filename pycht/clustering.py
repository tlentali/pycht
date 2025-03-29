"""
Module for performing color clustering on images using K-Means.
"""

import cv2
import numpy as np


class Clustering:
    """
    Perform K-Means clustering on image data to group similar colors.
    """

    @staticmethod
    def compute(Z: np.ndarray, nb_clusters: int):
        """
        Apply K-Means clustering to the given data and return the clustered result.

        Parameters:
        ----------
        Z : np.ndarray
            Flattened image data (pixels) of shape (num_pixels, num_channels), dtype float32.
        nb_clusters : int
            The number of color clusters to form.

        Returns:
        -------
        np.ndarray
            The clustered image data where each pixel is replaced by the centroid of its cluster,
            with dtype uint8 and the same shape as Z.
        """
        _, label, center = cv2.kmeans(
            Z,
            nb_clusters,
            None,
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1),
            10,
            cv2.KMEANS_RANDOM_CENTERS,
        )
        center = np.uint8(center)  # Convert centroid colors to uint8
        res = center[label.flatten()]  # Replace pixel values with their cluster center
        return res
