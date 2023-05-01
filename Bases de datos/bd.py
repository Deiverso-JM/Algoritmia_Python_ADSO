#Instanciando o conectando a la BD

import mysql.connector

midb=mysql.connector.connect(
    host='localhost',
    user='Johan',
    password='johan12345',
    database='Pruebas'
)

#asignando
cursor=midb.cursor()

# Listar datos
#cursor.execute('select * from Usuario')
# Fetchall TODOS  --- Fetchone UNO SOLO
# resultado= cursor.fetchall() 
# print(resultado)

#Limites

# cursor.execute('select * from Usuario limit 1')
# Resultado = cursor.fetchall()
# print(Resultado)

#Ver deficiones de tablas
#cursor.execute('show create table Usuario')


#Insertando a la BD
# sql = 'insert into Usuario (username, gmail, edad) values(%s, %s,%s)'
# values = ('micorreo@correo.co.nz', 'nombreusuario', 45)



#Actualizar los datos
# sql =  'update usuario set username = %s where id = %s'
# values = ('Pabloperes',5)
# cursor.execute(sql,values)

# midb.commit()

#print(cursor.rowcount)


#eliminar datos

# sql = 'delete from usuario where id = %s'
# values = (4,)
# cursor.execute(sql,values)
# midb.commit()