import ee


class ImgCollection:

    __Collection: ee.ImageCollection

    """
    Nome: __init__

    Input: identificatore della collezione di immagini da importare.

    Output:

    Comportamento: inizializza la variabile JsonManagement importando la collezione di immagini.
    """
    def __init__(self, collection_identifier: str):
        self.__Collection = ee.ImageCollection(collection_identifier)

    """
    Nome: filteredCollection
    
    Input: data di inizio e di fine del periodo in cui filtrare la collezione
    
    Output: collezione filtrata
    
    Comportamento: Mappa la funzione sul periodo inserito e considera la mediana.
                   Carica i dati Sentinel-2 adattati per l'elaborazione delle modifiche
                   verificatesi dopo la data finale (endDate)
    """
    def filtered_collection(self, start_date: str, end_date: str):
        return self.__Collection.filterDate(start_date, end_date).filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))

    """
    Nome: filtered_bound

    Input: una collezione e una geometria in cui filtrare la collezione

    Output: collezione filtrata

    Comportamento: filtra la collezione passata in input con geometria passata in input
    """
    def filter_bound(self, coll, geometry):
        return coll.filterBounds(geometry)
