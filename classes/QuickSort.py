from Sorter import *
from random import randint

def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = (start + end)//2
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


class QuickSort(Sorter):
    def __init__(self, entrada):
        super().__init__("QuickSort", entrada)

    def sort(self):
        entrada = self.getEntrada()[:]
        quick_sort(entrada, 0, len(entrada) - 1)

        self.setSaida(entrada)
        return entrada

