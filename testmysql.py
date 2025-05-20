import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Frirea1k17"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
