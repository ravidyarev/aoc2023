import re

a_file = open("day1input.txt", "r")
list_of_lists = [((line.strip()).split()) for line in a_file]
a_file.close()
k=0
l=0
#print(list_of_lists)

for i in range(0,len(list_of_lists)):
    p=list_of_lists[i][0]
    q=[(i, c) for i, c in enumerate(p) if c.isdigit()] 
    if len(q)==1:
        k=int(q[0][1]+q[0][1])
    else:
        k=int(q[0][1]+q[len(q)-1][1])
    l=l+k
    
print(l)
