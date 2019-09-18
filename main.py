from classes.BubbleSort import *
from classes.BubbleSortPlus import *
from datetime import datetime

# Este método gera n números aleatórios
# entrada1 = Sorter.gerar_entrada(500)
# Este método gera um vetor ordenado
entrada1 = range(1000);
how_many_times = 3

# Declarando Ordenadores
bubbleSort = BubbleSort(entrada1)
bubbleSortPlus = BubbleSortPlus(entrada1)

# Registrando todos os orednadores numa lista
sorters = [bubbleSort, bubbleSortPlus]

# Varre cada ordenador para ordenar a entrada1
for srt in sorters:
    print("[" + srt.nome + "] Começando a executar agora!")
    # Começa a contar
    t0 = datetime.now()
    # Repete a ordenação how_many_times vezes
    for i in range(how_many_times):
        srt.sort()
    # Para de contar
    tf = datetime.now()
    delta = tf - t0
    print("[" + srt.nome + "] Concluído! Tempo decorrido: ", delta)
    print("")
