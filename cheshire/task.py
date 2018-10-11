from utils_mixin import KMeans
import config
import argparse
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def cheshire(nb_cluster, image_path):
    harry = KMeans()
    harry.separation(
        harry.exec_kmeans(
            nb_cluster,
            harry.convert_image(
                image_path
            )
        ),
        image_path
    )


if __name__ == "__main__":
    nb_cluster = config.NB_CLUSTER
    image_path = config.IMAGE_PATH
    cheshire(nb_cluster, image_path)
    print('Done!')
