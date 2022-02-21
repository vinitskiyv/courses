

def tester(start):
    state = start

    def nested(label):
        print(label, state)
        state += 1  # По умолчанию изменять нельзя (в Python 2.Х вообще никогда)

    return nested


F = tester(0)
F('spam')


def tester(start):
    state = start  # Каждый вызов получает собственное значение state

    def nested(label):
        nonlocal state  # Запоминает из объемлющей области видимости
        print(label, state)
        state += 1  # Нелокальную переменную разрешено изменять

    return nested


F = tester(0)
F('spam')
F('eggs')