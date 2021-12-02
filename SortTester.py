import random
import time
from SortAlgos import *

random.seed(0)

LOWER_BOUND = 0
UPPER_BOUND = 100
ARRAY_SIZE = 10000

def is_sorted(numbers: [float]):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

# Uniform test array
#TEST_ARRAY = [random.random()*(UPPER_BOUND - LOWER_BOUND) + LOWER_BOUND for _ in range(ARRAY_SIZE)]
# Gaussion test array
TEST_ARRAY = [
    max(
        LOWER_BOUND,
        min(
            UPPER_BOUND,
            random.gauss(
                (UPPER_BOUND - LOWER_BOUND)/2,
                (UPPER_BOUND - LOWER_BOUND)/8
            ) + LOWER_BOUND
        )
    ) for _ in range(ARRAY_SIZE)]

print("Unsorted list:")
print(TEST_ARRAY[:50])

"Quicksorted list:"
quicksort_array = TEST_ARRAY.copy()
start = time.time()
quick_sort(0,len(quicksort_array) - 1, quicksort_array)
end = time.time()
print(quicksort_array[:50])
print("Quicksort time: " + str(round(end - start, 2)) + "s")

"Python sorted list:"
pythonsort_array = TEST_ARRAY.copy()
start = time.time()
pythonsort_array.sort()
end = time.time()
print(pythonsort_array[:50])
print("Python sort time: " + str(round(end - start, 2)) + "s")

print("Ericsorted list:")
ericsort_array = TEST_ARRAY.copy()
start = time.time()
eric_sort(ericsort_array)
end = time.time()
print(ericsort_array[:50])
print("Ericsort time: " + str(round(end - start, 2)) + "s")

print("Bloissorted list:")
bloissort_array = TEST_ARRAY.copy()
start = time.time()
push_sort(bloissort_array)
end = time.time()
print(bloissort_array[:50])
print("Bloissort time: " + str(round(end - start, 2)) + "s")
print(is_sorted(bloissort_array))