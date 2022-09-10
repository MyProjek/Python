# Operator daam bentuk methods

### merubah case dari string

## merubah semua ke upper case

salam = "bro!"
print(" Normal = " + salam)
salam = salam.upper()
print(" Upper = " + salam)

# Merubah semua ke lower case
alay = " Aku Kece AbieeezZZZZ "
print(" Normal = " + alay)
alay = alay.lower()
print(" lower = " + alay)

# Pengecekan dengan isX method

# Contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha()    = untukk mengecek semua huruf
# isalnum()    = huruf dan angka
# isdecimal()  = angka saja
# isspace()    = spasi, tab, newline \n
# istitle()    = semua kata dimulai dengan huruf besar

judul = "It is Okay Not To Be Orkay"
cek_judul = judul.title() # hasil bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("End = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")