class Ojek():
    
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
        
    def cek_id_abang(self):
        print('Nama   : ',self.nama,'\nMotor  : ',self.transmisi,'\nDaerah : ',self.daerah)

class Gojek(Ojek):
    #pass
    def cek_id_abang(self):
        print("cek id abang ditimpa")
    

ojek1 = Ojek("Mario",'Manual','Bandung Selatan')
ojek1.cek_id_abang()

print(30*'=')

ojek2 = Gojek("Jakson",'Automatic','Tasikmalaya')
ojek2.cek_id_abang()


print(30*'=')