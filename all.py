import oswalk

def index(loc,locc):
    print "\n This may take several minutes...."
    for x in locc:
        list=loc[0]+":\\"
        print "Loading up %s ...." % (loc[0])
        oswalk.build(list)
        print "Done"
        del loc[0]