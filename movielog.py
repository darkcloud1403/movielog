import mysql.connector as sql
import pandas as pd
pas= input("Enter your mysql password: ")

try:
    mydb=sql.connect(host='localhost',user='root',password=pas)
    cur = mydb.cursor() 
except:
    print("Incorrect password")
    exit()
    


try: 
     mydb.autocommit = True
     cur.execute("create database show_db")
     cur.execute("use show_db")
     cur.execute("create table Login_id(User_name varchar(20) primary key ,password varchar(20))")
     cur.execute("create table show_table (Name varchar(40),Genre varchar(20),Status varchar(20), Score int(2), TV_or_Movie varchar(10))")
except:
     cur.execute("use show_db")

def reg_log():
     print('''
======================== WELCOME TO MOVIELOG =======================

     1. Register

     2. Login

     3. Exit
     
========================================================================
     ''')

     n=int(input('Enter your choice: '))


     if n== 1:
          name=input('Enter a Unique Username: ')
          passwd=int(input('Enter a Password: '))
          sql_insert="INSERT INTO Login_id (user_name,password) values ('{}','{}')".format(name,passwd)
          cur.execute(sql_insert)
          mydb.commit()
          print("User created succesfully")
          input("Press Enter to continue...")
          reg_log()

     elif  n==2 :
          name=input('Enter your Username: ')
          passwd=int(input('Enter your Password: '))
          cur.execute("select * from Login_id where user_name= '{}' and password='{}'".format(name,passwd))
          exist = cur.fetchall()

          if exist == []:
               print('Invalid username or password')
          else:
               print("Logged in!")
               menu()

     elif  n==3:
          print("THANK YOU!!")
          exit()

     else:
          print('''
Incorrect input
Try again!
''')   
          input("Press Enter to continue...")
          reg_log()
       
         
def display_all():
    cur.execute("select * from show_table")
    results=cur.fetchall()
    mydb.commit()
    df = pd.DataFrame(results, columns=cur.column_names)
    print(df)
    input("Press Enter to continue...")
    menu()    
    
    
def display_tv():
    cur.execute("select * from show_table where TV_or_Movie = 'TV Show' ")
    results=cur.fetchall()
    mydb.commit()
    df = pd.DataFrame(results, columns=cur.column_names)
    print(df)
    input("Press Enter to continue...")
    menu() 

def display_mov():
    cur.execute("select * from show_table where TV_or_Movie = 'Movie' ")
    results=cur.fetchall()
    mydb.commit()
    df = pd.DataFrame(results, columns=cur.column_names)
    print(df)
    input("Press Enter to continue...")
    menu() 
        
def add_show():
    name=input ("Enter the name of the show: ")
    genre=input( "Enter the genre of the show: ")
    status=input( "Enter the status of the show: ")
    score=int(input("Enter the score of the show out of 10:"))
    tvormov= int(input('''
It is a
    1. TV show
    2. Movie
->Enter the choice: 
                '''))
    if tvormov ==1:
        tv_mov = "TV Show"
    elif tvormov ==2:
        tv_mov = "Movie"   
    else:
        print('''
            Incorrect input
            Try again!
            ''')
        
    sql_insert="insert into show_table values('{}','{}','{}','{}','{}')".format(name,genre,status,score,tv_mov)
    cur.execute(sql_insert)
    mydb.commit()
    print("Show added successfully!")
    input("Press Enter to continue...")
    menu() 

def modify_menu():
    print(
'''============================= MOVIELOG =============================

    1. Change name of the movie

    2. Change genre of the movie

    3. Change status of the movie

    4. Change score of the movie

    5. Change type of the movie

    6. Back

    7. Exit

========================================================================
    ''')
            
    choice=int(input("->Enter the choice: "))  
    if choice==1:
        old_name= input("Enter the name of the movie you want to change: ")
        new_name= input(f"Enter the new name of {old_name}: ")
        cur.execute("update show_table set name = '{}' where name = '{}' ".format(new_name,old_name))
        mydb.commit()
        
    elif choice==2:
        old_name= input("Enter the name of the movie whose genre you want to change: ")
        new_genre= input(f"Enter the new genre of {old_name}: ")
        cur.execute("update show_table set genre = '{}' where name = '{}' ".format(new_genre,old_name))
        mydb.commit()
        
    elif choice==3:
        old_name= input("Enter the name of the movie whose status you want to change: ")
        new_status= input(f"Enter the new status of {old_name}: ")
        cur.execute("update show_table set status = '{}' where name = '{}' ".format(new_status,old_name))
        mydb.commit()
        
    elif choice==4:
        old_name= input("Enter the name of the movie whose score you want to change: ")
        new_score= input(f"Enter the new score of {old_name}: ")
        cur.execute("update show_table set score = '{}' where name = '{}' ".format(new_score,old_name))
        mydb.commit()
        
    elif choice==5:
        old_name= input("Enter the name of the movie whose type you want to change: ")
        tvormov= int(input('''
It is a
    1. TV show
    2. Movie
->Enter the choice: 
                '''))
        if tvormov ==1:
            cur.execute("update show_table set TV_or_Movie = 'TV Show' where name = '{}' ".format(old_name))
            mydb.commit()
        elif tvormov ==2:
            cur.execute("update show_table set TV_or_Movie = 'Movie' where name = '{}' ".format(old_name))
            mydb.commit()
        else:
            print('''
Incorrect input
Try again!
                ''')
        input("Press Enter to continue...")
        menu()           
            
            
    elif choice==6:
        menu()
    elif choice==7:
        print("THANK YOU!")
        exit()
    else:
        print('''
Incorrect input
Try again!
''')
    input("Press Enter to continue...")
    menu() 
        

def delete_show():
    delete_row_name= input("Enter the name of the show you want to delete: ")
    cur.execute("delete from show_table where name = '{}' ".format(delete_row_name))
    mydb.commit()
    input("Press Enter to continue...")
    menu() 
    
def user_list():
    cur.execute("select user_name from Login_id order by user_name asc")
    user=cur.fetchall()
    df = pd.DataFrame(user, columns=cur.column_names)
    print(df)
    input("Press Enter to continue...")
    menu() 
    
def menu():
    print(
'''============================= MOVIE LOG =============================

    1. Display all the shows

    2. Display TV shows

    3. Display Movies

    4. Add a show

    5. Modify a show

    6. Delete a show

    7. Users list

    8. Exit
    
========================================================================
    ''')
    
    choice=int(input("->Enter the choice: "))  
    if choice==1:
        display_all()
    elif choice==2:
        display_tv()
    elif choice==3:
        display_mov()
    elif choice==4:
        add_show()
    elif choice==5:
        modify_menu()
    elif choice==6:
        delete_show()
    elif choice==7:
        user_list()
    elif choice==8:
        print("THANK YOU!!")
        exit()   
    else:
        print('''
Incorrect input
Try again!
''')
    input("Press Enter to continue...")
    menu() 

def main():
    reg_log()
            
if __name__ == "__main__":
    main()


    

    


    



    
