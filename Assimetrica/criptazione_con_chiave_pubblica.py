from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# lettura chiave pubblica
with open("chiave_pubblica.pem", "rb") as key_file:
    chiave_pubblica = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend())

# lettura contenuto file di testo
f = open('test.txt', 'rb')
messaggio = f.read()
print(messaggio)
f.close()

# criptazione contenuto file di testo
cripta = chiave_pubblica.encrypt(
    messaggio,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None))

f = open('test_criptato.txt', 'wb')
messaggio = f.write(cripta)
print(cripta)
f.close()






