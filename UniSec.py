
#!/usr/bin/python

#Unisec imports
import nmap 
from lib.common import 

print """
[##############################################################################]
|                                                                              |
|                          UniSec - Universal Security for all.                |
|______________________________________________________________________________|
|                                                                              |
|                                                                              |
|                                                                              |
|                 User Name:          [   unisec   ]                           |
|                                                                              |
|                 Password:           [               ]                        |
|                                                                              |
|    Author: Shadman Ahmmed                                                    |
|                                                                              |
|    My Email : shadmanahmmed@protonmail.com                                   |
|                                                                              |
|                                                                              |
|                                   [ OK ]                                     |
|______________________________________________________________________________|

                  	    Script by Shadman Ahmmed
                     	    Version : Beta
"""
print "Type your network/localhost Default Gateway . For example:,"
print "192.128.0.1 "
print "You can type 'ifcomfig' on your terminal for getting your localhost IP and if your IP is 192.128.0.4",
print "then you have to replace that 4 with 1 which is your Default Gateway."
print "Please enter your network[localhost] IP:"
ip = raw_input()
def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popopen(command)
    results = str(process.read())
    return results
print (get_nmap('-Sv',  ))

