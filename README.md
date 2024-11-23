# Algoritma Sorting: Merge Sort dan Bubble Sort

Proyek ini mengimplementasikan dua algoritma sorting, yaitu **Merge Sort** dan **Bubble Sort**, untuk membandingkan performa keduanya dalam mengurutkan array bilangan acak. Program ini juga mengukur waktu eksekusi dari kedua algoritma untuk menunjukkan perbedaan efisiensi.

---

## Daftar Isi
- [Deskripsi](#deskripsi)
- [Algoritma yang Digunakan](#algoritma-yang-digunakan)
  - [Merge Sort](#merge-sort)
  - [Bubble Sort](#bubble-sort)
- [Analisis Kompleksitas Waktu](#analisis-kompleksitas-waktu)
- [Persyaratan](#persyaratan)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Perbandingan Kinerja](#perbandingan-kinerja)

---

## Deskripsi
Sorting adalah salah satu operasi mendasar dalam ilmu komputer yang bertujuan untuk mengurutkan data. Proyek ini bertujuan untuk:
1. Menunjukkan perbedaan efisiensi antara algoritma **Merge Sort** dan **Bubble Sort**.
2. Mengukur waktu eksekusi dari kedua algoritma.
3. Memvisualisasikan hasil pengurutan array.

---

## Algoritma yang Digunakan

### Merge Sort
- **Tipe**: Divide-and-conquer.
- **Cara Kerja**:
  - Membagi array menjadi dua bagian hingga mencapai ukuran terkecil (sub-array dengan satu elemen).
  - Menggabungkan kembali sub-array secara berurutan.
  - Cocok untuk dataset besar karena efisiensinya.
  
### Bubble Sort
- **Tipe**: Comparison-based.
- **Cara Kerja**:
  - Membandingkan elemen yang bersebelahan dan menukarnya jika tidak berurutan.
  - Melakukan iterasi ini berulang-ulang hingga array terurut.
  - Sederhana tetapi tidak efisien untuk dataset besar.

---

## Analisis Kompleksitas Waktu

### 1. Merge Sort
- **Kompleksitas dalam Notasi Big-O dan Big-Theta**:
  - **Best Case (\( \Theta(n ⋅ log n) \))**:
    - Operasi pembagian array menjadi dua dan penggabungan tetap sama, terlepas dari bagaimana data awal terurut.
  - **Worst Case (\( O(n ⋅ log n) \))**:
    - Sama dengan best case karena jumlah operasi pembagian dan penggabungan tetap konstan.
  - **Rata-rata (\( \Theta(n ⋅ log n) \))**:
    - Efisiensi rata-rata tetap konsisten pada setiap data input karena algoritma selalu membagi dan menggabungkan dengan cara yang sama.

- **Penjelasan**:
  - **Pembagian Array**:
    - Setiap langkah membagi array menjadi dua bagian, memakan waktu konstan, yaitu **O(1)**.
  - **Penggabungan**:
    - Operasi penggabungan membutuhkan waktu **O(n)** pada setiap tingkat rekursi.
  - **Kedalaman Rekursi**:
    - Dengan setiap pembagian, rekursi mencapai kedalaman hingga **log₂(n)**.
  - **Total Kompleksitas**:
    \[
    T(n) = O(n ⋅ log n)
    \]

### 2. Bubble Sort
- **Kompleksitas dalam Notasi Big-O dan Big-Theta**:
  - **Best Case (\( \Theta(n^2) \))**:
    - Karena implementasi ini tidak memiliki optimasi "early stopping", semua iterasi tetap dilakukan bahkan jika array sudah terurut.
  - **Worst Case (\( O(n^2) \))**:
    - Terjadi saat array dalam kondisi terbalik. Setiap elemen harus dibandingkan dan ditukar pada setiap iterasi.
  - **Rata-rata (\( \Theta(n^2) \))**:
    - Pada umumnya, algoritma ini membutuhkan waktu kuadrat untuk mengurutkan data acak.

- **Penjelasan**:
  - **Perbandingan Elemen**:
    - Pada iterasi pertama, ada **n-1** perbandingan. Pada iterasi kedua, ada **n-2**, dan seterusnya.
  - **Jumlah Total Perbandingan**:
    - Dihitung menggunakan deret aritmatika:
      \[
      \frac{n(n-1)}{2}
      \]
    - Kompleksitas total menjadi **O(n^2)**.

---

## Perbandingan Kinerja
| Algoritma    | Best Case (\( \Theta \)) | Worst Case (\( O \)) | Rata-rata (\( \Theta \)) |
|--------------|--------------------------|-----------------------|--------------------------|
| Merge Sort   | \( \Theta(n⋅log n) \) | \( O(n ⋅ log n) \) | \( \Theta(n ⋅ log n) \) |
| Bubble Sort  | \( \Theta(n^2) \)           | \( O(n^2) \)           | \( \Theta(n^2) \)          |

---

## Persyaratan
- **Python 3.x**
- Modul bawaan Python:
  - `time`
  - `random`

---
