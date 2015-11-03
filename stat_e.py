import os
import parse
import sys

'''
0-3 inode info
4 user id
5 group id
6 size in bytes
7 time of access
8 time of modification
9 creation time
'''
def s1(adr):
    stats=os.stat(adr)

    print stats
    parse.size(stats)
    parse.time(stats[7])
    parse.time(stats[8])
    parse.time(stats[9])

   # sys.exit() #stops it from duplicating

