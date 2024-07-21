import timeit
import numpy as np
from random import randint

def generate_random_array():
    """Generate_random_array"""
    array_length = 1000
    random_array = np.random.randint(low=0, high=1000, size=array_length)
    return random_array

def insertion_sort(lst):
    """Insertion_sort function"""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    """Merge_sort function"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def default_sort(lst):
    lst.sort()
    return lst

# compute insertion_sort time
def insertion_sort_time():
    SETUP_CODE = '''
from __main__ import insertion_sort, generate_random_array
'''
    TEST_CODE = '''
arr_list = generate_random_array()
insertion_sort(arr_list)'''

# timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=10,
                          number=10)
    
# printing min exec.time
    print(f'Insertion_sort time: {format(min(times))}')

# compute merg_sort time
def merg_sort_time():
    SETUP_CODE = '''
from __main__ import merge_sort, generate_random_array
'''
    TEST_CODE = '''
arr_list = generate_random_array()
merge_sort(arr_list)'''

# timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=10,
                          number=10)
    
# printing min exec.time
    print(f'Merg_sort time: {format(min(times))}')

    # compute merg_sort time

# compute default_sort time
def default_sort_time():
    SETUP_CODE = '''
from __main__ import default_sort, generate_random_array
'''
    TEST_CODE = '''
arr_list = generate_random_array()
default_sort(arr_list)'''

# timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=10,
                          number=10)
    
# printing min exec.time
    print(f'Default_sort time: {format(min(times))}')

if __name__ == "__main__":
    insertion_sort_time()
    merg_sort_time()
    default_sort_time()
