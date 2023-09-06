import paramiko
import os

# Configura tus credenciales y detalles del servidor SSH
ssh_host = 'HOST'
ssh_port = 22
ssh_user = 'USER'
ssh_password = 'PASS'

# Configura el archivo y directorios
local_file_aux_diario = 'C:/Users/dolmedo/ftp/icaro/N_aux_diario.txt'
local_file_control_de_presencia = 'C:/Users/dolmedo/ftp/icaro/N_control_de_presencia.txt'
local_file_rastreo_por_localidad_1 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_1.txt'
local_file_rastreo_por_localidad_2 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_2.txt'
local_file_rastreo_por_localidad_3 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_3.txt'
local_file_rastreo_por_localidad_4 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_4.txt'
local_file_rastreo_por_localidad_5 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_5.txt'
local_file_rastreo_por_localidad_6 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_6.txt'
local_file_rastreo_por_localidad_7 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_7.txt'
local_file_rastreo_por_localidad_8 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_8.txt'
local_file_rastreo_por_localidad_9 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_9.txt'
local_file_rastreo_por_localidad_10 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_10.txt'
local_file_rastreo_por_localidad_11 = 'C:/Users/dolmedo/ftp/icaro/N_rastreo_por_localidad_11.txt'
local_file_control_de_presencia_logout = 'C:/Users/dolmedo/ftp/icaro/N_control_de_presencia_logout.txt'
remote_directory = '/datos/htdocs/reporting_total/TyS_txt'
remote_directory_aux = '/datos/htdocs/reporting_total/Planificacion_txt'
remote_file_aux_diario = f'{remote_directory_aux}/{os.path.basename(local_file_aux_diario)}'
remote_file_control_de_presencia = f'{remote_directory}/{os.path.basename(local_file_control_de_presencia)}'
remote_file_rastreo_por_localidad_1 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_1)}'
remote_file_rastreo_por_localidad_2 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_2)}'
remote_file_rastreo_por_localidad_3 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_3)}'
remote_file_rastreo_por_localidad_4 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_4)}'
remote_file_rastreo_por_localidad_5 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_5)}'
remote_file_rastreo_por_localidad_6 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_6)}'
remote_file_rastreo_por_localidad_7 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_7)}'
remote_file_rastreo_por_localidad_8 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_8)}'
remote_file_rastreo_por_localidad_9 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_9)}'
remote_file_rastreo_por_localidad_10 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_10)}'
remote_file_rastreo_por_localidad_11 = f'{remote_directory}/{os.path.basename(local_file_rastreo_por_localidad_11)}'
remote_file_control_de_presencia_logout = f'{remote_directory}/{os.path.basename(local_file_control_de_presencia_logout)}'

# Crea una conexión SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_host, port=ssh_port, username=ssh_user, password=ssh_password)

# Crea una conexión SFTP
sftp = ssh.open_sftp()

# Obtener la lista de archivos y carpetas en la carpeta remota
lista_archivos = sftp.listdir(remote_directory)

# Eliminar cada archivo y carpeta en la carpeta remota
for archivo in lista_archivos:
    ruta_archivo = remote_directory + '/' + archivo
    sftp.remove(ruta_archivo)


# Verificar si el archivo existe
comando = f'test -f {remote_file_aux_diario} && echo "Archivo encontrado" || echo "Archivo no encontrado"'
stdin, stdout, stderr = ssh.exec_command(comando)

# Leer la salida del comando
salida = stdout.read().decode().strip()

# Comprobar si el archivo existe
if salida == "Archivo encontrado":
    sftp.remove(remote_file_aux_diario)
else:
    print(f"El archivo {remote_file_aux_diario} no existe en el servidor remoto.")


# Copia el archivo local al servidor Unix
sftp.put(local_file_aux_diario, remote_file_aux_diario)
sftp.put(local_file_control_de_presencia, remote_file_control_de_presencia)
sftp.put(local_file_rastreo_por_localidad_1, remote_file_rastreo_por_localidad_1)
sftp.put(local_file_rastreo_por_localidad_2, remote_file_rastreo_por_localidad_2)
sftp.put(local_file_rastreo_por_localidad_3, remote_file_rastreo_por_localidad_3)
sftp.put(local_file_rastreo_por_localidad_4, remote_file_rastreo_por_localidad_4)
sftp.put(local_file_rastreo_por_localidad_5, remote_file_rastreo_por_localidad_5)
sftp.put(local_file_rastreo_por_localidad_6, remote_file_rastreo_por_localidad_6)
sftp.put(local_file_rastreo_por_localidad_7, remote_file_rastreo_por_localidad_7)
sftp.put(local_file_rastreo_por_localidad_8, remote_file_rastreo_por_localidad_8)
sftp.put(local_file_rastreo_por_localidad_9, remote_file_rastreo_por_localidad_9)
sftp.put(local_file_rastreo_por_localidad_10, remote_file_rastreo_por_localidad_10)
sftp.put(local_file_rastreo_por_localidad_11, remote_file_rastreo_por_localidad_11)
sftp.put(local_file_control_de_presencia_logout, remote_file_control_de_presencia_logout)

# Cierra las conexiones SFTP y SSH
sftp.close()
ssh.close()

#print(f'Archivo {local_file} copiado a {remote_file}')









