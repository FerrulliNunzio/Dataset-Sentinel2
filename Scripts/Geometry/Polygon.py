import ee


class Polygon:
    __Polygon: ee.Geometry.Polygon = None

    """ Nome: __init__
        
        Input: lista di coordinate
        
        Output: //
        
        Comportamento: Inizializza la variabile __Polygon
    """
    def __init__(self, coordinates: list):
        self.__Polygon = ee.Geometry.Polygon(coordinates)

    """ Nome: get_polygon_coordinates

        Input: //

        Output: lista di coordinate

        Comportamento: restiruisce una lista di coordinate
    """
    def get_polygon_coordinates(self):
        return self.__Polygon.coordinates().getInfo()

    """ Nome: get_polygon

        Input: //

        Output: Geometria

        Comportamento: restituisce la variabile __Poligon 
    """
    def get_polygon(self):
        return self.__Polygon

    """ Nome: get_area

        Input: //

        Output: int

        Comportamento: restituisce l'area della geometria in metri quadrati
    """
    def get_area(self):
        return self.__Polygon.area().divide(1000 * 1000)

    """ Nome: get_perimeter

        Input: //

        Output: int

        Comportamento: restituisce il perimetro della geometria in metri    
    """
    def get_perimeter(self):
        return self.__Polygon.perimeter().divide(1000)

    """ Nome: get_geojson_type

        Input: //

        Output: string

        Comportamento: restituisce il tipo delle geometria come una stringa    
    """
    def get_geojson_type(self):
        return self.__Polygon.type()
