from db_func import emp_table, emp_value

emp_table()

# emp_value('Alice','20','35')

with open('input.csv') as f:
    emp_list = f.readlines()
    emp_list_no_header = emp_list[2:] # added 2 as start index, not to duplicate Alice
    for emp in emp_list_no_header:
        name, rate, hours = emp.split(',')
        emp_value(name, rate, hours)