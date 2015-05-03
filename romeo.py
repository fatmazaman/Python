#open the file 
story = open("romeo.txt", 'r').read()

#tokenize the file

tokenized_story = story.split(" ")
#print tokenized_story






# store the value of file in list
wdata = []
for row in tokenized_story:
    split_row  = row.split('\n')
    wdata.append(split_row)
print wdata    
'''#function to remove punctuation
no_punctuation_tokens = []
def remove_punctuation(token):
  
    token = token.replace(".", "")
    token = token.replace(",", "")
    token = token.replace("'", "")
    token = token.replace("'", "")
    token = token.replace(";", "") 
    token = token.replace("\n","")
    return token.lower()
for token in tokenized_story:
    token = remove_punctuation(token)
    no_punctuation_tokens.append(token) 
    

print no_punctuation_tokens'''

'''
def uniq_val(l):
    return list(set(l))

print uniq_val(no_punctuation_tokens)'''



