from typing import Tuple
from PIL import Image
import numpy as np
from pathlib import Path


class ImageProcessing:
    """
    A collection of image processing methods for loading, transforming,
    and segmenting colors within an image using Pillow instead of OpenCV.
    """

    def process(self, input_path: Path) -> np.ndarray:
        """
        Load an image from disk and flatten it into a 2D array of float32 pixels.
        """
        if not input_path.exists():
            raise FileNotFoundError(f"Image not found at: {input_path}")
        img = Image.open(input_path).convert("RGB")
        return np.float32(np.array(img).reshape((-1, 3)))

    @staticmethod
    def write_image(image: np.ndarray, output_path: Path) -> None:
        """Write image to a file."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img = Image.fromarray(image)
        img.save(output_path)

    @staticmethod
    def to_bgra_with_alpha(image: np.ndarray, alpha_mask: np.ndarray) -> np.ndarray:
        """
        Convert an RGB image to RGBA using a binary alpha mask.
        """
        h, w, _ = image.shape
        rgba = np.zeros((h, w, 4), dtype=np.uint8)
        rgba[:, :, :3] = image
        rgba[:, :, 3] = alpha_mask
        return rgba

    def color_separation(
        self,
        clustered_pixels: np.ndarray,
        input_path: Path,
        output_dir: Path,
        background_color: Tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        """
        Generate and save separate stencil images for each color cluster in the input image.
        """
        clustered_image, shape = self._load_and_prepare(input_path, clustered_pixels)
        unique_colors = np.unique(clustered_pixels, axis=0)

        for i, color in enumerate(unique_colors, start=1):
            stencil_bgra = self._create_stencil_image(clustered_image, color, background_color)
            self.write_image(stencil_bgra, output_dir / f"stencil_{i}.png")

        self.write_image(clustered_image, output_dir / "stencil_final.png")

    def _load_and_prepare(self, input_path: Path, clustered_pixels: np.ndarray) -> Tuple[np.ndarray, Tuple[int, int]]:
        """
        Load the original image to extract its shape and reshape the clustered pixel data accordingly.
        """
        if not input_path.exists():
            raise FileNotFoundError(f"Image not found at: {input_path}")
        img = Image.open(input_path).convert("RGB")
        w, h = img.size
        clustered_image = clustered_pixels.reshape((h, w, 3)).astype(np.uint8)
        return clustered_image, (h, w)

    def _create_stencil_image(
        self, clustered_image: np.ndarray, color: np.ndarray, background_color: Tuple[int, int, int]
    ) -> np.ndarray:
        """
        Create a RGBA stencil image where only the selected color cluster is visible and the rest is transparent.
        """
        mask = np.all(clustered_image == color, axis=2)
        stencil = np.full_like(clustered_image, background_color, dtype=np.uint8)
        stencil[mask] = color
        alpha = (mask * 255).astype(np.uint8)
        return self.to_bgra_with_alpha(stencil, alpha)
