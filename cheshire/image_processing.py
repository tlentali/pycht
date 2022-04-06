"""
Project settings
"""
import cv2
import sys
import numpy as np
import pandas as pd


class Image_Processing:
    """
    Project settings
    """
    def convert_image_to_float(self, input_path:str):
        """
        Project settings
        """
        img = cv2.imread(input_path)
        Z = img.reshape((-1, 3))
        # convert to np.float32
        Z = np.float32(Z)
        return Z
    
     def separation(self, res, input_path:str, output_path:str) -> None:
        """
        Project settings
        """
        img = cv2.imread(input_path)
        # separate differants colors
        df = pd.DataFrame(res)
        df.columns = ['col1', 'col2', 'col3']
        df['tot'] = df["col1"].astype(
            str) + df["col2"].astype(str) + df["col3"].astype(str)
        df['tot'].unique()
        cmp = 1
        for i in df['tot'].unique():
            df_annexe = df.copy()
            df_annexe["col1"].loc[(df['tot'] != i)] = 0
            df_annexe["col2"].loc[(df['tot'] != i)] = 0
            df_annexe["col3"].loc[(df['tot'] != i)] = 0
            res_annexe = df_annexe[["col1", "col2", "col3"]].as_matrix()
            res_annexe2 = res_annexe.reshape((img.shape))
            cv2.imwrite("stencil_" + str(cmp) + ".jpg", res_annexe2)
            cmp += 1
        res_1 = df[["col1", "col2", "col3"]].as_matrix()
        res_2 = res.reshape((img.shape))
        cv2.imwrite(output_path, res_2)

    def ShowImage(self, result_path:str, res) -> None:
        """
        Project settings
        """
        # generate final image
        res2 = res.reshape((self.img.shape))
        cv2.imwrite(result_path, res2)
        cv2.imshow('res2', res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()