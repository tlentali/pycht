"""
Project settings
"""
from .image_processing import ImageProcessing
from .clustering import Clustering


class Pycht:
    """
    Project settings
    """

    def __init__(self) -> None:
        self.image_processing = ImageProcessing()
        self.clustering = Clustering()

    def stencil(self, input_path: str, output_path: str, nb_colors: int) -> None:
        return self.image_processing.color_separation(
            self.clustering.exec_kmeans(
                self.image_processing.process(input_path), nb_colors
            ),
            input_path,
            output_path,
        )
