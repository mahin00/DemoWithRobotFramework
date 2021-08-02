# python -m pip install filetype
import sys
import os
import pathlib
import filetype

def test_current_dir():
    current_dir = os.getcwd()
    print(current_dir)
    return  current_dir
def test_previous_dir():
    previousDir = pathlib.Path(__file__).parent.parent
    print(previousDir)
    return previousDir

def listdir():
        filename= os.listdir()
        return filename

def deleteImage(i):
    if (os.path.isfile(i)):
        if(filetype.is_image(i)):
            print("deleted image file name {0}".format(i))
            os.remove(i)

def test_iteration():
    dir = test_current_dir()
    directory= listdir()
    print(dir)
    for i in directory:
        deleteImage(i)
test_iteration()