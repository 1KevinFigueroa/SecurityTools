######################################################################################
#   Name:    ftp_AnonymousTester_v0.3.py
#   Author:  Kevin Figueroa
#   License: BSD
#   Purpose: Test Anonymous FTP login with 
#               username: anonoymous 
#               password: <blank>
#            
#            If login successful, display connection steps, FTP banner grab, and 
#            retreive FTP root directory listing.
#
#   
#   Copyright (c) 2017, Kevin Figueroa
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this
#      list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#   ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#   The views and conclusions contained in the software and documentation are those
#   of the authors and should not be interpreted as representing official policies,
#   either expressed or implied, of the FreeBSD Project.
########################################################################################

#!/usr/bin/env python

import os, sys
import socket
import ftplib


# Attempt socket banner grab

def soc_banner():

    # Perform port banner grab
    ftp_port = int(21)
    ftpsoc = socket.socket()
    ftpsoc.connect((ftpname,ftp_port))
    ftp_banner = ftpsoc.recv(2048)


def main():
    global ftpname

    # Username and password used for Anonymous FTP login
    username = ("anonymous")
    password = (" ")

    # Connect to FTP server
    ftp =  ftplib.FTP(ftpname)

    # Display connection information and login attempt
    ftp.set_debuglevel(2)
    ftp.connect()
    ftp.login(username, password)

    # Perform port banner grab
    ftp_port = int(21)
    ftpsoc = socket.socket()
    ftpsoc.connect((ftpname,ftp_port))
    ftp_banner = ftpsoc.recv(2048)


    # If successful, connect and display directory listing
    print ("Connected to FTP server...")
    ftp.dir()

    # Append information to List
    dl = []
    dirList = ftp.dir(dl.append)
    print (dirList)

    # Terminate and close connection
    ftp.quit()
    ftp.close()

    # Return FTP login directory listing
    print ("---------------")
    print ("\nFTP BANNER:\n")
    print (ftp_banner)
    print ("---------------")
    print ("\nFTP LOGIN DIRECTORY LIST:\n")
    for row in dl:
        print(row)
    print ('------------')


if __name__ == '__main__':
    print('\n')
    # User selects Anonymous FTP Server
    ftpname = input("Select Anonymous FTP Server: ")
    soc_banner()
    main()


#END
