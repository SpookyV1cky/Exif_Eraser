import os
from os.path import join, getsize
import colorama
from colorama import Back, Fore, Style
from exif import Image

UBICATION = [(51, 23, 21.3612),(30, 5, 56.4108)] #new location to overwrite, leave '0' if u want to delete
LATITUDE_REF = "N"
LONGITUDE_REF = "E"

def process(tasklist):
    colorama.init(autoreset = True)
    print(UBICATION)
    for task in tasklist:
        
        print( Fore.MAGENTA + "Cleaning... " + task['name'])
        
        try:
            with open(task['path'], 'rb') as f:
                coolImage = Image(f)
            if(coolImage.gps_latitude):
                print(coolImage.gps_latitude)
                print(coolImage.gps_longitude)

            coolImage.gps_latitude = UBICATION[0]
            coolImage.gps_longitude = UBICATION[1]

            coolImage.gps_latitude_ref = LATITUDE_REF
            coolImage.gps_longitude_ref = LONGITUDE_REF

            with open(task['out'], 'wb') as new_image:
                new_image.write(coolImage.get_file())

        except:
            os.replace(task['path'] , task['out']) #IF NOT LOCATION FOUND THIS WILL RENAME THE ORIGINAL FILE
            
            
