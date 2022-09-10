"""
def pembagian(a,b):
    return a/b

penyebut = int(input("masukan angka penyebut ?\n")) # 1
pembilang = int(input("masukan angka pembilang ?\n")) # 0

print(pembagian(penyebut,pembilang))
"""
print('='*30)
print("Ini adalah program pembagian")
while True:
    try:
        penyebut = int(input("masukan angka penyebut: "))
        pembilang = int(input("masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except Exception as err:
        print(err)
    """
    except ValueError:
        print("yang anda masukan bukan angka\n")
    except ZeroDivisionError:
        print("angka pembilang yang anda masukan adalah nol, pilih yang lain ya brosis\n")
    """
    
print("berhasil, anda memasukan angka: ", hasil)
print('='*30)

"""
    Type of exception errors :
    1. IOError
    2. ImportError
    3. ValueError
    4. Division by zero
    5. KeybordInterupted
    6. EOFError

"""

