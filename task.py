from utils_mixin import KMeans
import config
import argparse


def main():
    harry = KMeans()
    harry.separation(
        harry.exec_kmeans(
            config.NB_CLUSTER,
            harry.convert_image(
                config.IMAGE_PATH
            )
        ),
        config.IMAGE_PATH
    )


if __name__ == "__main__":
    # build the ArgumentParser
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--clusters', dest='clusters')
    parser.add_argument('--file', dest='file_path')

    args = parser.parse_args()

    config.IMAGE_PATH = args.file_path
    config.NB_CLUSTER = args.clusters
    """
    main()
