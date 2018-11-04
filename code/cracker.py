######################################################
# simple file to read a password file , extract encrypted password value, 
# and compare it with a dictionary of passwords in cleartext to get the unecrypted version of the password
# It is assumed salt value is first 2 characters appended to the encrypted password
# for unix systems, import 'crypt' and use crypt.crypt function.
# Below program is written for python2.7 on windows . Install fcrypt seperately 
# output is password in clear text if found in the dictionary or else reports "No password was found"
# to use this script , use your own passwords and dictionary file
# each record in the password file for this program had the format "login : encrypted password : time :....."
######################################################

# import libraries
import fcrypt

# read password file
def read_file():
    f = open('HW3passwords.txt','r')
    for line in f:
        #print line
        ###extract password
        login, pwd, rest = line.split(':',2)
        #print(login)
        pwd=pwd.strip()
        print("password : " + pwd)
        #print(rest)
        hpwd = read_dic(pwd)
        print('\n')
        
print("file complete")


def read_dic(pwd):
    
    ## initialize pwd_match_flag to 0
    pwd_match_flag=0
    ## salt value is first 2 characters of the pwd
    salt=pwd[:2]
    print('salt "' + salt +'"')
    
    ## open dictionary and crypt each password using the salt value
    dic = open('HW3dictionary.txt','r')
    for d in dic:
        
        d=d.strip()
        # using crypt from hcrypt, create an encrypted password valueusing the derived salt value
        hpwd=fcrypt.crypt(d,salt)
        
        # not required to print all passwords
        #print(d," : ",hpwd)
        
        ## compare each derived encrypted password with the pwd to obtain the unencrypted value
        if pwd == hpwd:
            # set pwd_match_flag to 1
            pwd_match_flag=1
            print('pwd matched to "'+ d +'"')
            break
    
    if pwd_match_flag==0:
        print("no password was found")

    

