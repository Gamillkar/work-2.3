number = input("Введите выражение ").split(' ')
try: # задание №2 деление на строки
    x = int(number[1])
    s = int(number[2])
    assert len(number) < 4, 'Введено больше 3 символов' # задание № 2
except ValueError as ex:
    print('операции со строками невозможны', ex)


else:
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
            assert int(num[1]) > 0, 'На ноль делить нельзя'
        except Exception as e:
            print(e)
        else:
            print(num[0] / (num[1]))

    elif signs == '*':
        print(num[0] * (num[1]))


