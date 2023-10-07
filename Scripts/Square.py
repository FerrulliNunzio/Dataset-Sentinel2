import ee
import json
from shapely import MultiPolygon
from shapely.geometry import shape


class Square:
    def __init__(self, path):
        with open(path) as file:
            features = json.load(file)

        # create a shapely MultiPolygon from each GeoJSON polygon
        union = MultiPolygon(shape(feature['geometry']) for feature in features['features'])
        # create a new Polygon from the bounds of the union
        self.extent = union.bounds
        self.square = ee.Geometry.Polygon([
            [self.extent[0], self.extent[3]],
            [self.extent[2], self.extent[3]],
            [self.extent[2], self.extent[1]],
            [self.extent[0], self.extent[1]],
            [self.extent[0], self.extent[3]],
        ])

    def getSquare(self):
        return self.square