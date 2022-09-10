nam=''
def numbercheck(a):
    if a.isdigit():
        return a
    else:
        while a.isdigit()==False:
            a=input("Please enter digits for amount: QAR ")
        return a
def withdraw(main):
    global nam
    if log==0:
        print("Please login to use bank services.")
        main=''
        return main
    else:
        main=main.split()
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
            if int(j[0])<int(withdraw):
                print("You have Insufficient Funds in your Current account. Cannot withdraw.")
                print("Current Balance QAR",j[0])
            else:
                mycursor.execute("update acc set mainbal=mainbal-'"+withdraw+"' where name='"+nam+"'")
                mydb.commit()
                print("Withdrew QAR",withdraw,"from Current")
                print("Remaining Balance QAR",(int(j[0])-int(withdraw)))
        else:
            mycursor.execute("select savings from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            if int(j[0])<int(withdraw):
                print("You have Insufficient Funds in your Savings account. Cannot withdraw.")
                print("Savings Balance QAR",j[0])
            else:
                mycursor.execute("update acc set savings=savings-'"+withdraw+"' where name='"+nam+"'")
                mydb.commit()
                print("Withdrew QAR",withdraw,"from Savings")
                print("Remaining Balance QAR",(int(j[0])-int(withdraw)))
def deposit(main):
    global nam
    if log==0:
        print("Please login to use bank services.")
        main=''
        return main
    else:
        main=main.split()
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
        if ans2=='c':
            mycursor.execute("update acc set mainbal=mainbal+'"+deposit+"' where name='"+nam+"'")
            print("Deposited QAR",deposit,"into Current")
            mydb.commit()
            mycursor.execute("select mainbal from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            print("Available Balance QAR",j[0])
        else:
            mycursor.execute("update acc set savings=savings+'"+deposit+"' where name='"+nam+"'")
            print("Deposited QAR",deposit,"into Savings")
            mydb.commit()
            mycursor.execute("select savings from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            print("Available Balance QAR",j[0])
def transfer(main):
    global nam
    if log==0:
        print("Please login to use bank services.")
        main=''
        return main
    else:
        main=main.split()
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
        if ans2=='c':
            mycursor.execute("select mainbal from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            if int(j[0])<int(tran):
                print("You have Insufficient Funds in your Current account. Cannot transfer.")
                print("Current Balance QAR",j[0])
            else:
                mycursor.execute("update acc set mainbal=mainbal-'"+tran+"' where name='"+nam+"'")
                mydb.commit()
                print("Transfering Amount QAR",tran,"from Current")
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
        elif ans2=='s':
            mycursor.execute("select savings from acc where name='"+nam+"'")
            j=()
            for j in mycursor:
                pass
            if int(j[0])<int(tran):
                print("You have Insufficient Funds in your Savings account. Cannot transfer.")
                print("Current Balance QAR",j[0])
            else:
                mycursor.execute("update acc set savings=savings-'"+tran+"' where name='"+nam+"'")
                mydb.commit()
                print("Transfering Amount QAR",tran,"from Savings")
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
def chknam(passw):
    global nump
    global splp
    nump=0
    splp=0
    for i in passw:
        if i.isalpha()==True:
            pass
        elif i.isdigit()==True:
            nump+=1
        else:
            splp+=1
def login(main):
    global att,nam
    main=main.split()
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
        passw=input("Enter your Password: ")
        main.append(passw)
    if len(main)>3:
        print ("The syntax you've used is incorrect.\nThe correct syntax is '/login [username] [password]' or simply '/login'")
        return 0
    nam=main[1]
    passw=main[2]
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
    j=()
    for j in mycursor:
        pass
    if j[0]==passw:
        print("User",nam,"successfully logged in...")
        return 1
    else:
        att=att-1
        if att==0:
            print("Too many incorrect attempts. Please wait for 30 seconds.")
            time.sleep(5)
            att=4
        else:
            print("Incorrect Password entered. Login attempt failed.\nYou have",att,"attempt(s) left.")
        return 0
def register(main):
    main=main.split()
    if len(main)==1:
        nam=input("Account name: ")
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
        passw=input("Create a Password: ")
        main.append(passw)
    if len(main)>3:
        print ("The syntax you've used is incorrect.\nThe correct syntax is '/register [username] [password]' or simply '/register'")
        main=''
        return main
    nam=main[1]
    passw=main[2]
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
    chknam(passw)
    if len(passw)<8 or splp==0 or nump==0:
            passw=input("The password must be atleast 8 characters long\nIt should have at least 1 special character and 1 digit\nRetype Password: ")
            chknam(passw)
    while True:
        if len(passw)<8:
            passw=input("The password must be atleast 8 characters long\nRetype Password: ")
            chknam(passw)
        elif splp==0 and nump==0:
            passw=input("The password must have at least 1 special character and 1 digit\nRetype Password: ")
            chknam(passw)
        elif splp==0:
            passw=input("The password must have at least 1 special character\nRetype Password: ")
            chknam(passw)
        elif nump==0:
            passw=input("The password must have at least 1 digit\nRetype Password: ")
            chknam(passw)
        else:
            break
    mycursor.execute("select accno from acc")
    j=()
    for j in mycursor:
        pass
    if j==():
        j=1
    else:
        j=j[0]+1
    mycursor.execute("insert into acc (accno,name,password) values (%s,%s,%s)",(j,nam,passw))
    mydb.commit()
    print ("An account with the name",nam,"has been created!\nWe hope you have a great time using our services.")
print("***Welcome to WAY Banks Ltd***")
import time
time.sleep(0)
print("Initializing Program")
time.sleep(0)
print("This program requires MySQL to be installed.\nWe need your permission. Please provide the details.")
time.sleep(0)
ans=input("Does this device have MySQL installed? (y/n): ")
while ans not in ["Y","y","n","N"]:
    ans=input("Please enter (y/n): ")
if ans not in ["y","Y"]:
    print("Sorry but you need to have MySQL Server 8.0 to run this program.")
    print("Developed by Akash, Wahab, Yusra.")
    print("Program will terminate shortly.")
    time.sleep(4)
    quit()
print()
#Custom SQL User
def customuser():
    global root
    ans1=input("Did you set up an account during installation?\nIf not, the root user will be used (y/n): ")
    while ans1 not in ["Y","y","n","N"]:
        ans1=input("Please enter (y/n): ")
    if ans1 in ["y","Y"]:
        root=input("Enter your Username: ")
    else:
        root="root"
customuser()
#Database Password Entry
def password():
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
mycursor=mydb.cursor()
if os.path.exists("Logs.txt"):
    pass
else:
    f=open("Logs.txt","w")
#Yusra will do here
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
mycursor.execute("show tables")
i=() #Empty Tuple works only in 3.8.3
for i in mycursor:
    pass
if 'acc' not in i:
    mycursor.execute("create table acc(accno INTEGER PRIMARY KEY,name varchar(20),password varchar(1000),mainbal INTEGER DEFAULT 0,savings INTEGER DEFAULT 0,deptotal INTEGER DEFAULT 0,withtotal INTEGER DEFAULT 0)")
main=''
print("Database connected successfully...\n\nMainConsole")
#Main Console
log=0
att=4
while main!='/quit':
    main=input(">>>")
    if main=='/help':
        print("/register")
        print("/cancel acc")
        print("/login")
        print("/logout")
        print("/deposit")
        print("/withdraw")
        print("/transfer")
        print("/balance")
        print("/stat")
        print("/enteradmin or /godmode")
        print("/quit")
        print("/change pass")
        print("/change username")
        print("/about")
    elif main=="":
        continue
    elif main=="/about":
        print("WAY Banks Limited")
        print("Project Developed by - Akash, Wahab, Yusra")
    elif "/register" in main:
        register(main)
    elif "/login" in main:
        if log==1:
            print("A current session is already logged in. Please logout by /logout.")
        else:
            log=login(main)
    elif "/deposit" in main:
        deposit(main)
    elif "/withdraw" in main:
        withdraw(main)
    elif "/transfer" in main:
        transfer(main)
    elif main=="/logout":
        if log==0:
            print("Please login first!")
            main=''
        elif log==1:
            print("You have successfully logged out...")
            log=0
            main=''
    elif main=="/quit":
        if log==1:
            print("You have successfully logged out...")
            log=0
        print("Thank you for using WAY Banks Ltd. User logs saved.")
        print("Developed by Akash, Wahab, Yusra.")
        print("Program will terminate shortly.")
        time.sleep(4)
        quit()
    else:
        print(main,"is not recognised as a valid command.\nTry /help to get a list of all the valid commands")
    
