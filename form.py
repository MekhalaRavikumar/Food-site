#!C:\python 311\python.exe

import cgi
import mysql.connector
print("Content-type:text/html\r\n\r\n")


print("<html>")
print("<body>")

form=cgi.FieldStorage()
fname=form.getvalue("name")
femail=form.getvalue("email")
fphone=form.getvalue("phone")
fquantity=form.getvalue("quantity")
ffood=form.getvalue("food")
faddress=form.getvalue("address")

mydb=mysql.connector.connect(
           host="localhost",
           user="root",
           password="",
           database="speedy"
           )

mycursor=mydb.cursor()
sql="Insert into items(Name,Email,Phone,Quantity,Food,Address)values(%s,%s,%s,%s,%s,%s)"
val=(fname,femail,fphone,fquantity,ffood,faddress)

mycursor.execute(sql,val)
mydb.commit()

print("<h1>",fname,femail,fphone,fquantity,ffood,faddress,"</h1>")
print("</body>")
print("</html>")