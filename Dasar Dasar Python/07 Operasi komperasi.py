# Operasi komperasi

# Setiap hasil dari komperasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a=4
b=2

# lebih besar dari >
print('========= lebih besar dari (>) ========')
hasil = a > 3
print(a,'>',3,'=', hasil)
hasil = b > 3
print(b,'>',3,'=', hasil)
hasil = a > 2
print(a,'>',2,'=', hasil)

# lebih kurang dari <
print('========= kurang besar dari (<) ========')
hasil = a < 3
print(a,'<',3,'=', hasil)
hasil = b < 3
print(b,'<',3,'=', hasil)
hasil = a < 2
print(a,'<',2,'=', hasil)

# lebih besar dari sama dengan >=
print('========= lebih besar dari (>=) ========')
hasil = a >= 3
print(a,'>=',3,'=', hasil)
hasil = b > 3
print(b,'>=',3,'=', hasil)
hasil = a >= 2
print(a,'>=',2,'=', hasil)

#  sama dengan ==
print('========= sama dengan (==) ========')
hasil = a == 3
print(a,'==',3,'=', hasil)
hasil = b == 2
print(b,'==',2,'=', hasil)
hasil = a == 2
print(a,'==',2,'=', hasil)

#  tidak sama dengan !=
print('========= tidak sama dengan (!=) ========')
hasil = a != 3
print(a,'!=',3,'=', hasil)
hasil = b != 2
print(b,'!=',2,'=', hasil)
hasil = a != 2
print(a,'!=',2,'=', hasil)

# 'is" sebagai komperasi object identity
x = 5 # ini adalah assigment membuat projek
y = 5 
print('nilai x =',x,',id=',hex(id(x)))
print('nilai y =',y,',id=',hex(id(y)))
hasil= x is y
print('x is y =',hasil)

# Soal Jawaban Latiahn 2
print(30*'=')
a = 52
b = 10
hsl = a >= b
print("Nilai",a,">=",b,"=",hsl)

a = (3+3)
b = (3*3)
hsl = a > b
print("Nilai",a,">",b,"=",hsl)

a = x**(9)
b = 3
hsl = a = b
print("Nilai",a,"=",b,"=",hsl)

print(30*'=')
