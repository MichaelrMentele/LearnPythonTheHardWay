def write_to(filename):
	
	content = raw_input("What do you want to write? ")
	write_file = open(filename, 'w')
	write_file.write(content)
	write_file.close()

#hmm, much easier to use the shell. I need the full path probably for this file. Awesome yes. You just need the full path!!!!!
#remember that!