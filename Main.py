import avail
import index
import search
import os
import sys

print "Drives detected: %s" % (avail.get_available_drives())

loc = avail.get_available_drives()
loc2= avail.get_available_drives()

if os.path.exists("D:\\index") == False:
    os.mkdir("D:\\index")

if len(sys.argv)>=2: #command line options
    arg1 = sys.argv[1]
    if arg1=='s':
        search.search()
        quit()
    if arg1=='f':
        index.all(loc,loc2)
    if arg1=='d' and len(sys.argv)>=3:
        index.drive(sys.argv[2])
        print "Complete"
        quit()

    #maybe add clean up for instances run using commands.

choose = raw_input("Full index or single Drive?: ").lower()
if choose == 'exit':
    quit()

if choose in ['s', 'single', 'o', 'one']:
    cloc = raw_input("What drive? eg C:\\ : ") #maybe get to handle C ect
    if cloc == 'exit': quit() #remove later
    print "Drive: %s selected" % (cloc)
    print "Rebuilding Index files. This may take several minutes.... " #maybe add progress ellipses
    index.drive(cloc) #now with (some) error checking

elif choose in ['f', 'full','a', 'all']:
    print "Checking drives %s" % loc
    index.all(loc,loc2)
else:
    print 'Choose a option that exists next time.'
    quit()

print "Complete"

#done if in command line #add option to search without rebuilding, stand alone

#expand to more than just name search maybe stat()
more= raw_input("\nSearch for something? ").lower()
if more in ['y', 'yes']:
    search.search()
else: exit()

