from Sorter import *
from random import randint

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


			aux = entrada[smallestInd]
			entrada[smallestInd] =  entrada[i]
			entrada[i] = aux



		self.setSaida(entrada)
		return entrada



