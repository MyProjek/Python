# fungsi dengan menggunakan argumen sederhana
"""
def siswa(nama):
    print('siswa ini bernama :',nama)

siswa('mario')

# fungsi dengan menggunakan keyword arguments

def guru(nama,pelajaran):
    print('Guru ini bernama :',nama)
    print('mengajar :',pelajaran)

guru(nama='Popong',pelajaran='Seni Rupa')
guru(pelajaran="Olah raga",nama="Endang")
guru('olah raga','raihan') # ini contoh yang salah
"""
def penjagaSekolah(nama, shift='Siang',galak='tidak'):
    print('penjaga sekolah ini bernama :',nama)
    print('shiftnya :', shift)
    print('galak :',galak)

penjagaSekolah('Entis')
penjagaSekolah('Maman', shift='malam')
penjagaSekolah('Asep',galak='Sangat')
# penjagaSekolah(shift="malam",galak='iya') Salah karna Nilai Variabel Nama tidak ada
