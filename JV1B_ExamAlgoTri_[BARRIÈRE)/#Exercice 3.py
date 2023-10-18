#Exercice 3
#Insertion
myTable = [8, 12, 3, 22, 15]
for n in range(len(myTable)):
    pluspetitevaleur =  myTable[n]
    emplacement=n
    for i in range(n,len(myTable)):
        if(myTable[i]<pluspetitevaleur):
            pluspetitevaleur = myTable[i]
            emplacement = i

    myTable.pop(emplacement)
    myTable.insert(n, pluspetitevaleur)
print(myTable)

#Tri à bulle
def tri_bulle(myTable):
    n = len(myTable)
    for i in range(n):
        for j in range(0, n-i-1):
            if myTable[j] > myTable[j+1] :
                myTable[j], myTable[j+1] = myTable[j+1], myTable[j]
myTable = [8, 12, 3, 22, 15]
 
tri_bulle(myTable)
for i in range(len(myTable)):
    print ("%d" %myTable[i])