# Episode operator bitwise, operasi biner, binary
# contoh
# untuk -> 2 -> 00000010 = 7,6,5,4,3,2,1,0 karna 2^1 = 2
# untuk -> 9 -> 00001001 = 7,6,5,4,3,2,1,0 karna 2^3 + 2^0 = 9

a = 9
b = 5

# bitwise OR (|)
c = a | b 
print(10*"=","[ OR ]",10*"=")
print('Nilai :',a,', binary :', format(a,'08b'))
print('Nilai :',b,', binary :', format(b,'08b'))
print(30*"-", "[ | ]")
print('Nilai :',c,', binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b 
print(10*"=","[ AND ]",10*"=")
print('Nilai :',a,', binary :', format(a,'08b'))
print('Nilai :',b,', binary :', format(b,'08b'))
print(30*"-", "[ & ]")
print('Nilai :',c,', binary :',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b 
print(10*"=","[ XOR ]",10*"=")
print('Nilai :',a,', binary :', format(a,'08b'))
print('Nilai :',b,', binary :', format(b,'08b'))
print(30*"-", "[ ^ ]")
print('Nilai :',c,', binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a  
print(10*"=","[ NOT ]",10*"=")
print('Nilai :',a,', binary :', format(a,'08b'))
print(30*"-", "[ ~ ]")
print('Nilai :',c,', binary :',format(c,'08b'))
d =0b0000001001
e =0b1111111111
print('Nilai :',e^d,' , binary :',format(e^d,'08b'))

# Shifting

# Shift right (>>)
c = a >> 2
print(30*"=")
print('Nilai :',a,', binary :',format(a,'08b'))
print(30*"=","[>>]")
print('Nilai :',c,', binary :',format(c,'08b'))


# Shift left (<<)
c = a << 2
print(30*"=")
print('Nilai :',a,', binary :',format(a,'08b'))
print(30*"=","[<<]")
print('Nilai :',c,', binary :',format(c,'08b'))
