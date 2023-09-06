import paramiko

def sftp_copy_files(hostname, port, username, password, remote_path, local_path):
    # Crea una instancia de cliente SFTP
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conecta al servidor SFTP
        client.connect(hostname, port, username, password)
        sftp = client.open_sftp()

        # Lista los archivos remotos en la carpeta
        remote_files = sftp.listdir(remote_path)

        # Copia los archivos remotos a la carpeta local
        for file in remote_files:
            remote_file = remote_path + '/' + file
            local_file = local_path + '/' + file
            sftp.get(remote_file, local_file)
            print(f"Archivo '{file}' copiado exitosamente.")

        # Cierra la conexión SFTP
        sftp.close()
        print("Copia de archivos completada.")

    except paramiko.AuthenticationException:
        print("Error de autenticación. Verifica las credenciales.")
    except paramiko.SSHException as e:
        print(f"Error en la conexión SSH: {str(e)}")
    except Exception as e:
        print(f"Error desconocido: {str(e)}")

    # Cierra la conexión SSH
    client.close()

# Configuración de conexión SFTP
hostname = 'HOST'
port = 22
username = 'USER'
password = 'PASS'
remote_path = '/opt/Avaya/avpom/POManager/public/default/export'
# local_path = 'C:/Users/dolmedo/ftp/nelida'
local_path = 'Z:/REPORTES'

# Llama a la función para copiar los archivos
sftp_copy_files(hostname, port, username, password, remote_path, local_path)


