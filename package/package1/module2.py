"""
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
import os

for i in sys.path:
    print(i)
print('-' * 20)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)
sys.path.append(BASE_DIR)
print('-' * 20)
for i in sys.path:
    print(i)
"""

from package.package1.module1 import test1
from package.package2.module3 import test3


def test2():
    print(f'Good import funcs {test1.__name__}, {test3.__name__}')


if __name__ == '__main__':
    test2()
