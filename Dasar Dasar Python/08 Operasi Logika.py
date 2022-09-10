# Oeprasi Logika atau Boolean
# not, or, and, xor

print('====NOT====')
a = True
c = not a
print('data a = ',a)
print('=========== NOT')
print('data c =',c)

#OR ( Jikq slah satu hasilnya True, maka hasilnya adalah true)
print('===== OR ====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,' =',c)

a = True
b = False
c = a or b
print(a,' OR',b,'=',c)

a = True
b = True
c = a or b
print(a,' OR',b,' =',c)

#AND ( Jika dua buah nilai  True, maka hasilnya adalah true)
print('===== OR ====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,' =',c)

a = True
b = False
c = a and b
print(a,' AND',b,'=',c)

a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

#XOR ( Akan true jika salah satu true, sisanya False)
print('===== OR ====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)

a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
