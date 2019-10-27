from Sorter import *

class InsertionSort(Sorter):
    def __init__(self, entrada):

        super().__init__("InsertionSort", entrada)

    def sort(self):

        entrada = self.getEntrada()[:]
        tamanho = len(entrada)
        for i in range(0, tamanho):
            chave = entrada[i]
            j = i - 1
            #Loop que varre e vai colocando todos os elementos 1 posição
            #a frente da sua atual, até encontrar a posição correta de inserção
            #do novo elemento
            while j >= 0 and chave < entrada[j]:
                entrada[j + 1] = entrada[j]
                j = j - 1

            entrada[j + 1] = chave

        self.setSaida(entrada)
        return entrada

