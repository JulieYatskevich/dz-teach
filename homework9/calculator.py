class Calculator:

    print("Выбери действия.\n1.Сложение\n2.Вычитание\n3.Умножение\n4.Деление")


    def add(x, y: float):
        return x + y

    def sub(x, y: float):
        return x - y

    def mult(x, y: float):
        return x * y

    def divide(x, y: float):
        return x / y



    while True:
        try:
            choice = input("Enter choice: ")

            if choice in ('1', '2', '3', '4'):
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))

                if choice == '1':
                    print(number1, "+", number2, "=", add(number1, number2))

                elif choice == '2':
                    print(number1, "-", number2, "=", sub(number1, number2))

                elif choice == '3':
                    print(number1, "*", number2, "=", mult(number1, number2))

                elif choice == '4':
                    print(number1, "/", number2, "=", divide(number1, number2))
            else:
                print("Неверный выбор")
        except ZeroDivisionError:
            print("На 0 делить нельзя")
            continue
        except ValueError:
            print("Введи число")    
            continue