import hashlib
from ctypes import CDLL

#The following five lists contain the ciphertext unicode values

# cipone contains unicode values of character at 1,6,11,16... 121 place and has 25 characters.
cipone=[5, 39, 41, 35, 35, 42, 43, 35, 53, 54, 39, 63, 39, 46, 40, 52, 46, 33, 25, 25, 35, 22, 8, 63, 59]
# ciptwo contains unicode values of character at 2,7,12,17... 117 place and has 24 characters.
ciptwo=[24, 3, 2, 36, 4, 27, 7, 19, 36, 3, 25, 7, 4, 22, 16, 18, 18, 12, 31, 53, 57, 50, 48, 40]
# cipthree contains unicode values of character at 3,8,13...118 place and has 24 characters.
cipthree=[28, 1, 58, 7, 1, 11, 30, 38, 17, 27, 22, 6, 23, 30, 23, 59, 52, 11, 51, 0, 45, 19, 45, 42]
# cipfour contains unicode values of character at 4,9,14...119 place and has 24 characters.
cipfour=[38, 96, 32, 34, 39, 2, 36, 41, 51, 47, 2, 46, 37, 45, 9, 50, 45, 14, 55, 14, 19, 21, 10, 14]
# cipfive contains unicode values of character at 5,10,15... 120 place and has 24 characters.
cipfive=[56, 19, 60, 41, 63, 37, 62, 35, 35, 45, 56, 8, 9, 47, 47, 30, 43, 63, 15, 33, 47, 35, 15, 24]
#All in all there are (25+24+24+24+24) 121 characters in the ciphertext.

br=0

#The following loops iterate through key values (aa-ab-ac-ad-ae) AAAAA to zzzzz and convert ciphertext to plaintext using xor (self-inverse).

#If statements are used to break the xor-ing loop and iterate to the next key value if an unprntable character is generated.

#First if statement (if br==1:) is there to break the loop if answer and key have been generated.

#Second if statement (if x>=33 and x<=126:) is used to break the loop generating the plaintext if a wrong chracter(unprintable or otherwise) is generated
for aa in range(65,91)+ range(97,123):
    if br==1:
        break
    loopone=0
    plaone=""
    for i in cipone:
        x=aa^i
        if x>=33 and x<=126:
            plaone+=chr(x)
        else:
            plaone=""
            loopone=1
            break
    if loopone!=1:
        for ab in range(65,91)+range(97,123):
            if br==1:
                break
            looptwo=0
            platwo=""
            for j in ciptwo:
                x=ab^j
                if x>=33 and x<=126:
                    platwo+=chr(x)
                else:
                    platwo=""
                    looptwo=1
                    break
            if looptwo!=1:
                for ac in range(65,91)+range(97,123):
                    if br==1:
                        break
                    loopthree=0
                    plathree=""
                    for k in cipthree:
                        x=ac^k
                        if x>=33 and x<=126:
                            plathree+=chr(x)
                        else:
                            plathree=""
                            loopthree=1
                            break
                    if loopthree!=1:
                        for ad in range(65,91)+range(97,123):
                            if br==1:
                                break
                            loopfour=0
                            plafour=""
                            for l in cipfour:
                                x=ad^l
                                if x>=33 and x<=126:
                                    plafour+=chr(x)
                                else:
                                    plafour=""
                                    loopfour=1
                                    break
                            if loopfour!=1:
                                for ae in range(65,91)+range(97,123):
                                    if br==1:
                                        break
                                    loopfive=0
                                    plafive=""
                                    for m in cipfive:
                                        x=ae^m
                                        if x>=33 and x<=126:
                                            plafive+=chr(x)
                                        else:
                                            plafive=""
                                            loopfive=1
                                            break
                                    if loopfive!=1:
                                        plaintext=""
                                        aaa=chr(aa)
                                        aab=chr(ab)
                                        aac=chr(ac)
                                        aad=chr(ad)
                                        aae=chr(ae)
                                        value=aaa+aab+aac+aad+aae
                                        print value
                                        for a in range(0,24):
                                            plaintext+=plaone[a]+platwo[a]+plathree[a]+plafour[a]+plafive[a]
                                        plaintext=plaintext+plaone[24]
                                        flag="{"+plaintext+"}"
                                        if hashlib.md5(flag).digest().encode("hex") == "d444d1ac3799a86d31f34b4a8a3243c6":
                                            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                                            print "Yeah!....You are a genius!"
                                            print ""
                                            ans=value
                                            fin=flag
                                            br=1
print ans
print ""
print fin
