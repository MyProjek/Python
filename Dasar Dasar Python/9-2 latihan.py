print("\n",10*"=","\n")
inputUser = float(input("Masukan angka yang bernilai  :"))

# ------0+++++++
#lebih dari 3
isLebihDari = (inputUser > 0)
print( "Lebih Dari 0    =",isLebihDari)

# +++++++5--------
#Kurang dari 5
isKurangDari = (inputUser  < 5)
print( "Kurang Dari 10  =",isKurangDari)

#--------0+++++++++5------
# Kasus Irisan
isCorrect = isKurangDari and isLebihDari

# ------8+++++++
#lebih dari 3
isLebihDari = (inputUser > 8)
print( "Lebih Dari 8   =",isLebihDari)

# +++++++11--------
#Kurang dari 11
isKurangDari = (inputUser  < 11)
print( "Kurang Dari 10 =",isKurangDari)

#--------8+++++++++11------
# Kasus Irisan
isCorrect01 = isKurangDari and isLebihDari
Hasilnya = isCorrect or isCorrect01
print("Angka Yang anda masukkan :",Hasilnya)

print(6*"=","| TUGAS |",6*"=")

inputUser =float(input(" Masukkan angka Numerik  :"))
x = (inputUser < 0) 
print(" Kurang dari 0  :",x)
y = (inputUser > 5)
print(" lebih dari 5   :",y)
z = (inputUser < 8)
print(" kurang dari 8  :",z)
w = (inputUser > 11)
print(" lebih dari 11  :",w)
print(30*"=")
print ("Hasilnya adalah :", ((x and y) or (z and w)))
print(30*"=")
