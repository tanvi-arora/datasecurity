from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources
from PIL import Image
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long

def encrypt(filename):
    # substitute below value with a secret key
    key=b'This is a key123'
    IV = os.urandom(16)
    
    chunksize = 128
    filesize = os.path.getsize(filename)
    #size of the putput imges
    width = 1024
    height = 1024
        

    
    print("ready to encrypt")
    
    #CBC mode
    #create encryptor objects for all 3 modes
    encryptor_CBC = AES.new(key, AES.MODE_CBC, IV)
    #"initialize blocks for encrypted code"
    blocks_cbc = []
    #open source image file as a data file and encrypt it in chunks
    with open(filename, 'rb') as infile:

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                elif len(chunk) % 128 !=0:
                    #pad data with ' ' if length is not a chunk of 128
                    chunk += bytes(' ',encoding = 'ascii') * (128 - (len(chunk) % 128))
                    
                blocks_cbc.append(encryptor_CBC.encrypt(chunk))
            cipher_data_cbc= b''.join(blocks_cbc)
            
    img_cbc = Image.frombytes("RGB",(width,height), cipher_data_cbc )
    img_cbc.save('~/images/image_cbc.jpg')
    
    #ECB mode
    #create encryptor objects for all 3 modes
    encryptor_ECB = AES.new(key, AES.MODE_ECB)
    #"initialize blocks for encrypted code"
    blocks_ecb = []
    #open source image file as a data file and encrypt it in chunks
    with open(filename, 'rb') as infile:

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                elif len(chunk) % 128 !=0:
                    #pad data with ' ' if length is not a chunk of 128
                    chunk += bytes(' ',encoding = 'ascii') * (128 - (len(chunk) % 128))
                blocks_ecb.append(encryptor_ECB.encrypt(chunk))   
            cipher_data_ecb= b''.join(blocks_ecb)    
    img_ecb = Image.frombytes("RGB",(width,height), cipher_data_ecb )
    img_ecb.save('~/images/image_ecb.jpg')
    
    #CTR mode
    #ctr = Counter_pycrypto.new(128, initial_value=int(IV, 16))
    #create encryptor objects for all 3 modes
    ctr = Counter.new(128, initial_value = bytes_to_long(IV))
    encryptor_CTR = AES.new(key, AES.MODE_CTR, counter = ctr)
    #"initialize blocks for encrypted code"
    blocks_ctr = []
    #open source image file as a data file and encrypt it in chunks
    with open(filename, 'rb') as infile:

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                elif len(chunk) % 128 !=0:
                    #pad data with ' ' if length is not a chunk of 128
                    chunk += bytes(' ',encoding = 'ascii') * (128 - (len(chunk) % 128))
                    
                blocks_ctr.append(encryptor_CTR.encrypt(chunk))
            cipher_data_ctr= b''.join(blocks_ctr)
    

    img_ctr = Image.frombytes("RGB",(width,height), cipher_data_ctr )
    img_ctr.save('~/images/image_ctr.jpg')   
    
   


