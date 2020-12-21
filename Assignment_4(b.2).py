# Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.


# HERE WE ARE DEFINING A FUNCTION FOR TAKING A CHARACTER AS A INPUT
def character(u):
     if(u=='a' or u=='e' or u=='i' or u=='o' or u=='u'):
         return True
     else:
        return False

print(character('t'))