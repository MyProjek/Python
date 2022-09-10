# List adalah sekumpulan data pada variabel

print("\n")
Data = [1,4,9,16,25,36,49,64]

# Mengakses list
Subdata1  = Data[3]
print(Subdata1)
Subdata2  = Data[-3]
print(Subdata2)

# Memotong List
Subdata3 = Data[0:4]
print(Subdata3)
Subdata4 = Data[:4]

Data2 = [100,200,300,400,500,600,700,800]

# Menambah List

Data3 = Data + Data2
print(Data3)
print("\n")

# Merubah content dari list

print(Data,"\n")
Data[4] = 87

# Mengcopy list ke variable baru
a = Data[:]
a[7] = 87
print(a,"\n")

# Merubah content list dengan menggunakan metode slicing
Data[3:5] = [11,12]

# List dalam list
x = [Data,Data2]

# Mengakses list dalam multidimensional list

y = x[1] [4]
print(x,"\n")
print(y,"\n")

# Methods untuk list

Data.append(30)

# Function yang bisa kita gunakan kepada list

panjang_list = len(Data)

print(Data)
print(panjang_list)