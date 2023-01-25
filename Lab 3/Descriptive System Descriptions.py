from logic import TruthTable

y = 'Y'
prop = []
case =[]
count = 0
check = []



while y == 'Y':
    proposition = input("Enter a propositon:")
    prop.append(proposition)
    y = input("Would you like to enter more [Y/N]: ")

myTable = TruthTable(prop)

print ('Your Program uses propositonal variables', myTable.vars)


qq = myTable.vars






while count < len(qq):
    case.append(input("Enter meaning of " + qq[count] + ': '))
    count = 1 + count


for count in myTable.table:
    check.append(count[1])
for r in check:
     if (r[2] == 1):
          print ('Your description is consistent when:')
          
          print ('It is not the case when', case[0])
          
          print ('It is not the case when', case[1])
          
          break
     else:
        print ('Your description is inconsistent')
        
        print ('It is not the case when', case[0])
        
        print ('It is not the case when', case[1])
        
        break
