import pymysql
db = pymysql.connect('localhost', 'root', 'kindness', 'Mahiti_task')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS plotHub")

sql = """CREATE TABLE plotHub(
     id INT NOT NULL UNIQUE,
     plotType CHAR(20) NOT  NULL,
     area FLOAT,
     name  CHAR(20) NOT NULL
 )"""
cursor.execute(sql) # PREPARING COMMAND TO EXECUTE
db.commit() #COMMIT THE CHANGES TO DB

sql = """INSERT INTO plotHub(id, plotType, area, name) VALUES (1, 'A', 2, 'ASD')"""
cursor.execute(sql)
db.commit()

sql = """INSERT INTO plotHub(id, plotType, area, name) VALUES 
    (2, 'B', 2.3, 'XYZ'), 
    (3, 'C', 1.5, 'PLZ'), 
    (4, 'D', 3, 'OKP'),
    (5, 'A', 3.7, 'SSW'),
    (6, 'B', 3.3, 'LKJ'),
    (7, 'D', 2, 'KJL'),
    (8, 'A', 4, 'QWE'),
    (9, 'B', 2.6, 'FOL')"""
cursor.execute(sql)
db.commit()

sql = "SELECT area, name FROM plotHub ORDER BY area DESC LIMIT 5"
cursor.execute(sql)

myresult = cursor.fetchall()
for x in myresult:
    print(x)

sql = "SELECT SUM(area), plotType FROM plotHub GROUP BY plotType"
cursor.execute(sql)

myresult = cursor.fetchall()
for x in myresult:
    print(x)

db.close()
