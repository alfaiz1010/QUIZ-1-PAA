# naive.py
import random

# Fungsi untuk menghasilkan bilangan acak
def generate_random_numbers(count, lower, upper, seed):
    random.seed(seed)  # Menetapkan seed
    return [random.randint(lower, upper) for _ in range(count)]

# Algoritma Bubble Sort untuk sorting secara naive
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Parameter
count = 50
lower = 0
upper = 100
seed = 40

# Menghasilkan bilangan acak
random_numbers = generate_random_numbers(count, lower, upper, seed)
print("Bilangan Acak Sebelum Sorting:")
print(random_numbers)

# Melakukan sorting dengan Bubble Sort
sorted_numbers = bubble_sort(random_numbers)
print("\nBilangan Acak Setelah Sorting:")
print(sorted_numbers)