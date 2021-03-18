while True:
    num1=input('give me number ')
    num2=input('give me second number ')
    calc=input('Dwse mou tin praksi ')
    if calc=='+':
        try:
            print(float(num1)+float(num2))
            break
        except ValueError:
            print('give me numbers and not strings')

    elif calc=='-':
        try:
            print(float(num1)-float(num2))
            break
        except ValueError:
            print('give me numbers and not strings')
    elif calc=='*':
        try:
            print(float(num1)*float(num2))
            break
        except ValueError:
            print('give me numbers and not strings')
    elif calc=='/':
        try:
            print(float(num1)/float(num2))
            break
        except ValueError:
            print('give me numbers and not strings')
