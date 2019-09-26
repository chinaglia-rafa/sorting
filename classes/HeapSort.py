from Sorter import *
from random import randint

debug = 1

class HeapSort(Sorter):
    def __init__(self, entrada):
        super().__init__("HeapSort", entrada)


    def heapify(self, arr, n, i):
        maior = i
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # Verifica se o filho a esquerda da raiz existe e
        # se é maior que a raiz
        if l < n and arr[i] < arr[l]:
            maior = l

            # Verifica se o filho a direita da raiz existe e
            # se é maior que a raiz
        if r < n and arr[maior] < arr[r]:
            maior = r

            # Troca a raiz se necessario
        if maior != i:
            arr[i],arr[maior] = arr[maior],arr[i] # troca

            self.heapify(arr, n, maior)

    # funcao que ordena o array
    def sort(self):
        entrada = self.getEntrada()
        n = len(entrada)

        for i in range(n, -1, -1):
            self.heapify(entrada, n, i)

        for i in range(n-1, 0, -1):
            entrada[i], entrada[0] = entrada[0], entrada[i] # swap
            self.heapify(entrada, i, 0)

        self.setSaida(entrada)
        return entrada

#Area de testes

if (debug):
	l = [randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000)]
	#l = [5, 4, 3, 2, 1]
	print ("Array Desordenado:\n", l, "\n")
	teste = HeapSort(l)
	print ("Array Ordenado:\n", teste.sort())
