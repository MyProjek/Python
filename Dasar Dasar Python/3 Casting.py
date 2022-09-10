# Kita belajar Casting
# merubah dari satu tipe ke tipe lainnya
# tipe data = int, float, str, bool

print("======INTEGER=====")
data_int = 9;
print("data =", data_int,",type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data =", data_float,",type =",type(data_float))
print("data =", data_str,",type =",type(data_str))
print("data =", data_bool,",type =",type(data_bool))

print("======FLOAT=====")
data_float = 9.5;
print("data =", data_float,",type =",type(data_float))

data_int = int(data_float) #akan dibuat ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float= 0
print("data =", data_int,",type =",type(data_int))
print("data =", data_str,",type =",type(data_str))
print("data =", data_bool,",type =",type(data_bool))

print("======BOOLEAN=====")
data_bool = True;
print("data =", data_bool,",type =",type(data_bool))

data_int = int(data_bool) #akan dibuat ke bawah
data_str = str(data_bool)
data_float = float(data_bool) # akan True jika nilai float= 1
print("data =", data_int,",type =",type(data_int))
print("data =", data_str,",type =",type(data_str))
print("data =", data_float,",type =",type(data_float))

print("======BOOLEAN=====")
data_bool = False;
print("data =", data_bool,",type =",type(data_bool))

data_int = int(data_bool) #akan dibuat ke bawah
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai float= 0
print("data =", data_int,",type =",type(data_int))
print("data =", data_str,",type =",type(data_str))
print("data =", data_float,",type =",type(data_float))

print("======STRING=====")
data_str = "";
print("data =", data_str,",type =",type(data_str))

#data_int = int(data_str) # string harus berbentuk angka
#data_float = float(data_str) # sring harus berbentuk angka
data_bool = bool(data_str)# akan false jika nilai string kosong
#print("data =", data_int,",type =",type(data_int))
#print("data =", data_float,",type =",type(data_float))
print("data =", data_bool,",type =",type(data_bool))





