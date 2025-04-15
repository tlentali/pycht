"""
Module for performing color clustering on images using K-Means.
"""

import numpy as np
from sklearn.cluster import KMeans


class Clustering:
    """
    Perform K-Means clustering on image data to group similar colors.
    """

    @staticmethod
    def compute(pixel_array: np.ndarray, nb_clusters: int, random_state: int = 0) -> np.ndarray:
        """
        Apply K-Means clustering to the given data and return the clustered result.

        Parameters
        ----------
        pixel_array : np.ndarray
            Flattened image data (pixels), shape (num_pixels, num_channels).
        nb_clusters : int
            The number of color clusters to form.
        random_state : int
            Random seed for reproducibility.

        Returns
        -------
        np.ndarray
            The clustered image data where each pixel is replaced by the centroid of its cluster,
            with dtype uint8 and the same shape as pixel_array.
        """
        kmeans = KMeans(n_clusters=nb_clusters, n_init=10, random_state=random_state)
        labels = kmeans.fit_predict(pixel_array)
        centers = np.uint8(kmeans.cluster_centers_)
        return centers[labels]
