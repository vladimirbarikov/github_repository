# Задача 5. Частота слова — часть 1

# Часто при построении моделей машинного обучения на текстах одним из входных параметров модели является частотность
# вхождения слова в текст. В этой задаче мы решим проблему нахождения частоты слова в документе.

# В переменной document_text задан текст. Нужно найти частоту использования каждого уникального слова и положить его
# в словарь word_frequency. Преобразовывать слова в начальную форму не нужно.

# Рекомендации:
# Для удаления лишних символов используйте метод replace для текстов.
# Для подсчёта частот используйте метод count на списках.

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


if __name__ == '__main__':
    word_frequency = frequency(document_text)
    for k, v in word_frequency.items():
        print(f' {k}: {v}')
