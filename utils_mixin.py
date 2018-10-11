import numpy as np
import cv2
import pandas as pd


class KMeans(object):
    def convert_image(self, file_path):
        img = cv2.imread(file_path)
        Z = img.reshape((-1, 3))
        # convert to np.float32
        Z = np.float32(Z)
        return Z

    def exec_kmeans(self, nb_cluster, Z):
        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = nb_cluster
        ret, label, center = cv2.kmeans(
            Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        # Now convert back into uint8, and make original image
        center = np.uint8(center)  # value off the color selected by algo
        res = center[label.flatten()]
        return res

    def separation(self, res, file_path):
        img = cv2.imread(file_path)
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
            cv2.imwrite("results/resultat_" + str(cmp) + ".jpg", res_annexe2)
            cmp += 1
        res_1 = df[["col1", "col2", "col3"]].as_matrix()
        res_2 = res.reshape((img.shape))
        cv2.imwrite("results/resultat_final.jpg", res_2)

    def ShowImage(self, result_path, res):
        # generate final image
        res2 = res.reshape((self.img.shape))
        cv2.imwrite(result_path, res2)
        cv2.imshow('res2', res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
