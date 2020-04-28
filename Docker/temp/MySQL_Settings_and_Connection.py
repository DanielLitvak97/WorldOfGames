#from pymysql import 11111connect
import pymysql
from time import sleep
sleep(120)

#Connect to the MySQL and create a database
conn = pymysql.connect(host='db-mysql', port=3306, user='root', passwd='Password123', autocommit=True)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE games;")
cursor.close()

#Connect to the MySQL and create a table
conn = pymysql.connect(host='172.17.0.3', port=3306, user='root', passwd='Password123', db='games', autocommit=True)
cursor = conn.cursor()
cursor.execute("CREATE TABLE users_scores (score INTEGER);")
cursor.close()
