

def func_recursion(s1, s2):
    s1 = s1 + s2
    return func_recursion(s1, s2)


if __name__ == '__main__':
    func_recursion('x', 'y')
