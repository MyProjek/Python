# Pengenalan Class
class mahasiswa():

    jurusan = " Teknik Tata Boga"
    __nilai = 0 # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim # public

    def uts(self,input_nilai):
        self.__nilai += input_nilai
    
    def uas(self, input_nilai):
        self.__nilai += input_nilai
    
    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,"Tidak Lulus")
        else:
            print(self.nama,"Lulus")

# Main Programnya

otong = mahasiswa("Oton Surotong", 1234234)
ucup = mahasiswa("Michael Ucup",14325678)

otong.uts(10)
otong.uas(50)

otong.check_status()

ucup.uts(5)
ucup.uas(25)

ucup.check_status()



