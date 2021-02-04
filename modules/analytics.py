import os
from pathlib import Path

try:
    from ..access import dbx
except ImportError:
    print("You've not edited your access file. You need dropbox access_token!")
    

def localStorage(json):
    path = Path('./var/analytics/analytics')
    if not path.is_file():
        f = open(path.absolute, "w+")
    
        

def createFile():

    if dbx[0] != 'access_token':
        
        import dropbox
        from dropbox.files import WriteMode
        from dropbox.exceptions import ApiError, AuthError
        import sys 
        
        try:
            dbox = dropbox.Dropbox(dbx[0])
        except:
            #connection error -> turn to local storage 
            localStorage()
        
        
        
    else:
        #turn to local storage 
        localStorage()