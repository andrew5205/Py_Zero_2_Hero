
stock_price = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]

for item in stock_price:
    print(item)
                        # ('APPL', 200)
                        # ('GOOG', 400)
                        # ('MSFT', 100)


# tuple unpacking 
for ticker, price in stock_price:
    print(ticker)
    print(price)



work_hours = [("Abby", 100), ("billy", 400), ("Cassie", 800)]

def employee_check(work_hours):
    current_max = 0
    employee_og_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_og_month = employee
        else:
            pass
    return (employee_og_month, current_max)

print(employee_check(work_hours))               # ('Cassie', 800)


result = employee_check(work_hours)
name, hour = employee_check(work_hours)
print(result)                                   # ('Cassie', 800)
print(name)                                     # Cassie
print(hour)                                     # 800



# # # how to check tuple elements 
# # item = function()
# # print(item)
# result = employee_check(work_hours)
# name, hour, bonus = employee_check(work_hours)

# Traceback (most recent call last):
#   File "46_tuple_unpacking.py", line 47, in <module>
#     name, hour, bonus = employee_check(work_hours)
# ValueError: not enough values to unpack (expected 3, got 2)
