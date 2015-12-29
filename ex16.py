from sys import argv #import feature argv from module or package or library sys


script, filename = argv # unpack

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename, 'w') #create file object

print "Truncating the file. Goodbye!"
target.truncate() # delete contents of file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#stringtest = "%s \n %s \n %s \n" % (line1, line2, line3)
target.write("%s \n %s \n %s \n" % (line1, line2, line3))
"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""

print "And finally, we close it."
target.close()
