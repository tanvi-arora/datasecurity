#################################
# create a simple Python-based port scanner. Using the socket library, you will create a script that iterates through a
# IP addresses, and will identify the active ports available for that IP address. At least ports
# corresponding to telnet, ftp SSH, smtp, http, imap, and https services should be scanned and identified
#################################



# import libraries

import socket
import sys

# enter inputs
remoteserverip = "X.X.X.X"

print"Testing ports 20-FTP ,21-FTP ,22-SSH ,23-Telnet,25-SMTP,80-HTTP,143-IMAP,443-HTTPS,587-Secure SMTP, 1433 - MSSQL "
print"Please wait..."

# handle exceptions
try:
    for testport in [20,21,22,23,25,80,143,443,587,1433]:
        # instantiate socket class : address format is host and port number
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteserverip,testport))
        if result==0:
            print"Port  {} is open".format(testport)
        sock.close()
        
except socket.error:
        print "Could not connect to remote server"
        sys.exit()

print("Test completed")



