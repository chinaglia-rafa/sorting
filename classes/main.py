from Sorter import *
from BubbleSort import *
from BubbleSortPlus import *
from HeapSort import *
from InsertionSort import *
from MergeSort import *
from SelectionSort import *
from ShellSort import *
from QuickSort import *
from QuickSortPI import *
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
#TO DO: INSERIR QUICK SORTS
times = []
for entrada in lista_de_entradas:
    print("\n\n", len(entrada), "Entradas \n\n")
    sorters = [BubbleSortPlus(entrada[:]), BubbleSort(entrada[:]), QuickSortPI(entrada[:]), QuickSort(entrada[:]), HeapSort(entrada[:]), InsertionSort(entrada[:]), MergeSort(entrada[:]), SelectionSort(entrada[:]),
                ShellSort(entrada[:])]

    #MEDINDO TEMPO DE ORDENAÇÃO
    for sorter in sorters:
        start = time.time()
        sorter.sort()
        end = time.time()

        tempo = end - start
        times.append(tempo)


        print("TEMPO",sorter.nome ,len(entrada),"ENTRADAS:", tempo)

    # #QUICK SORT COM PIVO NO INCIO
    # l = Sorter.gerar_entrada(10000)
    #
    # start = time.time()
    # quick_sort(l, 0, 99)
    # end = time.time()
    #
    # tempo = end - start
    # times.append(tempo)


    # print("TEMPO QUICK SORT PI",len(entrada),"ENTRADAS:", tempo)
