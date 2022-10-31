# AES-Square-Attack
This tool is the implementation of the Square-Attack on an AES-128


An AES-128 reduced to 4 rounds is vulnerable to this attack if the MixColumns operation is forgotten on the last round

*More Informations [here](https://www.researchgate.net/publication/2646816_The_block_cipher_Square)*

# Usage :
- ``main.py``  
```python
from binascii import hexlify
from SquareAttack import *

cts = [b'...']

key = Square_attack(cts).Crack_key()
print(hexlify(key))
```
*(``cts`` is an array with the 256 ciphertexts)*

## Dataset :  

We can create a dataset :  
```python
encrypted_ds = []
	for i in range(256):
		data = bytearray([i,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		encrypted_ds.append(Encrypt_AES(data))
    return encrypted_ds
```

*This tools was inspired by many writings/codes of other people from previous CTF Writeup*
