from utils.AES_utils     import *
from utils.AES_rev_utils import *

def oneRoundDecrypt(s, ks, r):
    return InvSubBytes(InvShiftrows(InvMixColumns(AddRoundKey(s,ks,r))))
    
def finalRoundDecrypt(s, ks, r):
    return InvSubBytes(InvShiftrows(AddRoundKey(s,ks,r)))

def Decrypt(message, key):
    ks = KeyExpansion(key)
    x = finalRoundDecrypt([
            message[:4],
            message[4:8],
            message[8:12],
            message[12:16]
        ], ks, 4)
    x = oneRoundDecrypt(x, ks, 3)
    x = oneRoundDecrypt(x, ks, 2)
    x = oneRoundDecrypt(x, ks, 1)
    x = AddRoundKey(x,ks,0)
    return sum(x, [])