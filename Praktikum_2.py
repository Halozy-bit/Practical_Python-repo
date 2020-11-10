# Tugas 1

n = 100000
a = 60 * 60 * 24
hari = int(n / a)
b = a * hari
c = n - b
jam = int(c / (60*60))
d = jam * (60*60)
e = c - d
menit = int(e / 60)
detik = n % 60
print("Hasil dari 100.000 detik")
print(hari, " hari ", jam, " jam ", menit, " menit ", detik, " detik")
print("")

# Tugas 2
import numpy as np 

DET = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
print("Matriks 3x3")
print (DET)
print("Hasil Determinan Menggunakan NUMPY Library")
print (np.linalg.det(DET))
print("Hasil Determinan Menggunakan Operator Dasar")
print (6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))
print("")

# Tugas 3
def cetak_matriks(matriks):
    for row in matriks:
        print (row)
 
def pjg_matriks(matriks):
    return len(matriks[0])
 
def lbr_matriks(matriks):
    return len(matriks)
 
def transpose_matriks(mat_a):
    temp_row = []
    temp_mat = []
 
    for i in range(0, pjg_matriks(mat_a)):
        for j in range(0, lbr_matriks(mat_a)):
            temp_row.append( mat_a[j][i])
        temp_mat.append(temp_row)
        temp_row = []
    return temp_mat
 
TRANS = [[1, 2, 3, 5], [3, 4, 5, 6], [5, 6, 7, 8]]

 
print ("matriks_a : ")
cetak_matriks(TRANS)
print ("transpose matriks_a : ")
trp_mat_a = transpose_matriks(TRANS)
cetak_matriks(trp_mat_a)
 

