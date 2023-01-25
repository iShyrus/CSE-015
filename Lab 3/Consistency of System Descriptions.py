from logic import TruthTable

propistionlist = [ ]
y = 'Y'
while (y == 'Y'):
    prop = input("Enter a propositon:")
    propistionlist.append(prop)


    
    y = input("Would you like to enter more [Y/N]: ")

myTable = TruthTable(propistionlist)



pro = [ ]
for i in myTable.table:
    pro.append(i[1])

for checker in pro:
    if (checker[0] == checker[1]):
        if (checker[0] == 0):
            print("Your description is consistent.")
            break
        
        else:
             print("Your description is not consistent.")
             break
