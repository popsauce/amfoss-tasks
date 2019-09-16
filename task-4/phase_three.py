#the only way to lessen processing time was to reduce the number of possible combinations
#ran the following script 5 times to show me the probable 1,6,11,.. and 2,7,12,.. and 3,8,13,.. and 4,9,14,.. and 5,10,15,.. placed characters if x (a-z&&A-Z) was the key
a=raw_input()
a=a.decode("hex")

for i in range(65,91) + range(97, 123):
    c=chr(i)
    print c
    plain=""
    for j in range(0,125,5):
        plain += chr(ord(a[j]) ^ i)
    print ""
    print plain
    print ""




# Manual Hit And Try Method, Sequences for checking readable characters that make up a meaningful string
# Sequence 1 consists of characters at 0, 6, 11, ... 120  place in the probable plaintext
# Similiarly sequence 2 consists of characters at 1, 7, 12, ... 116  place in the probable plaintext
    """
    for sequence 1;start with 0, end with 125
    for sequence 2;start with 1, end with 121
    for sequence 3;start with 2, end with 122
    for sequence 4;start with 3, end with 123
    for sequence 5;start with 4, end with 124
    
    for sequence 1;start with 5, end with 125;; excluding 1 character
    for sequence 2;start with 6, end with 121;; excluding 1 character
    for sequence 3;start with 7, end with 122;; excluding 1 character
    for sequence 4;start with 8, end with 123;; excluding 1 character
    for sequence 5;start with 9, end with 124;; excluding 1 character
    
    for sequence 1;start with 10, end with 125;; excluding 2 characters
    for sequence 1;start with 11, end with 121;; excluding 2 characters
    for sequence 1;start with 12, end with 122;; excluding 2 characters
    for sequence 1;start with 13, end with 123;; excluding 2 characters
    for sequence 1;start with 14, end with 124;; excluding 2 characters
    """
