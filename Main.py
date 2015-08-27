import oswalk
import avail
import all
import search
import os

print "Drives detected: %s" % (avail.get_available_drives())

loc = avail.get_available_drives()
loc2= avail.get_available_drives()

choose = raw_input("Full index or single Drive?: ")

#add in some timeout thing so a update can be run automaticly

if os.path.exists("D:\\index\\index") == True:
    os.remove("D:\\index\\index")

    #add code to create file/folder if not found

if choose == 's' or choose == 'single' : #or maybe add in S and Single or change it to just check for the s.
    cloc = raw_input("What drive? eg C:\\ : ") #maybe get to handle C ect
    if cloc == 'exit': quit() #remove later
    print "Drive: %s selected" % (cloc)
    print "Rebuilding Index files. This may take several minutes.... " #maybe add progress ellipses
    oswalk.build(cloc) #who needs error handling.
else:
    print "Checking drives %s" % loc
    all.index(loc,loc2)

print "Complete"

#add option to search without rebuilding, stand alone

#expand to more than just name search maybe stat()
more= raw_input("\nSearch for something? ")
if more == "yes" or more == "y": #maybe add Yes/Y
    search.search()
else: exit()