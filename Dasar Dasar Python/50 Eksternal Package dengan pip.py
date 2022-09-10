"""
import numpy as np
a = np.array([1,2,3,4])  
b = np.array([5,6,7,8])  
                         
print(a + b)
"""
# untuk mmengecek versi python: python --version
# untuk mengecek pip: pip3 python --version
# untuk mengecek list package: pip3 list --format=columns
# untuk mengunistall pip: pip3 uninstall

from PIL import Image

im = Image.open("img.jpg")

print(" format file: " + im.format)
print(" ukuran: " + str(im.size))
print(" Kode file: " + im.mode)

im.show()
