L1=[["/register","Register a new account"],["/login","Login to a registered account"],["/logout","Logout from current session"],["/deposit","Deposit Funds to your account"],["/withdraw","Withdraw Funds from your account"],["/transfer","Transfer Funds to a different account"],["/balance","Display your current balance"],["/stat","Display total statistics"],["/change pin","Change your account PIN"],["/change username","Change your account Username"],["/cancel acc","Delete your account permanently"],["/enteradmin","Access Admin Mode"],["/godmode","Same Use as /enteradmin"],["/help","Display list of all valid commands"],["/feedback","Submit feedback through Survey"],["/about","Display Project Information"],["/quit","Exit the Program"]]
L2=[["/clear","Remove all records of clients"],["/delete","Delete a single client record"],["/defund","Clear Deposits"],["/help","Display a list of all valid Admin Commands"],["/view","Fetch and Display all records"],["/exitadmin","Return to Client Interface"]]
def help(L1):
    n=len(L1)
    n=n+4
    L=[0,2,n-1]
    H=["Command","Description"]
    for i in range(n):
        if i in L:
            for j in range(70):
                if j in [0,18,69]:
                    print("+",end="")
                else:
                    print("-",end="")
            print()
        else:
            a=0
            if i==1:
                j=0
                while j!=70:
                    if j in [0,18,69]:
                        print("|",end="")
                        j=j+1
                    else:
                        print(H[a],end="")
                        j=j+len(H[a])
                        a=a+1
                        while j not in [0,18,69]:
                            print(" ",end="")
                            j=j+1  
            else:
                a=0
                j=0
                while j!=70:
                    if j in [0,18,69]:
                        print("|",end="")
                        j=j+1
                    else:
                        print(L1[i-3][a],end="")
                        j=j+len(L1[i-3][a])
                        a=a+1
                        while j not in [0,18,69]:
                            print(" ",end="")
                            j=j+1
            print()
help(L1)
