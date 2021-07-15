import cx_Oracle

#conn = cx_Oracle.connect('HR/HR@//localhost:1521/orcl')
conn = cx_Oracle.connect('test_dev/1234@//localhost:1521/orcl')
#print(conn.version)

#create cursor

cur = conn.cursor()

sql_create = """
CREATE TABLE test_dev.CEO_DETAILS
(
FIRST_NAME VARCHAR2(50),
LAST_NAME VARCHAR2(50),
COMPANY VARCHAR2(50),
AGE NUMBER
)
"""

cur.execute(sql_create)

print('Table Created.')

