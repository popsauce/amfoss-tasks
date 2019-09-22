#using urandom instead of normal hit and try
#still have to stop repetition of an already generated key

from os import urandom
from ctypes import CDLL
import string
import hashlib

key = ""
plaintext = ""
keys=[]
rkey_list=[]

def get_key():
    global key
    c = urandom(1)
    if len(key)!=5:
        if c not in string.ascii_lowercase and c not in string.ascii_uppercase :
            get_key()
        else:
            key += c
            get_key()
    for i in rkey_list:
        if rkey_list[i] == key:
            key = ""
            get_key()
        else:
            rkey_list.append(key)    

def xor_decrypt(x):
    global key
    global plaintext
    get_key()
    
    hex_key = key.encode("hex")
    key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]
    print""
    print""
    print key
    print""
    print""
    for i in xrange(len(x)):
        plaintext += chr(ord(x[i]) ^ int(key_list[i%5], 16))
    flag="{"+plaintext+"}"
    if hashlib.md5(flag).digest().encode("hex") == "d444d1ac3799a86d31f34b4a8a3243c6":
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "Yeah!....You are a genius!"
        print "______________________________________________________________"
        print plaintext
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    else:
        xor_decrypt(ciphertext)

if __name__ == "__main__":
    a = raw_input("Enter the ciphertext to be decrypted: ")
    ciphertext = a.decode("hex")
    xor_decrypt(ciphertext)
