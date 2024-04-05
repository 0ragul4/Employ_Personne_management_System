import mysql.connector
password=1234
username="admin"

connection = mysql.connector.connect(host="localhost",user="root",password="",database="emp_details")

if connection.is_connected():
    print("successfully connected...")
    access = connection.cursor()
    

else:
    print("failed to connect...")



def Main_pgm():
    u_name = input("enter username:")
    passw = int(input("enter password:"))

    if (username==u_name and password==passw):
        print("Successfully logedin...")
        loop=1

        while(loop==1):

            n=int(input("view=1\nAdd=2\nmodify=3\ndelete=4\n n:"))
            
            if n==1:
                id=int(input("enter the id you want to see:"))
                query = str('SELECT * FROM `employees` WHERE Emp_id = ' + str(id))
                access.execute(query)
                result = access.fetchall()
                if result is None:
                    print("No data Found...")
                else:
                    print(result)
            
            elif n==2:
                id = str(input("enter employee id:"))
                name = str(input("enter employee name:"))
                phno= str(input("enter phone no:"))
                salary = str(input("enter salary:"))
                title = str(input("enter the title:"))
                query = f"INSERT INTO `employees` VALUES ('{id}', '{name}' , '{phno}', '{salary}', '{title}')"
                access.execute(query)
                connection.commit()
            
            elif n==3:
                data = int(input("enter what data you want to modify:\n NAME=1:\n PHONE NO:2\n SALARY:3 \n TITTLE:4 \n NO:"))
                id = int(input("enter the employee id you want to modify:"))
                if data==1:
                    name = input("enter the name:")
                    query = f"UPDATE employees SET Emp_Name='{name}' WHERE Emp_id='{id}'"
                    print(query)
                    access.execute(query)
                    connection.commit()

                elif data==2:
                    phno= int(input("enter the phone no:"))
                    query = f"UPDATE employees SET Emp_phno='{phno}' WHERE Emp_id='{id}'"
                    print(query)
                    access.execute(query)
                    connection.commit()

                elif data==3:
                    salry= int(input("enter the Salary:"))
                    query = f"UPDATE employees SET Emp_phno='{salry}' WHERE Emp_id='{id}'"
                    print(query)
                    access.execute(query)
                    connection.commit()

                elif data==4:
                    titil= input("enter the Tittle:")
                    query = f"UPDATE employees SET Emp_Tittle='{titil}' WHERE Emp_id='{id}'"
                    print(query)
                    access.execute(query)
                    connection.commit()

                else:
                    print("Invalid operation")

            elif n==4:
                id = int(input("enter the employee id you want to delete:"))
                query = f"DELETE FROM employees WHERE Emp_id='{id}'"
                print(query)
                access.execute(query)
                connection.commit()

            else:
                print("Invalid operation")
            loop = int(input("To continue press 1 else 0....."))



            
                
Main_pgm()
connection.close()
