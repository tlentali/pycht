import numpy as np
import cv2
import os
import shutil
import pytest
from pycht.image_processing import ImageProcessing


@pytest.fixture(scope="module")
def sample_image(tmp_path_factory):
    """Create a 4x4 RGB image with 2 color clusters."""
    img = np.zeros((4, 4, 3), dtype=np.uint8)
    img[:2, :] = [255, 0, 0]  # Red
    img[2:, :] = [0, 255, 0]  # Green

    img_path = tmp_path_factory.mktemp("data") / "input.png"
    cv2.imwrite(str(img_path), img)
    return img_path


def test_color_separation_creates_stencils(sample_image, tmp_path):
    processor = ImageProcessing()
    img = cv2.imread(str(sample_image))
    reshaped = img.reshape((-1, 3))

    processor.color_separation(reshaped, str(sample_image), str(tmp_path))

    stencil_files = list(tmp_path.glob("stencil_*.png"))
    assert len(stencil_files) >= 2  # At least one stencil + final

    for f in stencil_files:
        result = cv2.imread(str(f), cv2.IMREAD_UNCHANGED)
        assert result is not None
        if f.name == "stencil_final.png":
            assert result.shape[2] == 3  # BGR
        else:
            assert result.shape[2] == 4  # BGRA
