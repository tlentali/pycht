import numpy as np
from PIL import Image
import pytest
from pycht.image_processing import ImageProcessing
from pathlib import Path


@pytest.fixture(scope="module")
def sample_image(tmp_path_factory):
    """Create a 4x4 RGB image with 2 color clusters using Pillow."""
    img = np.zeros((4, 4, 3), dtype=np.uint8)
    img[:2, :] = [255, 0, 0]  # Red
    img[2:, :] = [0, 255, 0]  # Green

    img_dir = tmp_path_factory.mktemp("data")
    img_path = img_dir / "input.png"
    Image.fromarray(img).save(img_path)
    return img_path


def test_color_separation_creates_stencils(sample_image: Path, tmp_path: Path):
    processor = ImageProcessing()

    # Simule la sortie d'un clustering KMeans
    img = Image.open(sample_image).convert("RGB")
    reshaped = np.array(img).reshape((-1, 3))

    processor.color_separation(reshaped, sample_image, tmp_path)

    stencil_files = list(tmp_path.glob("stencil_*.png"))
    assert len(stencil_files) >= 2  # At least one stencil + final

    for f in stencil_files:
        with Image.open(f) as result:
            if f.name == "stencil_final.png":
                assert result.mode == "RGB"
            else:
                assert result.mode == "RGBA"
