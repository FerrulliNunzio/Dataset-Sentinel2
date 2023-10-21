from Scripts.ExportToDrive.Task import Task


class ExportDataset:

    __ExportOptions = {}
    __Task = Task()

    """
    Nome: __init__
    
    Input: //
    
    Output: //
    
    Comportamento: inizializza le variabili __ExportOptions, __Task.
    """
    def __init__(self):
        self.__ExportOptions = {}
        self.__Task = Task()

    """
    Nome: __init__

    Input: option

    Output: //

    Comportamento: inizializza la variabile __ExportOptions con il parametro passato.
    """
    def __init__(self, option: dict):
        self.__ExportOptions = option

    """
    Nome: set_export_option

    Input: export_option: dizionario contenente le opzioni di esportazione.

    Output: //

    Comportamento: Avvalora la variabile __ExportOptions con il parametro passato.
    """
    def set_export_option(self, export_option: dict):
        self.__ExportOptions = export_option

    """
    Nome: get_export_option

    Input: //

    Output: //

    Comportamento: restituisce il valore della variabile __ExportOptions.
    """
    def get_export_option(self):
        return self.__ExportOptions

    """
    Nome: start_export_dataset

    Input: //

    Output: //

    Comportamento: Inizia l'esportazione delle immagini trovate.
    """
    def start_export_dataset(self):
        self.__Task.set_task(self.__ExportOptions)
        self.__Task.start_task()
        self.__Task.activity_status_monitoring()
        self.__Task.export_completed()