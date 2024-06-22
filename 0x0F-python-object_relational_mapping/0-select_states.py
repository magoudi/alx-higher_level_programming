#!/usr/bin/python3
from sys import argv;
import MySQLdb

""" qsdvnlasng bwajkbgjnawskmf"""

db = MySQLdb.connect(
    host="localhost", 
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    charset="utf8"
)

cur = db.cursor()
cur.execute("select * from states")
cur.close()
db.close()