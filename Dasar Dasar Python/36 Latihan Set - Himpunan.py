# set, himpunan :
print(45*'=')
superhero = { "wiro sableng",
              "si buta dari goa hantu",
              "saras 008",
              "gundala",
              "gatot kaca"}

superhero.add("mak lampir")
superhero.add("gundala")

print(superhero)

print(45*'=')
# Atau bisa juga menggunakan struktur seperti ini

superhero = set()
superhero.add("wiro sableng")
superhero.add("gundala")
superhero.add("saras 008")
superhero.add(212)

# print(sorted(superhero)) untuk mengurutkan data dari index terkecil
 
print(superhero)

print(45*'=')

# set, himpunan ( Gabungan & Irisan ) :

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap)) # Gabungan 
print(ganjil.intersection(prima)) # irisan
