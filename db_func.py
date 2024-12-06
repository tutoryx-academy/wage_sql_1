import sqlite3

def set_conn():
    conn = sqlite3.connect('employees-database.db')
    cursor = conn.cursor()
    return cursor,conn

def emp_table():
    cursor, conn = set_conn()
    cursor.execute(
            """
                Create table if not exists employees (
                            id integer primary key autoincrement,
                            name text not null,
                            rate real not null,
                            hours real not null           
                            )
            """
                )
    conn.commit()
    conn.close()


def emp_value(name, ratee, hours):
    cursor, conn = set_conn()
    cursor.execute(
        " Insert Into Employees (name, rate, hours) values (?, ?, ?)",(name, ratee, hours)
    )
    conn.commit()
    conn.close()