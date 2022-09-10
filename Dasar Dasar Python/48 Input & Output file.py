# input output file


"""
w = write mode / mode menu dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambanhkan data diakhir baris
r+ = write and read mode

"""

# membuat file text

file = open("data.txt", 'w')

file.write("Ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nIni adalah baris kedua")
file.write("\nIni adalah baris ketiga")
file.write("\nIni adalah baris keempat")

file.close()

# membaca file text

file2 = open('data.txt', 'r')

#print(file2.read(10))
print(file2.readline())
print(file2.readline())

file2.close()

# appending mode

file3  = open("data.txt",'a')

file3.write("\nBaris ini dibuat dengan menggunakan mode append")

file3.close()



