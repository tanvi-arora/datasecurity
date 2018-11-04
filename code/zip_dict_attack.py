#############################################
# performs a dictionary attack on the password protected zip file.
# outputs each password tried incorrectly and stops at the correct password .Also displays contents of the zip file once sucessfully retrieved
# zip file used can be relaced for object 'zf' and password dictionary for object 'pwdf'
#############################################

# import libraries used
import zipfile


# zipfile extractor with exception
def __zipfile_dic_attk__():
    # zip file
    zf = open('evil.zip','r')
    # password dictionary
    pwdf = open('HW3dictionary.txt','r')
   
    #instantiate a new ZipFile class
    zc=zipfile.ZipFile(zf)
    
    # to perform dictionary attack, try each password from the password dictionary on the zip file
    for passwd in pwdf:
        passwd=passwd.strip()
        # enclose zip extractor in a try-exception block to check for  bad pwds or any other runtime error
        try:
            print("trying password : " + passwd )
            # use extractall method using the given password
            zc.extractall(pwd=passwd)
            print(passwd + "is the correct password")
            zc.printdir()
            break
        except Exception as e:
            # store the exception error as e and print it. This can be used for any type of run time exceptions for this block
            print("Exception :" + str(e))
     
        
