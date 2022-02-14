# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.
def lst_convertor(str):
    str = str.replace("a","")
    str = str.replace("e","")
    str = str.replace("i","")
    str = str.replace("o","")
    str = str.replace("u","")
    str = str.replace(" ","") #Remove spaces

    lst = []        #Create an empty list
    lst[0:] = str   #Insert the string into the list #NOTE the slicing

   #sorted() is a function that takes different parameters to determine how it should sort the input. Default function is to sort alphabetically
    return sorted(lst) 
print(lst_convertor("world of warcraft"))
print(type(lst_convertor("worldofwarcraft")))