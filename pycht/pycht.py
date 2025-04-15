"""
Main project logic for generating color-separated stencils from an input image.
"""

from .image_processing import ImageProcessing
from .clustering import Clustering


class Pycht:
    """
    Main interface for generating color-separated stencils from an input image.

    This class orchestrates the image processing and clustering steps by
    using the `ImageProcessing` and `Clustering` components.
    """

    def __init__(self, image_processor: ImageProcessing = None, clustering_model: Clustering = None) -> None:
        self.image_processing = image_processor or ImageProcessing()
        self.clustering = clustering_model or Clustering()

    def stencil(self, input_img: str, nb_colors: int = 3, output_path: str = "./") -> None:
        """
        Generate color stencils from an input image using K-Means clustering.

        Parameters
        ----------
        input_img : str
            Path to the input image file.
        output_path : str
            Directory path to save the stencil images.
        nb_colors : int
            Number of color clusters to segment the image into.
        """
        flattened_img = self.image_processing.process(input_img)
        clustered_img = self.clustering.compute(flattened_img, nb_colors)
        self.image_processing.color_separation(clustered_img, input_img, output_path)
