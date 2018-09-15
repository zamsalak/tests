import sqlite3
import sys

#-------------------------------------------------------
conn = sqlite3.connect('school.sqlite')
cur = conn.cursor()
#-------------------------------------------------------
def student_list():
    cur.execute("""SELECT student_name, student_no, school_name, city_name, school_type, city_traffic_code FROM student
                INNER JOIN school ON student.school_id = school.school_id
                INNER JOIN city ON school.city_id = city.city_id""")

    for i in cur.fetchall():
        print('{}, {}, {} ({} - {} - {})'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
#-------------------------------------------------------
def school_list():
    cur.execute("SELECT school_name, school_type FROM school")
    for i in cur.fetchall():
        print('{}, {}'.format(i[0], i[1]))
    conn.close()
#-------------------------------------------------------
def city_list():
    cur.execute("SELECT city_name, city_traffic_code FROM city")
    for i in cur.fetchall():
        print('{}, {}'.format(i[0], i[1]))
    conn.close()
#-------------------------------------------------------
def add_school():
    cur.execute("SELECT city_name, city_id FROM city")
    cities = dict(i for i in cur.fetchall())
    print(cities)

    try:
        new_school_city = input('Input city: ')
        new_school_city = new_school_city.capitalize()
        if new_school_city not in cities:
            raise KeyError
        else:
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
    finally:
        conn.close()
#-------------------------------------------------------
def add_city():
    try:
        new_city_name = input('Input new city: ')
        new_city_name = new_city_name.capitalize()
        if len(new_city_name) < 2:
            raise ValueError

        new_city_traffic_code = input('Input traffic code: ')
        assert int(new_city_traffic_code)
        assert len(str(new_city_traffic_code)) == 2
    except ValueError:
        print('Invalid input')
    except AssertionError:
        print('City traffic code must be 2 digits long')
    else:
        cur.execute("INSERT INTO city(city_name, city_traffic_code) VALUES (?, ?)", (new_city_name, new_city_traffic_code))
        conn.commit()
        print(new_city_name, 'added!')
    finally:
        conn.close()
#-------------------------------------------------------
def add_student():
    import random
    cur.execute("""SELECT school_name, school_id FROM school""")
    schools = dict(i for i in cur.fetchall())

    try:
        new_student_name = input('Input student name: ')
        assert ' ' in new_student_name
        new_student_name = new_student_name.capitalize()

        student_no = input('Input a student no of your choosing: ')
        student_no = random.randint(500, 5001)
        print('Not so fast, dear. You don\'t get to choose your number!? Your number is {}'.format(student_no))

        school_name = input('Input school name: ')
        if school_name not in schools:
            raise ValueError('There is no such school!')

    except AssertionError:
        print('How about some surname, sweetheart?')
    except ValueError as e:
        print(e)
    else:
        cur.execute("INSERT INTO student(student_name, student_no, school_id) VALUES (?, ?, ?)", (new_student_name, student_no, schools[school_name]))
        conn.commit()
        print(new_student_name, 'added!')
    finally:
        conn.close()
#-------------------------------------------------------
def main():
    func_dict = {1: student_list, 2: school_list, 3: city_list, 4: add_student, 5: add_school, 6: add_city, 7: sys.exit}
    while True:
        print('-------------------------------------------------------')
        entry = int(input("Press 1 to List Students\nPress 2 to List Schools\nPress 3 to List Cities\nPress 4 to Add Student\nPress 5 to Add School\nPress 6 to Add city\nPress 7 to Exit\n"))
        if entry not in func_dict:
            print('-------------------------------------------------------')
            print('There is no {}, smartass...'.format(entry))
            main()
        else:
            print('-------------------------------------------------------')
            func_dict[entry]()


if __name__ == '__main__':
    main()