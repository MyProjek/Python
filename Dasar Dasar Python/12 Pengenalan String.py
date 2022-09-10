data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunaan string single qoute  '....'
    2. dengan menggunaan string double qoute  "...."

'''

data = 'menggunakan single qoute'
print(data)

data = "menggunakan double qoute"
print(data)

print('"Hallo, Apa kabar ?"')
print("'Hallo, Apa kabar ?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("c:\\user\\ucup")

# tab
print("ucup\t\t\totong, semakin jauhan")

# backspace 
print("ucup \botong, jadi deketan")

# newLine
print("baris pertama.\n baris kedua") # LF -> line feed -> unix, macos, linux
print("baris pertama.\r baris kedua") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3 String Literal atau raw

# hati - hati
print('c:\new folder')

# menggunakan raw string
print(r'c:\new folder')

# multiline literal string
print('''
Nama  : Ucup
Kelas : 3 SD
''')

# multiline literal string and raw
print(r'''
Nama  : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
''')



