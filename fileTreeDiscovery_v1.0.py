######################################################################################
#   Name:    FileTreeDiscovery_v1.0.py
#   Author:  Kevin Figueroa
#   License: BSD
#   Purpose: Displays directory and file tree structure selected by user. User may 
#             also select optional flags to display details about each file or directory
#	      listed.
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
import time
import argparse

# optional flags for output
parser = argparse.ArgumentParser(description="FLAG OPTIONS")
parser.add_argument('-a', '--alldates', action='store_true', help='returns all file or directory details')
parser.add_argument('-t', '--treelist', action='store_true', help='returns file tree list')
parser.add_argument('-s', '--size', action='store_true', help='returns size value')
parser.add_argument('-c', '--creation', action='store_true', help='returns creation date')
parser.add_argument('-l', '--lastaccess', action='store_true', help='returns last access date')
parser.add_argument('-m', '--lastmodified', action='store_true', help='returns last modified')
args = parser.parse_args()

# function displays file tree list
def treelist():
	rootDir = raw_input("\nSelect what tree path: ")
	for dirName, subdirList, fileList in os.walk(rootDir):
		if dirName:
			print ('+--%s' % dirName)
		for fn in fileList:
			print ('\t|--%s' % fn)
	print("\n\t******LISTING COMPLETE!******\n")

# function displays file tree & size per item listed
def fsize():
	rootDir = raw_input("\nSelect file or directory size of: ")
	print (rootDir)
	for dirName, subdirList, fileList in os.walk(rootDir):
		if dirName:
			print ('+---%s' % dirName)
			print ('\t|\t|---SIZE: %s bytes' % os.path.getsize(dirName))
		for fn in fileList:
			fnsize = ((dirName) + '/' + fn)
			print('\t|--%s' % fn)
			print('\t|\t|---SIZE: %s bytes' % os.stat(fnsize).st_size)
	print("\n\t******LISTING COMPLETE!******\n")
			
# function displays creation date ***HOWEVER output varies depending on the OS is being executed on 
def creation():
	rootDir = raw_input("\nSelect file or directory to view creation date: ")
	for dirName, subdirList, fileList in os.walk(rootDir):
		if dirName:
			print ('+---%s' % dirName)
			print ('\t\t|---CREATION DATE: %s' % time.ctime(os.stat(dirName).st_ctime))
		for fn in fileList:
			fncreation = ((dirName) + '/' + fn)
			print('\t|--%s' % fn)
			print('\t|\t|---CREATION DATE: %s' % time.ctime(os.stat(fncreation).st_ctime))
	print("\n\t******LISTING COMPLETE!******\n")
	
# function displays modification date per item listed
def moddate():
	rootDir = raw_input("\nSelect file or directory to view modified date: ")
	for dirName, subdirList, fileList in os.walk(rootDir):
		if dirName:
			print ('+---%s' % dirName)
			print ('\t|\t|---Modified Date: %s' % time.ctime(os.stat(dirName).st_mtime))
		for fn in fileList:
			fnmodified = ((dirName) + '/' + fn)
			print('\t|--%s' % fn)
			print('\t|\t|---Modified Date: %s' % time.ctime(os.stat(fnmodified).st_mtime))
	print("\n\t******LISTING COMPLETE!******\n")
		
# function displays last access date per item listed	
def lastaccess():
	rootDir = raw_input("\nSelect file or directory to view last access date: ")
	for dirName, subdirList, fileList in os.walk(rootDir):
		if dirName:
			print ('+---%s' % dirName)
                        print ('\t|\t|---Last Access: %s' % time.ctime(os.stat(dirName).st_atime))
                for fn in fileList:
			fnaccess = ((dirName) + '/' + fn)
                        print('\t|--%s' % fn)
                        print('\t|\t|---Last Access: %s' % time.ctime(os.stat(fnaccess).st_atime))
	print("\n\t******LISTING COMPLETE!******\n")

# function displays all optional flags
def allstat():
	rootDir = raw_input("\nSelect file or directory to view stats information: ")
        for dirName, subdirList, fileList in os.walk(rootDir):
                if dirName:
                        print ('+---%s' % dirName)
			print ('\t|\t|---Size: %s bytes' % os.path.getsize(dirName))
			print ('\t|\t|---Creation Date: %s' % time.ctime(os.stat(dirName).st_ctime))
			print ('\t|\t|---Modified Date: %s' % time.ctime(os.stat(dirName).st_mtime))
                        print ('\t|\t|---Last Access: %s' % time.ctime(os.stat(dirName).st_atime))
        	for fn in fileList:
			fnall = ((dirName) + '/' + fn)
                	print('\t|--%s' % fn)
			print('\t|\t|---Size: %s bytes' % os.stat(fnall).st_size)
			print('\t|\t|---Creation Date: %s' % time.ctime(os.stat(fnall).st_ctime)) 
			print('\t|\t|---Modified Date: %s' % time.ctime(os.stat(fnall).st_mtime))
                	print('\t|\t|---Last Access: %s' % time.ctime(os.stat(fnall).st_atime))
	print("\n\t******LISTING COMPLETE!******\n")
				

if len(sys.argv) == 1:
	parser.print_help()
elif (args.treelist):
	treelist()
elif (args.size):
	fsize()
elif (args.creation):
	creation()
elif (args.lastmodified):
	moddate()
elif (args.lastaccess):
	lastaccess()
else:
	allstat()
#END
