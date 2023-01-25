
count = int(0)
number = int(0)
integerlist = [ ]
oddlist = [ ]
largest = int(0)
index = int(0)

while (count != 10):
    count = count +1
    print "Please enter an integer: "
    number = raw_input()
    integerlist.append(number)
    if int(number) % 2 == 1:
        oddlist.append(number)
        

    
        
        

print integerlist
print oddlist

if len(oddlist) == 0:
    print "No odd numbers were entered"


while (index != len(oddlist)):
    if int(largest) < int (oddlist[index]):
        largest = oddlist[index]
    index = index +1
    
print "The largest number is: " + largest


