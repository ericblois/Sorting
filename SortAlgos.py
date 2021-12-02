import math
import itertools

def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

def insertion_sort(numbers: [float]):
    for i in range(1, len(numbers)):
        num = numbers[i]
        j = i - 1
        while j >= 0 and num < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = num


def eric_sort(numbers: [float], desired_bucket_length = 10, sort_func = insertion_sort):

    # Calculate the number of buckets so that the average length of a bucket is (20)
    num_buckets = min(int(len(numbers)/desired_bucket_length), 100000) # O(1) time

    max_num = max(numbers) # O(n) time
    min_num = min(numbers) # O(n) time

    bucket_size = (max_num - min_num) / num_buckets
    buckets: [[float]] = [[] for _ in range(num_buckets)]
    # Put all numbers in a bucket, O(n) time
    for num in numbers:
        i = math.floor((num - min_num) / bucket_size)
        if i >= num_buckets:
            i -= 1
        buckets[i].append(num)

    last_i = 0
    # Sort buckets
    for bucket in buckets:
        #sort_func(0, len(bucket) - 1, bucket)
        sort_func(bucket)
        #bucket.sort()
        numbers[last_i : last_i + len(bucket)] = bucket
        last_i = last_i + len(bucket)


def blois_sort(numbers: [float]):

    if len(numbers) <= 1:
        return
    elif len(numbers) <= 2:
        numbers[0] = min(numbers)
        numbers[1] = max(numbers)
        return

    max_num = max(numbers) # O(n) time
    min_num = min(numbers) # O(n) time
    half = (max_num - min_num)/2 + min_num

    if half <= 0:
        return

    bucket1: [float] = []
    bucket2: [float] = []

    # Put all numbers in a bucket, O(n) time
    for num in numbers:
        if num >= half:
            bucket2.append(num)
        else:
            bucket1.append(num)

    blois_sort(bucket1)
    blois_sort(bucket2)

    numbers[:] = bucket1 + bucket2

def blois1_sort(numbers: [float]):

    max_num = max(numbers) # O(n) time
    min_num = min(numbers) # O(n) time

    sorted_nums = [None for _ in range(len(numbers))]

    # Put all numbers in a bucket, O(n) time
    for num in numbers:
        estimated_i = math.floor(((num - min_num) / (max_num - min_num))*len(numbers))
        if estimated_i >= len(sorted_nums):
            estimated_i -= 1
        if sorted_nums[estimated_i] is None:
            sorted_nums[estimated_i] = num
        else:
            inserted = False
            for i in range(estimated_i,len(sorted_nums)):
                if sorted_nums[i] is None:
                    sorted_nums[i] = num
                    inserted = True
                    break
            if not inserted:
                for i in range(estimated_i, -1, -1):
                    if sorted_nums[i] is None:
                        sorted_nums[i] = num
                        break

def blois2_sort(numbers: [float], desired_bucket_length = 10):
    # Check if list is small
    if len(numbers) <= 1:
        return
    elif len(numbers) <= 2:
        if numbers[0] <= numbers[1]:
            return
        else:
            numbers[:] = numbers[::-1]
            return

    # Calculate the number of buckets so that the average length of a bucket is (desired_bucket_length)
    #num_buckets = min(int(len(numbers)/desired_bucket_length), 100000) # O(1) time
    num_buckets = 4

    max_num = max(numbers) # O(n) time
    min_num = min(numbers) # O(n) time

    if max_num - min_num <= 0:
        return

    bucket_size = (max_num - min_num) / num_buckets
    buckets: [[float]] = [[] for _ in range(num_buckets)]
    # Put all numbers in a bucket, O(n) time
    for num in numbers:
        i = math.floor((num - min_num) / bucket_size)
        if i >= num_buckets:
            i -= 1
        buckets[i].append(num)


    last_i = 0
    # Sort buckets
    for bucket in buckets:
        #sort_func(0, len(bucket) - 1, bucket)
        blois2_sort(bucket)
        numbers[last_i : last_i + len(bucket)] = bucket
        last_i = last_i + len(bucket)

def divy(numbers: [float]):
    nums = []
    for i in range(0, len(numbers), 2):
        if numbers[i] > numbers[i + 1]:
            nums.insert(0, numbers[i + 1])
            nums.append(numbers[i])
        else:
            nums.insert(0, numbers[i])
            nums.append(numbers[i + 1])
    numbers[:] = nums

def divy1(numbers: [float]):
    nums = []
    streak = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            num = numbers.pop(i)
            numbers.insert(len(numbers) - streak, num)
            streak += 1
            i -= 1
        else:
            streak = 0

def push_sort(numbers: [float]):
    divy1(numbers)
    quick_sort(0, len(numbers) - 1, numbers)
    #for _ in range(int(len(numbers)/2)):
        #divy1(numbers)


