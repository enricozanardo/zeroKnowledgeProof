from cryptography.fernet import Fernet
key = b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0=' # usare stessa chiave per decriptare
input_file = 'test.txt'
output_file = 'test-criptato.txt'

with open(input_file, 'rb') as f:
    data = f.read()


fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)
