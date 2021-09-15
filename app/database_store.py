import sqlite3
from contextlib import closing


def data_store(first_name, last_name, birthday, password, file_name=None):
    with closing(sqlite3.connect("password_data.db")) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, birthday TEXT, password TEXT, log_file TEXT);")
            if file_name is None:
                cursor.execute(
                    f"INSERT INTO passwords (first_name, last_name, birthday, password) VALUES ('{first_name}', '{last_name}', '{birthday}', '{password}');")
                conn.commit()
            else:
                cursor.execute(
                    f"INSERT INTO passwords (first_name, last_name, birthday, password, log_file) VALUES ('{first_name}', '{last_name}', '{birthday}', '{password}', '{file_name}');")
                conn.commit()
    return


if __name__ == '__main__':
    data_store("lewis", "blaine", "2000-05-08", "test_password")
    data_store("lewis", "blaine", "2000-05-08", "test_password", "password_report_210915_140130")
