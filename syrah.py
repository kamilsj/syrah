# -*- coding: utf-8 -*- 

import socket, requests, validators, certifi
from smart import checkURL
from modules.json import creatJSON
from modules.sort import sortData
from modules.search import search
from termcolor import colored
from bs4 import BeautifulSoup
from tqdm import tqdm


#some init requests
socket.setdefaulttimeout(10)
requests.packages.urllib3.disable_warnings()

json  = creatJSON()
addr  = 0
skip  = ['127.0.0.1', '127.0.1.1', '0.0.0.0']

def isConnected():
    return 1

def scanIP(args):

    if args.fromto is not None:
        ft = args.fromto
    if args.skip is not None:
        s  = args.skip 
    if args.search is not None:
        request = args.search
        search.search(request)
        
        
        
    if args.url == 'N':
        #scaning IP adress in ip range, without entry 69.59.196.211
        a = 69
        b = 59
        c = 196
        d = 211
        with tqdm(total = ((255-a)*(255-b)*(255-c)*(255-d) - len(skip)), desc="scanning") as bar:
            for num in range(a,255):
                for num2 in range(b,255):
                    for num3 in range(c,255):
                        for num4 in range(d,255):
                            global addr
                            addr = str(num)+"."+str(num2)+"."+str(num3)+"."+str(num4)
                            if not addr in skip:
                                parseURL(addr)
                                bar.set_description(desc="scanning: "+str(num)+"."+str(num2)+"."+str(num3)+"."+str(num4))
                                bar.update(1)
    elif validators.url(str(args.url)):
        scanDomain(str(args.url))
    else:
        pass


def lookup(addr):
    try:
        #look for better solution, because it does not work properly most of the time 
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return None, None, None


def loadURL(url):

    global ssl 
    if not url.startswith("https://") and not url.startswith("http://"):
        url2 = "https://"+url        
    try:
        html = requests.get(url2, verify=certifi.where(), timeout=20)
        if html.status_code == 200:
            ssl = 1
            return html
        else: return 0
    except requests.exceptions.SSLError:
        html = requests.get("http://"+url, verify=False, timeout=20)
        if html.status_code == 200:
            ssl = 0
            return html
        else: return 0
    except requests.exceptions.ConnectionError:
        exit("It seems you lost internet connection")
    except  requests.exceptions.HTTPError:
        return 0


def scanDomain(url):
    html = loadURL(url)
    if html != 0:
        content = BeautifulSoup(html.text, 'html.parser')
        if content.title != None:
            title = content.title.text
            title = title.encode('utf-8')
            #print(colored(title.decode(), "yellow"))

            for link in content.find_all('a'):
                url = link.get('href')
                if validators.url(str(url)):
                    #adding addition url addresses found on the particual webpage
                    pass
                else:
                    pass


            for meta in content.find_all('meta'):
                m = meta.get('meta')                                    

            texts = content.findAll(text=True)
            #There is something wrong with this part and I don't know what
            sortData.sort(texts)

        checkURL(url, addr, json)



def parseURL(addr):
    #Printing which ip address is being currently scanned 
    #print(colored(addr, 'green'))
    url, alias, addressList = lookup(addr) 
    if isConnected:
        if url != None:
            scanDomain(url)
    else:
        exit("You need internet connection.")







