# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.

# HERE WE ARE DECLARING OUR OWN FUNCTION FOR CALCULATING OUR LONGER WORD LIST
def filterlongwords(lst,num):

    x = []                               # HERE WE ARE TAKING A EMPTY LIST FOR COLLECTING OUR NEW LONGER WORD LIST
    for i in range(0,len(lst)):          # HERE WE ARE USING FOR LOOP FOR ITERATING OUR LIST
        if i>=num:                       # HERE WE ARE USING CONDITION FOR COLLECTING OUR NEW LIST
            x.append(lst[i])             # HERE WE ARE USING LIST APPEND METHOD 
    return x

# HERE WE ARE DECLARING OUR LIST AND INTEGER VALUE FOR PASSING INTO THE FUNCTION
lst = ['s','r','g','x','k','l','n','m']
num = 2

# HERE WE ARE CALLING OUR FUNCTION WITH PASSING OUR LIST AND INTEGER VALUE
print(filterlongwords(lst,num))