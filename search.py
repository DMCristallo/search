import os

def search():

    if os.path.exists("D:\\index\\index") == False:
        print "Index not found."
        quit()

    search = open("D:\\index\\index", "r")
    results=''

    case= raw_input("Case sensitive? [Y]/[N] " ) #default case insensitive

    phrase = raw_input("Enter Search Query ")
    #phrase = "test"
    print "Searching for %s \n" % (phrase)

    if case in ['N', 'n']:
        for line in search:
            if phrase.lower() in line.lower():
                results=line+results
                print line
    else:
        for line in search:
            if phrase in line:
                results=line+results
                print line

    again = raw_input("Search the results? ")
    if again in ['Y', 'y']:
        research(results)
    else:
        search.close()

def research(results):
    print "results = %s" % results #remove later
    phrase = raw_input("Enter Search Query ")
    for line in results:
        print 'lower phrase: %s    lower line: %s  ' %(phrase.lower(),line.lower())
        if phrase.lower() in line.lower():
            print line

    #maybe add search the search