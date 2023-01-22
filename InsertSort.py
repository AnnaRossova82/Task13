import random
from random_words import RandomWords
import time

random.seed(0)

str_list = []
w = RandomWords()
for i in range(0, 5000):
    str_list.append(w.random_words())
print(str_list)

float_list = []
for i in range(0, 5000):
    float_list.append(random.uniform(0.1, 100.0))
print(float_list)

int_list = []
for i in range(0, 1000):
    int_list.append(random.randint(1, 5000))
print(int_list)

#lists created

def insertion_sort(data):
    for scanIndex in range(1, len(data)):
        tmp = data[scanIndex]
        minIndex = scanIndex
        while minIndex > 0 and tmp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1
        data[minIndex] = tmp

cur_time = time.time()
insertion_sort(int_list)

print(f"Duration time: {time.time() - cur_time}")