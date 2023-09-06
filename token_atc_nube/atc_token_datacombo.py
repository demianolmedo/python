import mysql.connector
import datetime


# Conexión a la base de datos fuente
source_db = mysql.connector.connect(
    host='150.1.88.224',
    user='dolmedo',
    password='D4t4c0m',
    database='APPLPORDB',
    charset='utf8'
)

# Conexión a la base de datos destino
destination_db = mysql.connector.connect(
    host='89.117.59.147',
    user='datacombo',
    password='D4t4comiano$2023!',
    database='CORE',
    charset='utf8'
)

# Obtener el cursor de la base de datos fuente
source_cursor = source_db.cursor()

# Obtener el cursor de la base de datos destino
destination_cursor = destination_db.cursor()


########################################################## USERS ##################################################################################

# Nombre de la tabla que deseas copiar
table_name = 'TOKEN'

try:
    # Obtener los datos de la tabla de la base de datos fuente
    source_cursor.execute(f"SELECT U.ENCRYPTED_USER_PASSWORD,U.ENCRYPTED_FOUNDATION_PASSWORD,U.USER_ID,U.USER_NAME,U.DESCRIPTION,U.EMAIL_ADDRESS,U.LOGIN_CMS,E.EMPLOYEE_NUM,U.L1_ORGANIZACION,U.L2_DEPARTAMENTO,U.L3_AREA,U.L4_GERENCIA, U.L5_UNIDAD,U.L6_PLATAFORMA,U.L7_CARGO,A.area,P.plataforma as PLATAFORMA,L.unidad AS UNIDAD,E.IDREL_SUPERVISOR,SUPERVISOR.DESCRIPTION AS NOM_SUPERVISOR, SUPERVISOR.EMAIL_ADDRESS AS EMAIL_SUPERVISOR,E.IDREL_COORDINADOR,COORDINADOR.DESCRIPTION AS NOM_COORDINADOR,COORDINADOR.EMAIL_ADDRESS AS EMAIL_COORDINADOR, JEFE_SUP.USER_ID AS ID_JEFE_SUP,JEFE_SUP.DESCRIPTION AS NOM_JEFE_SUP,JEFE_SUP.EMAIL_ADDRESS AS EMAIL_JEFE_SUP, PE.AP_PICTURE1, E.MOBILE_TELEPHONE, E.PERSONAL_CELLPHONE FROM USERS U INNER JOIN EMPLOYEES E ON U.USER_ID=E.EMPLOYEE_ID INNER JOIN L6_PLATAFORMA P ON P.id_auto=U.L6_PLATAFORMA INNER JOIN L3_AREA A ON A.id_auto=U.L3_AREA INNER JOIN L5_UNIDAD L ON L.id_auto=U.L5_UNIDAD LEFT JOIN USERS SUPERVISOR ON SUPERVISOR.USER_ID=E.IDREL_SUPERVISOR LEFT JOIN USERS COORDINADOR ON COORDINADOR.USER_ID=E.IDREL_COORDINADOR LEFT JOIN EMPLOYEES EMPSUPERVISOR ON EMPSUPERVISOR.EMPLOYEE_ID=SUPERVISOR.USER_ID LEFT JOIN USERS JEFE_SUP ON JEFE_SUP.USER_ID=EMPSUPERVISOR.IDREL_SUPERVISOR LEFT JOIN PERSONS PE ON U.EMPLOYEE_ID=PE.PERSON_ID WHERE (    (U.END_DATE = '0000-00-00 00:00:00') AND ((U.BLOCKED_ACCESS > NOW()) or (U.BLOCKED_ACCESS = '0000-00-00 00:00:00')));")
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
