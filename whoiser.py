#!/usr/bin/env python3

import sys, threading, time, os, urllib, re, requests, pymysql
from html.parser import HTMLParser
from urllib import request
from xml.dom import minidom
from bs4 import BeautifulSoup
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET

# HEADER CONF
headers = {
        'User-Agent': 'Mozilla/5.1 (Macintosh; Intel Mac OS X 10.9; rv:43.0) Gecko/20100101 Firefox/43.0'
      }

# FILE TO WRITE
fileOutput = open('results.html', 'w')

# FILE TO READ
inputFile = sys.argv[1]
fileInput = open(inputFile)

# PARSING FUNCTION
def emailLookup(line):
	db = pymysql.connect(host='localhost', user='whoiser', passwd='whoiser', db='whoiser', charset='utf8')
	conn = db.cursor()
	try:
		r = requests.get("http://www.freewhois.us/index.php?query="+line+"&submit=Whois", headers = headers)
		data = BeautifulSoup(r.text)
		getAhref = data.find_all('a')
		getAllData = data.find('pre').text

		try:
			findEmail = re.compile('([-a-z0-9]+\@.+?\.\w{2,5})').search(str(getAhref))
			email = findEmail.group(1)
		except Exception as e:
			email = "0"

		try:
			findPhone = re.compile('Phone: (.+)').search(getAllData)
			phone = findPhone.group(1).replace(".", "")
		except Exception as e:
			phone = "0"

		try:
			findCreationDate = re.compile('Creation Date: (.+)T').search(getAllData)
			creDate = findCreationDate.group(1)
		except Exception as e:
			creDate = "0"

		try:
			findExperiationDate = re.compile('Expiration Date: (.+)T').search(getAllData)
			expDate = findExperiationDate.group(1)
		except Exception as e:
			expDate = "0"

		try:
			findUpdatedDate = re.compile('Updated Date: (.+)T').search(getAllData)
			updDate = findUpdatedDate.group(1)
		except Exception as e:
			updDate = "0"

		try:
			findRegistrar = re.compile('Registrar: (.+)').search(getAllData)
			registrar = findRegistrar.group(1)
		except Exception as e:
			registrar = "0"

		try:
			findDomainStatus = re.compile('Domain Status: (.+?)http.+').search(getAllData)
			domStat = findDomainStatus.group(1)
		except Exception as e:
			domStat = "0"
			
		try:
			findRegistrantName = re.compile('Name: (.+)').search(getAllData)
			regName = findRegistrantName.group(1)
		except Exception as e:
			regName = "0"

		try:
			registrantCountry = re.compile('Registrant Country: (\w{1,3})|CountryCode: (\w{1,3})').search(getAllData)
			regCountry = registrantCountry.group(1)
		except Exception as e:
			regCountry = "0"

		#fileOutput.write("<li>"+line+" ; "+email+" ; "+phone+" ; "+creDate+" ; "+expDate+" ; "+updDate+" ; "+registrar+" ; "+domStat+" ; "+regName+" ; "+regCountry+"</li>")
		checkDuplicates = conn.execute("SELECT * FROM whoiser WHERE domain = %s", (line))
		if checkDuplicates:
			try:
				conn.execute("UPDATE whoiser SET creDate = %s, expDate = %s, updDate = %s, registrar = %s, domain_status = %s, name = %s, country = %s, phone = %s, email = %s WHERE domain = %s", (creDate, expDate, updDate, registrar, domStat, regName, regCountry, phone, email, line))
				db.commit()
			except Exception as e:
				db.rollback()
		else:
			try:
				conn.execute("INSERT INTO whoiser (domain, creDate, expDate, updDate, registrar, domain_status, name, country, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (line, creDate, expDate, updDate, registrar, domStat, regName, regCountry, phone, email))
				db.commit()
			except Exception as e:
				db.rollback()
		db.close()
	except Exception as e:
		print(e)

# BEGIN PARSING (THREADS)
with fileInput as file:
	for line in file:
		t = threading.Thread(target=emailLookup, args=(line,))
		t.start()
		time.sleep(0.2)