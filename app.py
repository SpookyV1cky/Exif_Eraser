import os
import sys
from os.path import join, getsize
from util.process import *
from util.file_finder import find_something


def main():
    
    print('########################################')
    print('########### UWUcation Eraser ###########')
    print('############ By SpookyV1cky ############\n')
    
    
    tasklist = find_something()
    process(tasklist)


main()

