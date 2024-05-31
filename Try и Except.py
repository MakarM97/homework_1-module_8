def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up('4', 5.5))
print(add_everything_up(4, 'apple'))
print(add_everything_up(4.5, 5))
