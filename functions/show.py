def get_table(table, s_list, rows_number):
    row_number = 0
    for row in s_list:
        if row_number < rows_number:
            table.add_row([row.id, row.age, row.gender, row.state])
            row_number += 1
        elif row_number == rows_number:
            table.add_row(["...", "...", "...", "..."])
            row_number += 1
        else:
            return table
    return table
        

def get_max_age(s_list, init_age):
    if max(s_list, key=lambda x: x.age).age > init_age:
        return max(s_list, key=lambda x: x.age).age
    return init_age