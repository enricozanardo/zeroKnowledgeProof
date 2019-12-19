from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# lettura chiave privata
with open("chiave_privata.pem", "rb") as key_file:
    chiave_privata = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend())

# lettura contenuto file di testo criptato
f = open('test_criptato.txt', 'rb')
messaggio_originale = f.read()
print(messaggio_originale)

# deriptazione contenuto file di testo
decripta = chiave_privata.decrypt(
        messaggio_originale,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))

f = open('test_decriptato.txt', 'wb')
messaggio_originale = f.write(decripta)
print(decripta)
f.close()


















