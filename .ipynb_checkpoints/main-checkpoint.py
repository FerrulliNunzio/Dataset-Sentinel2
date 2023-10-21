# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
import ee
import geemap
import csv
from ee.batch import Export

#from Scripts.Collection.GeoGeometry import GeoGeometry
from Scripts.Connection.Autentication import Autentication
from Scripts.Collection.ImgCollection import ImgCollection
from Scripts.PathManager.PathManager import PathManager
from Scripts.Utility.VisualParams import VisualParams

COPERNICUS_SURFACE_REFLECTANCE_ID = "COPERNICUS/S2_SR_HARMONIZED"
COPERNICUS_TOP_OF_ATMOSPHERE_REFLECTANCE_ID = "COPERNICUS/S2_HARMONIZED"
PATH = 'C:/Users/Utente/Desktop/DatasetSentinel/geojson_78.geojson'
START_DATE = "2018-10-01"
END_DATE = "2018-11-01"

def maskS2clouds(image):
    qa = image.select('QA60')
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11
    mask = (qa.bitwiseAnd(cloudBitMask).eq(0)) and (qa.bitwiseAnd(cirrusBitMask).eq(0))
    return image.updateMask(mask).divide(10000)

if __name__ == '__main__':
    #Start

    #Connecting to Google Earth Engine
    Autenticate = Autentication()
    Autenticate.autentication()
    Autenticate.initializate()

    semi_path = ""
    while True:
        print("Inserire: \n"
            "1: per selezionare file GeoJSON;\n"
            "2: per selezionare file shape.\n")
        option = input()
        if int(option) == 1 or int(option) == 2:
            break

    if int(option) == 1:
        semi_path = "JSON_File"
    elif int(option) == 2:
       semi_path = "Shape_File"

    Path = PathManager()
    Path.set_complete_path(semi_path)
    selected_file = ""
    while True:
        index = 1
        print("inserire:")
        for item in Path.get_file_in_path():
            print(str(index) + ": " + item)
            index = index + 1
        selection = 0
        selection = input()
        if int(selection) > 0 and int(selection) <= index - 1:
            break

    path_with_file = ""
    path_with_file = Path.get_complete_path() + "/" + Path.get_file_in_path()[int(selection) - 1]

    print(path_with_file)

    # Loading data from Google Earth Engine
    id = COPERNICUS_SURFACE_REFLECTANCE_ID
    ImgCollection = ImgCollection(id)

    # Creation of the customized dataset
    Dataset = ImgCollection.filtered_collection(START_DATE, END_DATE)
    Dataset.map(maskS2clouds)

    # Loaded the GeoJSON file to get the geometry of the first feature of the file
    Geojson = GeoGeometry(path_with_file)
    first_feature = Geojson.get_first_feature()
    Geometry = first_feature['geometry']
    Dataset = ImgCollection.filter_bound(Dataset, Geometry)
    print(Dataset.size().getInfo())
    #end











#Coord = Geojson.get_Coordinates()

#    print(len(Coord))

    #print(Coord[0][0][0][0]) un elemento di Coord contiene una lista che contiene una lista che contiene una lista che contiene una lista di due elementi