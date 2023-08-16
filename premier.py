#les nombres premiers a partir un donnee nbr n
while 1:
    n = int(input("les nombre premiers inferieure de nombre:"))
    if n>1:
        break

for i in range(1,n+1):
    val = 0
    for j in range(1,i+1):
        if i%j==0:
            val+=1
            if val>2:   #amelioration : low algo complexity
                break
    if val==2:
        print(i)



#test si un nombre est premier
nb = int(input("donner un nombre pour le tester si premier: "))
def premier(x):
    for i in range(2,round(x/2)+1):
        if x%i==0:
            return False
    return True

result = premier(nb)
if result==True:
    print("yes")
else:
    print("no")

