# Latihan

# kalkulator Sederhana

print(12*"=","[ KALKULATOR ]",12*"=")

angka_1 =float(input("Masukkan  Angka pertama\t\t= "))
operator = input("Operator ( + , - , x , / )\t= ")
angka_2 =  float(input("Masukkan Angka Kedua\t\t= "))

# percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print(44*"-")
    print(f"Hasilnya Adalah = {hasil}")
    print(44*"-")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(44*"-")
    print(f"Hasilnya Adalah = {hasil}")
    print(44*"-")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(44*"-")
    print(f"Hasilnya Adalah = {hasil}")
    print(44*"-")
elif operator == ":" or operator == "/":
    hasil = angka_1 / angka_2
    print(44*"-")
    print(f"Hasilnya Adalah = {hasil}")
    print(44*"-")

else :
    print("Masukan yang bener dong !, aku pusying !")

print("Akhir dari program, Terima Kasoih")