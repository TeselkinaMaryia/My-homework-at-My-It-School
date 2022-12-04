import sqlite3
from typing import List, Any


def create_table():  # create a function without parameters
    cursor_.execute('''CREATE TABLE IF NOT EXISTS text_table(text_ TEXT)''')  # create a table with one column
    conn_.commit()  # save the table

    cursor_.execute('''CREATE TABLE IF NOT EXISTS num_table(number INTEGER)''')  # create a table with one column
    conn_.commit()  # save the table


def add_to_table(list_: List[Any]):  # create a function with one parameter
    for elem in list_:  # cycle
        if type(elem) == str:  # condition
            cursor_.execute('''INSERT INTO text_table(text_) VALUES(?)''', (elem,))  # add some values to the table
            conn_.commit()  # save changes

            len_of_word: int = len(elem)  # a variable refers to the len of word
            cursor_.execute('''INSERT INTO num_table(number) VALUES(?)''', (len_of_word,))  # add the value to the table
            conn_.commit()  # save changes

        elif type(elem) == int:  # alternative condition

            if elem % 2 == 0:  # condition
                cursor_.execute('''INSERT INTO num_table(number) VALUES(?)''', (elem,))  # add the number to the table
                conn_.commit()  # save changes

            else:  # alternative condition
                cursor_.execute('''INSERT INTO text_table(text_) VALUES('odd')''')  # add the text to the table
                conn_.commit()  # save changes


def work_with_database():  # create the function without parameters
    cursor_.execute('''SELECT COUNT(*) FROM num_table''')  # count the rows from the table
    count_row = cursor_.fetchall()
    # print(count_row)

    cursor_.execute('''SELECT * FROM text_table''')  # select all values from the table
    elements = cursor_.fetchall()
    # print(elements)

    if count_row[0][0] > 5:  # condition
        cursor_.execute('''DELETE FROM text_table WHERE text_=?''', (elements[0][0],))
        # delete the rows where text = first word in the table
        conn_.commit()  # save changes

    else:  # alternative condition
        cursor_.execute('''UPDATE text_table SET text_="Hello" WHERE text_=?''', (elements[0][0],))
        # change the text in the table
        conn_.commit()  # save changes


def main(list_):  # main function
    create_table()  # call all functions
    add_to_table(list_)
    work_with_database()


conn_ = sqlite3.connect('homework.db')  # create a database
cursor_ = conn_.cursor()  # create an object of the cursor

my_list: List[Any] = [1, 2, 3, 4, 5, 6, 'hi', 'dog', 'hello', 'trust', 'present', 9, 10, 11, 15]
main(my_list)  # call the function

# cursor_.execute('''SELECT * FROM text_table''')
# k = cursor_.fetchall()
# cursor_.execute('''SELECT * FROM num_table''')
# a = cursor_.fetchall()
# print(k, a, sep='\n')
