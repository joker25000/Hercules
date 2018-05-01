#!/usr/bin/env python
#
# Author  : Joker-Security
# Hercules - Automated VPN Connect
# Twitter: https://twitter.com/SecurityJoker
# Channel ; https://www.youtube.com/c/Professionalhacker25
# FACE Pg2: https://facebook.com/kali.linux.pentesting.tutorials

import os
import re
import sys 
import time
import urllib2


def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass

def banner():
	print("""\033[92m                                        
              (O)
              <W     _______                         __   
              <M    |   |   |.-----.----.----.--.--.|  |.-----.-----. 
   o          <M    |       ||  -__|   _|  __|  |  ||  ||  -__|__ --| 
  /| ......  /:M\------------------------------------------------,,,,,,
(O)[]XXXXXX[]I:K+}=============================================------------> \033[94m
  \| ^^^^^^  \:W/------------------------------------------------''''''  
   o          <W    |___|___||_____|__| |____|_____||__||_____|_____|      
              <W
              <W             \033[92m Hercules - Automated VPN Connect  
              (O)                C0d3n4m3:\033[91m Joker-Security \033[92m       
\033[93m                                  github.com/joker25000                                                                                                                                                                                       
""")
def command():
	os.system('clear')
	os.system('rm -f vpnbook-us1-*')
	os.system('rm -f VPNBook.com-OpenVPN-US1.zip*')

def download():
	link = 'wget http://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip'
	print ' \033[94m\n[+]\033[94m ---> Downloading VPN-FREE \n\n' 
	os.system(link)

def unzip():
	download()
	crack = 'unzip VPNBook.com-OpenVPN-US1.zip'
	print '\n \033[94m\n[+]\033[94m ---> Unzip File\n\n'
	out = os.path.isfile('VPNBook.com-OpenVPN-US1.zip')
	if out:
		os.system(crack)
	else:
		print 'Error: \033[93m\n[+]\033[93m ---> No Unzip File'

def getpass():
	print '\n \033[94m\n[+]\033[94m ---> Getting New Password\n\n'
	global user, passwd
	user = 'vpnbook'
	try:
		openUrl = urllib2.urlopen('http://www.vpnbook.com/freevpn')
	except urllib2.URLError:
		exit('Verify that you are connected to the Internet')
	kader = openUrl.read()
	joker = '''<li>Password: <strong>(.+?)</strong></li>'''
	dz = re.findall(joker, kader)
	if dz:
		passwd = dz[0]
	print '''
		\t\033[94m\n[+]\033[91m---> Username: {0}
		\t\033[94m\n[+]\033[93m---> Password: {1}
	\n'''.format(user, passwd)

def connect():
	os.system('openvpn --config vpnbook-us1-tcp80.ovpn')

def main():
	banner()
	unzip()
	getpass()
	connect()
	exit()
def exit():
	os.system('exit')
	print "\nCtrl + C -> Exiting!!"
if __name__ == '__main__':
	main()
