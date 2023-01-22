import random
from random_words import RandomWords
import time

random.seed(0)

str_list = []
w = RandomWords()
for i in range(0, 5000):
    str_list.append(w.random_words())
print(str_list)

def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
               data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
               swapped = True
        if not swapped:
            break

cur_time = time.time()
bubble_sort(str_list)
print(f"Duration time: {time.time() - cur_time}")