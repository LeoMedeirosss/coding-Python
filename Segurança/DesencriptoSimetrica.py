from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def descriptografar(iv, texto_cifrado, tag, key):
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()
    
    texto_decifrado = decryptor.update(texto_cifrado) + decryptor.finalize()
    
    return texto_decifrado.decode()
    
key = b'\xf1\xe1\x04\x10}m\x03\x94\xae\xe1\x1d\xfaGl^.wm\x93\xff&\n{G\xd3\x08\xd2\xfe\x84\xe8\xf8\xe4'  # Substituir pela key real utilizada
iv = b'\xc41S\x8d\x1aXC\x0c\xeebI\xbf'   # Substituir pelo IV real gerado
texto_cifrado = b':,\x19\xb2f\xcf>\xe3\xa4@\x8dZ'  # Substituir pelo texto cifrado real gerado
tag = b'd\x93\x0e\x86\xda\xc6\x0e@\xec\x9bmpL\xb6uG'  # Substituir pela tag real gerada

texto_decifrado = descriptografar(iv, texto_cifrado, tag, key)
    
print("Texto decifrado:", texto_decifrado)