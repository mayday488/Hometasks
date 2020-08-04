f = open("Text.txt", "r+")

list_of_lines = f.readlines()
newlist = list_of_lines.split()

print (newlist)
    
f.close()