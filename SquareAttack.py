from binascii import unhexlify
from itertools import product

from utils.AES import *

class Square_attack:

    def __init__(self,CT_256):
        self.ct = [[c for c in unhexlify(x)] for x in CT_256]

    backup = lambda self, ct, byteGuess, byteIndex: invsbox[ct[byteIndex] ^ byteGuess]

    def Reverse_key(self):
        candidates = [self.Itgr(i) for i in range(16)]
        for roundKey in product(*candidates):
            masterKey = self.Round2Key(roundKey)
            plain = ''.join(chr(c) for c in Decrypt(self.ct[1], masterKey))
            if '\0\0\0\0' in plain:
                return bytes(masterKey)

    def Itgr(self,index):
        if len(self.ct) != 256:
            return 'Invalid len of ciphertexts (!= 256)'
        possible = []
        for candidateByte in range(256):
            sum = 0
            for ciph in self.ct:
                oneRoundDecr = self.backup(ciph, candidateByte, index)
                sum ^= oneRoundDecr
            if sum == 0:
                possible.append(candidateByte)
        return possible

    def Round2Key(self,rk):
        Nr,Nk,Nb=(4,4,4)
        w = [[0,0,0,0] for i in range(Nb*(Nr+1))]
            
        for i in range(Nk):
            w[i] = [rk[4*i],rk[4*i+1], rk[4*i+2], rk[4*i+3]]

        for j in range(Nk,Nb*(Nr+1)):
            if (j%Nk) == 0:
                w[j][0] = w[j-Nk][0] ^ sbox[w[j-1][1] ^ w[j-2][1]] ^ rcon[Nr - j//Nk][0]
                for i in range(1,4):
                    w[j][i] = w[j-Nk][i] ^ sbox[w[j-1][(i+1) % 4] ^ w[j-2][(i+1) % 4]]
            else:
                w[j] = XorW(w[j-Nk], w[j-Nk-1])
                
        return sum(w[16:], [])