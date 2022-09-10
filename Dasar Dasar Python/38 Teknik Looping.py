# Teknik looping
print(45*'=')

nama_band = ['Payung Teduh',
            'Fourtwnty',
            'Dialog Dini Hari',
            'Mr. Sonjaya',
            'Parahyena',
            'Syahrini']

kumpulan_lagu = ["Akad",
                "Zona Nyaman",
                "Rumahku",
                "Sang Filsuf",
                "Sindoro",
                "Jodohku"]

iterasi = 1;
for band in nama_band :
    print('No.',iterasi,"Nama Band :",band)
    iterasi+=1

print(45*'=')

# enumarate
# Cara Simplenya menggunakan enumarate
i = 1
for i, band in enumerate(nama_band):
    i+=1
    print(i,':',band)

print(45*'=')

# Zip
# Zip digunkan saat menggabungkan 2 atau lebih sebuah data list

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'-> Menyanyikan Lagu Berjudul :',lagu)

print(45*'=')

# Set
playlist01 = {'baby baby',
            'ada apa dengan cinta',
            'cenat-cenut',
            'jarang goyang',
            'gorgom',
            'kuda',
            'kucing'}

for lagu in sorted(playlist01): # sorted berguna untuk mengurutkan data
    print(lagu)

print(45*'=')

# Dictionary
playlist02 ={'Payung Teduh':'Akad',
            'Fourtwnty':'Zona Nyaman',
            'Dialog Dini Hari':'Rumahku'}

for i,v in playlist02.items():
    print(i, "lagunya adalah ",v)

print(45*'=')

# reversed -> untuk membalikkan data
for i in reversed(range(1,10,1)):
    print(i)
    
print(45*'=')
    


