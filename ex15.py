from sys import argv	# import argv in sys module

script, filename = argv	# input 2 parameters from argv(keyboard)

txt = open(filename)	# mapping variable txt with the features of filename

print "Here's your file %r:" % filename	# print out user input (filename)
print txt.read()	# print out the contens of the file

print "Type the filename again:"
file_again = raw_input("> ")	# Why 2 times input and output ?

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
