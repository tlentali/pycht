"""
Package building.
"""

from .pycht import Pycht
from .image_processing import ImageProcessing
from .clustering import Clustering
from .cli import compute

__all__ = ["Pycht", "ImageProcessing", "Clustering", "compute"]


def stencil(input_img: str, nb_colors: int = 3, output_path: str = "."):
    return Pycht().stencil(input_img, nb_colors, output_path)
