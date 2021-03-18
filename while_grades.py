sum_of_grades=0
for i in range(10):
    grade=input('pease enter a grade between 1 and 10')
    while not grade.isdigit() or int(grade)<1 or int(grade)>10:
        print('incorrect input, please try again\n')
        grade=input('pease enter a grade between 1 and 10')
    sum_of_grades+=int(grade)
print(sum_of_grades/10)




'''
sum_of_grades=0
for i in range(10):
    grade=-1
    while not ((grade.isdigit()) and (0<=int(grade)<=10)):
        grade=input('please enter a grade between 1 and 10')
    
'''
