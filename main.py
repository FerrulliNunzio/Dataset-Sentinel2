# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
import json
import os

import ee
import folder as folder
import geemap
import csv
import geopandas as gdp
from ee import collection, image
from ee.batch import Export

from Scripts.Collection.GeoGeometry import GeoGeometry
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




while True:
    while True:
        print("inserisci:\n"
              "1: convertire file GeoJSON in file Shape\n"
              "2: creare un dataset con file GeoJSON")
        choise = input()
        if int(choise) == 1 or int(choise) == 2:
            break

    if int(choise) == 1:
        GeoJson_folder_directory = PathManager()
        GeoJson_folder_directory.set_complete_path("JSON_File")
        while True:
            print("inserisci:")
            index = 1
            for item in GeoJson_folder_directory.get_file_in_path():
                print(str(index) + ": " + item)
                index =index + 1
            option = input()
            if int(option) > 0 and int(option) <= index - 1:
                break
        Geo_file_selected = GeoJson_folder_directory.get_file_in_path()[int(option) - 1]
        GeoJson_file_path = GeoJson_folder_directory.get_complete_path() + "/" + Geo_file_selected
        Shape_forlder_directory = PathManager()
        Shape_forlder_directory.set_complete_path("Shape_File")
        try:
            os.makedirs(Shape_forlder_directory.get_complete_path() + "/" + Geo_file_selected)
            Shape_file_path = Shape_forlder_directory.get_complete_path() + "/" + Geo_file_selected
            GeoCoordinate = GeoGeometry(GeoJson_file_path)
            Coordinate = GeoCoordinate.get_Coordinates()
            gdp = gdp.read_file(GeoJson_file_path)
            gdp.to_file(Shape_file_path + "/" + Geo_file_selected + ".shp")
        except FileExistsError:
            print("Esiste già una cartella con questo nome e questi file salvati")

    if int(choise) == 2:
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
        CollectionImage = ImgCollection(id)

        # Creation of the customized dataset
        Dataset = CollectionImage.filteredCollection(START_DATE, END_DATE)
        Dataset.map(maskS2clouds)

        # Loaded the GeoJSON file to get the geometry of the first feature of the file
        Geojson = GeoGeometry(path_with_file)
        first_feature = Geojson.get_first_feature()
        Geometry = first_feature['geometry']
        Dataset = CollectionImage.filter_bound(Dataset, Geometry)
        print(Dataset.size().getInfo())
    #end











#Coord = Geojson.get_Coordinates()

#    print(len(Coord))

    #print(Coord[0][0][0][0]) un elemento di Coord contiene una lista che contiene una lista che contiene una lista che contiene una lista di due elementi