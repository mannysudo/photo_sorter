# Manuel Martinez
# Program Name: Photo File Type Sorter and Reorganizer 
""" Overview of Program: program checks each photo file in specified Directory1 and moves
JPG files to specified Directory2 and RAW files to specified Directory3. Program does not copy files,
it moves them to a new directory and therefore Directory1 will be emptied when program finalizes. """

import numpy as np
import os
import shutil
from datetime import datetime


# Four directories specified by user input
#dir1 = input('Enter directory one - where files will be CHECKED (in quotes ie "DIR/Here"): ')
#dir2 = input('Enter directory two - where JPG files will be STORED: ')
#dir3 = input('Enter directory three - where RAW files will be STORED: ')





def scanner(pam1, pam2, pam3):
    # counts initialized
    jcount = 0
    rcount = 0
    
    for filename in os.listdir(pam1):
        filename = filename.lower()
        if filename.endswith('.jpg'):
            oldfname = os.path.join(pam1, filename)
            newfname = os.path.join(pam2, filename)
            shutil.move(oldfname, newfname)
            jcount += 1

        if filename.endswith('.arw'):
            oldfname = os.path.join(pam1, filename)
            newfname = os.path.join(pam3, filename)
            shutil.move(oldfname, newfname)
            rcount += 1

    return jcount, rcount

if __name__ == "__main__":

    print(os.getcwd())
    dir_arr = []
    f = open("inputs.txt", "r")
    # Strips the newline character
    for line in f: 
        tmp = line.strip()
        tmp = os.path.join(os.getcwd(), tmp)
        dir_arr.append(tmp)

    # function call
    start = datetime.now()
    jn, rn = scanner(dir_arr[0], dir_arr[1], dir_arr[2])
    end = datetime.now()
    print(end-start)

    totalpics = jn + rn
    print('Files moved to the JPG directory: {}'.format(jn))
    print('Files moved to the RAW directory: {}'.format(rn))
    print('Total files moved: {}'.format(totalpics))
                