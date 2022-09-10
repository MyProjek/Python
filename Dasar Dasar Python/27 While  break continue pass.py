angka = 0
"""
while angka < 5 :
    print("Nilai Angka adalah",angka)
    angka = angka + 1
    
print("Di luar While")
"""
"""
# While Start if angka 100 menggunakan Boolean :
start = True # Variabel boolean
angka = 0

while start :
    print("di dalam While")
    if angka is 100 :
        start  = False
        print("Oke ! Angka 100 ditemukan")
    angka += 1
"""
"""
# While angka < 5
# menggunakan else, break, continue, pass

angka = 0

while angka < 5 :
    print('Nilai Angka adalah : ',angka)
    angka += 1
else :
    print('Nilai Angka diakhir while adalah',angka)
"""

print(30*'=','\n')
angka = 0
while angka < 10 :
    if angka is 5 :
        print("Checkpoint 1")
        break
        print("Checkpoint 2")
    print('Nilai Angka adalah : ',angka)
    angka += 1
else :
    print('Nilai Angka diakhir while adalah',angka)

print("Di Luar While")
print('\n',30*'=')

"""
print(30*'=','\n')
angka = 0
while angka < 10 :
    if angka is 5 :
        #print("Checkpoint 1")
        angka += 1
        continue
        #print("Checkpoint 2")
    print('Nilai Angka adalah : ',angka)
    angka += 1
else :
    print('Nilai Angka diakhir while adalah',angka)

print("Di Luar While")
print('\n',30*'=')
"""
print(30*'=','\n')
angka = 0
while angka < 10 :
    if angka is 5 :
        print("Checkpoint 1")
        pass
        print("Checkpoint 2")
    print('Nilai Angka adalah : ',angka)
    angka += 1
else :
    print('Nilai Angka diakhir while adalah',angka)

print("Di Luar While")
print('\n',30*'=')
