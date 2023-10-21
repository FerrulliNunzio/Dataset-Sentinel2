import json
from Scripts.Geometry.MbrPolygon import MbrPolygon


class JsonManager:
    """
    Nome: __init__

    Input:

    Output:

    Comportamento: Costruttore che inizializza le variabili Data e Coordinates.
    """

    def __init__(self, path):
        self.File_path = path
        with open(self.File_path, 'r') as json_file:
            self.Data = json.load(json_file)
        self.Coordinates = []

    """
    Nome: __extract_geometry
    
    Input:
    
    Output:
    
    Comportamento: inserisce nella lista Coordinates le coordinate delle geometrie delle feature.
    """

    def __extract_geometry(self):
        # Verificato se il file JSON contiene geometrie GeoJSON (Feature o FeatureCollection)
        if 'type' in self.Data and self.Data['type'] == 'FeatureCollection':
            features = self.Data['features']
            for feature in features:
                if 'geometry' in feature:
                    geometry = feature['geometry']
                    if 'type' in geometry and geometry['type'] == 'Polygon':
                        # Coordinate poligono
                        self.Coordinates.append(geometry['coordinates'])

    """
    Nome: contain_geometry
    
    Input:
    
    Output: restituisce un booleano
    
    Comportamento: restituisce True se la lista Coordinates non è vuota (ci sono geometrie nel file), 
                   restituisce False altrimenti
    """

    def contain_geometry(self):
        self.__extract_geometry()
        if len(self.Coordinates) > 0:
            return True
        elif len(self.Coordinates) == 0:
            return False

    """
    Nome: get_first_feature
    
    Input:
    
    Output: restituisce il primo elemento della variabile Data
    
    Comportamento: restituisce la prima feature del file se il file contiene geometrie
    """

    def get_first_feature(self):
        if self.contain_geometry():
            return self.Data['features'][0]
        else:
            print("Il file JSON non contiene una struttura GeoJSON valida")

    """
    Nome: get_data
    
    Input:
    
    Output: restituisce la variabile Data
    
    Comportamento: restituisce la variabile Data
    """

    def get_data(self):
        return self.Data

    """
    Nome: get_Coordinates
    
    Input:
    
    Output: restituisce la lista Coordinates
    
    Comportamento: se la lista Coordinates e vuota la riempie 
                   estraendo le geometrie dalle feature del file e restituisce la lista Coordinates piena
    """

    def get_coordinates(self):
        if len(self.Coordinates) == 0:
            self.__extract_geometry()
        return self.Coordinates

    def get_outside_rectangle(self, path):
        rectangle = MbrPolygon(path)
        return rectangle.get_square()
