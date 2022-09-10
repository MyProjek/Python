Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

print(30*'=')

# beberapa method yang bisa digunakan untuk memanipulasi list
Barang.append('sepeda')
print(Barang)

Barang.extend('dompet')
print(Barang)

Barang.insert(3,'sepeda')
print(Barang)

# method untuk menghitung anggota
jumlahSepeda = Barang.count('sepeda')
print('Jumlah sepeda adalah :',jumlahSepeda)

print(30*'=')

# meremove data
Barang.remove('sepeda')
print(Barang)

Barang.reverse()
print(Barang)

print(30*'=')

Stuff = Barang.copy()
Stuff.append('gelas')
print(Stuff)
print(Barang)

"""
data = "test"
for i in data :
    print(i)

data = "test"
print(data[2])
"""

