calls = 0
def count_calls(call):
    global calls
    calls += call
    return calls

def string_info(string):
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    count_calls(1)
    return a

def is_contains(string_info, is_contains):
    is_contains_2 = []
    count_calls(1)
    for i in is_contains:
        is_contains_2.append(i.lower())
    return(string_info.lower() in is_contains_2)


print(string_info('Капибара'))
print(string_info('Армагеддон'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('цикл', ['переработка', 'циклический']))
print(calls)