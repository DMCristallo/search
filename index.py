from __future__ import print_function
import os


def all(loc,locc):

    if os.path.exists("D:\\index\\index") == True:
        os.remove("D:\\index\\index")

    print ("\nThis may take several minutes....")
    for x in locc:
        list=loc[0]+":\\"
        print ("Loading up %s ...." % (loc[0]))
        drive(list)
        print ("Done")
        del loc[0]

def drive(loc):
    import glob

    if os.path.exists("%s:\\" % (loc)) ==False:
        print ("drive not found")
        quit()

    if os.path.exists("D:\\index\\index") == True:
        os.remove("D:\\index\\index")

    os.chdir(loc)
    log = open("D:\\index\\index", "a")
    for files in glob.glob("*.*"):
        print(files, file = log)

    os.path
    dir = (loc)
    os.chdir(dir)
    for root, dirs, files in os.walk(dir):
        for f in files:
            fullpath = os.path.join(root, f)
            print (fullpath, file = log)