import os

FOLDER = "/Materiale"


class PathManager:

    __Path: str

    """
    Nome: __init__

    Input: //

    Output: //

    Comportamento: Inizializza la variabile path.
    """

    def __init__(self):
        self.__Path = ""

    """
    Nome: __convert_path

    Input: path: string

    Output: //

    Comportamento: sostituisce il carattere '\ ' con il carattere '/'.
    """

    def __convert_path(self, path: str):
        s = "\ "
        node_path = path.split(s[0])
        correct_path = ""
        for node in node_path:
            if not correct_path:
                correct_path = node
            else:
                correct_path = correct_path + "/" + node
        return correct_path

    """
        Nome: __get_general_path

        Input: //

        Output: string

        Comportamento: Restituisce il path della cartella del progetto.
        """

    def __get_general_path(self):
        self.__Path = os.getcwd()
        return self.__convert_path(self.__Path)

    """
        Nome: get_file_in_path

        Input: //

        Output: list

        Comportamento: Restituisce una lista contenente i file in una cartella.
        """

    def get_file_in_path(self):
        if self.__Path != "":
            return os.listdir(self.__Path)
        else:
            empty_list = []
            return empty_list

    """
        Nome: get_complete_path

        Input: //

        Output: string

        Comportamento: restituisce la variabile Path.
        """

    def get_complete_path(self):
        return self.__Path

    """
        Nome: set_complete_path

        Input: semi_path: string

        Output: //

        Comportamento: Avvalora la variabile Path con il path del file.
        """

    def set_complete_path(self, semi_path: str):
        self.__Path = self.__get_general_path() + FOLDER + "/" + semi_path

    """
        Nome: print_file_in_path

        Input: //

        Output: //

        Comportamento: Visualizza a video i file in una cartella.
        """

    def print_file_in_path(self):
        files_list = os.listdir(self.__Path)
        if not files_list:
            print("La cartella non contiene nessun elemento")
        else:
            for item in files_list:
                print(item)
