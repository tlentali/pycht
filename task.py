from utils_mixin import KMeans


def main():
    harry = KMeans()
    harry.separation(harry.exec_kmeans(
        4, harry.convert_image('misc/cat.jpg')), 'misc/cat.jpg')


if __name__ == "__main__":
    main()
