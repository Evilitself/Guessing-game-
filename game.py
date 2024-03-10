import random

def game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
        x, y = is_valid_num(), is_valid_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        is_valid_number(x, y)
        if continue_game():
            continue
        else:
            break

def is_valid(n): # проверка на соответствие введенного значения условию
    return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100
 

def is_valid_num():
    while True:
        n = input('Попробуйте угадать число от 1 до 100 ... ')
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def continue_game(): 
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return True        


def is_valid_number(down_num, up_num):
    num = random.randint(down_num, up_num)
    total = 0
    while True:
        n = is_valid_num()
        total += 1
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

game()