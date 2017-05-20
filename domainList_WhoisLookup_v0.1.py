######################################################################################
#   Name:    verifyDomains.py
#   Author:  Kevin Figueroa
#   License: BSD
#   Purpose: Displays directory and file tree structure selected by user. User may 
#             also select optional flags to display details about each file or directory
#         listed.
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


import os, sys, time
import csv
import whois

# user select name of CSV output file
outputFile = raw_input("Enter CSV file name for output: ")
wof = open(outputFile + '.csv', 'a')
wf = csv.writer(wof, delimiter=',')


# user select file to import
importFile = raw_input("Select import file: ")
with open(importFile, 'r') as rf:
    readinput = csv.reader(rf, delimiter=',')


# iterates through the select CSV file, identify url in column 1
    for col in readinput:

        try:
            rdn = whois.whois(col[0])    # retrieve WHOIS information
            ndn = rdn.domain             # domain select
            ordn = rdn.country           # country domain resides
            cidn = rdn.city              # city domain resides
            cdn = rdn.creation_date      # creation date of domain
            exdn = rdn.expiration_date   # expiration date of domain
            ldn = rdn.updated_date       # last update to domain
            try:
                wf.writerow([ndn,ordn,cidn,cdn,exdn,ldn]) # attempt to write retreive WHOIS information
            except (UnicodeEncodeError):                  # if "UnicodeEncodeError" is encounter
                continue                                  # skip and continue through list

            print ndn
            print ordn
            print cidn
            print cdn
            print exdn
            print ldn

        except (whois.parser.PywhoisError):                  # "PywhoisError" may be encounter because
            print("Domain is not register or non-existint")  # domain is not register or non-existent
            print(col)
            wf.writerow(['Non-existint: %s' % col])          # mark non-existent domains

#END
