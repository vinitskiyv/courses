"""
list1 = [1, 2, 3]
list2 = list1.append(4)
print(len(list2))  # 3, 4, None, Error


list1 = [1, 2]
list2 = [3, 4]
list2 = list1.extend(list2)
print(list2[4])  # 1, 2, 3, 4, 0, None, Error


list1 = [1, 2, 3, 4, 1]
for value in list1:
    list1[value] = 0
print(list1)

[1, 0, 0, 0, 0]
[1, 2, 3, 4, 1]
[0, 0, 0, 0, 0]
[0, 0, 3, 0, 1]
[]
Error

"""
import copy


def print_objects(name='list', *args):
    print("-" * 20)
    for idx, val in enumerate(args):
        print(f'{name}{idx + 1} {val}')
    print("-" * 20)


list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print_objects('list', list1, list2)


list2 = list1.copy()
list2.append(5)
print_objects('list', list1, list2)


dict1 = {1: 'one', 2: 'two', 3: 'three'}
dict2 = dict1
dict2[1] = 'test'
print_objects('dict', dict1, dict2)


def example_1():
    """
    Поверхностная копия - создает новый составной объект, и затем  (по мере
                          возможности) вставляет в него ссылки на объекты,
                          находящиеся в оригинале.
                          copy.copy()
    Глубокая копия - создает новый составной объект, и затем рекурсивно
                     вставляет в него копии объектов, находящихся в оригинале.
                     copy.deepcopy()
    """
    list2 = list1
    list3 = copy.copy(list1)
    print_objects('list', list1, list2, list3)
    list2[0] = ['ZERO', 'ONE', 'TWO']
    list3[1] = ['ZERO', 'ONE', 'TWO']
    print_objects('list', list1, list2, list3)


def example_2():
    list2 = copy.copy(list1)
    list3 = copy.deepcopy(list1)
    list4 = list1.copy()
    print_objects('list', list1, list2, list3, list4)
    list2[0][0] = 'change0'
    list3[0][1] = 'change1'
    list4[0][2] = 'change2'
    print_objects('list', list1, list2, list3, list4)


def example_3():
    dict1 = {
        1: 'one',
        2: {'test1': 'value1', 'test2': 'value2'},
        3: {'python2': 'old', 'python3': 'new'},
    }
    dict2 = copy.copy(dict1)
    dict3 = copy.deepcopy(dict1)
    dict4 = dict1.copy()
    print_objects('dict', dict1, dict2, dict3, dict4)
    dict2[1] = dict2[1].upper()
    dict2[2]['test1'] = 'change1'
    dict3[2]['test2'] = 'change2'
    dict4[3]['python2'] = 'LEGACY'
    print_objects('dict', dict1, dict2, dict3, dict4)

#
example_1()
example_2()
example_3()

