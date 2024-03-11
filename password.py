import random

digit = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

len_pass_all = int(input('Укажите количество паролей для генерации: '))
len_pass_one = int(input('Укажите длину одного пароля: '))
len_pass_numbers = input('Включать ли цифры 0123456789? ')
len_pass_byk = input('Включить ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
len_pass_byk2 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
len_pass_symbols = input('Включать ли символы !#$%&*+-=?@^_? ')
len_pass_no_symbols = input('Исключать ли неоднозначные символы il1Lo0O? ')

if len_pass_numbers.lower() == 'д' or len_pass_numbers.lower() == 'Да' or len_pass_numbers.lower() == 'Lf' or len_pass_numbers.lower() == 'lf' or len_pass_numbers.lower() == 'да':
    chars += digit
if len_pass_byk.lower() == 'д' or len_pass_byk.lower() == 'Да' or len_pass_byk.lower() == 'Lf' or len_pass_byk.lower() == 'lf' or len_pass_byk.lower() == 'да':
    chars += uppercase_letters
if len_pass_byk2.lower() == 'д' or len_pass_byk2.lower() == 'Да' or len_pass_byk2.lower() == 'Lf' or len_pass_byk2.lower() == 'lf' or len_pass_byk2.lower() == 'да':
    chars += lowercase_letters
if len_pass_symbols.lower() == 'д' or len_pass_symbols.lower() == 'Да' or len_pass_symbols.lower() == 'Lf' or len_pass_symbols.lower() == 'lf' or len_pass_symbols.lower() == 'да':
    chars += punctuation
if len_pass_no_symbols.lower() == 'д' or len_pass_no_symbols.lower() == 'Да' or len_pass_no_symbols.lower() == 'Lf' or len_pass_no_symbols.lower() == 'lf' or len_pass_no_symbols.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(len_pass_one, chars):
    password = ''
    for j in range(len_pass_one):
        password += random.choice(chars)
    return password

for _ in range(len_pass_all):
    print(generate_password(len_pass_one, chars))