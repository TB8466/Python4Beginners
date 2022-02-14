f = open("test.txt","r") #Select the file. "r" <- read

x = f.read() #Read the file, and save it as a variable

print(x)


f = open("test.txt","a+")
f.write('\nGood morning vietnam') #write to the file

