# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.

import ee
from ee import EEException
from Scripts.ExportToDrive.ExportDataset import ExportDataset
from Scripts.ExportToDrive.ExportOption import ExportOption
from Scripts.ExportToDrive.TaskException import TaskException
from Scripts.JsonManagement.JsonManager import JsonManager
from Scripts.Connection.Autentication import Autentication
from Scripts.Dataset.ImgCollection import ImgCollection
from Scripts.PathManager.PathManager import PathManager
from Scripts.Dataset.Dataset import Dataset

COPERNICUS_SURFACE_REFLECTANCE_ID = "COPERNICUS/S2_SR_HARMONIZED"
COPERNICUS_TOP_OF_ATMOSPHERE_REFLECTANCE_ID = "COPERNICUS/S2_HARMONIZED"
PATH = 'C:/Users/Utente/Desktop/DatasetSentinel/geojson_78.geojson'
START_DATE = "2018-10-01"
END_DATE = "2018-10-31"


def mask_s2_clouds(image):
    qa = image.select('QA60')
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11
    mask = (qa.bitwiseAnd(cloudBitMask).eq(0)) and (qa.bitwiseAnd(cirrusBitMask).eq(0))
    return image.updateMask(mask).divide(10000)


if __name__ == '__main__':
    # Start

    # Connecting to Google Earth Engine
    Autenticate = Autentication()
    Autenticate.autentication()
    Autenticate.initializate()

    Path = PathManager()
    Path.set_complete_path("JSON_File")
    count = 0
    while count <= 93:
        try:
            print(f"provo a scaricare il file {count} \n\n\n")
            path_with_file = ""
            FileName = "geojson_" + str(count) + ".geojson"
            path_with_file = Path.get_complete_path() + "/" + FileName
            print(path_with_file)

            try:
                # Loading data from Google Earth Engine
                print("Loading the mask from Google Earth Engine assets...\n")
                mask = ee.Image("projects/nunzioferrulli/assets/mask_" + str(count))
                print("Loading data from Google Earth Engine...\n")
                id = COPERNICUS_SURFACE_REFLECTANCE_ID
                CollectionImage = ImgCollection(id)
                # Creation of the customized dataset
                print(f"Filtering the data of the period {START_DATE}/{END_DATE}...\n")
                FilteredCollection = CollectionImage.filteredCollection(START_DATE, END_DATE)
                print("Cloud mask applied...\n")
                FilteredCollection.map(mask_s2_clouds)
                # Loaded the GeoJSON file to get the geometry of the first feature of the file
                print("Creating geometry...\n")
                Geojson = JsonManager(path_with_file)
                Geometry = JsonManager.getOutsideRectangle(path_with_file, path_with_file)
                print("Creating dataset...\n")
                dataset = Dataset(FilteredCollection)
                print("Filtering the image collection with geometry...\n")
                dataset.set_image(CollectionImage.filter_bound(FilteredCollection, Geometry))
                print(f"Le immagini trovate nel periodo {START_DATE} - {END_DATE} "
                      f"sono: {dataset.get_collection_length()}")
                BandsList = ['B1', 'B2', 'B3',
                             'B4', 'B5', 'B6',
                             'B7', 'B8', 'B9',
                             'B8A', 'B11', 'B12', 'SCL']
                print("Select bands to download...\n")
                dataset.select_bands(BandsList)
                print("Mask transform extraction...\n")
                Projection = mask.projection()
                Transform = Projection.getInfo()['transform']
                print("Extraction of the image median...\n")
                imageToExtraxt = dataset.extract_median()
                print("Starting to export images to the drive...\n")
                ExportOptions = ExportOption(imageToExtraxt, "Immagine", 'DataSetSentinel2_2018', 'geojson_' + str(count), Geometry, 'GeoTIFF', 'EPSG:4326', Transform)
                try:
                    exportDataset = ExportDataset(ExportOptions.get_export_option())
                    exportDataset.start_export_dataset()
                except TaskException:
                    print("Il task di esportazione non è stato avviato. Riprovare")
            except EEException:
                print("La mschera cercata non esiste")
        except FileNotFoundError:
            print("Il file cercato non è stato trovato")

        count += 1

    # end
