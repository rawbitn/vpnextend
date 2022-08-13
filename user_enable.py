import mysqlconn
import sshconn
logfile = 'log.txt'
command_file = 'command_file.txt'
datafile_name = 'datafile.txt'
datafile = open(datafile_name, "r+")
print("Reading 'datafile.txt'.......",end='')
user_array = datafile.readlines()
print('Done')
len_user_array = len(user_array)
print("Querying MySQL database and fetching configurations to the device.......")
for i in range(0,len_user_array):
    tmp_data_array = user_array[i].split()
    user_name = str(tmp_data_array[0])
    expire_date = str(tmp_data_array[1])
    db_return_code = mysqlconn.getavailable_usernames(user_name,logfile)
    if db_return_code == True:
        script = open(command_file,'w+')
        command = '#' + '\n' + 'sys' + '\n' + 'user-manage user ' + user_name + ' domain sslvpn' + '\n' + 'expire-time ' + expire_date + '\n' + '#'
        script.writelines(command)
        script.close()
        sshconn.ssh_connect('192.168.0.1','username','Password',command_file,logfile)
        print('Info: User extended, ' + user_name)
    else:
        print('')
        print('Error: Invalid User Name, ' + user_name)
datafile.close()