import os
import sys
import colorama
from os.path import join, getsize
from util.process import *
from util.file_finder import find_something
from colorama import Back, Fore, Style

def main():
    colorama.init(autoreset = True)
    print(Fore.CYAN + '########################################')
    print(Fore.CYAN + '########### UWUcation Eraser ###########')
    print(Fore.CYAN + '############ By SpookyV1cky ############\n')
    
    
    tasklist = find_something()
    process(tasklist)


main()

