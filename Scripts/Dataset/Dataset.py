import ee


class Dataset:

    __ImageCollection = None

    """
    Nome: __init__

    Input: collection_image

    Output: //

    Comportamento: Inizializza  la variabile __ImageCollection.
    """
    def __init__(self, collection_image: ee.ImageCollection):
        self.__ImageCollection = collection_image

    """
    Nome: set_image

    Input: image_collection

    Output: //

    Comportamento: Avvalora la variabile __ImageCollection con il parametro passato.
    """
    def set_image(self, image_collection: ee.ImageCollection):
        self.__ImageCollection = image_collection

    """
    Nome: get_image

    Input: //

    Output: __ImageCollection

    Comportamento: restituisce il valore della variabile __ImageCollection.
    """
    def get_image(self):
        return self.__ImageCollection

    """
    Nome: select_bands

    Input: bands

    Output: //

    Comportamento: restituisce il valore della variabile __ImageCollection.
    """
    def select_bands(self, bands: list):
        self.__ImageCollection = self.__ImageCollection.select(bands)

    """
    Nome: extract_median

    Input: //

    Output: restituisce la mediana delle immagini della variabile __ImageCollection.

    Comportamento: restituisce la mediana delle immagini della variabile __ImageCollection.
    """
    def extract_median(self):
        return self.__ImageCollection.median()

    """
    Nome: get_collection_length

    Input: //

    Output: restituisce il numero delle immagini della variabile __ImageCollection.

    Comportamento: restituisce il numero delle immagini della variabile __ImageCollection.
    """
    def get_collection_length(self):
        return self.__ImageCollection.size().getInfo()

