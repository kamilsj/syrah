# -*- coding: utf-8 -*-

import sys, pymysql, json
from termcolor import * #not yet used, but is here
from modules.sort import sortData #our code yeah
from modules.db import database
from urllib.parse import urlparse


global cur

try:	
	from access import db as data
except ImportError:
	print("You have not edited access.py file") 
 
try:
	db = pymysql.connect(
	        host=data[0],
	        user=data[1],
	        passwd=data[2],
	        db=data[3],
			autocommit=True)

	
	
	cur = db.cursor()
	database.createDatabase(cur)
	
except pymysql.MySQLError:
	exit("Lack of MySQL connection")
except pymysql.InternalError:
	exit("I don't know what have just happend")
except pymysql.NotSupportedError:
	exit("I don't know what have just happened")

def addURL(url, addr, json):		
	
	sql   = "INSERT INTO url (main_url, path, ip) VALUE (%s, %s, %s)"
	table = urlparse(url)
	
	if len(table.netloc) > 0:
		netloc = table.netloc
	else:
		netloc = None
		
	if len(table.path) > 0:
		path   = table.path
	else:	
		path   = None
		
	cur.execute(sql, (netloc, path, addr))
	
	if cur.rowcount == 1:
		print(colored(url, 'red')+": added")
	
	

def checkURL(url, addr, json):
	
	sql = "SELECT ip FROM url WHERE ip=%s"
	cur.execute(sql, (addr))
	res = cur.fetchone()
	if cur.rowcount == 0:
		addURL(url, addr, json)
	
		
	