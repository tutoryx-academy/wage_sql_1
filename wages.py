import sqlite3

conn = sqlite3.connect('employees.db')

cursor = conn.cursor()

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

cursor.execute(
    """
        INSERT into employees (name, rate, hours) values ('Alice','20','35')
    """
)

conn.commit()

conn.close()