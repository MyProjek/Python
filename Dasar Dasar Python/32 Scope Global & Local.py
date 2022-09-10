# scope variable : local

namaKucing = 'cassandra'

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('saya rubah nama kucing menjadi',namaKucing)

rubahNamaKucing('ketie')
print('nama kucing saya menjadi',namaKucing)

print(30*'=')

# scope variable : global

namaKucing = 'cassandra'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('saya rubah nama kucing menjadi',namaKucing)

rubahNamaKucing('ketie')
print('nama kucing saya menjadi',namaKucing)

print(30*'=')

namaKucing = 'cassandra'
makananKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru # Variabel global
    nama = namaBaru # Variabel local
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('Ketie')
kasihMakanKucing('universal','Alex')

print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)




