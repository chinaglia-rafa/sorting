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

total_start = time.time()

tamanhos = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
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
            times.append([sorter.nome, len(entrada), tempo])


            print("TEMPO",sorter.nome ,len(entrada),"ENTRADAS:", tempo)

    return times

def reset_entradas(lista_de_entradas):
    for entrada in lista_de_entradas:
        entrada.clear()
    return lista_de_entradas


tempo_aleatorio = tempo_crescente = tempos_decrescente = []

#---------------------------- NUMEROS EM ORDEM ALEATORIA ---------------------------------------#

#ENTRADAS COM TAMANHOS DIFERENTES E NUMEROS ALEATORIOS
entrada0 = Sorter.gerar_entrada(tamanhos[0])
entrada1 = Sorter.gerar_entrada(tamanhos[1])
entrada2 = Sorter.gerar_entrada(tamanhos[2])
entrada3 = Sorter.gerar_entrada(tamanhos[3])
entrada4 = Sorter.gerar_entrada(tamanhos[4])
entrada5 = Sorter.gerar_entrada(tamanhos[5])
entrada6 = Sorter.gerar_entrada(tamanhos[6])
entrada7 = Sorter.gerar_entrada(tamanhos[7])
entrada8 = Sorter.gerar_entrada(tamanhos[8])
entrada9 = Sorter.gerar_entrada(tamanhos[9])
entrada10 = Sorter.gerar_entrada(tamanhos[10])

#LISTA COM LISTAS DE ENTRADA
lista_de_entradas1 = [entrada0, entrada1, entrada2, entrada3, entrada4, entrada5,
                    entrada6, entrada7, entrada8, entrada9, entrada10]


#CHAMANDO FUNÇÃO DE MEDICAO COM NUMEROS ALEATORIOS
tempo_aleatorio = medicao_tempo(lista_de_entradas1)


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
for i in range(tamanhos[7]):
        lista_de_entradas2[7].append(i)
for i in range(tamanhos[8]):
        lista_de_entradas2[8].append(i)
for i in range(tamanhos[9]):
        lista_de_entradas2[9].append(i)
for i in range(tamanhos[10]):
        lista_de_entradas2[10].append(i)

tempo_crescente = medicao_tempo(lista_de_entradas2)


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
for i in range(tamanhos[7]):
        lista_de_entradas3[7].append(tamanhos[7] - i)
for i in range(tamanhos[8]):
        lista_de_entradas3[8].append(tamanhos[8] - i)
for i in range(tamanhos[9]):
        lista_de_entradas3[9].append(tamanhos[9] - i)
for i in range(tamanhos[10]):
        lista_de_entradas3[10].append(tamanhos[10] - i)

tempos_decrescente = medicao_tempo(lista_de_entradas3)

file = open("results.csv", "w")
first_line = '"Algoritmo", "entrada", "tempo"\n'
file.write(first_line)
for line in tempo_aleatorio + tempo_crescente + tempos_decrescente:
    current_line = "\"" + str(line[0]) + "\"," + str(line[1]) + "," +str(line[2]) + "\n"
    file.write(current_line)

total_end = time.time()

total_delta = total_end - total_start

print("Arquivo de saida results.csv gerado!")

print("\nCodigo finalizado em", total_delta, "segundos!")
