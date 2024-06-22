#!/usr/bin/python3

"""lsfjglaerjsglasglnvlsrnljeargsV"""


from sys import argv
import MYSQLdb as mdb

if __name__ == "__main__":
    curr = mdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")

    cur = curr.cursor()
    cur.excute("SELECT * FROM")
