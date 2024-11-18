import time

# Implementasi Bubble Sort untuk mengurutkan secara ascending
def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Implementasi Bubble Sort untuk mengurutkan secara descending
def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Implementasi Quick Sort untuk mengurutkan secara ascending
def quick_sort_ascending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort_ascending(less_than_pivot) + [pivot] + quick_sort_ascending(greater_than_pivot)

# Implementasi Quick Sort untuk mengurutkan secara descending
def quick_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    greater_than_pivot = [x for x in arr[1:] if x >= pivot]
    less_than_pivot = [x for x in arr[1:] if x < pivot]
    return quick_sort_descending(greater_than_pivot) + [pivot] + quick_sort_descending(less_than_pivot)

# Array untuk diuji
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Array asli A:", A)
print("Array asli B:", B)

# Bubble Sort untuk A (ascending)
start_time = time.time()
sorted_A_bubble_asc = bubble_sort_ascending(A.copy())
bubble_sort_time_A_asc = time.time() - start_time
print("Bubble Sort (ascending) untuk A:", sorted_A_bubble_asc)
print(f"Waktu komputasi: {bubble_sort_time_A_asc:.6f} detik")

# Bubble Sort untuk B (descending)
start_time = time.time()
sorted_B_bubble_desc = bubble_sort_descending(B.copy())
bubble_sort_time_B_desc = time.time() - start_time
print("Bubble Sort (descending) untuk B:", sorted_B_bubble_desc)
print(f"Waktu komputasi: {bubble_sort_time_B_desc:.6f} detik")

# Quick Sort untuk A (ascending)
start_time = time.time()
sorted_A_quick_asc = quick_sort_ascending(A.copy())
quick_sort_time_A_asc = time.time() - start_time
print("Quick Sort (ascending) untuk A:", sorted_A_quick_asc)
print(f"Waktu komputasi: {quick_sort_time_A_asc:.6f} detik")

# Quick Sort untuk B (descending)
start_time = time.time()
sorted_B_quick_desc = quick_sort_descending(B.copy())
quick_sort_time_B_desc = time.time() - start_time
print("Quick Sort (descending) untuk B:", sorted_B_quick_desc)
print(f"Waktu komputasi: {quick_sort_time_B_desc:.6f} detik")

# Analisis Keefektifan
"""
Quick Sort lebih efisien dibandingkan Bubble Sort karena pendekatannya yang membagi array menjadi bagian-bagian kecil
dan mengurutkannya secara rekursif. Hal ini memberikan efisiensi waktu lebih baik, terutama untuk dataset besar.
Bubble Sort lambat karena membutuhkan banyak iterasi untuk setiap elemen, sehingga tidak cocok untuk penggunaan
dengan dataset besar. Dalam contoh ini, Quick Sort memberikan performa lebih cepat untuk mengurutkan A dan B.
"""