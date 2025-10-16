import base64

# step 1: caesar cipher decryption
ciphertext = 'mznxpz'
shift = 21


def decrypt_ciphertext(text, shift):
 result = ''
 
 for i in range(len(text)):
    char = text[i]
    
    if char.isupper():
       result += chr((ord(char) - shift - 65) % 26 + 65)
     
    elif char.islower():
       result += chr((ord(char) - shift - 97) % 26 + 97)
     
    else:
       result += char
    
   
 return result
  


decrypted = decrypt_ciphertext(ciphertext, shift)

print('ciphered text:', ciphertext)
print('decrypted text:', decrypted)


# step 2: solve the anagram
# rearranged letters in 'rescue' to form 'secure, a fundamental concept in cryptography
passphrase = 'secure'
print('passphrase:', passphrase)


# step 3: 
base64_ciphertext = 'Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ='

cipher_bytes = base64.b64decode(base64_ciphertext)
key = passphrase.encode('ascii')

# XOR decryption
plaintext = ''
for i in range(len(cipher_bytes)):

    key_byte = key[i % len(key)]
    plaintext_byte = cipher_bytes[i] ^ key_byte
    plaintext += chr(plaintext_byte)

print('XOR decrypted plaintext:', plaintext)
