import os
from os.path import exists
import rsa


class EncryptionManager:
    def __init__(self, current_dir):
        # Check if keys exist, if not create them
        if not exists(current_dir+'/keys/public.txt') or not exists(current_dir+'/keys/private.txt'):
            print("Generating new RSA keys")
            pub_key, pri_key = rsa.newkeys(512)
            pub_file = open(current_dir + '/keys/public.txt', 'w')
            pub_file.write(pub_key.save_pkcs1().decode('utf8'))
            pub_file.close()
            pri_file = open(current_dir + '/keys/private.txt', 'w')
            pri_file.write(pri_key.save_pkcs1().decode('utf8'))
            pri_file.close()
        # Load keys from respective files
        print("Loading RSA keys")
        public_key_file = open(current_dir + '/keys/public.txt', 'r')
        public_key_data = public_key_file.read()
        self.public_key = rsa.PublicKey.load_pkcs1(public_key_data, 'PEM')
        private_key_file = open(current_dir + '/keys/private.txt', 'r')
        private_key_data = private_key_file.read()
        self.private_key = rsa.PrivateKey.load_pkcs1(private_key_data, 'PEM')


