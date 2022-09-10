def kuadrat(argumen):
    total = argumen**2
    print('Nilai kuadrat dari',argumen,'adalah :',total)
    return total # untuk bisa memakai variabel selanjtunya

kuadrat(3)
a = kuadrat(3)
print(a)

a = kuadrat(4)
print(a)
print(kuadrat(4))

print('='*30)

# fungsi dengan return value dan multiple argumen
def tambah(argumen1,argument2):
    total = argumen1 + argument2
    print(argumen1,"+",argument2,"=",total)
    return total

def kali(argumen1,argument2):
    total = argumen1 * argument2
    print(argumen1,"x",argument2,"=",total)
    return total

a = tambah(3,4)
b = kali(3,a)
b = kali(3,tambah(3,4))
print(a)
print(b)


