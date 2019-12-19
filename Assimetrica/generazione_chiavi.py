from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#Generazione Chiavi
chiave_privata = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
chiave_pubblica = chiave_privata.public_key()

# salva chiave privata/pubblica
from cryptography.hazmat.primitives import serialization
pem = chiave_privata.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
with open('chiave_privata.pem', 'wb') as f:
    f.write(pem)

pem = chiave_pubblica.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
with open('chiave_pubblica.pem', 'wb') as f:
    f.write(pem)

