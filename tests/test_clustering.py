import numpy as np
from pycht.clustering import Clustering


def test_clustering_output_shape_and_values():
    # Generate synthetic pixel data with 3 distinct color zones
    data = np.vstack(
        [
            np.full((10, 3), [255, 0, 0]),  # Red
            np.full((10, 3), [0, 255, 0]),  # Green
            np.full((10, 3), [0, 0, 255]),  # Blue
        ]
    ).astype(np.float32)

    clustered = Clustering.compute(data, nb_clusters=3)

    assert clustered.shape == data.shape
    unique_colors = np.unique(clustered, axis=0)
    assert len(unique_colors) == 3  # Should find 3 distinct clusters
    for color in unique_colors:
        assert color.dtype == np.uint8
        assert color.shape == (3,)  # RGB triplet
