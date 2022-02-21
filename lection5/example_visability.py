import builtins


a = 5


def one():
    print(f'one {a}')


def two():
    a = 3
    print(f'two {a}')


if __name__ == '__main__':
    one()
    two()
    print(f'global {a}')
    print(dir(builtins))
