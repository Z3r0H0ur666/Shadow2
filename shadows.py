#!/usr/bin/env python3

import sys
import platform
import requests
from selenium import webdriver
driver = webdriver.Firefox(executable_path= '/usr/local/bin/geckodriver')

ver = plat	form.python_version()

if (ver <= '3'):
	print("\033[91m Shadows Traffic isn't compatible with python2 use python 3.x\033[00m")
	sys.exit(1)

import random
import time
import os

try:
	from stem import Signal
	from stem.control import Controller
	import requests

except ImportError:

	print("\033[91m Install stem and requests with pip\033[00m")

	sys.exit(1)

print("""\033[91m

 ######    #####   ########   #######  ##        #######   ######   ######  
##    ##  ##   ##  ##     ## ##     ## ##       ##     ## ##    ## ##    ## 
##       ##     ## ##     ##        ## ##              ## ##       ##       
##       ##     ## ##     ##  #######  ##        #######   ######   ######  
##       ##     ## ##     ##        ## ##              ##       ##       ## 
##    ##  ##   ##  ##     ## ##     ## ##       ##     ## ##    ## ##    ## 
 ######    #####   ########   #######  ########  #######   ######   ######\033[00m

				\033[93mv.1.0
				By C0d3l3ss\033[00m
""")

#tor_password = input("\033[92m Enter your tor password: \033[00m")

links = ['https://sophiamobile.com','https://sophiamobile.com/category','https://sophiamobile.com/bookpage?book=%D9%88%D8%AD%D8%AF%D9%87%20%D8%A7%D9%84%D9%88%D9%82%D8%AA%20%D9%8A%D9%83%D8%B4%D9%81%20%D8%A7%D9%84%D8%AD%D9%82%D9%8A%D9%82%D8%A9','https://sophiamobile.com/bookpage?book=%D8%AC%D8%B1%D8%A7%D8%A6%D9%85%20%D8%A7%D9%84%D8%A3%D8%AD%D8%B1%D9%81%20%D8%A7%D9%84%D9%85%D8%B2%D8%AE%D8%B1%D9%81%D8%A9']
#address = input("\033[92m Enter target address:  \033[00m")

views = int(input(10000)


# signal Tor for new identity

def renew_connection():

	with Controller.from_port(address="127.0.0.1", port = 9051) as controller:

		controller.authenticate(password="")   #password can be found in torrc file(HashedControlPassword)

		controller.signal(Signal.NEWNYM)

		controller.signal(Signal.HUP)

		time.sleep(5)


def tor_session():

#setup proxies

	session = requests.session()

	session.proxies = {}

	session.proxies['http'] = 'socks5://localhost:9050'

	session.proxies['https'] = 'socks5://localhost:9050'

	return session


def visit():

#file which contains user-agent lists

	with open('agents.txt','r') as file:

		lines = open('agents.txt').read().splitlines()

	for num in range(views):

		header_value = random.choice(lines)

		header = {}

		header['User-Agent'] = header_value

		session = tor_session()

		session.get(address, headers=header)	#visiting the URL given by the user
		for link in links:
			driver.get(link)
    	
    	
		

		print("\033[92m-\033[00m" * 150)

		print("\033[92m Page Visited with following ip with user-agent..\033[00m")

		print(session.get('http://httpbin.org/ip').text)	#display current ip

		print(session.get('http://httpbin.org/user-agent', headers=header).text)	#display current user-agent
		driver.quit()
		renew_connection()

		if num == (views - 1):
			print("\033[92m-\033[00m " * 150)
			print("\033[01m\033[93m Shadows Traffic Successfully Visited & Viewed Target Website ",views, "times\033[00m")
			sys.exit(0)


visit()


