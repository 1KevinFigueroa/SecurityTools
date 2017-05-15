######################################################################################
#   Name:    dns_LookupResolver_v0.1.py
#   
#   Author:  Kevin Figueroa
#   
#   Purpose: Collects DNS information for a given domain 
#
#   License: BSD
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
########################################################################################i

#!/usr/bin/env python

# Must download python-dnspython library
import socket
import datetime
import dns.resolver


def main():
    # Ask user to select domain
    domain_name = raw_input("\nEnter Domin Name: ")

    # Remove "www." if user insert www before based domain
    if ("www." in domain_name):
        rootDomain = domain_name.replace("www.", "")

    # Resolve domain to IP address and reverse lookup on the IP address of the domain
    dn_results = socket.gethostbyname(domain_name)
    ip_results = socket.gethostbyaddr(dn_results)

    # Display domain, IP address, and reverse lookup of the IP address
    print ("\n[+] DOMAIN NAME: %s") % (domain_name)
    print ("\t|-- RESOLVES TO: %s") % (dn_results)
    print ("\n[+] REVERSE LOOKUP FOR %s") % (dn_results)
    print ("\t|-- RESOLVES TO: %s \n") % (ip_results[0])

    # Retrieve DNS SOA information
    for sdata in dns.resolver.query(rootDomain, "SOA"):
        extime = str(datetime.timedelta(seconds=sdata.expire))
        mintime = str(datetime.timedelta(seconds=sdata.minimum))
        reftime = str(datetime.timedelta(seconds=sdata.refresh))
        rettime = str(datetime.timedelta(seconds=sdata.retry))
        print ("[+] EXPIRE: %s seconds, which converts to: %s") % (sdata.expire, extime)
        print ("[+] MINIMUM: %s seconds, which converts to %s") % (sdata.minimum, mintime)
        print ("[+] REFRESH: %s seconds, which converts to: %s") % (sdata.refresh, reftime)
        print ("[+] RETRY: %s seconds, which converts to: %s") % (sdata.retry, rettime)
        print ("[+] SERIAL: %s  TECH: %s") % (sdata.serial, sdata.rname)
    print ("----------------------------------------------------")

    # Retrieve DNS NS record
    for ndata in dns.resolver.query(rootDomain, "NS"):
        print ("[+] NAME SERVER RECORD: %s") % (ndata)
    print ("---------------------------------------------------")

    # Retrieve DNS CNAME record
    for cdata in dns.resolver.query(rootDomain, "CNAME"):
        print ("[+] Canonical Name Record: %s") % (cdata)
    print ("----------------------------------------")

    # Retrieve DNS A record
    for adata in dns.resolver.query(rootDomain, "A"):
        print ("[+] DNS A Record: %s") % (adata)
    print ("---------------------------------")

    # Retrieve DNS MX record
    for mdata in dns.resolver.query(rootDomain, "MX"):
        print ("[+] DNS MX Record: %s has preference of: %s") % (mdata.exchange, mdata.preference)
    print ("--------------------------------------------------------------------------------")

    # Retrieve DNS TXT record
    for tdata in dns.resolver.query(rootDomain, "TXT"):
        print ("[+] SPF RECORD: %s") % (tdata)
    print ("------------------------------------------------------------------------------\n")


if __name__ == "__main__":
    main()

#END
