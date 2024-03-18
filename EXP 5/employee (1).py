import pickle

class employee:
    pass

f = open('employee.py', 'wb')
n = int(input('How many employees? '))

for i in range(n):
    id = int(input('Enter id: '))
    name = input('Enter name: ')
    sal = float(input('Enter salary: '))

    e = employee()
    e.id = id
    e.name = name
    e.salary = sal
    pickle.dump(e, f)

f.close()
