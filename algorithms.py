import tests
import data_structures as ds
import random

def bubble_sort(data):
    data_length = len(data)
    # print(data)
    for i in range(data_length):
        for j in range(1, data_length):
            if data[j] < data[j - 1]:
                (data[j], data[j - 1]) = (data[j - 1], data[j])
    # print(data)
    return data


def insertion_sort(data:list):
    i = 1
    data_length = len(data)
    while i < data_length:
        if data[i] < data[i - 1]:
            j = i - 1
            while j >= 0 and data[j] > data[i]:
                j -= 1
            i_value = data[i]
            del data[i]
            data.insert(j + 1, i_value)
            i += 1
        else:
            i += 1
    return data


def selection_sort(data):
    data_length = len(data)
    for i in range(data_length):
        min = i
        for j in range(i + 1, data_length):
            min = j if data[j] < data[min] else min
        min_value = data[min]
        del data[min]
        data.insert(i, min_value)
    return data


def quick_sort_left(data):
    return quick_sort(data, "l")


def quick_sort_right(data):
    return quick_sort(data, "r")


def quick_sort_random(data):
    return quick_sort(data, "r")


def quick_sort_middle(data):
    return quick_sort(data, "m")


def quick_sort(data, pivot_type):
    # print(data)
    data_length = len(data)
    if data_length < 2:
        return data
    else:
        if pivot_type == "l":
            pivot = 0
        elif pivot_type == "r":
            pivot = data_length - 1
        elif pivot_type == "ra":
            pivot = random.randint(0, data_length)
        elif pivot_type == "m":
            pivot = data_length // 2

        pivot_value = data[pivot]
        # print(pivot_value)
        smaller = [a for a in data if a < pivot_value]
        bigger = [a for a in data if a > pivot_value]
        middle = [a for a in data if a == pivot_value]
        return quick_sort(smaller, pivot_type) + middle + quick_sort(bigger, pivot_type)


def shell_sort(data):
    distances = [4, 2, 1]
    for distance in distances:
        for bias in range(distance):
            sort = insertion_sort(data[bias::distance])
            # print(sort)
            for idx in range(len(sort)):
                data[idx * distance + bias] = sort[idx]
    return data


def heap_sort(data):
    heap = ds.Heap()
    heap.add_list(data)
    # print(heap)
    sort = list()
    for i in range(heap.size):
        sort.append(heap.take_max())
    return sort[::-1]



