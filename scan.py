#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import sys, argparse
from syrah import scanIP

version = "0.0.0.2.2"


def main(argv = None):
        
    parser = argparse.ArgumentParser(description='Scan website links and content', usage='Type your url link or type N to scan the whole web, yeah')
    parser.add_argument('--url', dest="url", type=str, help='url of website to scan', default='N', required=True)
    parser.add_argument('--search', dest="search", type=str, help='search a phrase you want to find in web')
    parser.add_argument('--version', action='version', help='print version of syrahsearch', version = version)
    parser.add_argument('--fromto', dest="fromto", type=int, help='depth of searching', required=False)
    parser.add_argument('--skip', dest="skip", type=str, help='skip some domains and ip addrss', required=False)

    args = parser.parse_args()
    
    #print(args.url)
    if args:
        scanIP(args)
    else:
        exit(0)
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
