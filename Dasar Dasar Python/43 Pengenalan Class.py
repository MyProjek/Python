# Pengenalan Class
class mahasiswa():
    nama = 'nama' #--> Disebut sebagai Atribut/ Nilai yang menempel pada kelas tersebut


    def belajar(self, kondisi):  #--> Disebut method
        print(self.nama," Sedang Belajar", kondisi) # self.nama = untuk mengakses sebuah data tersendiri
    
    def tidur(self, kondisi):
        print(self.nama, " Tidur di Kelas", kondisi)

# Main Programnya

otong = mahasiswa()
ucup = mahasiswa()

otong.nama = " Otong Surotong"
ucup.nama = " Michel Ucup"

#print(otong.nama)
#print(ucup.nama)

otong.belajar(" dengan giat")
ucup.tidur(" dengan pulas ")
    
