import os
from os.path import join, getsize
import colorama
from colorama import Back, Fore, Style

def find_something():
    
    tasklist = []
    colorama.init(autoreset = True)

    rootfolder = input(Fore.CYAN + "folder path: ")
    
    print(Fore.GREEN + " Scanning... ")

    for root, dirs, files in os.walk(rootfolder):
        
        for name in files:
                
                if(name.split('.')[-1] == 'jpg'):
                    img_path = os.path.join(root, name)                    


                    out = os.path.join(root, "1312_" + name)
                    tasklist.append({
                         "name":name,
                         "path":img_path,
                         "out":out,
                    })
    print(tasklist)
        
    print(Fore.GREEN + " [ OK ] ")
    return tasklist