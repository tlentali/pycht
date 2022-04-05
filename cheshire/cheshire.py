"""
Project settings
"""
import cv2
import sys
import numpy as np
import pandas as pd
    
    
class Cheshire:
    """
    Project settings
    """
    def stencil(self, input_path:str, output_path:str, nb_cluster:int) -> None:
        self.separation(
            self.exec_kmeans(
                nb_cluster,
                self.convert_image_to_float(input_path)
            ),
            input_path, 
            output_path
        )


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

        
class Clustering:
    """
    Project settings
    """
    @staticmethod
    def exec_kmeans(nb_cluster:int, Z):
        """
        Project settings
        """
        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
        # Set flags (Just to avoid line break in the code)
        flags = cv2.KMEANS_RANDOM_CENTERS
        ret, label, center = cv2.kmeans(Z, nb_cluster, None, criteria, 10, flags)
        # Now convert back into uint8, and make original image
        center = np.uint8(center)  # value of the color selected by algo
        res = center[label.flatten()]
        return res
