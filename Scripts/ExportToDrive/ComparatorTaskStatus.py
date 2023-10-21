class ComparatorTaskStatus:
    """
    Nome: compare

    Input: status1, status2

    Output: booleano

    Comportamento: restituisce True se i parametri passati in input sono uguali,
                   restituisce False altrimenti
    """

    @staticmethod
    def compare(status1: str, status2: str):
        return status1 == status2