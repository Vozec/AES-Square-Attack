from utils.constants import sbox,rcon

def rowsToCols(state):
   return [[state[x][y] for x in range(4)] for y in range(4)]
    
def KeyExpansion(key):
    Nk,Nb,Nr = (4,4,4)    
    w=[[0,0,0,0] for i in range(Nb*(Nr+1))]
    
    for i in range(0,Nk):
        w[i] = [
                key[4*i],
                key[4*i+1],
                key[4*i+2],
                key[4*i+3]
            ]

    tp = [0,0,0,0]
    for i in range(Nk,Nb*(Nr+1)):
        tp = w[i-1]
        if (i % Nk) == 0:
            tp = XorW(SubW(RotW(tp)), rcon[i//Nk-1])
        w[i] = XorW(w[i-Nk], tp)

    return w

def AddRoundKey(s,ks,r):
    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j] = s[i][j] ^ ks[r*4+i][j]
    return s
    
def RotW(w):
    return [w[1],w[2],w[3],w[0]]

def SubW(w):
    return [sbox[w[0]],sbox[w[1]],sbox[w[2]],sbox[w[3]]]

def XorW(w1, w2):
    return [w1[i] ^ w2[i] for i in range(len(w1))]

def Gmult(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256
