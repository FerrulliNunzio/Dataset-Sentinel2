import ee


class Autentication:
    Autenticate: bool
    Initializate: bool

    def __init__(self):
        self.Autenticate = False
        self.Initializate = False

    def isAutenticate(self):
        return self.Autenticate

    def isInitializate(self):
        return self.Initializate

    def autentication(self):
        if not self.isAutenticate():
            ee.Authenticate()
            self.Autenticate = True
        else:
            print("Il tuo profilo Google Earth Engine è già autenticato")

    def initializate(self):
        if not self.isInitializate():
            ee.Initialize()
            self.Initializate = True
        else:
            print("Inizializzazione già eseguita.")



