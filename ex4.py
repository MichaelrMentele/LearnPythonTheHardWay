#variable assignment, remember that in programs that don't manage memory allocation for you that this is really (or usually) pointing to a location in memory where some binary is stored. 

#Also in python variable assignment typing is implicit and dependent on the form of the information you put inside the variable.

#You can easily insert variables into a print statement by using a ',' between strings and then putting a variable name and another comma like so: ',variable,'

#A traceback is a basically, a flag gets raised when there is an error but it doesn't happen exactly when the event gets handled so it has to be tracebacked to where it actually happened on the stack.

#The error he gives here is that he called a variable that was not yet defined. 

#Space in a car is OK to use an integer value for

#for the print function you need to use %s for strings and %d for decimals. Alright. So. 'Let's talk about %s' % variable if the variable is a string use %s if a number use %d
pounds = 100
poundperkilo = 2.2
kilos = pounds/poundperkilo 

print "%r" %kilos