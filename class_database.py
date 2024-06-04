import mysql.connector as mc


def mysqlconnect():
    M = mc.connect(host="localhost",user="root",password="1711",database="amazone")
    return M;