class ValueCannotBeNegative(Exception):
    pass

numbers = [int(input()) for _ in range(5)]

try:
    for num in numbers:
        if num < 0:
            raise ValueCannotBeNegative
        print('No exception')
except:
    print('Exception handled')