# conquer.py
import random

# Fungsi untuk menghasilkan bilangan acak
def generate_random_numbers(count, lower, upper, seed):
    random.seed(seed)  # Menetapkan seed
    return [random.randint(lower, upper) for _ in range(count)]

# Algoritma Merge Sort menggunakan Divide and Conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

# Fungsi untuk menggabungkan dua list yang sudah terurut
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Parameter
count = 50
lower = 0
upper = 100
seed = 40

# Menghasilkan bilangan acak
random_numbers = generate_random_numbers(count, lower, upper, seed)
print("Bilangan Acak Sebelum Sorting:")
print(random_numbers)

# Melakukan sorting dengan Merge Sort
sorted_numbers = merge_sort(random_numbers)
print("\nBilangan Acak Setelah Sorting:")
print(sorted_numbers)