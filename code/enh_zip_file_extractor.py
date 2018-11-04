######################################
# Use the except Exception exception handler to catch exceptions and print them out when an incorrect password
# is used. Execute your script with an incorrect password and exception handler
# this is enhanced version of the zip_file_extractor, with an added feature of exception handling
######################################

# import libraries used
import zipfile


# zipfile extractor with exception
def __zipfile_ext_ex__():
    zf = open('evil.zip','r')
    # set password
    passwd='secret2'
    #instantiate a new ZipFile class
    zc=zipfile.ZipFile(zf)
    # enclose zip extractor in a try-exception block to check for  bad pwds or any other runtime error
    try:
        # use extractall method using the given password
        zc.extractall(pwd=passwd)
        zc.printdir()
    except Exception as e:
        # store the exception error as e and print it. This can be used for any type of run time exceptions for this block
        print("Exception :" + str(e))
        
