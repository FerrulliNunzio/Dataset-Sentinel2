import os

FOLDER = "/Materiale"

class PathManager:
    def __init__(self):
        self.Path = ""

    def __convert_path(self, path):
        s="\ "
        node_path = path.split(s[0])
        correct_path = ""
        for node in node_path:
            if not correct_path:
                correct_path = node
            else:
                correct_path = correct_path + "/" + node
        return  correct_path

    def __get_general_path(self):
        self.Path = os.getcwd()
        return self.__convert_path(self.Path)

    def get_file_in_path(self):
        if self.Path != "":
            return os.listdir(self.Path)
        else:
            empty_list = []
            return empty_list

    def get_complete_path(self):
        return self.Path

    def set_complete_path(self, semi_path):
        self.Path = self.__get_general_path() + FOLDER + "/" + semi_path

    def print_file_in_path(self):
        files_list = os.listdir(self.Path)
        if not files_list:
            print("La cartella non contiene nessun elemento")
        else:
            for item in files_list:
                print(item)


