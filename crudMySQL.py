import pymysql

#conexion
mydb = pymysql.connect(host = "localhost", user = "root", password = "", database = "crud")
print(mydb)

#crear tabla
cursor = mydb.cursor()
cursor.execute("CREATE TABLE tbproductos (codigo VARCHAR(40), nombre VARCHAR(100), valorunidad INT, stock INT)")

#mostar tablas
cursor.execute("SHOW TABLES")
for name in cursor:
    print(name)

#llave primaria
cursor.exceute("ALTER TABLE tbproductos ADD PRIMARY KEY(codigo)")

#insert
sql = "INSERT INTO tbproductos(codigo, nombre, valorunidad, stock) VALUES(%s, %s, %s, %s)"
val = ("GR-0001", "Arroz Roa 5kg", 15000, 10)
cursor.execute(sql, val)
mydb.commt()
print("Registro insertado: ", cursor.rowcount)

#insertar varias filas
val = [("GR-0002", "Maiz", 15000, 100), ("GR-0003", "Frijoles", 15000, 200), ("GR-0004", "Lentejas", 15000, 300), ("GR-0005", "Garbanzos", 15000, 400), ("GR-0006", "Arberjas", 15000, 500)]
cursor.executemany(sql, val)
mydb.commt()
print("Registro insertado: ", cursor.rowcount)