import sys
import MySQLdb
import csv

# Función para conectarme a la base de datos.
def conectar_bd():
    try:
        return MySQLdb.connect("localhost", "root", "", "mariadb")
    except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos", e)
        sys.exit(1)

# Función para eliminar tabla 'datos' en caso de que exista y crear un nueva con 5 columnas.
def crear_tabla(cursor):
    cursor.execute("DROP TABLE IF EXISTS datos")
    cursor.execute("CREATE TABLE datos (provincia VARCHAR(50), id INT, localidad VARCHAR(50), cp INT, id_prov_mstr INT)")

# Función para importar los archivos csv en la BD
def importar_datos_desde_csv(cursor, archivo_csv):
    with open(archivo_csv, newline='') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)
        datos = [tuple(fila) for fila in lector_csv]
        sql = "INSERT INTO datos (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.executemany(sql, datos)
            db.commit()
            print("Datos importados correctamente.")
        except Exception as e:
            print("Error al importar los datos:", e)
            db.rollback()

# Función para agrupar localidades por provincia
def agrupar_localidades_por_provincia(cursor):
    localidades_por_provincia = {}
    cursor.execute("SELECT provincia, localidad FROM datos")
    for provincia, localidad in cursor.fetchall():
        if provincia in localidades_por_provincia:
            localidades_por_provincia[provincia].append(localidad)
        else:
            localidades_por_provincia[provincia] = [localidad]
    return localidades_por_provincia

# Función para exportar localidades por provincia
def exportar_a_csv(localidades_por_provincia):
    for provincia, localidades in localidades_por_provincia.items():
        nombre_archivo = f"{provincia}_localidades.csv"
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['Localidad'])
            escritor_csv.writerows([[localidad] for localidad in localidades])
        print(f"Archivo {nombre_archivo} creado exitosamente.")

# Esta función ejecuta todas las demás funciones.
if __name__ == "__main__":
    db = conectar_bd()
    cursor = db.cursor()
    crear_tabla(cursor)
    importar_datos_desde_csv(cursor, 'localidades.csv')  
    localidades_por_provincia = agrupar_localidades_por_provincia(cursor)
    exportar_a_csv(localidades_por_provincia)
    db.close()



# faltó cambiar excecutemany (para insertar todo de una, es más eficiente para hacer la insercion)