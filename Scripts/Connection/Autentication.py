import ee


class Autentication:
    __Autenticate: bool

    """
    Nome: __init__

    Input: //

    Output: //

    Comportamento: Costruttore che inizializza le variabili __Autenticate.
    """
    def __init__(self):
        self.__Autenticate = False

    """
    Nome: is_autenticate

    Input: //

    Output: restituisce il valore della variabile __Autenticate.

    Comportamento: restituisce il valore della variabile __Autenticate.
    """
    def is_autenticate(self):
        return self.__Autenticate

    """
    Nome: autentication

    Input: //

    Output: //

    Comportamento: controlla se l'utente si è gia autenticato. 
                   Se l'utente non si è gia autenticato effettua l'autenticazione.
    """
    def autentication(self):
        if not self.is_autenticate():
            ee.Authenticate()
            self.__Autenticate = True
        else:
            print("Il tuo profilo Google Earth Engine è già autenticato")

    """
    Nome: initializate

    Input: //

    Output: //

    Comportamento: Inizializza  la libreria di Google Earth Engine.
    """
    def initializate(self):
        ee.Initialize()

