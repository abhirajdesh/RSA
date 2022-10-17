# importing from the libraries
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# create files
def CreateFile(info,FileName,mode):
    f = open(FileName,mode)
    f.write(info)
    f.close()

# read and retrieve data from files
def ReadFile(FileName,mode):
    f = open(FileName,mode)
    data = f.read()
    f.close()
    return data

message = b'-----//The secret is inside the Box//-----'

key = RSA.generate(2084)
public_key = key.publickey()
public_KeyPEM = public_key.exportKey()
private_KeyPEM = key.exportKey()

# Keys Creation
print('Keys Creation ...')
CreateFile(public_KeyPEM, "public_Key.pem", "wb")
CreateFile(private_KeyPEM, "private_key.pem", "wb")

# Using folder to import private and public keys
imported_publicKey = RSA.import_key(ReadFile("public_Key.pem",'r'))
imported_privateKey = RSA.import_key(ReadFile("private_key.pem",'r'))

# Using the public key to encrypt the data
print('Encrypt the Data')
encrypt_cipher = PKCS1_OAEP.new(imported_publicKey)
encrypted = encrypt_cipher.encrypt(message)

# Writing encryption result to a file
print("Creating ciphertext and saving it to a file ...")
CreateFile(encrypted, "encryptedMessage.txt", "wb")

# Decrypting the encrypted message by importing it
encryptedMessage = ReadFile("encryptedMessage.txt", 'rb')

# Using a private key to decrypt
print("File Description ...")
decrypt_cipher = PKCS1_OAEP.new(imported_privateKey)
decrypted = decrypt_cipher.decrypt(encryptedMessage)
print('Decrypted Message: \n \t', decrypted.decode('utf_8'))