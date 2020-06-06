def title(txt='', sep='-', sep_len=2, allformat=False):
    lenght = int(sep_len) if allformat is True else int(len(txt) + sep_len)

    line(sep, lenght)
    print(f'{txt:^{lenght}}')
    line(sep, lenght)


def line(sep='-', len='full'):
    if len == 'full':
        len = 182
    print(sep * len)


def readmoney(msg):
    test = str(input(msg).replace(',', '.')).strip()
    while test.isalpha() or test.strip() == '':
        print(color(f'"{test}" não é um preço válido.\n', 'red'))
        test = str(input(msg).replace(',', '.')).strip()
    return float(test)


def formatmoney(num):
    return f'R$ {num:.2f}'.replace('.', ',')


def colortxt(expression, colorname):
    if colorname == 'blue':
        return '\033[34m' + expression + '\033[m'
    if colorname == 'magenta':
        return '\033[35m' + expression + '\033[m'
    if colorname == 'red':
        return '\033[31m' + expression + '\033[m'
    if colorname == 'yellow':
        return '\033[33m' + expression + '\033[m'


def menu(lista):
    for i, p in enumerate(lista):
        print(f'{i + 1} - {p}')
    return


def leiaint(msg):
    while True:
        try:
            i = int(input('\n' + msg))
            break
        except:
            print(colortxt('Erro! Digite uma opção válida!', "red"))
    return i


def leiafloat(msg):
    while True:
        try:
            f = float(input('\n' + msg).replace(",", "."))
            break
        except:
            print(colortxt('Erro! O valor digitado não é um NÚMERO REAL.', "red"))
    return f


def validateinput(msg, test):
    validate = input(f'\n>>> {msg} ')
    while True:
        if validate == test:
            return True
        else:
            valid_option = False
            print(colortxt(f'Erro! Digite uma opção válida!', 'red'))
            validate = input(f'\n>>> {msg} ')


def findfile(filename):
    try:
        fn = open(filename, 'rt')
        fn.close()
    except FileNotFoundError:
        print(colortxt(f'O arquivo "{filename}" não foi encontrado!', "red"))
        return False
    else:
        print(f'O arquivo "{filename}" já existe!')
        return True


def createfile(filename):
    try:
        fn = open(filename, 'wt+')
    except:
        print(f'Erro na criação do arquivo')
    else:
        print(f'Arquivo criado com sucesso!')


def readfile(filename):
    try:
        fn = open(filename, 'rt')
    except:
        print(f'Erro durante a leitura do arquivo')
    else:
        print(fn.readline())