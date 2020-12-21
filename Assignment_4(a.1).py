# Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.

                 # area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
                 
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.



# HERE WE ARE DECLARING A PARENT CLASS FOR TAKING THE LENGTH OF SIDES  
class area():
    def __init__(self,a,b,c):                     # HERE WE ARE USING __INIT__ FUNCTION FOR INITIALIZING THE VARIABLES 
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
# HERE WE ARE TAKING THE INPUT AS FLOAT FOR SIDES
a= float(input("a="))
b= float(input("a="))
c= float(input("a="))



# HERE WE ARE DECLARING A CHILD CLASS FOR CALCULATING THE AREA OF TRAINGLE
class traingle(area):                 
    def __init__(self,a,b,c):                      # HERE WE ARE USING __INIT__ FUNCTION FOR INITIALIZING THE VARIABLES 
        super().__init__(a,b,c)                    # HERE WE ARE USING THE SUPER() METHOD FOR INHERITING THE PROPERTIES OF PARENT CLASS

    def get_area(self):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5 
        
t = traingle(a,b,c)                                # HERE WE CREATED A OBJECT FOR CHULD CLASS THAT WILL BE INHERITATE ALL THE PROPERTIES OF PARENT CLASS
print(t.get_area())