import mysql.connector
import datetime

def getavailable_usernames(username,logfile,mysql_host,mysql_user,mysql_password,mysql_db):
    log_file = open(logfile,'a+')
    return_value = False
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_password,
                                   database=mysql_db, charset="utf8")
    mycursor = mydb.cursor()
    sql = "select username from username where username like '%" + username +"%';"
    mycursor.execute(sql)
    myresult = mycursor.fetchall();
    log_file.writelines(str(datetime.datetime.now()) + str(myresult))
    mydb.close();
    len_myresult = len(myresult)
    if len_myresult == 1:
        tmp_return_value = str(myresult[0]).split("'")
        if username == str(tmp_return_value[1]):
            return_value = True
    log_file.close()
    return return_value