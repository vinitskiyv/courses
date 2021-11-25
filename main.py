#!/usr/bin/python3

def hello_world():
    print(f'Hello world')


def module_name():
    return __name__


if __name__ == '__main__':
    hello_world()
    print(module_name())

