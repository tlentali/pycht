"""
Image processing utilities for reading, displaying, reshaping, and performing color separation
to generate final stencils from clustered images.
"""

import cv2
import numpy as np
import pandas as pd


class ImageProcessing:
    """
    A collection of image processing methods for loading, transforming,
    displaying, and segmenting colors within an image.
    """

    def process(self, input_path: str) -> np.ndarray:
        """
        Load an image from disk, reshape it, and convert it to float32 format.

        Parameters
        ----------
        input_path : str
            Path to the input image file.

        Returns
        -------
        np.ndarray
            Flattened image array with dtype np.float32.
        """
        img = self.read_image(input_path)
        Z = self.reshape_image(img)
        return self.convert_image_to_float(Z)

    @staticmethod
    def read_image(input_path: str) -> np.ndarray:
        """
        Load an image from the specified file path.

        Parameters
        ----------
        input_path : str
            Path to the input image file.

        Returns
        -------
        np.ndarray
            The loaded image as a NumPy array (BGR format).
        """
        return cv2.imread(input_path)

    @staticmethod
    def reshape_image(image: np.ndarray) -> np.ndarray:
        """
        Reshape the image into a 2D array of pixels.

        Parameters
        ----------
        image : np.ndarray
            Original image array.

        Returns
        -------
        np.ndarray
            Reshaped array of shape (num_pixels, 3).
        """
        return image.reshape((-1, 3))

    @staticmethod
    def write_image(res: np.ndarray, output_path: str) -> None:
        """
        Save an image to disk.

        Parameters
        ----------
        res : np.ndarray
            Image array to write.
        output_path : str
            Destination file path.
        """
        cv2.imwrite(output_path, res)

    @staticmethod
    def convert_image_to_float(Z):
        """
        Convert an image array to float32 format.

        Parameters
        ----------
        Z : np.ndarray
            Input image array.

        Returns
        -------
        np.ndarray
            Converted array with dtype np.float32.
        """
        return np.float32(Z)

    def color_separation(self, res, input_path: str, output_path: str) -> None:
        """
        Separate and isolate each color cluster from an image and save each cluster
        as a separate stencil with transparency.

        Parameters
        ----------
        res : np.ndarray
            Clustered image data (flattened).
        input_path : str
            Path to the original image (for reshaping purposes).
        output_path : str
            Path to save the combined clustered image.
        """
        img = self.read_image(input_path)
        # separate differants colors
        df = pd.DataFrame(res)
        df.columns = ["col1", "col2", "col3"]
        df["tot"] = df["col1"].astype(str) + df["col2"].astype(str) + df["col3"].astype(str)
        df["tot"].unique()
        cmp = 1
        for i in df["tot"].unique():
            df_annexe = df.copy()
            df_annexe.loc[(df["tot"] != i), "col1"] = 0
            df_annexe.loc[(df["tot"] != i), "col2"] = 0
            df_annexe.loc[(df["tot"] != i), "col3"] = 0

            res_annexe = df_annexe[["col1", "col2", "col3"]].values
            res_annexe2 = res_annexe.reshape((img.shape))

            # Create transparency mask: non-black areas become visible
            color = (0, 0, 0)
            mask = np.where((res_annexe2 == color).all(axis=2), 0, 255).astype(np.uint8)

            # Convert to BGRA and add alpha channel
            result = res_annexe2.copy()
            result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
            result[:, :, 3] = mask

            cv2.imwrite("stencil_" + str(cmp) + ".png", result)
            cmp += 1
        res_2 = res.reshape((img.shape))
        self.write_image(res_2, output_path + "stencil_final.png")
