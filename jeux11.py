from random import*
T=[]
while len(T)<4 :
    x=randint(1,9)
    if x not in T:
        T.append(x)
compteur=0
bp=0
while compteur<10  and bp<4 :
    bp=0 
    nc=0
    compteur=compteur+1
    P=[]
    for i in range(4):
        p=int(input("T["+str(i)+"]="))
        P.append(p)
    for i in range(4):
        if T[i]==P[i]:
            bp=bp+1
        elif P[i] in T :
            nc=nc+1

    print(bp,",",nc)

if bp==4:
    print("Excellent!")
else:
    print(T)
    print("--Game over--")
