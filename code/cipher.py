 
    
def caesar_dec():
    print("inside decipher")
    #ask for user input
    ciphertext = input("Enter sentence to dencrypt")
    
    #since we have 26 letters run a loop for bruteforce logic to check for shift values from 0-25
    for shift in range(0,25):
        print("shift value is ",shift)
        str_dec = ''
        # decode each letter of the input
        for x in ciphertext:
            #get ascii value of the alphabet
            asc = ord(x)
            #if the ascii value is a letter in uppercase, get encoded value that is ascii-shift value, circle back to 'Z' after 'A'
            if (asc >= 65 and asc <= 90):
                str_dec = str_dec + chr((asc-65 - shift)%26 + 65)
            #if the ascii value is a letter in lowercase, get encoded value that is ascii-shift value, circle back to 'Z' after 'a'
            elif (asc >=97 and asc <= 122):
                str_dec = str_dec + chr((asc-97 - shift)%26 + 97)
            #for any letter other than alphabet, keep it as is
            else:
                str_dec = str_dec + x    
        print("The decoded phrase is : ",str_dec)
       
    
def caesar_en():
    
    print("inside cipher")
    #ask for user input
    plaintext = input("Enter sentence to encrypt")
    shift = int(input("Enter shift value"))
        
    str_enc = ''
    # encode each letter of the input
    for x in plaintext:
            #get ascii value of the alphabet
            asc = ord(x)
            #if the ascii value is a letter in uppercase, get encoded value that is ascii+shift value, circle back to 'A' after 'Z'
            if (asc >= 65 and asc <= 90):
                str_enc = str_enc + chr((asc-65 + shift)%26 + 65)
            #if the ascii value is a letter in lowercase, get encoded value that is ascii+shift value, circle back to 'a' after 'z'
            elif (asc >=97 and asc <= 122):
                str_enc = str_enc + chr((asc-97 + shift)%26 + 97)
            #for any letter other than alphabet, keep it as is
            else:
                str_enc = str_enc + x
    
    print("The encoded phrase is : " , str_enc)
    

def caesar_en1():
    
    print("inside cipher")
    #ask for user input
    plaintext = input("Enter sentence to encrypt")
    shift = int(input("Enter shift value"))
        
    str_enc = ''
    # encode each letter of the input
    for x in plaintext:
            #get ascii value of the alphabet
            asc = ord(x)
            #if the ascii value is a letter in uppercase, get encoded value that is ascii+shift value, circle back to 'A' after 'Z'
            if (asc >= 65 and asc <= 90):
                str_enc = str_enc + 'X'
            #if the ascii value is a letter in lowercase, get encoded value that is ascii+shift value, circle back to 'a' after 'z'
            elif (asc >=97 and asc <= 122):
                str_enc = str_enc + 'x'
            #for any letter other than alphabet, keep it as is
            else:
                str_enc = str_enc + x
    
    print("The encoded phrase is : " , str_enc)
    
    
 
    
