#!C:\python 311\python.exe

import cgi
import mysql.connector
print("Content-type:text/html\r\n\r\n")

print("<html>")
print("<body>")


form=cgi.FieldStorage()
fname=form.getvalue("name")
fage=form.getvalue("age")
fgender=form.getvalue("gender")
fphone=form.getvalue("phone")
femail=form.getvalue("email")
fqualification=form.getvalue("qualification")
fwork=form.getvalue("work")
fexperience=form.getvalue("experience")
farea=form.getvalue("area")

mydb=mysql.connector.connect(
           host="localhost",
           user="root",
           password="",
           database="speedy"
           )

mycursor=mydb.cursor()
sql="Insert into apply(NAME,AGE,GENDER,PHONE,EMAIL,QUALIFICATION,WORK,EXPERIENCE,AREA)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(fname,fage,fgender,fphone,femail,fqualification,fwork,fexperience,farea)

mycursor.execute(sql,val)
mydb.commit()

print("<h1>",fname,fage,fgender,fphone,femail,fqualification,fwork,fexperience,farea,"</h1>")
print("</body>")
print("</html>")   
