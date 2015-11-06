import hashlib
import binascii

value = 0
while (value <= 9999):
    tested = '0000'+str(value)
    tested = (tested)[len(tested)-4:]
    m = hashlib.sha1()
    m.update(bytes(("It"+tested).encode()))
    hexa = m.hexdigest();
    if(hexa == '6D209CE47FEC653F2947F0E3D09580130C05C3CC'.lower()):
        print ('Found Value!: ', value)
        print('Hash: ', hexa)
        break
    del m
    value +=1


#https://docs.python.org/2/library/hashlib.html
