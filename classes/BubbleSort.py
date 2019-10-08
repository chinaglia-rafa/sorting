from Sorter import *


class BubbleSort(Sorter):
    def __init__(self, entrada):
        #   Passar o nome do algoritmo de ordenação no primeiro parâmetro
        super().__init__("BubbleSort", entrada)

    #   Metodo abstrato que executará a ordenação (chamado uma vez só, qualquer
    #   recursão deve ser feita usando outros métodos)
    def sort(self):
        #   A notação [:] faz uma copia de self.__entrada, ao invés de entrada ser
        #   uma referência para self.__entrada
        entrada = self.getEntrada()[:]
        tamanho_entrada = len(entrada)
        #   Validando entrada de dados
        if tamanho_entrada == 0:
            print("["+ self.nome +"]", " ERRO: Algoritmo nao possui entrada!")

        for i in range(0, tamanho_entrada - 1):
            for j in range(0, tamanho_entrada - 1 - i):
                if entrada[j] > entrada[j + 1]:
                    hold_this_number_please = entrada[j]
                    entrada[j] = entrada[j + 1]
                    entrada[j + 1] = hold_this_number_please

        self.setSaida(entrada)
        return entrada
