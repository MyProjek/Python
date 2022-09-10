import tkinter
from typing import Text

main_window = tkinter.Tk()

def event_tekan() :
    label2 = tkinter.Label(main_window, text="Aku di Tekan ^_^")
    label2.pack()


label = tkinter.Label(main_window, text="Hallo, saya adalah \n GUI sederha dengan \n nenggunakan python")
tombol = tkinter.Button(main_window, text="Tekan Aku", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()