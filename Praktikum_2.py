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
