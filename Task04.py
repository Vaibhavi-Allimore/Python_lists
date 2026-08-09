salary=[36000,13000,34000,30000,15000]
print("Salaries of an employee:",salary)
print("Highest salary of an employee:",max(salary))
print("Lowest salary of an employee:",min(salary))
total=sum(salary)
average=total/5
print("Average salary of an employee:",average)
count=0
for x in salary:
    if x >= 30000:
        count=count+1
print("Greater than 30000",count)

