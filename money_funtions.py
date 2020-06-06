from myfunctions import color, title


def readmoney(msg):
    ismoney = False
    while not ismoney:
        firstinput = str(input(msg))
        tested = firstinput.replace(',', '').replace('.', '').strip()
        if not tested.isnumeric():
            print(color(f'"{firstinput}" não é um preço válido.\n', 'red'))
        else:
            ismoney = True
            return float(firstinput.replace(',','.'))


def formatmoney(num):
    return color(f'R$ {num:.2f}'.replace('.', ','), 'blue')


def formatpercent(num):
    return color(f'{num}%', 'yellow')


def resumemoney(num, fincrease=0, fdecrease=0):
    title('RESUMO DO VALOR', "-", 10)
    print(f'Preço analisado: {formatmoney(num)}')
    print(f'Dobro do preço: {double(num)}')
    print(f'Metade do preço: {half(num)}')
    print(f'Aumento de {formatpercent(fincrease)}: {increase(num, fincrease)}')
    print(f'Redução de {formatpercent(fdecrease)}: {decrease(num, fdecrease)}')


def half(num):
    h = num / 2
    return formatmoney(h)


def double(num):
    db = num * 2
    return formatmoney(db)


def increase(num, factor):
    i = num * (1 + factor/100)
    return formatmoney(i)


def decrease(num, factor):
    dc = num * (1 - factor/100)
    return formatmoney(dc)