from Sorter import *
from random import randint

debug = 1

class SelectionSort(Sorter):
	def __init__ (self, entrada):
		super().__init__("SelectionSort", entrada)

	def sort (self):
		entrada = self.getEntrada()[:]
		tamanhoEntrada = len(entrada)

		for i in range (tamanhoEntrada):
			#Variavel que guarda a posição com o menor indice
			smallestInd = i

			#Encontra a posicao com o menor indice do array
			for j in range (i+1, tamanhoEntrada):
				if entrada[smallestInd] > entrada[j]:
					smallestInd = j

				#Swap entre a posicao i e a posição com o menor indice do array
			if(debug):
				print ("Passo", i+1, ":", "Troca o indice", i, "Com o", smallestInd)
				print (entrada, "\n")

			aux = entrada[smallestInd]
			entrada[smallestInd] =  entrada[i]
			entrada[i] = aux



		self.setSaida(entrada)
		return entrada


#Area de testes
if (debug):
	l = [randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000),
		 randint(0, 1000), randint(0, 1000), randint(0, 1000)]
	#l = [5, 4, 3, 2, 1]
	print ("Array Desordenado:\n", l, "\n")
	teste = SelectionSort(l)
	print ("Array Ordenado:\n", teste.sort())
