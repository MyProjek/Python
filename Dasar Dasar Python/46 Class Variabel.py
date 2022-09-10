class mahasiswa():

    #jurusan = "ekonomi"

    jumlah_mahasiwa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim # public
        mahasiswa.jumlah_mahasiwa += 1

# main programnya


otong = mahasiswa("Oton Surotong", 1234234)
ucup = mahasiswa("Michael Ucup",14325678)
cassandra = mahasiswa(" Cassandra aja", 123456736)

print(mahasiswa.jumlah_mahasiwa)

"""
otong.jurusan = "Ekonomi Mikro"
print(mahasiswa.jurusan)
print(otong.jurusan)
print(ucup.jurusan)
print(mahasiswa.__dict__)
print(otong.__dict__)
"""