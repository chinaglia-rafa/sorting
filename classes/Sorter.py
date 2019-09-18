from abc import ABC, abstractmethod


class Sorter(ABC):

    def __init__(self, nome, entrada):
        #   Nome do algoritmo de ordenação
        self.nome = nome
        self.__entrada = entrada
        #   Guardará o conjunto ordenado. False caso não tenha sido ordenado ainda
        self.__saida = False

    def getEntrada(self):
        return self.__entrada

    def setEntrada(self, entrada):
        self.__entrada = entrada

    @abstractmethod
    def sort(self):
        """função que ficará responsável por fazer o sorting e guardar na saida"""
        pass
