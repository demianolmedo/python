import mysql.connector
import datetime


# Conexión a la base de datos fuente
source_db = mysql.connector.connect(
    host='HOST',
    user='USER',
    password='PASS',
    database='BD_NAME',
    charset='utf8'
)

# Conexión a la base de datos destino
destination_db = mysql.connector.connect(
    host='HOST',
    user='USER',
    password='PASS',
    database='BD_NAME',
    charset='utf8'
)

# Obtener el cursor de la base de datos fuente
source_cursor = source_db.cursor()

# Obtener el cursor de la base de datos destino
destination_cursor = destination_db.cursor()


########################################################## USERS ##################################################################################

# Nombre de la tabla que deseas copiar
table_name = 'USERS'
# table_name = 'PRUEBA_DEMIAN'
try:
    # Obtener los datos de la tabla de la base de datos fuente
    source_cursor.execute(f'SELECT * FROM {table_name}')
    data = source_cursor.fetchall()

    # Crear la tabla en la base de datos destino si no existe
    #destination_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} LIKE {table_name}")

    # Borra los registros la tabla en la base de datos destino si no existe
    destination_cursor.execute(f"DELETE FROM {table_name}_PRUEBA")

    
    # Insertar los datos en la tabla de la base de datos destino
    for row in data:

        # convert the tuple to a list
        row_list = list(row)
        #print(row_list) 

        cuenta=0
        for x in row_list:
            if row_list[cuenta] is None:
                row_list[cuenta] = ''
            elif cuenta == 3 or cuenta == 5 or cuenta == 9 or cuenta == 10 or cuenta == 11 or cuenta == 13 or cuenta == 29 or cuenta == 30 or cuenta == 31 :
                row_list[cuenta] = row_list[cuenta].strftime("%Y-%m-%d %H:%M:%S")
            cuenta += 1

        # convert the list back to a tuple
        row = tuple(row_list)
        # print({row})
        destination_cursor.execute(f"INSERT INTO {table_name}_PRUEBA VALUES {row}")        

    # Confirmar los cambios en la base de datos destino
    destination_db.commit()

    print('La tabla ' + table_name + ' se copió correctamente.')
except mysql.connector.Error as err:
    print(f'Error al copiar la tabla: {err}')


    ########################################################## EMPLOYEES ##################################################################################

# Nombre de la tabla que deseas copiar
table_name = 'EMPLOYEES'
# table_name = 'PRUEBA_DEMIAN'
try:
    # Obtener los datos de la tabla de la base de datos fuente
    source_cursor.execute(f'SELECT * FROM {table_name}')
    data = source_cursor.fetchall()

    # Crear la tabla en la base de datos destino si no existe
    #destination_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} LIKE {table_name}")

    # Borra los registros la tabla en la base de datos destino si no existe
    destination_cursor.execute(f"DELETE FROM {table_name}_PRUEBA")

    
    # Insertar los datos en la tabla de la base de datos destino
    for row in data:

        # convert the tuple to a list
        row_list = list(row)
        #print(row_list) 

        cuenta=0
        for x in row_list:
            if row_list[cuenta] is None:
                row_list[cuenta] = ''
            elif cuenta == 5 or cuenta == 7 or cuenta == 15 or cuenta == 16 or cuenta == 17 or cuenta == 18 or cuenta == 20 or cuenta == 21 or cuenta == 24 or cuenta == 24 or cuenta == 32 or cuenta == 54 or cuenta == 55 :
                row_list[cuenta] = row_list[cuenta].strftime("%Y-%m-%d %H:%M:%S")
            cuenta += 1

        # convert the list back to a tuple
        row = tuple(row_list)
        # print({row})
        destination_cursor.execute(f"INSERT INTO {table_name}_PRUEBA VALUES {row}")        

    # Confirmar los cambios en la base de datos destino
    destination_db.commit()

    print('La tabla ' + table_name + ' se copió correctamente.')
except mysql.connector.Error as err:
    print(f'Error al copiar la tabla: {err}')



    ########################################################## PERSONS ##################################################################################

    # Nombre de la tabla que deseas copiar
table_name = 'PERSONS'
# table_name = 'PRUEBA_DEMIAN'
try:
    # Obtener los datos de la tabla de la base de datos fuente
    source_cursor.execute(f'SELECT * FROM {table_name}')
    data = source_cursor.fetchall()

    # Crear la tabla en la base de datos destino si no existe
    #destination_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} LIKE {table_name}")

    # Borra los registros la tabla en la base de datos destino si no existe
    destination_cursor.execute(f"DELETE FROM {table_name}_PRUEBA")

    
    # Insertar los datos en la tabla de la base de datos destino
    for row in data:

        # convert the tuple to a list
        row_list = list(row)
        #print(row_list) 

        cuenta=0
        for x in row_list:
            if row_list[cuenta] is None:
                row_list[cuenta] = ''
            elif cuenta == 5 or cuenta == 7 or cuenta == 9 or cuenta == 14 or cuenta == 39 or cuenta == 51 :
                row_list[cuenta] = row_list[cuenta].strftime("%Y-%m-%d %H:%M:%S")
            cuenta += 1

        # convert the list back to a tuple
        row = tuple(row_list)
        # print({row})
        destination_cursor.execute(f"INSERT INTO {table_name}_PRUEBA VALUES {row}")        

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
