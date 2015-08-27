from __future__ import print_function
import os
import glob
def build(loc):
    import os
    import glob
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
"""
os.curdir
for  files in os.listdir("."):
    if files.endswith("."):
        print files

from os.path import join, getsize
for root, dirs, files in os.walk("/mydir"):
    print root, "consumes",
    print sum([getsize(join(root, name)) for name in files]),
    print "bytes in", len(files), "non-directory files"
    prit
    """


