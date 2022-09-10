#Welcome
#This is a Banking Management System Code. This code requires MySQL 8.0 to work.
#Developed by Akash, Wahab, Yusra.
#Now whether you are a tester or you are opening this code for first time to understand its working.
#It will be difficult to understand the entire code by yourself.
#Comments like these are added in many places in the code to help increase readability and ease of understanding.
#We also may recommend to read the Project Report which came along with this file.
nam=''
#Now we start by defining many functions which are used in the code multiple times.
#These first 3 functions print a nice table with messages in it.
def startup():
    print()
    f=open("Logs.txt","a")
    #If you notice this line, here we log the startup into Logs.txt which is located in same directory.
    lemon=datetime.datetime.now()
    apple=str(lemon)+": System Powered On\n"
    f.write(apple)
    f.close()
    print("+","-"*53,"+",sep="")
    print("|"," "*14,"Welcome to WAY Banks Ltd"," "*15,"|",sep="")
    print("+","-"*53,"+",sep="")
def quit1():
    print("+","-"*53,"+",sep="")
    print("|"," "*8,"Thank you for choosing WAY Banks Ltd"," "*9,"|",sep="")
    print("+","-"*53,"+",sep="")
    print("|"," "*4,"Computer Team Project by Akash, Wahab, Yusra"," "*5,"|",sep="")
    print("+","-"*53,"+",sep="")
def about():
    print("+","-"*53,"+",sep="")
    print("|"," "*20,"WAY Banks Ltd"," "*20,"|",sep="")
    print("+","-"*53,"+",sep="")
    print("|"," "*4,"Computer Team Project by Akash, Wahab, Yusra"," "*5,"|",sep="")
    print("+","-"*53,"+",sep="")
    main=''
    return main
import datetime
import time
import os
#Here are 5 functions which help to verify that user has not entered invalid data.
def numbercheck(a):
    while a.isdigit()==False:
        a=input("Please enter digits for amount: QAR ")
    return a
def numbercheckcPIN(a):
    while a.isdigit()==False or len(a)!=4:
        a=input("Please enter 4 digits for Current PIN: ")
    return a
def numberchecknPIN(a):
    while a.isdigit()==False or len(a)!=4:
        a=input("Please enter 4 digits for New PIN: ")
    return a
def numbercheckPIN(a):
    while a.isdigit()==False or len(a)!=4:
        a=input("Please enter 4 digits for PIN: ")
    return a
def namcheck(nam):
    while len(nam)>15:
        nam=input("Account Name cannot be more then 15 characters\nRetype: ")
    return nam
#Time wait for Processing Requests
def timewait():
    import time
    print("Your transaction is being processed. Please Wait",end="")
    for i in range(6):
        print(".",end="")
        time.sleep(0.5)
    print()
#Help Function
#Displays Main Help Table
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
#Here we start defining the main functions which perform the transaction or account manipulation.
#In almost all of them you may see a similar pattern-
#To check whether user is logged in
#Syntax checking and Input Verification
#and finally the actual update or addition of data into the database
def balance():
    global nam,log
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    mycursor.execute("SELECT MainBal,Savings FROM acc WHERE Name = '{}'".format(nam)) 
    LiBal = mycursor.fetchone()
    Bal = LiBal[0]
    Sav = LiBal[1]
    print("Retrieving Account Funds",end="")
    for i in range(4):
        print(".",end="")
        time.sleep(0.5)
    print()
    print("Your Current Balance is: QAR", Bal) #Display
    print("Your Savings are: QAR",Sav)
    Choice = input("Would you like to see the Total amount you have in this bank? (y/n): ")
    Choice = Choice.lower()
    while Choice not in ['y', 'n','yes','no']:
        print("Please enter a valid response!",end=' ')
        Choice = input("(y/n): ")
        Choice = Choice.lower()
    else:
        if Choice in ['n','no']:
            print("OK!")
        else:
            TotBal = Bal + Sav
            print("Total Funds in Bank: QAR", TotBal)
    lemon=datetime.datetime.now()
    apple=str(lemon)+": Balance Displayed\n"
    f.write(apple) #Logged
    main=''
    return main
def chpin(main): #Change PIN
    global nam,log,att1
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    else:
        mycursor.execute("SELECT password FROM acc WHERE name='{}'".format(nam))
        tpin=mycursor.fetchall()
        Oripin=tpin[0][0]
        main=main.split()
        if len(main)==2: #Syntax and Input Checks
            Curpin = input("Enter your current PIN: ")
            Curpin=numbercheckcPIN(Curpin)
            if Oripin!=Curpin: #PIN Check
                att1=att1-1
                if att1==0:
                    print("Too many incorrect attempts to verify PIN.")
                    print("User has been automatically logged out...")
                    log=0
                    main=''
                    return main
                print("PIN entered was incorrect. You have",att1,"attempt(s) left.")
                main=''
                return main
            main.append(Curpin)
        if len(main)==3:
            Curpin=main[2]
            Curpin=numbercheckcPIN(Curpin)
            if Oripin!=Curpin: #PIN Check
                att1=att1-1
                if att1==0:
                    print("Too many incorrect attempts to verify PIN.")
                    print("User has been automatically logged out...") #Penalty Log out
                    log=0
                    main=''
                    return main
                print("PIN entered was incorrect. You have",att1,"attempt(s) left.")
                main=''
                return main
            newpin = input("Choose new PIN: ")
            newpin=numberchecknPIN(newpin)
            main.append(newpin)
        if len(main)>4:
            print("The syntax you've used is incorrect.\nThe correct syntax is '/change pin [Old PIN] [New PIN]' or simply '/change pin'")
            main=''
            return main
    Curpin=main[2]
    Curpin=numbercheckcPIN(Curpin)
    newpin=main[3]
    newpin=numberchecknPIN(newpin)
    if Oripin!=Curpin: #PIN Check
        att1=att1-1
        if att1==0:
            print("Too many incorrect attempts to verify PIN.") #Penalty Log out
            print("User has been automatically logged out...")
            log=0
            main=''
            return main
        print("PIN entered was incorrect. You have",att1,"attempt(s) left.")
        main=''
        return main
    if (newpin==Curpin):
        att1=4
        print("Verifying PIN",end="")
        for i in range(4):
            print(".",end="")
            time.sleep(0.5)
        print()
        print("This is your current PIN. No changes were made...")
    else: #Database Update
        att1=4
        print("Verifying PIN",end="")
        for i in range(4):
            print(".",end="")
            time.sleep(0.5)
        print()
        print("Changing PIN",end="")
        for i in range(4):
            print(".",end="")
            time.sleep(0.5)
        print()
        mycursor.execute("UPDATE acc SET password = '{}' WHERE name = '{}'".format(newpin, nam))
        print("Your PIN was successfully changed...")
        lemon=datetime.datetime.now()
        apple=str(lemon)+": Account PIN changed\n" 
        f.write(apple) #Logged
        mydb.commit()
    main=''
    return main
def chname(main): #Change Username
    global nam,log
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    else:
        main=main.split() #Syntax and Input Checks
        if len(main)==2:
            newname=input("Please enter new Account Name: ")
            newname=namcheck(newname)
            main.append(newname)
        if len(main)>3:
            print("The syntax you've used is incorrect.\nThe correct syntax is '/change username [New Username]' or simply '/change username'")
            main=''
            return main
        newname=main[2]
        newname=namcheck(newname)
        mycursor.execute("select name from acc")
        j=()
        c=0
        for j in mycursor:
            if newname in j:
                c=1
        if c==1:
            print("This account username is already in use. Please try another one.")
            main=''
            return main
        print("Changing Username",end="")
        for i in range(4):
            print(".",end="")
            time.sleep(0.5)
        print()
        mycursor.execute("UPDATE acc SET NAME = '{}' WHERE name = '{}'".format(newname, nam))
        mydb.commit() #Database Update
        print("Username successfully changed to ",newname,"...",sep="")
        lemon=datetime.datetime.now()
        apple=str(lemon)+": Username changed\n" 
        f.write(apple) #Logged
        nam=newname
        main=''
        return main
def cancelacc(): #Cancel Account
    global nam,log
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    mycursor.execute("select mainbal from acc where name='"+nam+"'")
    f1=mycursor.fetchone()
    mycursor.execute("select savings from acc where name='"+nam+"'")
    f2=mycursor.fetchone()
    if f1[0]==0 and f2[0]==0:
        pass
    else:
        print("Warning! You still have funds in your account.\nPlease withdraw before cancelling your account.")
        main=''
        return main
    x=input("Are you sure you want to cancel your account? (y/n): ")
    x=x.lower()
    if x in ['no','n']:
        main=''
        return main
    elif x not in ['no','n','yes','y']:
        print ('Please enter a valid response. (y/n)')
        cancelacc()
    cnc="delete from acc where name='"+nam+"'" #Database Update
    mycursor.execute(cnc)
    mydb.commit()
    log=0
    print("Deleting Account",end="")
    for i in range(4):
        print(".",end="")
        time.sleep(0.5)
    print()
    print("Account Deleted")
    while True:
        surv=input("Do you want to let us know why you decided to cancel your account? (y/n) ")
        surv=surv.lower()
        lemon=datetime.datetime.now()
        apple=str(lemon)+": Account deleted. Username: "+nam+"\n" #Logged
        f.write(apple)
        if surv in ['y','yes']:
            os.system("start \"\" https://forms.gle/QinHTodsuV5wMyqG6")
            break
        elif surv in ['no','n']:
            break
        else:
            print ('Please enter a valid response.',end=" ")
            surv=input("(y/n): ")
            surv=surv.lower()
    print ("Thank You for choosing WAY Banks! We hope to see you soon.")
def tupledisplay(t): #Displaying Table Content (For Admin Mode)
    p=len(t)
    p=p+4
    L=[0,2,p-1]
    L1=[0,4,20,30,40,50,60,70]
    L2=[1,5,21,31,41,51,61]
    L3=[4,20,30,40,50,60,70]
    #Made completely manually with the help of + - or |
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
                        k=[('ANo',"Name","PIN","Current","Savings","Deposited","Withdrew")]
                        print(k[0][a],end="")
                        j=j+len(k[0][a])
                        a=a+1
                        while j not in L3:
                            print(" ",end="")
                            j=j+1
            print()
def stat(): #Statistics
    global nam,log
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    statt="select deptotal,withtotal from acc where name='"+nam+"'"
    mycursor.execute(statt) 
    i=mycursor.fetchone() #Fetching
    print("Retrieving Account Information",end="")
    for j in range(4):
        print(".",end="")
        time.sleep(0.5)
    print()
    print("You have deposited a total of",i[0],"QAR so far, and withdrawn a total of",i[1],"QAR.")
    print("We hope you are having a great time using our helpful services!")
    lemon=datetime.datetime.now()
    apple=str(lemon)+": Statistics Accessed\n"
    f.write(apple) #Logged
def enteradmin(main): #Admin Mode
    global nam,log
    chk2=0
    import time
    if log==1: #Login Check
        print("Please logout to use Admin Mode.")
        main=''
        return main
    else:
        main=main.split() #Syntax and Input Checks
        if len(main)==1:
            pass2=input("Enter Master Password: ")
            main.append(pass2)
        if len(main)>2:
            print("The syntax you've used is incorrect.\nThe correct syntax is '/enteradmin or /godmode [Password]' or simply '/enteradmin or /godmode'")
            main=''
            return main
        pass2=main[1]
        pass3='@akash/wahab=yusra@' #Master Password
        if pass2!=pass3:
            print("Incorrect Password Entered. Please wait 10 seconds.") #Penalty Wait Time
            time.sleep(10)
            print()
            main=''
            return main
        else:
            print("Admin Mode Activated...\n")
            lemon=datetime.datetime.now()
            apple=str(lemon)+": Admin Mode Activated\n"
            f.write(apple) #Logged
            mycursor.execute("select * from acc")
            t=mycursor.fetchall()
            tupledisplay(t)
            print()
            print("Now you have full control of the database. List of actions")
            X2=[["/clear","Remove all client records"],["/delete","Delete a single client record"],["/defund","Clear Deposits"],["/help","Display a list of all valid Admin Commands"],["/view","Fetch and Display all records"],["/exitadmin","Return to Client Interface"]]
            help(X2)
            L=["/clear","/delete","/defund","/exitadmin"]
            L1=["/register","/cancel acc","/login","/feedback","/logout","/deposit","/withdraw","/transfer","/balance","/stat","/quit","/change pin","/change username","/about"]
            g=''
            while g!="/exitadmin": #While loop for commands in Admin Mode
                print()
                g=input(">>>")
                if g=="/exitadmin":
                    break
                if g in L1:
                    print(g,"is not recognised as a valid internal command. Try /help to get a list of valid Admin commands.")
                    print("You are still in Admin Mode. Client Commands will not work here.\nUse /exitadmin to go back to Client Interface.")
                elif g=="/clear": #Clear all records
                    mycursor.execute("select * from acc")
                    t=mycursor.fetchall()
                    if len(t)!=0:
                        mycursor.execute("delete from acc")
                        mydb.commit()
                        print("All records are deleted. Bank database reset...")
                        lemon=datetime.datetime.now()
                        apple=str(lemon)+": An admininstrator deleted all records\n"
                        f.write(apple) #Logged
                    else:
                        print("Bank Database already empty.")
                elif g=="/help": #Display help table for Admin Mode
                    help(X2)
                elif g=="/delete": #Delete single record
                    mycursor.execute("select * from acc")
                    t=mycursor.fetchall()
                    if len(t)!=0: 
                        ac=input("Enter ANo: ")
                        while ac.isdigit()==False:
                            ac=input("Please enter digits: ")
                        ac=int(ac)
                        mycursor.execute("select accno from acc")
                        t=mycursor.fetchall()
                        chk=0
                        for jk in t:
                            if ac==jk[0]:
                                chk=1
                                break
                        if chk==0:
                            print("Specified Account number is not available.")
                        else:
                            ac=str(ac)
                            mycursor.execute("delete from acc where accno='"+ac+"'")
                            mydb.commit()
                            print("Record Deleted...")
                            lemon=datetime.datetime.now()
                            apple=str(lemon)+": An admininstrator deleted a single record\n"
                            f.write(apple) #Logged
                        mycursor.execute("select * from acc")
                        t=mycursor.fetchall()
                        tupledisplay(t)
                    else:
                        print("No Client records available in Bank to delete.")
                elif g=="/defund": #Clear all Funds
                    mycursor.execute("select * from acc")
                    t=mycursor.fetchall()
                    if len(t)!=0:
                        if chk2==0:
                            mycursor.execute("update acc set savings=0")
                            mydb.commit()
                            mycursor.execute("update acc set mainbal=0")
                            mydb.commit()
                            mycursor.execute("update acc set withtotal=0")
                            mydb.commit()
                            mycursor.execute("update acc set deptotal=0")
                            mydb.commit()
                            print("All funds set to 0. Bank still holds client details.")
                            mycursor.execute("select * from acc")
                            t=mycursor.fetchall()
                            tupledisplay(t)
                            lemon=datetime.datetime.now()
                            apple=str(lemon)+": An admininstrator defunded the bank\n"
                            f.write(apple) #Logged
                            chk=1
                        else:
                            print("No funds available to defund.")
                    else:
                        print("No Client records available in Bank to defund.")    
                elif g=="":
                    continue
                elif g=="/view": #View table content
                    mycursor.execute("select * from acc")
                    t=mycursor.fetchall()
                    if len(t)!=0:
                        tupledisplay(t)
                    else:
                        print("No Client records available in Bank to display.")
                elif g=="/enteradmin" or g=="/godmode":
                    print("You are already in Admin Mode.")
                else:
                    print(g,"is not recognised as a valid internal command.")
                    print("Try /help to get a list of valid Admin commands.")
            time.sleep(2)
            print("Admin Mode Deactivated...")
            print()
            lemon=datetime.datetime.now()
            apple=str(lemon)+": Admin Mode Deactivated\n"
            f.write(apple) #Logged
            print("Main Console")
            main=''
            return main
def withdraw(main):
    global nam
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    else:
        main=main.split() #Syntax and Input Checks
        if len(main)==1:
            withdraw=input("Withdrawal Amount: QAR ")
            withdraw=numbercheck(withdraw)
            main.append(withdraw)
        if len(main)==2:
            withdraw=main[1]
            withdraw=numbercheck(withdraw)
            print("Withdraw QAR",withdraw,"from Current or Savings?",end=" ")
            ans2=input("(c/s): ")
            ans2=ans2.lower()
            while ans2 not in ["c","s"]:
                ans2=input("Please enter only (c/s): ")
            main.append(ans2)
        if len(main)>3 or main[2].lower() not in ["c","s"]:
            print("The syntax you've used is incorrect.\nThe correct syntax is '/withdraw [Amount] [c/s]' or simply '/withdraw'")
            main=''
            return main
        withdraw=main[1]
        withdraw=numbercheck(withdraw)
        ans2=main[2].lower()
        if ans2=='c':
            mycursor.execute("select mainbal from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            timewait()
            if int(j[0])<int(withdraw): #Balance Check
                print("You have Insufficient Funds in your Current account. Cannot withdraw.")
                print("Current Balance QAR",j[0])
            else: #Database Update
                mycursor.execute("update acc set mainbal=mainbal-'"+withdraw+"' where name='"+nam+"'")
                mydb.commit()
                mycursor.execute("update acc set withtotal=withtotal+'"+withdraw+"' where name='"+nam+"'")
                mydb.commit()
                print("Withdrew QAR",withdraw,"from Current")
                lemon=datetime.datetime.now()
                apple=str(lemon)+": QAR "+withdraw+" withdrawn from Current\n"
                f.write(apple) #Logged
                print("Remaining Balance QAR",(int(j[0])-int(withdraw)))
        else:
            mycursor.execute("select savings from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            timewait()
            if int(j[0])<int(withdraw): #Balance Check
                print("You have Insufficient Funds in your Savings account. Cannot withdraw.")
                print("Savings Balance QAR",j[0])
            else: #Database Update
                mycursor.execute("update acc set savings=savings-'"+withdraw+"' where name='"+nam+"'")
                mydb.commit()
                mycursor.execute("update acc set withtotal=withtotal+'"+withdraw+"' where name='"+nam+"'")
                mydb.commit()
                print("Withdrew QAR",withdraw,"from Savings")
                lemon=datetime.datetime.now()
                apple=str(lemon)+": QAR "+withdraw+" withdrawn from Savings\n"
                f.write(apple) #Logged
                print("Remaining Balance QAR",(int(j[0])-int(withdraw)))
def deposit(main):
    global nam
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    else:
        main=main.split() #Syntax and Input Checks
        if len(main)==1:
            deposit=input("Deposit Amount: QAR ")
            deposit=numbercheck(deposit)
            main.append(deposit)
        if len(main)==2:
            deposit=main[1]
            deposit=numbercheck(deposit)
            print("Deposit QAR",deposit,"in Current or Savings?",end=" ")
            ans2=input("(c/s): ")
            ans2=ans2.lower()
            while ans2 not in ["c","s"]:
                ans2=input("Please enter only (c/s): ")
            main.append(ans2)
        if len(main)>3 or main[2].lower() not in ["c","s"]:
            print("The syntax you've used is incorrect.\nThe correct syntax is '/deposit [Amount] [c/s]' or simply '/deposit'")
            main=''
            return main
        deposit=main[1]
        deposit=numbercheck(deposit)
        ans2=main[2].lower()
        if ans2=='c': #Database Update
            mycursor.execute("update acc set mainbal=mainbal+'"+deposit+"' where name='"+nam+"'")
            timewait()
            print("Deposited QAR",deposit,"into Current")
            lemon=datetime.datetime.now()
            apple=str(lemon)+": QAR "+deposit+" deposited into Current\n"
            f.write(apple) #Logged
            mydb.commit()
            mycursor.execute("update acc set deptotal=deptotal+'"+deposit+"' where name='"+nam+"'")
            mydb.commit()
            mycursor.execute("select mainbal from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            print("Available Balance QAR",j[0])
        else: #Database Update
            mycursor.execute("update acc set savings=savings+'"+deposit+"' where name='"+nam+"'")
            timewait()
            print("Deposited QAR",deposit,"into Savings")
            lemon=datetime.datetime.now()
            apple=str(lemon)+": QAR "+deposit+" deposited into Savings\n"
            f.write(apple)#Logged
            mydb.commit()
            mycursor.execute("update acc set deptotal=deptotal+'"+deposit+"' where name='"+nam+"'")
            mydb.commit()
            mycursor.execute("select savings from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            print("Available Balance QAR",j[0])
def transfer(main):
    global nam
    if log==0: #Login Check
        print("Please login to use bank services.")
        main=''
        return main
    else:
        main=main.split() #Syntax and Input Checks
        if len(main)==1:
            tran=input("Transfer Amount: QAR ")
            tran=numbercheck(tran)
            main.append(tran)
        if len(main)==2:
            tran=main[1]
            tran=numbercheck(tran)
            print("Transfer QAR",tran,"from Current or Savings?",end=" ")
            ans2=input("(c/s): ")
            ans2=ans2.lower()
            while ans2 not in ["c","s"]:
                ans2=input("Please enter only (c/s): ")
            main.append(ans2)
        if len(main)==3:
            nam2=input("Recipient Account: ")
            main.append(nam2)
            mycursor.execute("select name from acc")
            j=()
            c=0
            for j in mycursor:
                if nam2 in j:
                    c=1
            if c==0:
                print("The Recipient account entered is invalid. Please enter an existing account.")
                main=''
                return main
        if len(main)==4:
            print("Transfer to Current or Savings of Recipient Account?",end=" ")
            ans3=input("(c/s): ")
            ans3=ans3.lower()
            while ans3 not in ["c","s"]:
                ans3=input("Please enter only (c/s): ")
            main.append(ans3)
        if len(main)>5 or main[2].lower() not in ["c","s"] or main[4].lower() not in ["c","s"]:
            print ("The syntax you've used is incorrect.\nThe correct syntax is '/transfer [Amount] [c/s] [username] [c/s]' or simply '/transfer'")
            main=''
            return main
        tran=main[1]
        ans2=main[2].lower()
        nam2=main[3]
        ans3=main[4].lower()
        mycursor.execute("select name from acc")
        j=()
        c=0
        tran=numbercheck(tran)
        for j in mycursor:
            if nam2 in j:
                c=1
        if c==0:
            print("The Recipient account entered is invalid. Please enter an existing account.")
            main=''
            return main
        if ans2=='c': #Balance Check
            mycursor.execute("select mainbal from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            timewait()
            if int(j[0])<int(tran):
                print("You have Insufficient Funds in your Current account. Cannot transfer.")
                print("Current Balance QAR",j[0])
            else: #Database Update
                mycursor.execute("update acc set mainbal=mainbal-'"+tran+"' where name='"+nam+"'")
                mydb.commit()
                print("Transfering Amount QAR",tran,"from Current...")
                print("Remaining Balance QAR",(int(j[0])-int(tran)))
                if ans3=='c':
                    mycursor.execute("update acc set mainbal=mainbal+'"+tran+"' where name='"+nam2+"'")
                    print("Recipient Name:",nam2)
                    print("Transfer Success...")
                    mydb.commit()
                elif ans3=='s':
                    mycursor.execute("update acc set savings=savings+'"+tran+"' where name='"+nam2+"'")
                    print("Recipient Name:",nam2)
                    print("Transfer Success...")
                    mydb.commit()
                lemon=datetime.datetime.now()
                apple=str(lemon)+": QAR "+tran+" transferred\n" 
                f.write(apple) #Logged
        elif ans2=='s': #Balance Check
            mycursor.execute("select savings from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            timewait()
            if int(j[0])<int(tran): 
                print("You have Insufficient Funds in your Savings account. Cannot transfer.")
                print("Current Balance QAR",j[0])
            else: #Database Update
                mycursor.execute("update acc set savings=savings-'"+tran+"' where name='"+nam+"'")
                mydb.commit()
                print("Transfering Amount QAR",tran,"from Savings...")
                print("Remaining Balance QAR",(int(j[0])-int(tran)))
                if ans3=='c':
                    mycursor.execute("update acc set mainbal=mainbal+'"+tran+"' where name='"+nam2+"'")
                    print("Recipient Name:",nam2)
                    print("Transfer Success...")
                    mydb.commit()
                elif ans3=='s':
                    mycursor.execute("update acc set savings=savings+'"+tran+"' where name='"+nam2+"'")
                    print("Recipient Name:",nam2)
                    print("Transfer Success...")
                    mydb.commit()
                lemon=datetime.datetime.now()
                apple=str(lemon)+": QAR "+tran+" transferred\n"
                f.write(apple) #Logged
def login(main):
    global att,nam
    main=main.split() #Syntax and Input Checks
    if len(main)==1:
        nam=input("Account name: ")
        main.append(nam)
        mycursor.execute("select name from acc")
        j=()
        c=0
        for j in mycursor:
            if nam in j:
                c=1
        if c==0:
            print("This account does not exist. To register a new account, use /register")
            main=''
            return main
    if len(main)==2:
        nam=main[1]
        mycursor.execute("select name from acc")
        j=()
        c=0
        for j in mycursor:
            if nam in j:
                c=1
        if c==0:
            print("This account does not exist. To register a new account, use /register")
            main=''
            return main
        passw=input("Enter your PIN: ")
        main.append(passw)
    if len(main)>3:
        print ("The syntax you've used is incorrect.\nThe correct syntax is '/login [username] [PIN]' or simply '/login'")
        return 0
    nam=main[1]
    passw=main[2]
    passw=numbercheckPIN(passw)
    mycursor.execute("select name from acc")
    j=()
    c=0
    for j in mycursor:
        if nam in j:
            c=1
    if c==0:
        print("This account does not exist. To register a new account, use /register")
        main=''
        return main
    mycursor.execute("select password from acc where name='"+nam+"'")
    print("Verifying PIN",end="")
    for i in range(4):
        print(".",end="")
        time.sleep(0.5)
    print()
    j=()
    for j in mycursor:
        pass
    if j[0]==passw: #Successful Login
        print("User",nam,"successfully logged in...")
        lemon=datetime.datetime.now()
        apple=str(lemon)+": User "+nam+" logged in\n"
        f.write(apple) #Logged
        att,att1=4,4
        return 1
    else: #Failed Login Attempt
        att=att-1
        if att==0:
            print("Too many incorrect attempts. Please wait for 30 seconds.") #Penalty Wait Time
            time.sleep(5)
            att=4
        else:
            print("Incorrect PIN entered. Login attempt failed.\nYou have",att,"attempt(s) left.")
        return 0
def register(main):
    if log==1: #Login Check
        print("Please logout to register new account.")
        main=''
        return main
    main=main.split() #Syntax and Input Checks
    if len(main)==1:
        nam=input("Account name: ")
        nam=namcheck(nam)
        main.append(nam)
        mycursor.execute("select name from acc")
        j=()
        c=0
        for j in mycursor:
            if nam in j:
                c=1
        if c==1:
            print("This account is already registered. Please Login to access bank services.")
            main=''
            return main
    if len(main)==2:
        nam=main[1]
        nam=namcheck(nam)
        mycursor.execute("select name from acc")
        j=()
        c=0
        for j in mycursor:
            if nam in j:
                c=1
        if c==1:
            print("This account is already registered. Please Login to access bank services.")
            main=''
            return main
        passw=input("Create a PIN: ")
        passw=numbercheckPIN(passw)
        main.append(passw)
    if len(main)>3:
        print ("The syntax you've used is incorrect.\nThe correct syntax is '/register [username] [PIN]' or simply '/register'")
        main=''
        return main
    nam=main[1]
    passw=main[2]
    nam=namcheck(nam)
    mycursor.execute("select name from acc")
    j=()
    c=0
    for j in mycursor:
        if nam in j:
            c=1
    if c==1:
        print("This account is already registered. Please Login to access bank services.")
        main=''
        return main
    passw=numbercheckPIN(passw)
    mycursor.execute("select accno from acc")
    j=()
    for j in mycursor:
        pass
    if j==():
        j=1
    else:
        j=j[0]+1
    print("Creating Account",end="")
    for i in range(4):
        print(".",end="")
        time.sleep(0.5)
    print()
    mycursor.execute("insert into acc (accno,name,password) values (%s,%s,%s)",(j,nam,passw))
    mydb.commit() #Database Update
    lemon=datetime.datetime.now()
    apple=str(lemon)+": User "+nam+" registered\n"
    f.write(apple) #Logged
    print ("An account with the name",nam,"has been created!\nWe hope you have a great time using our services.\nYou can start using your account by /login.")
    main=''
    return main
#We have defined all necessary user defined functions and now we can start the system
#Startup
startup() #First function called
print("Initializing System",end="")
for i in range(6):
    print(".",end="")
    time.sleep(0.5)
print("\n")
#After start, we ask for mandatory information to connect to the Database
#In real life these maybe already written in code or preloaded in system
#But this is an universal code hence it can connect to any database provided user gives correct credentials.
print("This program requires MySQL to be installed.\nWe need your permission. Please provide the details.")
print()
time.sleep(0.5)
ans=input("Does this device have MySQL installed? (y/n): ")
ans=ans.lower()
while ans not in ["y","yes","n","no"]:
    ans=input("Please enter (y/n): ")
    ans=ans.lower()
if ans not in ["y","yes"]: #If MySQL is not installed
    print()
    print("Sorry but you need to have MySQL Server 8.0 to run this program.")
    print("Developed by Akash, Wahab, Yusra.")
    print("Program will terminate shortly.")
    time.sleep(2)
    quit()
#Custom SQL User
def customuser():
    global root
    print()
    ans1=input("Did you set up an account during installation?\nIf not, the root user will be used (y/n): ")
    ans1=ans1.lower()
    while ans1 not in ["yes","y","n","no"]:
        ans1=input("Please enter (y/n): ")
        ans1=ans1.lower()
    if ans1 in ["y","yes"]:
        print()
        root=input("Enter your Username: ")
    else:
        root="root"
customuser()
#Database Password Entry
def password():
    print()
    global pass1
    pass1=input("Please enter Database Server Password: ")
password()
#Preliminary Checks
import os
import mysql.connector
def mysqlconn():
    try:
        global mydb
        mydb=mysql.connector.connect(
            host='localhost',
            user=root,
            password=pass1
            )
    except:
        print("The credentials were incorrect. Please try again.")
        customuser()
        password()
        mysqlconn()
mysqlconn()
#Now the database is connected with Python
#Commands for creating table and database bank if they do not exist
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
mycursor.execute("show tables")
i=()
for i in mycursor:
    pass
if 'acc' not in i:
    mycursor.execute("create table acc(accno INTEGER PRIMARY KEY,name varchar(15),password varchar(10),mainbal INTEGER DEFAULT 0,savings INTEGER DEFAULT 0,deptotal INTEGER DEFAULT 0,withtotal INTEGER DEFAULT 0)")
main=''
print("Database connected successfully...\n\nMainConsole")
#Main Console
log=0
att,att1=4,4
g=0
#Here is the main console where the client user interacts, whatever he types is checked and verified.
#If valid entry is present the corresponding functions you saw earlier above are called.
#Else we display error message or suggest using /help
while main!='/quit':
    f=open("Logs.txt","a")
    if g==1:
        print()
    main=input(">>>")
    g=1
    if main=='/help':
        X1=[["/register","Register a new account"],["/login","Login to a registered account"],["/logout","Logout from current session"],["/deposit","Deposit Funds to your account"],["/withdraw","Withdraw Funds from your account"],["/transfer","Transfer Funds to a different account"],["/balance","Display your current balance"],["/stat","Display total statistics"],["/change pin","Change your account PIN"],["/change username","Change your account Username"],["/cancel acc","Delete your account permanently"],["/enteradmin","Access Admin Mode"],["/godmode","Same Use as /enteradmin"],["/help","Display a list of all valid commands"],["/feedback","Submit feedback through Survey"],["/about","Display Project Information"],["/quit","Exit the Program"]]
        help(X1)
        main=''
    elif main=="":
        g=0
        continue
    elif main=="/about":
        about()
        print("Coded in Python 3.8.3 - Requires MySQL 8.0")
        print("Lines - 1082")
        print("Size - 42KB")
    elif main[:9]=="/register":
        register(main)
    elif main[:6]=="/login":
        if log==1:
            print("A current session is already logged in. Please logout by /logout.")
        else:
            log=login(main)
    elif main[:8]=="/deposit":
        deposit(main)
    elif main=="/cancel acc":
        cancelacc()
    elif main[:9]=="/withdraw":
        withdraw(main)
    elif main=="/stat":
        stat()
    elif main[:9]=="/transfer":
        transfer(main)
    elif main=="/feedback":
        log=0
        os.system("start \"\" https://forms.gle/GzQNWRQ1wbVgbXA5A")
        lemon=datetime.datetime.now()
        apple=str(lemon)+": Feedback Form Loaded\n"
        f.write(apple)
        main=''
    elif main=="/logout":
        if log==0:
            print("Please login first!")
            main=''
        elif log==1:
            print("You have successfully logged out...")
            att1,att=4,4
            lemon=datetime.datetime.now()
            apple=str(lemon)+": User "+nam+" Logged out\n"
            f.write(apple)
            log=0
            main=''
    elif main[:16]=='/change username':
        chname(main)
    elif main[:11]=='/change pin' or main[:11]=='/change PIN':
        main=chpin(main)
    elif main=='/balance':
        balance()
    elif main[:11]=='/enteradmin' or main[:8]=='/godmode':
        enteradmin(main)
        g=0
    elif main=="/quit":
        quit1()
        if log==1:
            print("You have been successfully logged out...")
            lemon=datetime.datetime.now()
            apple=str(lemon)+": User "+nam+" Logged out\n"
            f.write(apple)
            log=0
        print("User Logs Saved...")
        print("Program will terminate shortly...")
        lemon=datetime.datetime.now()
        guava="-"*60
        apple=str(lemon)+": System Powered Off\n"+guava+"\n"
        f.write(apple)
        time.sleep(3)
        f.close()
        quit()
    else:
        print(main,"is not recognised as a valid command.\nTry /help to get a list of all the valid commands.")
    f.close()
#End of Program
