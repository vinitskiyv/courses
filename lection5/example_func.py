

def func(arg1, arg2, *args, arg3=1, arg4='text', **kwargs):
    print(f'arg1 -> {arg1}')
    print(f'arg2 -> {arg2}')
    print(f'arg3 -> {arg3}')
    print(f'arg4 -> {arg4}')
    print(f'*arg -> {args}')
    print(f'**kwargs -> {kwargs}')
    return (1, 2, 3, 4)


if __name__ == '__main__':
    value, *other = func('arg1', 'arg2', 'position argument1',
                         *('position argument2', 'position argument3'),
                         arg3=3, arg4='arg4',
                         arg6=6, arg7='arg7',
                         **{'arg8': 8, 'arg9': 'arg9'})
    print('-' * 20)
    print(f'value -> {value}')
    print(f'*args -> {other}')
