"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""


def common_and_longest(text: str) -> tuple:
    words = text.split(" ")
    counter = {}
    for word in words:
        current = counter.setdefault(word, 0)
        counter[word] = current + 1
    common = words[0]
    longest = words[0]
    for word, num in counter.items():
        if num > counter[common]:
            common = word
        if len(word) > len(longest):
            longest = word
    return common, longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
