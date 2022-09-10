# Operasi dan manipulasi sring

# 1. menyambung string (concatenate)
nama_pertama="ucup"
nama_tengah="D"
nama_terakhir="Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_terakhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari" + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string

# . mengecek apakah ada komponen char atau string di string

d = "ucup"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

# . Mengulang string
print("wk"*10)
print(15*"wk")

#  . Indexing
print("Index ke-0              : " + nama_lengkap[0])
print("Index ke-6              : " + nama_lengkap[6])
print("Index ke-(-1)           : " + nama_lengkap[-1])
print("Index ke-(-2)           : " + nama_lengkap[-2])
print("Index ke-[0:3]          : " + nama_lengkap[0:4])
print("Index ke-[3:7]          : " + nama_lengkap[3:8])
print("Index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print(" ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char unntuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + "=" + str(jumlah))

