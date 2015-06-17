#Partial Word Searching
def word_search(query, seq):
    query = query.lower()
    result = [x for x in seq if query in x.lower()]
    return result if result else ['None']

def word_search(query, seq):
    return [x for x in seq if query.lower() in x.lower()] or ["None"]  

#Write an iterative function to reverse a string. 
#Do the same thing as a recursive function.

def rev_func(text):
	if text == "":
		return text
	else:
		return rev_func(text[1:])+text[0] # recursion

print rev_func("fatma")	

def rev(text):
	return text[::-1]
print rev("fatma")	

#Implement a function with signature find_chars(string1, string2) that takes two 
#strings and returns a string that contains only the characters found in string1 
#and string two in the order that they are found in string1. 
def find_chars(string1,string2):
	result = []
	for char in string1:
		if char in string2:
			result.append(char)
		return result
print find_chars("fatma","zaman")		


          








