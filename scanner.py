from bitcoin import *

priv = random_key()
pub = privtopub(priv)
addr = pubtoaddr(pub)
wifKey = encode_privkey(priv, 'wif')

print ('Bitcoin Address: ' + addr)
print ('WIF Key: ' + wifKey)

def check():
    with open('Untitled document.txt') as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if 'Balance' in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding
if check():
    print('True')
    f = open("Key.txt", "a")
    f.write(addr)
    f.close()
else:
    print('False')
