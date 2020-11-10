# Tugas 1
X = -3
Y = -2

if (X > 0)and(Y > 0):
  print("K = 1")
if (X > 0)and(Y < 0):
  print("K = 2")
if (X < 0)and(Y < 0):
  print("K = 3")
if (X < 0)and(Y > 0):
  print("K = 4")
if (X == 0)and(Y == 0):
  print("K = PUSAT")
print("")
# Tugas 2
array=[1, 2, 3, 4, 5]
for i in range(len(array)):
    array[i]=int(array[i])
jumlah=0
for i in range(len(array)):
    jumlah +=array[i]
rata=jumlah/len(array)
sigma = 0
for i in range(len(array)):
    hitung =(array[i]-rata)**2
    sigma += hitung
pembagianN=sigma/len(array)
standarDeviasi=pembagianN ** 0.5
print(standarDeviasi) 
print("")
# Tugas 3
def transform_number_to_roman_numeral(number):
    roman_value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_char_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ''
    for i in range(len(roman_value_list)):
        while number >= roman_value_list[i]:
            number -= roman_value_list[i]
            res += roman_char_list[i]
    return res
 
 
N = 27
roman_numeral_output = transform_number_to_roman_numeral(N)
print('number {0} equal to:{1}'.format(N, roman_numeral_output))