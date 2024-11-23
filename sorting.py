import time
import random

# Psudocode Merge sort 

# FUNCTION merge(arr, l, m, r)
#     n1 ← m - l + 1
#     n2 ← r - m

#     CREATE temporary array L of size n1
#     CREATE temporary array R of size n2

#     // Copy data ke array sementara
#     FOR i FROM 0 TO n1-1 DO
#         L[i] ← arr[l + i]
#     END FOR

#     FOR j FROM 0 TO n2-1 DO
#         R[j] ← arr[m + 1 + j]
#     END FOR

#     // Gabungkan kembali array sementara ke array utama
#     i ← 0  // Index array pertama
#     j ← 0  // Index array kedua
#     k ← l  // Index array gabungan

#     WHILE i < n1 AND j < n2 DO
#         IF L[i] <= R[j] THEN
#             arr[k] ← L[i]
#             i ← i + 1
#         ELSE
#             arr[k] ← R[j]
#             j ← j + 1
#         END IF
#         k ← k + 1
#     END WHILE

#     // Copy elemen yang tersisa dari L, jika ada
#     WHILE i < n1 DO
#         arr[k] ← L[i]
#         i ← i + 1
#         k ← k + 1
#     END WHILE

#     // Copy elemen yang tersisa dari R, jika ada
#     WHILE j < n2 DO
#         arr[k] ← R[j]
#         j ← j + 1
#         k ← k + 1
#     END WHILE
# END FUNCTION





def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m
 
    # membuat array sementara
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Salin data ke dalam array sementara tadi
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Gabungkan kemabli array sementara tadi ke dalam satu array yang baru
    i = 0     # Inisialisasi index Array pertama dari sub array
    j = 0     # Inisialisasi index Array kedua dari sub array
    k = l     # Inisialisasi index dari sub array gabungan
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1



def mergeSort(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 






# FUNCTION bubbleSort(arr)
#     n ← length of arr
#     FOR i FROM 0 TO n-1 DO
#         FOR j FROM 0 TO n-i-2 DO
#             IF arr[j] > arr[j+1] THEN
#                 SWAP arr[j] WITH arr[j+1]
#             END IF
#         END FOR
#     END FOR
# END FUNCTION




def bubbleSort(arr):
    n = len(arr)
    # Lakukan iterasi melalui seluruh elemen array
    for i in range(n):
        # Elemen terakhir sudah diurutkan, jadi tidak perlu diperiksa lagi
        for j in range(0, n-i-1):
            # Jika elemen yang sekarang lebih besar dari elemen berikutnya, tukar posisi
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]




x1 = [random.randint(1, 1000) for _ in range(100)]


n = len(x1)
print("Array yang akan di sort pakai merge sort")
for i in range(n):
    print("%d" % x1[i],end=" ")

time_start = time.perf_counter()
mergeSort(x1, 0, n-1)
time_end = time.perf_counter()
timeTotal = time_end - time_start
print("\nArray yang sudah di sort pakai merge sort")
print(f"\nTime Complexity Merge sort {timeTotal:.10f} second")
for i in range(n):
    print("%d" % x1[i],end=" ")
 

x2 = [random.randint(1, 1000) for _ in range(100)]



print("\nArray akan di sort pakai bubble sort")
for i in range(n):
    print("%d" % x2[i],end=" ")

time_start = time.perf_counter()
bubbleSort(x2)
time_end = time.perf_counter()
timeTotal = time_end - time_start
print(f"\nTime Complexity Bubble sort {timeTotal:.10f} second")
print("\nArray yang sudah di sort pakai bubble sort")
for i in range(n):
    print("%d" % x2[i],end=" ")
