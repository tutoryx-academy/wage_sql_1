from db_func import set_conn, wage_table

cursor, conn = set_conn()
cursor.execute("""Select 
                    id, 
                    name, 
                    rate, 
                    hours
                    /* rate * hours as wage_sql */
               From 
                    employees""")
emps = cursor.fetchall()

# print(emps)

wage_table()

for emp in emps:
    emp_id, emp_name, rate, hours = emp
    total_wage = rate * hours
    print(emp_id,emp_name,total_wage)
    cursor.execute("Insert or Replace Into wages (emp_id, name, total_wage) values (?, ?, ?)",(emp_id,emp_name,total_wage))

conn.commit()
conn.close()

#TODO: Can you transfer hours from employees to wages table