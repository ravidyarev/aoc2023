#got help from this stackoverflow thread : https://stackoverflow.com/questions/70983144/how-to-convert-words-to-integer-in-python
import re

a_file = open("day2input.txt", "r")
list_of_lists = [((line.strip()).split()) for line in a_file]
a_file.close()
k=0
l=0

number_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
          'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

number_dict.update({str(i): str(i) for i in range(10)})
numbers = re.compile("|".join(number_dict))

for i in range(0,len(list_of_lists)):
    p=list_of_lists[i][0]
    list_of_lists[i][0]="".join(number_dict[w] for w in numbers.findall(p))
    p=list_of_lists[i][0]
    q=[(i, c) for i, c in enumerate(p) if c.isdigit()] 
    if len(q)==1:
        k=int(q[0][1]+q[0][1])
    else:
        k=int(q[0][1]+q[len(q)-1][1])
    l=l+k
    
print(l)
