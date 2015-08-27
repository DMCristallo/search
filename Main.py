import avail
import index
import search
import os

print "Drives detected: %s" % (avail.get_available_drives())

loc = avail.get_available_drives()
loc2= avail.get_available_drives()

choose = raw_input("Full index or single Drive?: ").lower()

#add in some timeout thing so a update can be run automaticly

if os.path.exists("D:\\index\\index") == True:
    os.remove("D:\\index\\index")

    #add code to create file/folder if not found

if choose in ['s', 'single', 'o', 'one']:
    cloc = raw_input("What drive? eg C:\\ : ") #maybe get to handle C ect
    if cloc == 'exit': quit() #remove later
    print "Drive: %s selected" % (cloc)
    print "Rebuilding Index files. This may take several minutes.... " #maybe add progress ellipses
    index.drive(cloc) #who needs error handling.
elif choose in ['f', 'full','a', 'all']:
    print "Checking drives %s" % loc
    index.all(loc,loc2)
else:
    print 'Choose a option that exists next time.'

print "Complete"

#add option to search without rebuilding, stand alone

#expand to more than just name search maybe stat()
more= raw_input("\nSearch for something? ")
if more in ['y', 'yes']:
    search.search()
else: exit()