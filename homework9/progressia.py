import openpyxl
def sum_vklada():

    a = int(input("Сумма вклада: "))
    b = int(input("Размер процентов в год: "))

    while True:
        yield a
        a = a + (a/100*b)
        
prog = sum_vklada()

print(f"Начальная сумма вклада, {next(prog)}")
print(f"Сумма вклада через 1 год, {next(prog)}")
print(f"Сумма вкоала через 2 года, {next(prog)}")
print(f"Сумма вклада через 3 года, {next(prog)}")
print(f"Сумма вклада через 4 года, {next(prog)}")
print(f"Сумма вклада через 5 лет, {next(prog)}")





