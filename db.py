import os
import cx_Oracle

#con = cx_Oracle.connect('sv247/BlueTucson@2022@prophet.njit.edu')
dsn = cx_Oracle.makedsn("prophet.njit.edu", 1521, sid="course")
conn = cx_Oracle.connect(user="sv247", password="BlueTucson@2022", dsn=dsn, encoding="UTF-8")

print('Successfully connected to Oracle Database')

#Retrieve Data
cursor=conn.cursor() 

cursor.execute('SELECT * FROM SAVINGS_ACCT')
for acc_no, balance, fixed_int_rt in cursor:
    print("Account number: ", acc_no)
    print("Savings account balance: ", balance)
    print("Fixed Interest Rate:", fixed_int_rt)
conn.close()