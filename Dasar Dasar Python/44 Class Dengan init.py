# Class
class mahasiswa():
    
    def __init__(self,  input_nama,belajar, input_nim): # __init__ akan dijalankan saat melakukan inisiasi
        self.nama = input_nama
        self.nim = input_nim
        self.blj = belajar
    
class pelajar():

    def __init__(diri, inputNama, Apakegiatan, noSempak):
        diri.nama = inputNama
        diri.kegiatan = Apakegiatan
        diri.no = noSempak

    

# main programnya 

print(30*'=')
otong = mahasiswa("Otong Surotong","belajar dengan giat", 13317001)
print(otong.nama)
print(otong.blj)
print(otong.nim)

print(30*'=')

ucup = pelajar("Mixeal","Dan tidur", 1406789)
print(ucup.nama)
print(ucup.kegiatan)
print(ucup.no)
print(30*'=')







