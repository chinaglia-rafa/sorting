from Sorter import *
from BubbleSort import *
from BubbleSortPlus import *
from HeapSort import *
from InsertionSort import *
from MergeSort import *
from SelectionSort import *
from ShellSort import *
import time

tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000]

#ENTRADAS COM TAMANHOS DIFERENTES
entrada0 = Sorter.gerar_entrada(tamanhos[0])
entrada1 = Sorter.gerar_entrada(tamanhos[1])
entrada2 = Sorter.gerar_entrada(tamanhos[2])
entrada3 = Sorter.gerar_entrada(tamanhos[3])
entrada4 = Sorter.gerar_entrada(tamanhos[4])
entrada5 = Sorter.gerar_entrada(tamanhos[5])
entrada6 = Sorter.gerar_entrada(tamanhos[6])

#LISTA COM LISTAS DE ENTRADA
lista_de_entradas = [entrada0, entrada1, entrada2, entrada3, entrada4, entrada5,
                    entrada6]

#CRIAÇÃO E MEDIÇÃO DOS OBJETOS E DE SEUS RESPECTIVOS METODOS DE ORDENAÇÃO
#BubbleSort
Bubble_Sort_Tempos = []
for entrada in lista_de_entradas:
    Bubble = BubbleSort(entrada)
    #MEDINDO TEMPO DE ORDENAÇÃO
    start = time.time()
    Bubble.sort()
    end = time.time()

    tempo = end - start
    Bubble_Sort_Tempos.append(tempo)
    print("TEMPO BUBBLE: ", tempo)
