# Напишите функцию, которая проверяет пароль на соответствие условиям:

# Состоит не менее чем из 8 символов.
# Есть хотя бы одна буква в верхнем регистре.
# Есть хотя бы 2 цифры.
# В пароле не используются символы: § ±.
# В результате проверки функция должна выдать, соответствует ли данный пароль условиям. Если да — вывести «OK»,
# если нет — вывести все ошибки в данном пароле. Используйте декомпозицию.

# Подсказка:

# Для проверки того, является ли символ цифрой, можно использовать метод isdigit.
# Для проверки, стоит ли символ в верхнем регистре, можно использовать метод isupper.


def check_length(password):
    if len(password) >= 8:
        return True
    print('Длина менее 8 символов')
    return False


def check_upper(password):
    for character in password:
        if character.isupper():
            return True
    print('Используйте хотя бы одну букву в верхнем регистре')
    return False


def check_digits(password):
    digits = 0
    for character in password:
        if character.isdigit():
            digits += 1
    if digits > 1:
        return True
    print('Используйте хотя бы 2 цифры')
    return False


def check_special_characters(password):
    if not ('§' in password or '±' in password):
        return True
    print('Использован один из запрещенных символов: § ±')
    return False


def check_pass(password):
    errors = []
    errors.append(check_length(password))
    errors.append(check_upper(password))
    errors.append(check_digits(password))
    errors.append(check_special_characters(password))

    if False not in errors:
        print('OK')


check_pass('12abcABC')
