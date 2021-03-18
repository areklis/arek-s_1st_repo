def student(name, age=None):
    print(f'Student {name} is {age} years old')
    print(type(age))


student('Anna', 20)
#student(name='Anna',20)
student(20)
student('Anna')
student(20,'Anna')
