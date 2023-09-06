import os
from ftplib import FTP

# Configura tus credenciales y detalles del servidor FTP
ftp_host = 'HOST'
ftp_user = 'USER'
ftp_password = 'PASS'

# Configura el archivo y directorios
remote_file_aux_diario = 'N_aux_diario.txt'
remote_file_control_de_presencia = 'N_control_de_presencia.txt'
remote_file_rastreo_por_localidad_1 = 'N_rastreo_por_localidad_1.txt'
remote_file_rastreo_por_localidad_2 = 'N_rastreo_por_localidad_2.txt'
remote_file_rastreo_por_localidad_3 = 'N_rastreo_por_localidad_3.txt'
remote_file_rastreo_por_localidad_4 = 'N_rastreo_por_localidad_4.txt'
remote_file_rastreo_por_localidad_5 = 'N_rastreo_por_localidad_5.txt'
remote_file_rastreo_por_localidad_6 = 'N_rastreo_por_localidad_6.txt'
remote_file_rastreo_por_localidad_7 = 'N_rastreo_por_localidad_7.txt'
remote_file_rastreo_por_localidad_8 = 'N_rastreo_por_localidad_8.txt'
remote_file_rastreo_por_localidad_9 = 'N_rastreo_por_localidad_9.txt'
remote_file_rastreo_por_localidad_10 = 'N_rastreo_por_localidad_10.txt'
remote_file_rastreo_por_localidad_11 = 'N_rastreo_por_localidad_11.txt'
remote_file_control_de_presencia_logout = 'N_control_de_presencia_logout.txt'
local_directory = 'C:/Users/dolmedo/ftp/icaro'
local_file_aux_diario = os.path.join(local_directory, os.path.basename(remote_file_aux_diario))
local_file_control_de_presencia = os.path.join(local_directory, os.path.basename(remote_file_control_de_presencia))
local_file_rastreo_por_localidad_1= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_1))
local_file_rastreo_por_localidad_2= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_2))
local_file_rastreo_por_localidad_3= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_3))
local_file_rastreo_por_localidad_4= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_4))
local_file_rastreo_por_localidad_5= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_5))
local_file_rastreo_por_localidad_6= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_6))
local_file_rastreo_por_localidad_7= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_7))
local_file_rastreo_por_localidad_8= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_8))
local_file_rastreo_por_localidad_9= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_9))
local_file_rastreo_por_localidad_10= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_10))
local_file_rastreo_por_localidad_11= os.path.join(local_directory, os.path.basename(remote_file_rastreo_por_localidad_11))
local_file_control_de_presencia_logout= os.path.join(local_directory, os.path.basename(remote_file_control_de_presencia_logout))

# Obtenemos la lista de archivos dentro de la carpeta
archivos = os.listdir(local_directory)

# Eliminamos cada archivo de la lista
for archivo in archivos:
    ruta_archivo = os.path.join(local_directory, archivo)
    if os.path.isfile(ruta_archivo):
        os.remove(ruta_archivo)
        print(f"Archivo eliminado: {archivo}")

print("Proceso completado.")

# Conéctate al servidor FTP y autentícate
ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_password)

# Cambia al directorio donde se encuentra el archivo remoto
ftp.cwd(os.path.dirname(remote_file_aux_diario))

# Descarga el archivo de texto y guárdalo en el directorio local
with open(local_file_aux_diario, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_aux_diario}', f.write)



ftp.cwd(os.path.dirname(remote_file_control_de_presencia))
with open(local_file_control_de_presencia, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_control_de_presencia}', f.write)

ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_1))
with open(local_file_rastreo_por_localidad_1, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_1}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_2))
with open(local_file_rastreo_por_localidad_2, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_2}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_3))
with open(local_file_rastreo_por_localidad_3, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_3}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_4))
with open(local_file_rastreo_por_localidad_4, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_4}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_5))
with open(local_file_rastreo_por_localidad_5, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_5}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_6))
with open(local_file_rastreo_por_localidad_6, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_6}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_7))
with open(local_file_rastreo_por_localidad_7, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_7}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_8))
with open(local_file_rastreo_por_localidad_8, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_8}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_9))
with open(local_file_rastreo_por_localidad_9, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_9}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_10))
with open(local_file_rastreo_por_localidad_10, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_10}', f.write)
ftp.cwd(os.path.dirname(remote_file_rastreo_por_localidad_11))
with open(local_file_rastreo_por_localidad_11, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_rastreo_por_localidad_11}', f.write)
ftp.cwd(os.path.dirname(remote_file_control_de_presencia_logout))
with open(local_file_control_de_presencia_logout, 'wb') as f:
    ftp.retrbinary(f'RETR {remote_file_control_de_presencia_logout}', f.write)



# Cierra la conexión FTP
ftp.quit()

# print(f'Archivo {remote_file} copiado a {local_file}')


# from dateutil import parser
# from datetime import datetime, timedelta
# timestamp = ftp.sendcmd('MDTM /remote/path/test.txt')[4:].strip()
# time = parser.parse(timestamp)

# now = datetime.now()
# delta = timedelta(days=1)

# if now - time < delta:
# print('El archivo fue modificado hace menos de un día')
# else:
# print('El archivo no fue modificado hace menos de un día')

# print(time.strftime('%d/%m/%Y %H:%M:%S'))
