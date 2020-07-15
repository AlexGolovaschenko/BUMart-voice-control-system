import re


def bit_to_register(s):
    if s.isdigit():
        n = int(s)
        a = n // 16
        b = n % 16
        print(str(a) + '.' + str(b) + '\n')
    else :
        print('')


def register_to_bit(s):
    a = 0
    b = 0

    result = re.match(r'(\d+)', s)
    if result:
        n = int(result.group(1))
        a = n * 16

    result = re.match(r'\d+\D+(\d+)', s)
    if result:
        n = int(result.group(1))
        b = n 

    print(str(a+b) + '\n')