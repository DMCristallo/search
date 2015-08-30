
def search():
    search = open("D:\\index\\index", "r")

    case= raw_input("Case sensitive? [Y]/[N] " ) #default case insensitive

    phrase = raw_input("Enter Search Query ")
    #phrase = "test"
    print "Searching for %s \n" % (phrase)

    if case in ['N', 'n']:
        for line in search:
            if phrase.lower() in line.lower():
            #if phrase == line:
                print line
    else:
        for line in search:
            if phrase in line:
            #if phrase == line:
                print line

    search.close()

    #hmm looks case sensitive
    #maybe add search the search