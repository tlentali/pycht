from typing import Tuple

import cv2
import numpy as np


class ImageProcessing:
    """
    A collection of image processing methods for loading, transforming,
    and segmenting colors within an image.
    """

    def process(self, input_path: str) -> np.ndarray:
        """
        Load an image from disk and flatten it into a 2D array of float32 pixels.

        This function reads an image from the given file path, verifies it was loaded
        correctly, reshapes it into a 2D array where each row is a pixel with 3 color channels,
        and casts it to float32 for clustering.

        Parameters
        ----------
        input_path : str
            Path to the input image file.

        Returns
        -------
        np.ndarray
            2D array of shape (num_pixels, 3), dtype float32.

        Raises
        ------
        FileNotFoundError
            If the image cannot be loaded from the specified path.
        """
        img = cv2.imread(input_path)
        if img is None:
            raise FileNotFoundError(f"Image not found at: {input_path}")
        return np.float32(img.reshape((-1, 3)))

    @staticmethod
    def write_image(image: np.ndarray, output_path: str) -> None:
        """Write image in file."""
        cv2.imwrite(output_path, image)

    @staticmethod
    def to_bgra_with_alpha(image: np.ndarray, alpha_mask: np.ndarray) -> np.ndarray:
        """
        Convert a BGR image to BGRA using a binary alpha mask.

        Parameters
        ----------
        image : np.ndarray
            Input BGR image.
        alpha_mask : np.ndarray
            Alpha mask (0=transparent, 255=opaque).

        Returns
        -------
        np.ndarray
            BGRA image with alpha channel.
        """
        result = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        result[:, :, 3] = alpha_mask.astype(np.uint8)
        return result

    def color_separation(
        self,
        clustered_pixels: np.ndarray,
        input_path: str,
        output_dir: str,
        background_color: Tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        """
        Generate and save separate stencil images for each color cluster in the input image.

        This method reconstructs the clustered image from flattened pixel data,
        identifies all unique color clusters, and for each one generates a transparent
        stencil image. Each resulting image is saved with an alpha channel indicating
        where the cluster appears.

        Parameters
        ----------
        clustered_pixels : np.ndarray
            Flattened image data with clustered RGB values.
        input_path : str
            Path to the original input image, used to get image dimensions.
        output_dir : str
            Directory where stencil images will be saved.
        background_color : Tuple[int, int, int], optional
            RGB background color for non-cluster areas, by default black (0, 0, 0).
        """
        clustered_image, shape = self._load_and_prepare(input_path, clustered_pixels)
        unique_colors = np.unique(clustered_pixels, axis=0)

        for i, color in enumerate(unique_colors, start=1):
            stencil_bgra = self._create_stencil_image(clustered_image, color, background_color)
            self.write_image(stencil_bgra, f"{output_dir}/stencil_{i}.png")

        self.write_image(clustered_image, f"{output_dir}/stencil_final.png")

    def _load_and_prepare(self, input_path: str, clustered_pixels: np.ndarray) -> Tuple[np.ndarray, Tuple[int, int]]:
        """
        Load the original image to extract its shape and reshape the clustered pixel data accordingly.

        Parameters
        ----------
        input_path : str
            Path to the original input image.
        clustered_pixels : np.ndarray
            Flattened pixel array of shape (num_pixels, 3).

        Returns
        -------
        clustered_image : np.ndarray
            Image reshaped to (height, width, 3) with dtype uint8.
        shape : Tuple[int, int]
            The original image height and width.

        Raises
        ------
        FileNotFoundError
            If the input image cannot be read from the path.
        """
        img = cv2.imread(input_path)
        if img is None:
            raise FileNotFoundError(f"Image not found at: {input_path}")
        h, w, _ = img.shape
        clustered_image = clustered_pixels.reshape((h, w, 3)).astype(np.uint8)
        return clustered_image, (h, w)

    def _create_stencil_image(
        self, clustered_image: np.ndarray, color: np.ndarray, background_color: Tuple[int, int, int]
    ) -> np.ndarray:
        """
        Create a BGRA stencil image where only the selected color cluster is visible and the rest is transparent.

        Parameters
        ----------
        clustered_image : np.ndarray
            The full clustered image of shape (H, W, 3), dtype uint8.
        color : np.ndarray
            A 3-element array representing the RGB color of the cluster to extract.
        background_color : Tuple[int, int, int]
            The background RGB color to use where the cluster is not present.

        Returns
        -------
        np.ndarray
            A stencil image with shape (H, W, 4) in BGRA format, where the alpha channel masks out
            all areas except those matching the selected color cluster.
        """
        mask = np.all(clustered_image == color, axis=2)
        stencil = np.full_like(clustered_image, background_color)
        stencil[mask] = color

        alpha = (mask * 255).astype(np.uint8)
        return self.to_bgra_with_alpha(stencil, alpha)
