import mysql.connector

midb=mysql.connector.connect(
    host='localhost',
    user='Johan',
    password='johan12345',
    database='Pruebas'
)

cursor=midb.cursor()

cursor.execute('select * from Usuario')

resultado= cursor.fetchone()

print(resultado)