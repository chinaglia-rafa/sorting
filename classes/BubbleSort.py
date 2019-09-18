from classes.Sorter import *


class BubbleSort(Sorter):
    def __init__(self, entrada):
        #   Passar o nome do algoritmo de ordenação no primeiro parâmetro
        super().__init__("BubbleSort", entrada)

    #   Metodo abstrato que executará a ordenação (chamado uma vez só, qualquer
    #   recursão deve ser feita usando outros métodos)
    def sort(self):
        #   Validando entrada de dados
        if len(self.getEntrada()) == 0:
            print("["+ self.nome +"]", " ERRO: Algoritmo nao possui entrada!")
