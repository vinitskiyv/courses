import sys


def return_example():
    l1 = []
    for n in range(100):
        l1.append(n * 2)
    return l1


def yield_example():
    for n in range(100):
        yield n * 2


l1 = return_example()
l2 = yield_example()
l3 = [n * 2 for n in range(100)]



# for i in l1:
#     print(i)
#
# for i in l2:
#     print(i)


print(sys.getsizeof(l1), l1)
print(sys.getsizeof(l2), l2)
