import paramiko
import os
import stat

def server_connection():
    try:
        hostname = '10.48.19.56'
        port = 5522
        username = 'kpmg'
        password = '*Wur8ks%!YQjq9'

        # Create new SSH client
        ssh_client = paramiko.SSHClient()

        # Automatically add host keys
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to server
        ssh_client.connect(hostname, port, username, password)

        print('Connected')
        return ssh_client
    
    except paramiko.AuthenticationException:
        print('Authentication failed, please check username and password')
        return None
    except paramiko.SSHException as e:
        print('SSH connection failed:', e)
        return None
    except Exception as e:
        print('Error 1:', e)
        return None
    

def traverse_directories(ssh_client, base_directory):
    try:
        sftp = ssh_client.open_sftp()
        
        # Traverse directories recursively
        for item in sftp.listdir_attr(base_directory):
            # Check if it's a directory
            if stat.S_ISDIR(item.st_mode):
                if item.filename.endswith("-AP-Production"):
                    print("Directory:", os.path.join(base_directory, item.filename))
                    # Traverse the directory
                    traverse_directories(ssh_client, os.path.join(base_directory, item.filename))
            # It's a file
            else:
                print("File:", os.path.join(base_directory, item.filename))
        
        sftp.close()

    except Exception as e:
        print("Error:", e)


ssh_client = server_connection()
if ssh_client:
    base_directory = "/"  # Specify the base directory
    traverse_directories(ssh_client, base_directory)
else:
    print('Connection failed, check the error messages')
