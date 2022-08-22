import sqlite3
# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("База данных создана и успешно подключена к SQLite")
#
#     sqlite_select_query = "select sqlite_version();"
#     cursor.execute(sqlite_select_query)
#     record = cursor.fetchall()
#     print("Версия базы данных SQLite: ", record)
#
#     cursor.close()
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")

# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
#         id INTEGER PRIMARY KEY, name TEXT NOT NULL, email text NOT NULL UNIQUE, joining_date datetime, salary REAL NOT NULL);'''
#     cursor = sqlite_connection.cursor()
#     print("База данных подключена к SQLite")
#     cursor.execute(sqlite_create_table_query)
#     sqlite_connection.commit()
#     print("Таблица SQLite создана")
#     cursor.close()
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")

# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("База данных подключена к SQLite")
#     with open('sqlite_create_tables.sql', 'r') as sqlite_file:
#         sql_script = sqlite_file.read()
#     cursor.executescript(sql_script)
#     print("Скрипт SQLite успешно выполнен")
#     cursor.close()
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")

# import sqlite3
# import traceback
# import sys
# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("База данных подключена к SQLite")
#     sqlite_insert_query = """INSERT INTO unknown_table_1 (id, text) VALUES (1, 'Демо текст')"""
#     count = cursor.execute(sqlite_insert_query)
#     sqlite_connection.commit()
#     print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
#     cursor.close()
# except sqlite3.Error as error:
#     print("Не удалось вставить данные в таблицу sqlite")
#     print("Класс исключения: ", error.__class__)
#     print("Исключение", error.args)
#     print("Печать подробноcтей исключения SQLite: ")
#     exc_type, exc_value, exc_tb = sys.exc_info()
#     print(traceback.format_exception(exc_type, exc_value, exc_tb))
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")

# import sqlite3
# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("Подключен к SQLite")
#     sqlite_insert_query = """INSERT INTO sqlitedb_developers (id, name, email, joining_date, salary)
#                             VALUES (4, 'Alex', 'sale@gmail.com', '2020-11-20', 8600);"""
#     cursor.execute(sqlite_insert_query)
#     sql_update_query = """Update sqlitedb_developers set salary = 10000 where id = 4"""
#     cursor.execute(sql_update_query)
#     sql_delete_query = """DELETE from sqlitedb_developers where id = 4"""
#     cursor.execute(sql_delete_query)
#     sqlite_connection.commit()
#     cursor.close()
# except sqlite3.Error as error:
#     print("Ошибка при работе с SQLite", error)
# finally:
#     if (sqlite_connection):
#         print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")

# import sqlite3
# def progress(status, remaining, total):
#     print(f'Скопировано {total-remaining} из {total}...')
# try:
#     sqlite_con = sqlite3.connect('sqlite_python.db')
#     backup_con = sqlite3.connect('sqlite_backup.db')
#     with backup_con:
#         sqlite_con.backup(backup_con, pages=3, progress=progress)
#     print("Резервное копирование выполнено успешно")
# except sqlite3.Error as error:
#     print("Ошибка при резервном копировании: ", error)
# finally:
#     if(backup_con):
#         backup_con.close()
#         sqlite_con.close()


# import sqlite3
# try:
#     sqlite_connection = sqlite3.connect('sqlite_python.db')
#     cursor = sqlite_connection.cursor()
#     print("Подключен к SQLite")
#     sqlite_insert_query = """INSERT INTO sqlitedb_developers (id, name, email, joining_date, salary)
#         VALUES (2, 'Max', 'max04@gmail.com', '2020-11-19', 10000);"""
#     count = cursor.execute(sqlite_insert_query)
#     sqlite_connection.commit()
#     print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
#     cursor.close()
# except sqlite3.Error as error:
#     print("Ошибка при работе с SQLite", error)
# finally:
#     if sqlite_connection:
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")

# import sqlite3
# def insert_varible_into_table(dev_id, name, email, join_date, salary):
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#         sqlite_insert_with_param = """INSERT INTO sqlitedb_developers (id, name, email, joining_date, salary)
#                                         VALUES (?, ?, ?, ?, ?);"""
#         data_tuple = (dev_id, name, email, join_date, salary)
#         cursor.execute(sqlite_insert_with_param, data_tuple)
#         sqlite_connection.commit()
#         print("Переменные Python успешно вставлены в таблицу sqlitedb_developers")
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
# insert_varible_into_table(3, 'Viktoria', 's_dom34@gmail.com', '2020-11-19', 6000)
# insert_varible_into_table(4, 'Valentin', 'exp3@gmail.com', '2020-11-23', 6500)

# import sqlite3
# def insert_multiple_records(records):
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#         sqlite_insert_query = """INSERT INTO sqlitedb_developers (id, name, email, joining_date, salary)
#                 VALUES (?, ?, ?, ?, ?);"""
#         cursor.executemany(sqlite_insert_query, records)
#         sqlite_connection.commit()
#         print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
#         sqlite_connection.commit()
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
# records_to_insert = [(5, 'Jaroslav', 'idebylos@gmail.com', '2020-11-14', 8500),
#                      (6, 'Timofei', 'ullegyddomm@gmail.com', '2020-11-15',6600),
#                       (7, 'Nikita', 'aqillysso@gmail.com', '2020-11-27', 7400)]
# insert_multiple_records(records_to_insert)

#import sqlite3
# def read_sqlite_table():
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sqlite_select_query = """SELECT * from sqlitedb_developers"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Всего строк: ", len(records))
#         print("Вывод каждой строки")
#         for row in records:
#             print("ID:", row[0])
#             print("Имя:", row[1])
#             print("Почта:", row[2])
#             print("Добавлен:", row[3])
#             print("Зарплата:", row[4], end="\n\n")
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
# read_sqlite_table()


# import sqlite3
# def get_developer_info(id):
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sql_select_query = """select * from sqlitedb_developers where id = ?"""
#         cursor.execute(sql_select_query, (id,))
#         records = cursor.fetchall()
#         print("Вывод ID ", id)
#         for row in records:
#             print("ID:", row[0])
#             print("Имя:", row[1])
#             print("Почта:", row[2])
#             print("Добавлен:", row[3])
#             print("Зарплата:", row[4], end="\n\n")
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
# get_developer_info(2)

# import sqlite3
# def read_limited_rows(row_size):
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#         sqlite_select_query = """SELECT * from sqlitedb_developers"""
#         cursor.execute(sqlite_select_query)
#         print("Чтение ", row_size, " строк")
#         records = cursor.fetchmany(row_size)
#         print("Вывод каждой строки \n")
#         for row in records:
#             print("ID:", row[0])
#             print("Имя:", row[1])
#             print("Почта:", row[2])
#             print("Добавлен:", row[3])
#             print("Зарплата:", row[4], end="\n\n")
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
# read_limited_rows(2)

import sqlite3
def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = """Update sqlitedb_developers set salary = 11000 where id = 4"""
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
update_sqlite_table()