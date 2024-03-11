import os
from os.path import join, getsize


def find_something():
    
    tasklist = []

    rootfolder = input("folder path: ")
    
    print(" Scanning... ")

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
        
    print(" [ OK ] ")
    return tasklist