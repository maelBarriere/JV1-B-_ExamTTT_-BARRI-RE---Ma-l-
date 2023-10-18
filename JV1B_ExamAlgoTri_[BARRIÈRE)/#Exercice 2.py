#Exercice 2
myTable = [8, 12, 3, 22, 15]
plusgrandevaleur = myTable[4]
emplacement=0
for i in range(len(myTable)):
    if(myTable[i]>plusgrandevaleur):
        plusgrandevaleur = myTable[i]
        emplacement = i
myTable.pop(emplacement)
myTable.insert(4, plusgrandevaleur)
print(myTable)
