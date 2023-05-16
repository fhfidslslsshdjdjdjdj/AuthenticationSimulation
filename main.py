try:
    logincheck = 'admin'
    passwordcheck = 'admin'
    
    for i in range(3):
        login = str(input("Введіть логін: "))
        password = str(input('Введіть пароль: '))
        if login == logincheck and password == passwordcheck:
            print('Вас авторизовано')
            break

        elif i < 2:
            print("Повторіть спробу")

        else:
            print("Вас заблоковано")
        
except:
    print('error')
