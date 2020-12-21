# Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.

           # Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
           # Here 2,3 and 4 are the lengths of the words in the list.

# HERE WE ARE DECLARING OUR OWN character_length FOR COUNTING CHARACTER LENGTH
def character_length(lst):
    x = []                                 # HERE WE ARE TAKING A EMPTY LIST FOR COLLECTING OUR NEW LENGTH OF CHARACTER LIST
    for i in lst:                          # HERE WE ARE USING FOR LOOP FOR ITERATING OUR CHARACTER LIST
        x.append(len(i))
    return x

# HERE WE ARE DECLARING OUR OWN CHARACTER LIST FOR PASSING INTO THE FUNCTION
lst = ['agf' , 'yute' , 'ytewfe']

# HERE WE ARE CALLING OUR FUNCTION WITH PASSING OUR LIST AND INTEGER VALUE
print(character_length(lst))