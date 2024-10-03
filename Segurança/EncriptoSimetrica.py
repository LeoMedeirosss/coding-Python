from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def gerar_key():
    return os.urandom(32)

def criptografar(mensagem, key):
    iv = os.urandom(12)
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()
    
    texto_cifrado = encryptor.update(mensagem.encode()) + encryptor.finalize()
    
    return iv, texto_cifrado, encryptor.tag

key = gerar_key() 
mensagem = "CESAR School" 
    
iv, texto_cifrado, tag = criptografar(mensagem, key)

print("key:",key)
print("Texto cifrado:", texto_cifrado)
print("IV:", iv)
print("Tag:", tag)