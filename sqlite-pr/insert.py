import sqlite3

#-------------------------------------------------------
conn = sqlite3.connect('school.sqlite')
cur = conn.cursor()
#-------------------------------------------------------
def read_file(path):
    """Generator; extracts the data from file"""
    try:
        with open(path, 'r', encoding='UTF-8 sig') as f:
            for each in f.readlines():
                yield each.strip().split(', ')
    except Exception as e:
        print(e)
#-------------------------------------------------------
# for i in read_file('city.txt'):
#     cur.execute("INSERT INTO city(city_name, city_traffic_code) VALUES(?,?)", (i[0], i[1]))
# conn.commit()
# -------------------------------------------------------
cur.execute("SELECT city_name, city_id FROM city")
city_ids = dict(cur.fetchall())
print(city_ids)
#-------------------------------------------------------
# for i in read_file('school.txt'):
#     cur.execute("INSERT INTO school(school_name, city_id, school_type) VALUES(?, ?, ?)", (i[0], city_ids[i[1]], i[2]))
# conn.commit()
#-------------------------------------------------------
cur.execute("SELECT school_name, school_id FROM school")
school_ids= dict(cur.fetchall())
print(school_ids)
#-------------------------------------------------------
# for i in read_file('student.txt'):
#     cur.execute("INSERT INTO student(student_name, student_no, school_id) VALUES(?,?,?)", (i[0], i[1], school_ids[i[2]]))
# conn.commit()
#-------------------------------------------------------
conn.close()
#-------------------------------------------------------
