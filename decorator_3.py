import types
from datetime import datetime
from functools import wraps

def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            call = datetime.now()
            result = old_function(*args, **kwargs)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(f'Дата и время вызова функции {call}.\n'
                        f'Имя функции {old_function.__name__}.\n'
                        f'Аргументы {args}, {kwargs}.\n'
                        f'Возвращаемое значение {result}.\n'
                        f'----------------------------------\n')
            return result
        return new_function
    return __logger

@logger('decorator_3.log')
def flat_generator(list_of_lists):

    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_3():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_3()
