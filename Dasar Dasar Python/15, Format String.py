# format string

# contoh generic

# String
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# Boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# Angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# Bilangan Bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}" # d berfunsi untu menjadian bil bulat
print(format_str)

# Bilangan Ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# Bilangan Desimal
angka = 2005.54321
format_str = f"angka = {angka:.3f}"
print(format_str)

# Menampilkan Leading Zero
angka = 2005.54321
format_str = f"Desimal = {angka:010.3f}" # menghitung jumlah angka + space + 0
print(format_str)

# Menampilkan tanda + atau -
angka_minus = -10
anga_plus = +10.1234
format_minus = f"Minus = {angka_minus:+d}"
format_plus = f"Plus = {anga_plus:+.2f}"
print(format_minus)
print(format_plus)

# Memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
forma_binary = f"binary = {bin(angka)}"
forma_octal = f"octal= {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(forma_binary)
print(forma_octal)
print(format_hex)