import ee


class ImgCollection:
    """
    Nome: __init__

    Input: identificatore della collezione di immagini da importare.

    Output:

    Comportamento: inizializza la variabile Collection importando la collezione di immagini.
    """
    def __init__(self, CollectionIdentifier):
        self.Collection = ee.ImageCollection(CollectionIdentifier)

    """
    Nome: maskS2clouds
    
    Input: immagine
    
    Output: immagine con la maschera delle nuvole
    
    Comportamento: Funzione per mascherare le nuvole utilizzando la banda QA Sentinel-2
    """
    def maskS2clouds(image):
        qa = image.select('QA60')
        cloudBitMask = 1 << 10
        cirrusBitMask = 1 << 11
        mask = (qa.bitwiseAnd(cloudBitMask).eq(0)) and (qa.bitwiseAnd(cirrusBitMask).eq(0))
        return image.updateMask(mask).divide(10000)

    """
    Nome: filteredCollection
    
    Input: data di inizio e di fine del periodo in cui filtrare la collezione
    
    Output: collezione filtrata
    
    Comportamento: Mappa la funzione sul periodo inserito e considera la mediana.
                   Carica i dati Sentinel-2 adattati per l'elaborazione delle modifiche
                   verificatesi dopo la data finale (endDate)
    """
    def filteredCollection(self,startDate, endDate):
       return self.Collection.filterDate(startDate, endDate).filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))

    """
    Nome: filtered_bound

    Input: una collezione e una geometria in cui filtrare la collezione

    Output: collezione filtrata

    Comportamento: filtra la collezione passata in input con geometria passata in input
    """
    def filter_bound(self, Coll, Geometry):
        return Coll.filterBounds(Geometry)