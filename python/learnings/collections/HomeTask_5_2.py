# Задача 6. Частота слова — часть 2.

# Выведите все слова из word_frequency в порядке убывания частоты. Если частота одинаковая, выведите слова в порядке,
# обратном лексикографическому (то есть по убыванию).

# Подсказка 1: используйте функцию sorted для списков. Она сортирует список по возрастанию,
# если вызвать sorted(my_list), и по убыванию, если вызвать sorted(my_list, reverse=True).

# Подсказка 2: если сортируемый список будет состоять из кортежей, то он будет отсортирован по элементам,
# которые стоят на первом месте. Если элементы на первом месте равны, то сортировка производится по вторым элементам.

document_text = 'There are the Food Courts in the cities that seats a lot of people and caters \
                for every taste with dishes from all around the world. \
                The aromatic smells that come from the Food Courts arc so delicious that your mouth will water. \
                In recent years foreign foods have become a regular part of our life.'


def frequency(text):
    normalized_text = text.replace('.', ' ').split()
    word_frequency = {}
    for word in normalized_text:
        count = normalized_text.count(word)
        word_frequency[word] = count
    return word_frequency


def sorting(text):
    word_frequency = frequency(text)
    my_list = []
    for k, v in word_frequency.items():
        item = (v, k)
        my_list.append(item)
    return sorted(my_list, reverse=True)


if __name__ == '__main__':
    sorted_list = sorting(document_text)
    for elem in sorted_list:
        print(elem[1])
