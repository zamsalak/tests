import sqlite3

conn = sqlite3.connect('school.sqlite')
cur = conn.cursor()

def student_list():
    cur.execute("""SELECT student_name, student_no, school_name, city_name, school_type, city_traffic_code FROM student
                INNER JOIN school ON student.school_id = school.school_id
                INNER JOIN city ON school.city_id = city.city_id""")

    for i in cur.fetchall():
        print('{}, {}, {} ({} - {} - {})'.format(i[0], i[1], i[2], i[3], i[4], i[5]))

def school_list():
    cur.execute("SELECT school_name, school_type FROM school")
    for i in cur.fetchall():
        print('{}, {}'.format(i[0], i[1]))

def city_list():
    cur.execute("SELECT city_name, city_traffic_code FROM city")
    for i in cur.fetchall():
        print('{}, {}'.format(i[0], i[1]))

def add_school():
    cur.execute("SELECT city_name, city_id FROM city")
    cities = dict(i for i in cur.fetchall())
    print(cities)

    try:
        new_school_city = str(input('Input city: ')).title()
        if new_school_city not in cities:
            raise KeyError
        new_school = str(input('Input school name: '))
        new_school_type = str(input('Input school type: '))

    except KeyError:
        print('No such city')
    except TypeError:
        print('Invalid input')

    else:
        cur.execute("INSERT INTO school(school_name, city_id, school_type) VALUES (?, ?, ?)", (new_school, cities[new_school_city], new_school_type))
        conn.commit()
        print(new_school, 'added to school list.')

def add_city():
    pass

def add_student():
    pass

def main():
    pass





student_list()
school_list()
city_list()
add_school()