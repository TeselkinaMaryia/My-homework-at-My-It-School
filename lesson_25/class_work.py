import sqlite3
import random
import csv

# 1
conn_1 = sqlite3.connect('class_work_1.db')  # create a database
cursor_1 = conn_1.cursor()  # create an object of cursor

cursor_1.execute('''CREATE TABLE IF NOT EXISTS exercise_1(your_number INTEGER, text_1 TEXT, text_2 TEXT)''')
# create a table with three columns

for i in range(10):  # cycle
    num: int = int(input('Your number: '))  # variable that refers to a value entered from the keyboard
    text_1_inp: str = 'First text'  # variable refers to the string value
    text_2_inp: str = 'Second text'  # variable refers to the string value

    cursor_1.execute('''INSERT INTO exercise_1(your_number, text_1, text_2) VALUES(?,?,?)''',
                     (num, text_1_inp, text_2_inp))  # add to the table some values
    conn_1.commit()  # save the changes

cursor_1.execute('''SELECT * FROM exercise_1''')  # select all values from all columns from the table
table_1 = cursor_1.fetchall()  # get our selection
for elem in table_1:  # cycle
    print(*elem)  # print to the console elements of the unpacked tuple

# 2
conn_2 = sqlite3.connect('class_work_2.db')  # create a database
cursor_2 = conn_2.cursor()  # create an object of a cursor

cursor_2.execute('''CREATE TABLE IF NOT EXISTS exercise_2
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, first_num INTEGER, second_num INTEGER)''')
# create a table with three columns, where first column is a primary kay and stores id,
# and two others columns stores random numbers from 0 to 9
for i in range(2):  # cycle
    first_random_num: int = random.randint(0, 9)  # variable that refers to the random integer
    second_random_num: int = random.randint(0, 9)
    cursor_2.execute('''INSERT INTO exercise_2(first_num, second_num) VALUES(?,?)''',
                     (first_random_num, second_random_num))  # add to the table some values
    conn_2.commit()  # save all changes

cursor_2.execute('''SELECT first_num, second_num FROM exercise_2''')  # select two columns
table_2 = cursor_2.fetchall()  # the list of the tuples from the table

cursor_2.execute('''SELECT COUNT(*) FROM exercise_2''')  # count all rows in the table
count_ = cursor_2.fetchall()

cursor_2.execute('''SELECT AVG(first_num) FROM exercise_2''')  # an average value of second column
average_1 = cursor_2.fetchall()

cursor_2.execute('''SELECT AVG(second_num) FROM exercise_2''')  # an average of the third column
average_2 = cursor_2.fetchall()

average_ = (average_1[0][0] + average_2[0][0]) / 2  # the average of the two last columns

print(table_2, count_[0][0], average_1[0][0], average_2[0][0], average_, sep='\n')  # print to the console

if average_ > count_[0][0]:  # condition
    cursor_2.execute('''DELETE FROM exercise_2 WHERE id=4''')  # delete the record where id = 4
    conn_2.commit()

cursor_2.execute('''SELECT * FROM exercise_2''')  # select all values from all columns from the table
final_table = cursor_2.fetchall()
print(final_table)

# 3
conn_3 = sqlite3.connect('class_work_3.db')  # create a database
cursor_3 = conn_3.cursor()  # create an object of the cursor

cursor_3.execute('''CREATE TABLE IF NOT EXISTS exercise_3
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, random_1 INTEGER, random_2 INTEGER)''')
# create a table with three columns

num_1_random = random.randint(0, 9)  # variable refers to the random integer
num_2_random = random.randint(0, 9)  # variable refers to the random integer

cursor_3.execute('''INSERT INTO exercise_3(random_1, random_2) VALUES(?,?)''', (num_1_random, num_2_random))
# add some values to the table
conn_3.commit()  # save changes

cursor_3.execute('''SELECT COUNT(*) FROM exercise_3''')  # count all rows in the table
count_rows = cursor_3.fetchall()

random_row = random.randint(1, count_rows[0][0])  # variable refers to the random integer from 1 to number of rows
cursor_3.execute(f'''SELECT * FROM exercise_3 WHERE id = {random_row}''')
# select all values from all columns from the table
row = cursor_3.fetchall()
print(*row)

for tuple_ in row:  # cycle
    if tuple_[1] % 2 == 0 and tuple_[2] % 2 == 0:  # condition
        cursor_3.execute(f'''DELETE FROM exercise_3 WHERE id = {random_row}''')  # delete the row
        conn_3.commit()
    else:  # alternative condition
        cursor_3.execute(f'''UPDATE exercise_3 SET random_1=2, random_2=2 WHERE id= ?''', (random_row,))
        # update the table. We change the values of two last columns
        conn_3.commit()  # save changes

cursor_3.execute('''SELECT * FROM exercise_3''')  # select all values from all columns
final_tab_3 = cursor_3.fetchall()
print(final_tab_3)

# 5
conn_5 = sqlite3.connect('class_work_5.db')  # create a database
cursor_5 = conn_5.cursor()  # create an object of a cursor

cursor_5.execute('''CREATE TABLE IF NOT EXISTS exersice_5
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, col_text_1 TEXT, col_text_2 TEXT)''')
# create a table with three columns

for i in range(3):  # cycle
    text_col_1: str = input('Write some text: ')
    text_col_2: str = input('Write another text: ')
    cursor_5.execute('''INSERT INTO exersice_5(col_text_1, col_text_2) VALUES(?, ?)''', (text_col_1, text_col_2))
    # add some values
    conn_5.commit()  # save changes

cursor_5.execute('''DELETE FROM exersice_5 WHERE id=2''')  # delete the row
conn_5.commit()  # save

cursor_5.execute('''UPDATE exersice_5 SET col_text_1='hello', col_text_2="world" WHERE id=3''')
# change the values in two last columns

cursor_5.execute('''SELECT * FROM exersice_5''')  # select all values from all rows in the table
table_5 = cursor_5.fetchall()
print(table_5)

with open('table.csv', 'w', encoding='UTF-8', newline='') as file:  # open csv file for writing
    file_writer = csv.writer(file)  # create a writer object

    try:  # block of the code where can be some exceptions
        for elem in table_5:  # cycle
            file_writer.writerow(elem)  # write row
    except Exception as ex:  # block of the code catches exceptions
        print(ex)
