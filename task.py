from utils_mixin import KMeans
import config
import argparse


def main(nb_cluster, image_path):
    harry = KMeans()
    harry.separation(
        harry.exec_kmeans(
            nb_cluster,
            harry.convert_image(
                image_path
            )
        ),
        config.IMAGE_PATH
    )


if __name__ == "__main__":
    # build the ArgumentParser
    #"""
    parser = argparse.ArgumentParser()

    parser.add_argument('--clusters',
                        dest='clusters',
                        default=config.NB_CLUSTER)
    parser.add_argument('--file',
                        dest='file_path',
                        default=config.IMAGE_PATH)
    args = parser.parse_args()

    nb_cluster = args.clusters
    image_path = args.file_path
    #"""
    main(nb_cluster, image_path)
