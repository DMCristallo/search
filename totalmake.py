import oswalk
import os

print "All drives selected"

os.remove("c:\\cache\\index") #reset file
print "file reset"

print "Rebuilding Index files...."
loc = "C:\\"
oswalk.build(loc)
print "C:\\ done"
loc = "D:"
oswalk.build(loc)
print "D: done"

print "Complete"