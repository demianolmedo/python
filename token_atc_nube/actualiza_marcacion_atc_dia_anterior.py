import mysql.connector
import datetime

def timedelta_to_hms(delta):
    # Calcula la cantidad total de segundos en el objeto timedelta
    total_seconds = delta.total_seconds()

    # Calcula las horas, minutos y segundos
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    # Retorna el resultado formateado
    return f"{hours:02}:{minutes:02}:{seconds:02}"


# Conexión a la base de datos fuente
source_db = mysql.connector.connect(
    host='89.117.59.147',
    user='datacombo',
    password='D4t4comiano$2023!',
    database='bd_marcaciones',
    charset='utf8'
)

# Conexión a la base de datos destino
destination_db = mysql.connector.connect(
    host='150.1.88.224',
    user='dolmedo',
    password='D4t4c0m',
    database='bdd_semi',
    charset='utf8'
)

# Obtener el cursor de la base de datos fuente
source_cursor = source_db.cursor()

# Obtener el cursor de la base de datos destino
destination_cursor = destination_db.cursor()


########################################################## COPIA SOLO DEL DIA ANTERIOR LA MARCACION DE LA WEB ##################################################################################

# Nombre de la tabla que deseas copiar
table_name_origen = 'tbl_marcacion'
table_name_destino = 'sesiones_web'
# table_name = 'PRUEBA_DEMIAN'
try:
    # Obtener los datos de la tabla de la base de datos fuente
    source_cursor.execute(f'SELECT * FROM {table_name_origen} where fecha_ingreso = DATE_ADD(CURDATE(), INTERVAL -1 DAY) ')
    data = source_cursor.fetchall()

    # Crear la tabla en la base de datos destino si no existe
    #destination_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} LIKE {table_name}")

    # Borra los registros la tabla en la base de datos destino si no existe
    # destination_cursor.execute(f"DELETE FROM {table_name}_PRUEBA")

    
    # Insertar los datos en la tabla de la base de datos destino
    for row in data:

        # convert the tuple to a list
        row_list = list(row)
        #print(row_list) 

        cuenta=0
        for x in row_list:
            if row_list[cuenta] is None:
                row_list[cuenta] = ''
            elif cuenta == 2 or cuenta == 5 :
                row_list[cuenta] = row_list[cuenta].strftime("%Y-%m-%d %H:%M:%S")
            elif cuenta ==3 or cuenta == 6:
                formatted_time = timedelta_to_hms(row_list[cuenta])                 
                row_list[cuenta] = formatted_time
            cuenta += 1

        # convert the list back to a tuple
        row = tuple(row_list)
        # print({row})
        destination_cursor.execute(f"INSERT INTO {table_name_destino} VALUES {row}")        

    # Confirmar los cambios en la base de datos destino
    destination_db.commit()

    print('La tabla ' + table_name_destino + ' se copió correctamente.')
except mysql.connector.Error as err:
    print(f'Error al copiar la tabla: {err}')




# Cerrar las conexiones y los cursores
source_cursor.close()
destination_cursor.close()
source_db.close()
destination_db.close()
