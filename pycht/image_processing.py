"""
Project settings
"""
import cv2
import numpy as np
import pandas as pd


class ImageProcessing:
    """
    Project settings
    """

    def process(self, input_path: str) -> np.ndarray:
        """
        Convert to np.float32
        """
        img = self.read_image(input_path)
        Z = self.reshape_image(img)
        return self.convert_image_to_float(Z)

    @staticmethod
    def read_image(input_path: str) -> np.ndarray:
        """
        Read image from path
        """
        return cv2.imread(input_path)

    @staticmethod
    def reshape_image(image: np.ndarray) -> np.ndarray:
        """
        Reshape image
        """
        return image.reshape((-1, 3))

    @staticmethod
    def write_image(res: np.ndarray, output_path: str) -> None:
        cv2.imwrite(output_path, res)

    def ShowImage(self, result_path: str, res) -> None:
        """
        Project settings
        """
        # generate final image
        res2 = res.reshape((self.img.shape))
        cv2.imwrite(result_path, res2)
        cv2.imshow("res2", res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def convert_image_to_float(Z) -> np.ndarray:
        """
        Convert to np.float32
        """
        return np.float32(Z)

    def color_separation(self, res, input_path: str, output_path: str) -> None:
        """
        Project settings
        """
        img = self.read_image(input_path)
        # separate differants colors
        df = pd.DataFrame(res)
        df.columns = ["col1", "col2", "col3"]
        df["tot"] = (
            df["col1"].astype(str) + df["col2"].astype(str) + df["col3"].astype(str)
        )
        df["tot"].unique()
        cmp = 1
        for i in df["tot"].unique():
            df_annexe = df.copy()
            df_annexe["col1"].loc[(df["tot"] != i)] = 0
            df_annexe["col2"].loc[(df["tot"] != i)] = 0
            df_annexe["col3"].loc[(df["tot"] != i)] = 0
            res_annexe = df_annexe[["col1", "col2", "col3"]].as_matrix()
            res_annexe2 = res_annexe.reshape((img.shape))
            cv2.imwrite("stencil_" + str(cmp) + ".jpg", res_annexe2)
            cmp += 1
        res_1 = df[["col1", "col2", "col3"]].as_matrix()
        res_2 = res.reshape((img.shape))
        self.write_image(res_2, output_path)
