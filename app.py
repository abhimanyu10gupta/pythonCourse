
employee_file = open("employees.txt", 'r+')

print(employee_file.readable())
print(employee_file.readlines())
print(employee_file.readline())

print(employee_file.read())

for employee in employee_file.readlines():
    print(employee)

employee_file.write("\ntoby = human resources")

employee_file.close()
