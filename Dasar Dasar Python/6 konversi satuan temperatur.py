# Latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print("\n PROGRAM KONVERSI TEMPERATUR\n")

# celcius
celcius = float(input('Masukkan suhu dalam celcius : '))
print("- Suhu Celcius    =",celcius,"Celcius")

#Reamur
reamur =(4/5)*celcius
print("- Suhu Reamur     =",reamur,"Reamur")

#fahrenheit
fahrenheit=((9/5)*celcius)+32
print("- Suhu fahrenheit =",fahrenheit,"fahrenheit")

#kelvin
kelvin =celcius+273
print("- Suhu kelvin     =",kelvin,"kelvin")

print("=== TUGAS ===")

f=float(input('Masukkan nilai fahrenheit:' ))
print('-',f,"fahrenheit =",(5/9*(f-32)+273),"Kelvin")

k =float(input('Masukkan nilai fahrenheit:' ))
print('-',k,"kelvin     =",9/5*(k-273)+32,"Kelvin")







