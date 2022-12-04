import sqlite3


# 4
class DataBase:  # create a class

    def __init__(self):  # the initializer
        pass

    @staticmethod
    def work_with_database(first=None, second=None, third=None):  # method for working with database
        if first is not None and second is None and third is None:  # condition
            cursor_4.execute('''INSERT INTO exercise_4(column_2) VALUES(3)''')  # add some values to the table
            conn_4.commit()  # save changes

        elif first is not None and second is not None and third is None:  # alternative condition
            if type(second) == int:  # condition
                cursor_4.execute('''DELETE FROM exercise_4 WHERE id=1''')  # delete the row
                conn_4.commit()  # save changes

        else:  # alternative condition
            if type(third) == int:  # condition
                cursor_4.execute('''UPDATE exercise_4 SET column_2=77 WHERE id=3''')
                # change the value from the column 2 (where id-3) to 3
                conn_4.commit()


conn_4 = sqlite3.connect('class_work_4.db')  # create a database
cursor_4 = conn_4.cursor()  # create an object of the cursore

cursor_4.execute('''CREATE TABLE IF NOT EXISTS exercise_4(id INTEGER PRIMARY KEY AUTOINCREMENT, column_2 INT) ''')
# create a table with two columns
conn_4.commit()

cursor_4.execute('''SELECT * FROM exercise_4''')  # select all values from all columns from our table
tab = cursor_4.fetchall()

class_object = DataBase()  # create a class object
class_object.work_with_database(1)
class_object.work_with_database(2)
class_object.work_with_database(2, 'string')
class_object.work_with_database(1, 2, 3)
class_object.work_with_database(1, 4)

cursor_4.execute('''SELECT * FROM exercise_4''')
final_table = cursor_4.fetchall()
print(final_table)
