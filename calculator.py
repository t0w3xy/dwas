print("Арифметические: +, -, *, /, //, %, **")
print("Сравнения: ==, !=, >, <, >=, <=")
print("Логические: and, or, not")
print("Побитовые: &, |, ^, ~, <<, >>")


try:
    alavik = float(input("Введите первое число: "))
    renkk = input("Введите оператор: ")
    
    if renkk not in ['not', '~']:
        mikoyare = float(input("Введите второе число: "))

    if renkk == '+':
        result = alavik + mikoyare
    elif renkk == '-':
        result = alavik - mikoyare
    elif renkk == '*':
        result = alavik * mikoyare
    elif renkk == '/':
        result = alavik / mikoyare
    elif renkk == '//':
        result = alavik // mikoyare
    elif renkk == '%':
        result = alavik % mikoyare
    elif renkk == '**':
        result = alavik ** mikoyare
    elif renkk == '==':
        result = alavik == mikoyare
    elif renkk == '!=':
        result = alavik != mikoyare
    elif renkk == '>':
        result = alavik > mikoyare
    elif renkk == '<':
        result = alavik < mikoyare
    elif renkk == '>=':
        result = alavik >= mikoyare
    elif renkk == '<=':
        result = alavik <= mikoyare
    elif renkk == 'and':
        result = bool(alavik) and bool(mikoyare)
    elif renkk == 'or':
        result = bool(alavik) or bool(mikoyare)
    elif renkk == 'not':
        result = not bool(alavik)
        
    elif renkk == '&':
        result = int(alavik) & int(mikoyare)
    elif renkk == '|':
        result = int(alavik) | int(mikoyare)
    elif renkk == '^':
        result = int(alavik) ^ int(mikoyare)
    elif renkk == '~':
        result = ~int(alavik)
    elif renkk == '<<':
        result = int(alavik) << int(mikoyare)
    elif renkk == '>>':
        result = int(alavik) >> int(mikoyare)
        
    else:
        print("Неизвестный оператор!")
        exit()

    
    print("Результат:", result)
    
except ValueError:
    print("Ошибка: введите числа корректно!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
