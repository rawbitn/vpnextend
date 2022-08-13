import time
import paramiko
import datetime

def ssh_connect(ipaddress,username,password,command_file,logfile):
    log_file = open(logfile, 'a+')
    ssh_connection = paramiko.SSHClient()
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connection.connect(ipaddress, port=22, username=username, password=password)
    ssh_connection = ssh_connection.invoke_shell()
    output = ssh_connection.recv(65535)
    commands = open(command_file,'r+')
    command_array = commands.readlines()
    len_command_array = len(command_array)
    for i in range(0,len_command_array):
        log_file.writelines(str(datetime.datetime.now()) + str(command_array[i]))
        ssh_connection.send(command_array[i].encode("utf-8"))
        time.sleep(.6)
        output = ssh_connection.recv(65535).decode("utf-8")
        log_file.writelines(str(datetime.datetime.now()) + str(output))
    ssh_connection.close()
    commands.close()
    log_file.close()