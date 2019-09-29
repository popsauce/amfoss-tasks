# :rainbow:Advanced:fog::fog::fog:Xor  :sunrise:

> Looks attractive and doable for a hard task.Then the waters get rough.

## Understanding Advanced Xor

There is a script (advanced_xor.py) that encrypts plaintext provided as an input using a key generated using urandom and gives the ciphertext as output. A ciphertext with 242 characters has been provided that has been encrypted using the given script. Another script check_hash.py has been provided to check if an answer is generated.
'''
from os import urandom
from ctypes import CDLL
import string

key = ""
ciphertext = ""
def get_key():
    global key
    c = urandom(1)
    if len(key)!=5:
        if c not in string.ascii_lowercase and c not in string.ascii_uppercase :
            get_key()
        else:
            key += c
            get_key()
    
def xor_encrypt(x):
    global key
    global ciphertext
    get_key()
    
    hex_key = key.encode("hex")
    key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]
    print key
    for i in xrange(len(x)):
        ciphertext += chr(ord(x[i]) ^ int(key_list[i%5], 16))

    
if __name__ == "__main__":
    plaintext = raw_input("Enter the plaintext to be encrypted: ")
    xor_encrypt(plaintext)
    print ciphertext.encode("hex")
'''

### Encoding Script (advanced_xor.py)

## Tackling Advanced Xor
