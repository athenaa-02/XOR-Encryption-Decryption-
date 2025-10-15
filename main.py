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