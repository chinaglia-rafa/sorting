from Sorter import *
from BubbleSort import *
from BubbleSortPlus import *
from HeapSort import *
from InsertionSort import *
from MergeSort import *
from SelectionSort import *
from ShellSort import *
from QuickSort import *
from QuickSortPF import *
import time

tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000]
#CRIAÇÃO E MEDIÇÃO DOS OBJETOS E DE SEUS RESPECTIVOS METODOS DE ORDENAÇÃO
#COM NUMEROS GERADOS ALEATORIAMENTE
def medicao_tempo(lista_de_entradas):
    times = []
    for entrada in lista_de_entradas:
        print("\n\n", len(entrada), "Entradas \n\n")
        sorters = [BubbleSortPlus(entrada[:]), BubbleSort(entrada[:]), QuickSortPF(entrada[:]), QuickSort(entrada[:]), HeapSort(entrada[:]), InsertionSort(entrada[:]), MergeSort(entrada[:]), SelectionSort(entrada[:]),
                    ShellSort(entrada[:])]

        #MEDINDO TEMPO DE ORDENAÇÃO
        for sorter in sorters:
            start = time.time()
            sorter.sort()
            end = time.time()

            tempo = end - start
            times.append(tempo)


            print("TEMPO",sorter.nome ,len(entrada),"ENTRADAS:", tempo)

    return times

def reset_entradas(lista_de_entradas):
    for entrada in lista_de_entradas:
        entrada.clear()
    return lista_de_entradas


#---------------------------- NUMEROS EM ORDEM ALEATORIA ---------------------------------------#

#ENTRADAS COM TAMANHOS DIFERENTES E NUMEROS ALEATORIOS
entrada0 = Sorter.gerar_entrada(tamanhos[0])
entrada1 = Sorter.gerar_entrada(tamanhos[1])
entrada2 = Sorter.gerar_entrada(tamanhos[2])
entrada3 = Sorter.gerar_entrada(tamanhos[3])
entrada4 = Sorter.gerar_entrada(tamanhos[4])
entrada5 = Sorter.gerar_entrada(tamanhos[5])
entrada6 = Sorter.gerar_entrada(tamanhos[6])

#LISTA COM LISTAS DE ENTRADA
lista_de_entradas1 = [entrada0, entrada1, entrada2, entrada3, entrada4, entrada5,
                    entrada6]


#CHAMANDO FUNÇÃO DE MEDICAO COM NUMEROS ALEATORIOS
#tempo_aleatorio = medicao_tempo(lista_de_entradas1)


#---------------------------- NUMEROS EM ORDEM CRESCENTE ---------------------------------------#

#ENTRADAS COM NUMEROS EM ORDEM CRESCENTE
lista_de_entradas2 = reset_entradas(lista_de_entradas1)

for i in range(tamanhos[0]):
        lista_de_entradas2[0].append(i)
for i in range(tamanhos[1]):
        lista_de_entradas2[1].append(i)
for i in range(tamanhos[2]):
        lista_de_entradas2[2].append(i)
for i in range(tamanhos[3]):
        lista_de_entradas2[3].append(i)
for i in range(tamanhos[4]):
        lista_de_entradas2[4].append(i)
for i in range(tamanhos[5]):
        lista_de_entradas2[5].append(i)
for i in range(tamanhos[6]):
        lista_de_entradas2[6].append(i)

#tempo_crescente = medicao_tempo(lista_de_entradas2)


#---------------------------- NUMEROS EM ORDEM DECRESCENTE ---------------------------------------#

#ENTRADAS COM NUMEROS EM ORDEM DECRESCENTE
lista_de_entradas3 = reset_entradas(lista_de_entradas2)

for i in range(tamanhos[0]):
        lista_de_entradas3[0].append(tamanhos[0] - i)
for i in range(tamanhos[1]):
        lista_de_entradas3[1].append(tamanhos[1] - i)
for i in range(tamanhos[2]):
        lista_de_entradas3[2].append(tamanhos[2] - i)
for i in range(tamanhos[3]):
        lista_de_entradas3[3].append(tamanhos[3] - i)
for i in range(tamanhos[4]):
        lista_de_entradas3[4].append(tamanhos[4] - i)
for i in range(tamanhos[5]):
        lista_de_entradas3[5].append(tamanhos[5] - i)
for i in range(tamanhos[6]):
        lista_de_entradas3[6].append(tamanhos[6] - i)

tempos_decrescente = medicao_tempo(lista_de_entradas3)
