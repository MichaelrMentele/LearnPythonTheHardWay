#this imports the a part of sys. Sys is the module Argv is a function I believe. and we are just taking that part of it
from sys import argv

#unpack argv
script, filename = argv

#store the file in this variable?
txt = open(filename)

print "Here's your damn file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()
txt.close()


# close
# read
# open
# readline
# truncate
#write('stuff')
