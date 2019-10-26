from Sorter import *
from random import randint

class ShellSort(Sorter):
    def __init__(self, entrada):
        super().__init__("ShellSort", entrada)

    def sort(self):
        entrada = self.getEntrada()[:]
        size = len(entrada)
        gap = int(size/2)

        while(gap > 0):
            for i in range(gap, size):
                temp = entrada[i]
                posicao = i

                while(i >= gap and temp < entrada[i - gap]):
                    entrada[i] = entrada[i - gap]
                    i = i - gap

                entrada[i] = temp

            gap = int(gap/2)

        self.setSaida(entrada)
        return entrada

