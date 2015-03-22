#Given an array_of_ints, find the highest_product you can get from three of the integers.
#The input array_of_ints will always have at least three integers.
def highest_product_of_3(array_of_ints):
    if len(array_of_ints) < 3:
        raise Exception("Less than 3 items!")

   
    highest = max(array_of_ints[0], array_of_ints[1])
    lowest = min(array_of_ints[0], array_of_ints[1])

    highest_product_of_two = array_of_ints[0] * array_of_ints[1]
    lowest_product_of_two = array_of_ints[0] * array_of_ints[1]

    
    highest_product_of_three = array_of_ints[0] * array_of_ints[1] * array_of_ints[2]

    # walk through items, starting at index 2
    for current in array_of_ints[2:]:

        # do we have a new highest product of 3?
        # it's either the current highest, 
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_two,
            current * lowest_product_of_two)

        # do we have a new highest product of two?
        highest_product_of_two = max(
            highest_product_of_two,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_two = min(
            lowest_product_of_two,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_three