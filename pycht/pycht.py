"""
Main project settings and execution logic.
"""

from .image_processing import ImageProcessing
from .clustering import Clustering


class Pycht:
    """
    Main interface for generating color-separated stencils from an input image.

    This class orchestrates the image processing and clustering steps by
    using the `ImageProcessing` and `Clustering` components.
    """

    def __init__(self) -> None:
        self.image_processing = ImageProcessing()
        self.clustering = Clustering()

    def stencil(self, input_img: str, nb_colors: int = 3, output_path: str = "./") -> None:
        """
        Generate color stencils from an input image using K-Means clustering.

        This method reads the image, clusters its colors, and saves each cluster
        as a separate transparent stencil image.

        Parameters
        ----------
        input_img : str
            Path to the input image file.
        output_path : str
            Path to save the final clustered image.
        nb_colors : int
            Number of color clusters to segment the image into.
        """
        return self.image_processing.color_separation(
            self.clustering.compute(self.image_processing.process(input_img), nb_colors),
            input_img,
            output_path,
        )
