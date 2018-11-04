###########################################
# Write a quick script to test the use of the zipfile library. After importing the library, instantiate a new ZipFile class by
# specifying the filename of the password-protected zip file (evil.zip). utilize the extractall( ) method and specify
# the optional parameter for the password (secret)
# use any other zip file by replacing file name for object zf and password for object passwd
###########################################

# import libraries used
import zipfile

# zipfile extractor
def __zipfile_ext__():
    #open zip file
    zf = open('evil.zip','r')
    #define password for the zipfile
    passwd='secret'
    #instantiate a new ZipFile class
    zc=zipfile.ZipFile(zf)
    # use extractall method using the given password
    zc.extractall(pwd=passwd)
    zc.printdir()
    
