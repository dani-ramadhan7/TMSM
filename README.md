# TMSM
Transpose Minimum Selection Method (TMSM) merupakan sebuah pendekatan yang menggunakan dan memodifikasi dengan SSM sebagai basisnya.
Berikut adalah diagram alir input dan output metode Transpose Minimum Selection Method (TMSM) untuk menyelesaikan Transportation Problem (TP):

```
Input: Matriks TP -> Program GUI (TMSM_GUI) -> Executable C (TMSM) -> Output: Hasil TMSM
```

1. Input:
- Matriks TP: Matriks yang menggambarkan hubungan antara supply dan demand dalam masalah transportasi. Contoh matriks TP yang disimpan dalam file D01.txt adalah sebagai berikut:
```
3 3

32 40 120
60 68 104
200 80 60

20 30 45

30 35 30
```
Di sini, angka-angka di atas mewakili nilai supply, demand, dan biaya transportasi antar lokasi.

2. Proses:
- Pengguna menginputkan matriks TP melalui program GUI (TMSM_GUI).
- Program GUI menggunakan modul `subprocess` untuk mengintegrasikan GUI Python dengan program C yang berisi executable TMSM yang telah dikompilasi.
- Program GUI memanggil executable C TMSM dan menangkap output-nya.

3. Output:
- Hasil dari pengerjaan matriks TP dengan metode TMSM akan di-return kembali ke program GUI.
- Contoh hasilnya adalah sebagai berikut:
```
32 [0]	60 [30]	200 [0]	| 30	Total alloc : 30	Status = SATISFY
40 [20]	68 [0]	80 [15]	| 35	Total alloc : 35	Status = SATISFY
120 [0]	104 [0]	60 [30]	| 30	Total alloc : 30	Status = SATISFY

Total Alokasi tabel adalah: 5600
```
Penjelasan:
- Angka di dalam kurung siku menunjukkan alokasi barang dari supply ke demand.
- Status “SATISFY” menandakan bahwa solusi memenuhi semua persyaratan supply dan demand.
- Total alokasi tabel adalah 5600.
