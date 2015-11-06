import itertools
import hashlib

res = itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=', repeat=6) # 3 is the length of your result.

counter = 0

for case in res:
    if (counter < 8860000000):
        counter += 1
        if (counter%1000000000 == 0):
            print ("counter in: ", counter)
    else:
        case = "NT"+''.join(case)
        m = hashlib.sha1()
        m.update(bytes((case).encode()))
        hexa = m.hexdigest();
        if(hexa == '53425620DAF31B5659A7D96C168C4ED82CAAED13'.lower()):
            print ('Found Value!: ', case)
            print('Hash: ', hexa)
            break
        del m
        counter += 1
        if(counter%10000000 == 0):
            print ("Tested hashes: ",counter," Last password:", case[2:], "last hash:", hexa)
#http://stackoverflow.com/questions/10082094/generate-all-possible-passwords-based-on-character-mapping-possible-in-3-line
