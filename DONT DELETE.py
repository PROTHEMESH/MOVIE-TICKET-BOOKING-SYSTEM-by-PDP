# for askingname and number of tickets
print("####### HELLO! Welcome to PDP theaters ######")
print('')
print('')
y=input("pls enter your name: ")
print('')
print('')
print("how many tickets do you want ?")
z=int(input("enter number of tickets: "))


# This function is used for choosing the city
def city():
    print("")
    print("")
    print("In which City You wish to watch the movie ?")
    print("1,pune")
    print("2,mumbai")
    print("3,kolhapur")
    global p
    
    x=int(input("enter your choice:  "))
    if x==1:
        p="pune"
    elif x==2:
        p="mumbai"
    elif x==3:
        p="kolhapur"
    else:
        print("***invalid choice***")
        p=""
    return p   
    

# This function is used for choosing the type of theatre
def which():
    print("In which type of theatre you want to watch the movie ?")
    print("")
    print("")
    print("1,INOX")
    print("2,PvR")
    print("3,4DX")
    global q
    
    x=int(input("enter your choice: "))
    if x==1:
        q="INOX"
    elif x==2:
        q="PvR"
    elif x==3:
        q="4DX"
    else:
        print("***invalid choice***")
        q=""
    return q    


#this function is used forchoosing ehich type of screen do you want    
def screen():
    print("which screen do you prefer ?")
    print('')
    print('')
    print("1, 3D with A/C")
    print("2, 3D NON A/C")
    print("3, 2D with A/C")
    print("4, 2D NON A/C")
    
    global r
    x=int(input("enter your choice : "))
    if x==1:
        r="3D with A/C"
    if x==2:
        r="3D NON A/C"
    if x==3:
        r="2D with A/C"
    if x==4:
        r="2D NON A/C"
    return r    


#for asking which movie do you want to see
def movie():
    print("Availaible Movies are :- ")
    print("1, MOVIE#1")
    print("2, MOVIE#2")
    print("3, MOVIE#3")
    print("4, MOVIE#4")
    print("5, MOVIE#5")
    print("Which movie do you want to see ?")
    x=int(input("enter your choice: "))
    
    global s
    if x==1:
        s="MOVIE#1"
    if x==2:
        s="MOVIE#2"
    if x==3:
        s="MOVIE#3"
    if x==4:
        s="MOVIE#4"
    if x==5:
        s="MOVIE#5"
    return s    


#for asking your suitable time to watch the movie
def time():
    print("choose the time for the movie")
    global t
    if s=="MOVIE#1":
        print("1, 10:30-12:00")
        print("2, 12:30-14:00")
        print("3, 14:30-16:30")
        x=int(input("enter your choice: "))
        if x==1:
            t="10:30-12:00"
        if x==2:
            t="12:30-14:00"
        if x==3:
            t="14:30-16:00"
            
    if s=="MOVIE#2":
        print("1, 11:30-13:00")
        print("2, 13:30-15:00")
        print("3, 15:30-17:30")
        x=int(input("enter your choice: "))
        if x==1:
            t="11:30-13:00"
        if x==2:
            t="13:30-15:00"
        if x==3:
            t="15:30-17:00"   
            
            
    if s=="MOVIE#3":
        print("1, 9:30-11:00")
        print("2, 11:30-13:00")
        print("3, 13:30-15:30")
        x=int(input("enter your choice: "))
        if x==1:
            t="9:30-11:00"
        if x==2:
            t="11:30-13:00"
        if x==3:
            t="13:30-15:30"
            
    if s=="MOVIE#4":
        print("1, 10:00-12:00")
        print("2, 12:00-14:00")
        print("3, 14:00-16:00")
        x=int(input("enter your choice: "))
        if x==1:
            t="10:00-12:00"
        if x==2:
            t="12:00-14:00"
        if x==3:
            t="14:00-16:00"   
            
            
    if s=="MOVIE#5":
        print("1, 16:30-18:00")
        print("2, 18:30-20:00")
        print("3, 18:30-22:30")
        x=int(input("enter your choice: "))
        if x==1:
            t="16:30-18:00"
        if x==2:
            t="18:30-20:00"
        if x==3:
            t="18:30-22:30"
            
    return t
    
    
#asking confirmation    
def bye():   
    global tell
    c=input("CONFIRM YOUR TICKET BOOKING [Y/N]=  ")
    print("")
    print("")
    if c=="Y" or c=="y":
        print("YOU TICKET IS BOOKED!!!")
        print("ENJOY YOUR MOVIE!!!")
        tell="Y"
    else:
        print("###sorry ticket booking failed###")
        print("###please try again later###")
        tell="N" 
    return tell    
         
#this part is put the all user data in MySql table
tup=(y,z,city(),which(),screen(),movie(),time(),bye())       
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='SYSTEM',database='soft')
cur=con.cursor()
q="insert into mtbs(name,num_of_tickets,city,theatre,screen,movie_name,time,ticket_confirmation) values(%s,%s,%s,%s,%s,%s,%s,%s)"
cur.execute(q,tup)
con.commit()


























