import ee.batch
from ee.batch import Export
from Scripts.ExportToDrive.ComparatorTaskStatus import ComparatorTaskStatus
from Scripts.ExportToDrive.TaskException import TaskException


class Task:

    __Task: ee.batch.Task

    """
    Nome: __init__

    Input: //

    Output: //

    Comportamento: Inizializza la variabile __Task.
    """
    def __init__(self):
        self.__Task = None

    """
    Nome: set_task

    Input: esportOption: dizionario contenente le opzioni di esportazione.

    Output: //

    Comportamento: Avvalora la variabile __Task.
    """
    def set_task(self, esport_option: dict):
        self.__Task = Export.image.toDrive(**esport_option)

    """
    Nome: start_task

    Input: //

    Output: //

    Comportamento: Avvia il task di esportazione.
    """
    def start_task(self):
        self.__Task.start()

    """
    Nome: is_active

    Input: //

    Output: booleano

    Comportamento: restituisce se il task è ancora in esecuzione.
    """
    def is_active(self):
        return self.__Task.active()

    """
    Nome: get_task_status

    Input: //

    Output: dizionario

    Comportamento: se il task è attivo restituisce lo stato del task come dizionario.
    """
    def get_task_status(self):
        if self.is_active():
            return self.__Task.status()

    """
    Nome: get_task_state

    Input: //

    Output: string

    Comportamento: restituisce lo stato del task.
    """
    def get_task_state(self):
        return self.__Task.status()['state']

    """
    Nome: activity_status_monitoring

    Input: //

    Output: //

    Comportamento: Se il task è stato attivato lo stato del task viene stampato
                   a video fino a quando il task è attivo.
    """
    def activity_status_monitoring(self):
        if not self.is_active():
            raise TaskException("The task has not been started.")
        else:
            while self.__Task.active():
                print("Export status:", self.__Task.status())

    """
    Nome: task_completed

    Input: //

    Output: booleano

    Comportamento: restituisce se il task è stato completato.
    """
    def task_completed(self):
        return ComparatorTaskStatus.compare(self.get_task_state(), 'COMPLETED')

    """
    Nome: export_completed

    Input: //

    Output: //

    Comportamento: Se il task è stato completato viene visualizzato
                   a video che l'esportazione è completata.
    """
    def export_completed(self):
        if self.task_completed():
            print("Export completed.\n"
                  "Access your Google Drive to download the image.")
        else:
            print('Export failed or in progress.')
