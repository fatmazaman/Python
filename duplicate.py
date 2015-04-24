#list of duplicates in Python list
values = [2,3,4,4,5,6,7,7,8,8,8,9,9]

def dup_val(value):
    return list(set([x for x in value if value.count(x)>1]))

print dup_val(values)

#Find Unique value

l = [1,2,3,4,5,2,3,5,6,9,8,7,7,9]

def uniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output

print uniq(l)    

#Another way to find unique value

def uniq_val(l):
	return list(set(l))

print uniq_val(l)



