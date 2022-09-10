# Date and Time (latihan)

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2002,9,3)
print(tanggal)
print(f"hari ini adalah = {tanggal:%A}")

print("Silahkan masukkan tanggal , \nBulan dan \nTahun lahir anda")
tanggal =int(input("tanggal \t: "))
bulan =int(input("bulan \t\t: "))
tahun =int(input("tahun \t\t: "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari    lahir anda adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"umur anda dalam hari adalah    : {umur_hari}")
print(f"umur anda dalam setahun adalah : {umur_tahun} tahun")
print(f"Umur sisa bulan anda adalah ; {umur_bulan_sisa} bulan")

