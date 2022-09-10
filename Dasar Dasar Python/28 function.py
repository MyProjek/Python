print(30*'=','\n')
# Mendefiniskan fungsi
def fungsi():
    print("Ini adalah fungsi")

#memanggil fungsi
fungsi()

print('\n',30*'=')

# Membuat funsi sederhana :
def suaraayam():
     print('kukuruyuk!!!')

def hargaayam():
    suaraayam()
    print("Harga Ayam per 1 kg adalah 20.000")

hargaayam()

print('\n',30*'=')
# Membuat fungsi dengan input argument
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargatotal = kg*harga
    print("harga",kg,'ayam adalah',hargatotal)

hargaayam()
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)

print('\n',30*'=')
