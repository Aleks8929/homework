
Ваша задача:
Цель: применить на практике начальные знания о пространстве имён и оператор global. Закрепить навыки из предыдущих модулей.

Задача "Счётчик вызовов":

Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.

Давайте реализуем данную фишку самостоятельно!



Вам необходимо написать 3 функции:

Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
Пункты задачи:

Создать переменную calls = 0 вне функций.
Создайте функцию count_calls и измените в ней значение переменной calls. Эта функция должна вызываться в двух других функциях.
Создать функцию string_info с параметром string и реализовать логику работы по описанию.
Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
Вызовите соответствующие функции string_info и is_contains произвольное количество раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).


Пример результата выполнения программы:

Пример выполняемого кода:

печать(string_info('Капибара'))

печать(string_info('Армагеддон'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('цикл', ['переработка', 'циклический'])) # совпадений нет

печать (звонки)

Вывод на консоль:

(8, «КАПИБАРА», «капибара»)

(10, «Армагеддон», «армагеддон»)

Верно

Ложь

4

