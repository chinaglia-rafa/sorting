from Sorter import *
from random import randint

debug = 0

class MergeSort(Sorter):
    def __init__(self, entrada):
        super().__init__("MergeSort", entrada)

    def sort(self):

        entrada = self.getEntrada()[:]

        if(len(entrada) > 1):
            meio = len(entrada)//2

            ladoEsquerdo = entrada[:meio]
            ladoDireito = entrada[meio:]

            esquerda = MergeSort(ladoEsquerdo)
            direita = MergeSort(ladoDireito)

            listaEsquerda = esquerda.sort()
            listaDireita = direita.sort()

            #contadores, i controla a listaEsquerda, j a listaDireita e k a lista final
            i = j = k = 0

            while(i < len(listaEsquerda) and j < len(listaDireita)):
                if(listaEsquerda[i] < listaDireita[j]):
                    entrada[k] = listaEsquerda[i]
                    i = i + 1

                else:
                    entrada[k] = listaDireita[j]
                    j = j + 1

                k = k + 1

            while(i < len(listaEsquerda)):
                entrada[k] = listaEsquerda[i]
                i += 1
                k += 1

            while(j < len(listaDireita)):
                entrada[k] = listaDireita[j]
                j += 1
                k += 1

        self.setSaida(entrada)
        return entrada


#Area de testes

if (debug):
	l = [randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000)]
	#l = [5, 4, 3, 2, 1]
	print ("Array Desordenado:\n", l, "\n")
	teste = MergeSort(l)
	print ("Array Ordenado:\n", teste.sort())
