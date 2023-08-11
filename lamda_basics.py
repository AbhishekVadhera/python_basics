division = lambda x, y: x // y
print(division(500, 10))

name = lambda name: print('my name is ', name)
name('abhishek')


def division_function():
    return lambda x, y: x // y


divide = division_function()
print(divide(500, 10))
