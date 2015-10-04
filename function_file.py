from sys import argv

script, input_file = argv

#print all the content of a file
def print_all(f):
	print f.read()

# rewind the content of file
def rewind(f):
	print f.seek(0)

#print line by line
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First Let's print the whole file:\n"
print_all(current_file)


print "Let's prine three lines:"

current_line = 1
print_a_line (current_line, current_file)
print_a_line (current_line+1, current_file)
print_a_line (current_line+2, current_file)