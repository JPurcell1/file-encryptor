from cryptography.fernet import Fernet

#Generates an encryption key
key = Fernet.generate_key()
f = Fernet(key)

#save encryption key to a file
with open("key_file.key", "wb") as file:
  file.write(key)

#read key from file
with open("key_file.key", "rb") as file:
  my_key = file.read() 

#Encrypting the file
def encrypt_file(input, output, key):
  with open(input, "rb") as file:
    data = file.read() #string of info read from file
 
  encrypted_data = f.encrypt(data)

  with open(output, "wb") as file:
    file.write(encrypted_data)
  
  print(f'{input} file has been encrypted')

#Decrypting the previously encrypted file
def decrypt_file(input, output, key):
  with open(input, "rb") as file:
    encrypted_data = file.read() 

  decrypted_data = f.decrypt(encrypted_data)

  with open(output, "wb") as file:
    file.write(decrypted_data)
  
  print(f'{input} file has been decrypted')

original_file = "plain_text.txt"
enc_file = "encrypted.txt"
dec_file = "decrypted.txt"

encrypt_file(original_file, enc_file, key)
decrypt_file(enc_file, dec_file, key)