import rsa

public_key_path = 'private.pem'
file_path = 'hc.txt.enc'

# def encrypt_file_rsa(file_path, public_key_path):
#     # Load the public key
#     with open(public_key_path, 'rb') as f:
#         public_key = rsa.PublicKey.load_pkcs1(f.read())

#     # Open the file to be encrypted in binary mode
#     with open(file_path, 'rb') as f:
#         # Read the file contents
#         file_contents = f.read()

#     # Encrypt the data using the public key
#     encrypted_data = rsa.encrypt(file_contents, public_key)

#     # Open the encrypted file in binary mode
#     with open(file_path + '.enc', 'wb') as f:
#         # Write the encrypted data
#         f.write(encrypted_data)

def decrypt_file_rsa(file_path, private_key_path):
    # Load the private key
    with open(private_key_path, 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    # Open the encrypted file in binary mode
    with open(file_path, 'rb') as f:
        # Read the encrypted data
        encrypted_data = f.read()

    # Decrypt the data using the private key
    decrypted_data = rsa.decrypt(encrypted_data, private_key)

    # Open the decrypted file in binary mode
    with open(file_path.replace(".enc",""), 'wb') as f:
        # Write the decrypted data
        f.write(decrypted_data)

decrypt_file_rsa("hc.txt.enc","private.pem")