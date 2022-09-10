t=[(1, 'Akash', '9932', 20000, 0, 0, 0), (2, 'Wahab', '3809', 10000, 0, 0, 0), (3, 'Yusra', '3345', 119000, 67000, 0, 0)]
p=len(t)
p=p+4
L=[0,2,p-1]
L1=[0,4,20,30,40,50,60,70]
L2=[1,5,21,31,41,51,61]
L3=[4,20,30,40,50,60,70]
for i in range(p):
    if i in L:
        for j in range(71):
            if j in L1:
                print("+",end="")
            else:
                print("-",end="")
        print()
    else:
        a=0
        for j in range(71):
            if j in L1:
                print("|",end="")
            elif j in L2:
                if i>=3 and i!=(p-1):
                    print(t[i-3][a],end="")
                    j=j+len(str(t[i-3][a]))
                    a=a+1
                    while j not in L3:
                        print(" ",end="")
                        j=j+1
                elif i==1:
                    k=[('No',"Name","PIN","Current","Savings","Deposited","Withdrew")]
                    print(k[0][a],end="")
                    j=j+len(k[0][a])
                    a=a+1
                    while j not in L3:
                        print(" ",end="")
                        j=j+1
        print()
