number = input("Введите выражение ").split(' ')
try: # задание №2 операции не с числами
    x = int(number[1])
    s = int(number[2])
    arithmetic_operation = ['+', '-', '/', '*']
    assert len(number) < 4, 'Введено больше 3 символов' # задание № 2
    assert  number[0] in arithmetic_operation, 'первый элемент не арифметическая орперация'
except ValueError as ex:
    print('операции со строками невозможны', ex)

signs = number.pop(0)
num = []

for sign in number:
    num.append(int(sign))
if signs == '-':
    print(num[0] - (num[1]))
elif signs == '+':
    print(num[0] + (num[1]))
elif signs == '/':
    try: # задание №2 деление на ноль
        assert 0 > int(num[1]) or 0 < int(num[1]), 'На ноль делить нельзя'
    except Exception as e:
        print(e)
    print(num[0] / (num[1]))
elif signs == '*':
    print(num[0] * (num[1]))


