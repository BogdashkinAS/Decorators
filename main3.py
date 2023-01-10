# Решение к 3 задаче домашнего задания к лекции «Decorators»" (декоратор к предыдущему ДЗ по теме "Итераторы, генераторы")

import os
import datetime
import types


def logger(old_function):
    pass

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        date_time = datetime.datetime.now()
        with open('log_generators.log', 'a', encoding='utf8') as file:
            file.writelines(f'date_time: {date_time}, name_function: {old_function.__name__}, value: {args, kwargs}, result: {result}\n')
        return result
    return new_function

def test_1():

    path = 'main.log'
    if os.path.exists('log_generators.log'):
        os.remove('log_generators.log')
    
    @logger
    def flat_generator(list_of_lists):
        list_ = list_of_lists
        numbers = []
        for item in list_:
            numbers.extend(item)
        for item2 in numbers:
            yield item2

    @logger
    def test_2():

        list_of_lists_1 = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]

        for flat_iterator_item, check_item in zip(
                flat_generator(list_of_lists_1),
                ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ):
            # print(flat_iterator_item, check_item) # можно запустить для проверки идентичности списков

            assert flat_iterator_item == check_item

        assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

        assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    test_2()

if __name__ == '__main__':
    test_1()




