#1. Create a list of capital letters in the english alphabet
lst = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(lst)

#2. Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
newlst = [x for x in lst if x != "\u0046" and x != "\u004B" and x != "\u0050" and x != "\u0055"]
print(newlst)

#3. Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
def doStuff(lst):
    newlst2 = []
    for x in range(0,5):
        newlst2.append(lst[x])
    for x in range(5,15,2):
        newlst2.append(lst[x])
    for x in range(15,len(lst)):
        newlst2.append(lst[x])
    return newlst2