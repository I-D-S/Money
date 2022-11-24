coins = [64, 32, 16, 8, 4, 2, 1]
number_of_coins = []

while True:
    try:
        n = int(input('Введите сумму:  '))
        assert n > 0
        break
    except AssertionError:
        print('Число должно быть больше 0')
    except ValueError:
        print('Ошибка ввода, попробуйте ещё раз')


def checker(s, nominal):
    amount = 0
    while s >= nominal:
        s -= nominal
        amount += 1
    number_of_coins.append(amount)
    return s


for el in coins:
    n = checker(n, el)

for i in range(len(coins)):
    print('количество купюр номинала {1} = {0}'.format(number_of_coins[i], coins[i]))
print('Всего небходимо купюр ', sum(number_of_coins))
