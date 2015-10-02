from sys import argv

script, filename = argv

print "we're going to erase %r." % filename
print "if you ok with it then hit return"
raw_input("? ")

print "opening the file ...."
target = open(filename, 'w')

print "truncating the file"
target.truncate()

print "Now I am gonna to ask you three lines:"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "i'm gonna to write these on the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "finaly close the file"
target.close()
