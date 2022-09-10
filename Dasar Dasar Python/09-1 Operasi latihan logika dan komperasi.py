# Episode ltihan logika dan komperasi
# Membuat gabungan area rentang dari angka

# ++++++3--------10+++++++

inputUser = float(input("Masukan angka yang bernilai \n kurang dari 3 \n atau \n lebih besar dari 10 :"))

# ++++++3--------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print( "Kurang Dari 3 =",isKurangDari)

# --------10++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih Dari 10 =" ,isLebihDari)

# ++++++3--------10+++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan :", isCorrect)

# ---------3+++++++++10--------
# Kasus Irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukan angka yang bernilai \n lebih dari 3 \n atau \n kurang dari 10 :"))

# ------3+++++++
#lebih dari 3
isLebihDari = (inputUser > 3)
print( "Lebih Dari 3 =",isLebihDari)

# +++++++10--------
#Kurang dari 10
isKurangDari = (inputUser  < 10)
print( "Kurang Dari 10 =",isKurangDari)

#--------3+++++++++10------
# Kasus Irisan
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan :", isCorrect)





