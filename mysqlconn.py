import mysql.connector
import datetime
def getavailable_usernames(username,logfile):
    log_file = open(logfile,'a+')
    return_value = False
    mydb = mysql.connector.connect(host="0.0.0.0", user="username", passwd="password",
                                   database="dbname", charset="utf8")
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