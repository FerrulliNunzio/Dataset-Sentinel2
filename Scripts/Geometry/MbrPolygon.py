import json
from shapely import MultiPolygon
from shapely.geometry import shape
from Scripts.Geometry.Polygon import Polygon


class MbrPolygon:
    __Square = None

    """ Nome: __init__
    
        Input: pash: string
        
        Output: //
        
        Comportamento: Inizializza la variabile __Square
    """

    def __init__(self, path: str):
        with open(path) as file:
            features = json.load(file)

        # create a shapely MultiPolygon from each GeoJSON polygon
        union = MultiPolygon(shape(feature['geometry']) for feature in features['features'])
        # create a new Polygon from the bounds of the union
        self.extent = union.bounds
        self.__Square = Polygon([
            [self.extent[0], self.extent[3]],
            [self.extent[2], self.extent[3]],
            [self.extent[2], self.extent[1]],
            [self.extent[0], self.extent[1]],
            [self.extent[0], self.extent[3]],
        ])

    """ Nome: get_square
        
        Input: //
        
        Output: Geometry
        
        Comportamento: restituisce la Geometria della variabile __Square
    """
    def get_square(self):
        return self.__Square.get_polygon()
