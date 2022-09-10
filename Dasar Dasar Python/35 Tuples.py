# List
Ganjil = [1,3,5,7,9]

# Tuple
Genap = (2,4,6,8,10)

print(type(Ganjil))
print(type(Genap))
 
Ganjil[2] = 99
#Genap = 99

print(Ganjil)
print(Genap)

Ganjil.append(2)
#Genap.append(2)

print(Ganjil)
print(Genap)

"""
print(45*'=')
print(dir(Ganjil))
print(45*'=')
print(dir(Genap))
print(45*'=')
"""
print(Genap.count(6)) # count untuk menghituh jumlah angka yang ditunjuk pada kolom
print(Genap.index(10)) # menghitung jumlah urutan dari depan

print(50*'=')

# Tuples - mengecek besar data yang dimuat menggunakan import sys
import sys

data_list = [1,2,3,4,5,"pisang goreng","syahrini","via vallen",False,3.14]
data_tuple = (1,2,3,4,5,"pisang goreng","syahrini","via vallen",False,3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print("besar data list  : ",besar_datalist)
print("besar data tuple : ",besar_datatuple)

print(50*'=')

# Tuples - mengecek kecepatan data yang dimuat menggunakan import timeit
import timeit

data_list01  = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,]",number=1000000)
data_tuple02 = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,)",number=1000000)

print("waktu untuk memproses list  :",data_list01)
print("waktu untuk memproses tuple :",data_tuple02)




