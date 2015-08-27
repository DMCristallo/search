
def search():
    search = open("D:\\index\\index", "r")

    phrase = raw_input("Enter Search Query ")
    #phrase = "test"
    print "Searching for %s" % (phrase)

    for line in search:
        if phrase in line:
        #if phrase == line:
            print line
    search.close()