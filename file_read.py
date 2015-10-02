# Reading file
from sys import argv

script , filename = argv

txt = open(filename)

print " here is your file %s:" % filename
print txt.read()


print "Type the filename again:"
file_name = raw_input("type the file name please:-> ")


txt_again = open(file_name).read()

print txt_again
