from utils.constants import sbox
from utils.AES_utils import *

invsbox = [sbox.index(i) for i in range(256)]

def InvSubBytes(state):
    state = [list(c) for c in state]
    for i in range(len(state)):
        row = state[i]
        for j in range(len(row)):
            state[i][j] = invsbox[state[i][j]]
    return state

def colsToRows(state):
    return [
        [state[0][0], state[1][0], state[2][0], state[3][0]],
        [state[0][1], state[1][1], state[2][1], state[3][1]],
        [state[0][2], state[1][2], state[2][2], state[3][2]],
        [state[0][3], state[1][3], state[2][3], state[3][3]]
    ]    
   
def InvShiftrows(state):
    state = colsToRows(state)
    state[1].insert(0,state[1].pop())    
    state[2].insert(0,state[2].pop())
    state[2].insert(0,state[2].pop())    
    state[3].insert(0,state[3].pop())
    state[3].insert(0,state[3].pop())
    state[3].insert(0,state[3].pop())    
    return rowsToCols(state)  

def InvMixColumns(cols):
    def InvmixColumn(column):
        temp = [column[i] for i in range(len(column))]
        column[0] = Gmult(temp[0],0xE) ^ Gmult(temp[3],0x9) ^ Gmult(temp[2],0xD) ^ Gmult(temp[1],0xB)
        column[1] = Gmult(temp[1],0xE) ^ Gmult(temp[0],0x9) ^ Gmult(temp[3],0xD) ^ Gmult(temp[2],0xB)
        column[2] = Gmult(temp[2],0xE) ^ Gmult(temp[1],0x9) ^ Gmult(temp[0],0xD) ^ Gmult(temp[3],0xB)
        column[3] = Gmult(temp[3],0xE) ^ Gmult(temp[2],0x9) ^ Gmult(temp[1],0xD) ^ Gmult(temp[0],0xB)    
        return column
    r = [0,0,0,0]
    for i in range(len(cols)):
        r[i] = InvmixColumn(cols[i])
    return r

