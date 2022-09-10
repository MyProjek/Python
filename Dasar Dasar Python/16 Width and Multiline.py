# Width and Multiline

# Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# String Standart
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, data nomor sepatu = {data_nomor_sepatu}"
print(5*"="+"[Data String]"+5*"=")
print(data_string)

# String Multiline (dengan menggunkan enter, newline,\n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \ndata nomor sepatu = {data_nomor_sepatu}"
print(5*"="+"[Data String]"+5*"=")
print(data_string)

# String Multiline (kutip triplets)
data_string = f"""
nama              = {data_nama} 
umur              = {data_umur}
tinggi            = {data_tinggi}
data nomor sepatu = {data_nomor_sepatu}"""
print(5*"="+"[Data String]"+5*"=")
print(data_string)

# String Multiline (kutip triplets)
data_nama + "Ucup SUrucup"
data_tinggi = 105.17
data_string = f"""
nama              = {data_nama:>5} 
umur              = {data_umur:>5}
tinggi            = {data_tinggi:>5}
data nomor sepatu = {data_nomor_sepatu:>5}"""
print(5*"="+"[Data String]"+5*"=")
print(data_string)