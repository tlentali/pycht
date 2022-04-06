"""
Project settings
"""
from image_processing import Image_Processing
from clustering import Clustering
    
    
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
