Automated VPN user account expire time setter for Huawei Firewalls

Steps:

1. Update "datafile.txt" with the usernames and the correspoding expiration date according the example format.
2. Run the "main.py" file

Excecution proccess:

1.Convert "datafile.txt" in to a list
2.Check whether the username is available in radius database
3.If so, generate the "command_file.txt" according the given data
4.Connect to the firewall via ssh
5.Excecute the command file on the firewall
6.Write the input and the corresponding outputs to "log.txt" file
