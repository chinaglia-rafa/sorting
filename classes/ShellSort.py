from Sorter import *
from random import randint

debug = 0

class ShellSort(Sorter):
    def __init__(self, entrada):
        super().__init__("ShellSort", entrada)

    def sort(self):
        entrada = self.getEntrada()
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


#Area de testes

if (debug):
	l = [randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000)]
	#l = [5, 4, 3, 2, 1]
	print ("Array Desordenado:\n", l, "\n")
	teste = ShellSort(l)
	print ("Array Ordenado:\n", teste.sort())
