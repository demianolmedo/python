import mysql.connector
import datetime


# Conexión a la base de datos fuente
source_db = mysql.connector.connect(
    host='HOST',
    user='USER',
    password='PASS',
    database='BD_NOMBRE',
    charset='utf8'
)

# Conexión a la base de datos destino
destination_db = mysql.connector.connect(
    host='HOST',
    user='USER',
    password='PASS',
    database='BD_NOMBRE',
    charset='utf8'
)

# Obtener el cursor de la base de datos fuente
source_cursor = source_db.cursor()

# Obtener el cursor de la base de datos destino
destination_cursor = destination_db.cursor()


########################################################## USERS ##################################################################################

# Nombre de la tabla que deseas copiar
table_name = 'SOPORTE'

try:
    # Obtener los datos de la tabla de la base de datos fuente
    source_cursor.execute(f"SELECT S.area, REPLACE(T.integrantes_n,'&bull; ','') NOMBRE, E.MOBILE_TELEPHONE TELEFONO from SOLICITUDES S INNER JOIN tablero T ON S.id=T.id_rel INNER JOIN APPLPORDB.EMPLOYEES E ON E.EMPLOYEE_ID IN (T.integrantes) WHERE S.estado='EN PROCESO' AND (T.estado='PROCESO' OR T.estado='PRUEBAS' OR T.estado='COMPLETADO') AND S.id in (2070,2078,2083) and CURDATE() BETWEEN T.fecha_ini and T.fecha_fin")
    data = source_cursor.fetchall()

    # Crear la tabla en la base de datos destino si no existe
    #destination_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} LIKE {table_name}")

    # Borra los registros la tabla en la base de datos destino si no existe
    destination_cursor.execute(f"DELETE FROM {table_name}")

    
    # Insertar los datos en la tabla de la base de datos destino
    for row in data:

        
        # convert the tuple to a list
        row_list = list(row)
        #print(row_list) 

        cuenta=0
        for x in row_list:
            if row_list[cuenta] is None:
                row_list[cuenta] = ''
            cuenta += 1

        # convert the list back to a tuple
        row = tuple(row_list)
        # print({row})

        destination_cursor.execute(f"INSERT INTO {table_name} VALUES {row}")        

    # Confirmar los cambios en la base de datos destino
    destination_db.commit()

    print('La tabla ' + table_name + ' se copió correctamente.')
except mysql.connector.Error as err:
    print(f'Error al copiar la tabla: {err}')







# Cerrar las conexiones y los cursores
source_cursor.close()
destination_cursor.close()
source_db.close()
destination_db.close()
