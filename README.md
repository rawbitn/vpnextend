This solution is implemented for Huawei Eudemon1000E Firewall series where the user activation can be done using GUI or CLI and user authentication happens with a FreeRADIUS server with MySQL DB . For each user, a static IP is configured in the Database and it will send to the Firewall with radius reply.

Following steps explains how to use this programme.

#1. Ensure that Python 3 and connectivity to the VPN GW (ssh/tcp 22) is available for the environment where you plan to run code.

#2. Update "datafile.txt" with the usernames and the corresponding expiration date according the format "<username><space><expiration date>". Sample format file is available in initial "datafile.txt".

#3. Run the "main.py" file

Execution proccess.

1. Convert "datafile.txt" in to a list 
2. Check whether the username is available in radius database 
3. If so, generate the "command_file.txt" according the given data 
4. Connect to the firewall via ssh 
5. Excecute the command file on the firewall 
6. Write the input and the corresponding outputs to "log.txt" file
