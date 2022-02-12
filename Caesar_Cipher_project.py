# Запрос направления - шифрование или дешифрование
# Язык алфавита
# шаг сдвига (со сдвигом вправо)
# y = (x + k) % n
# x = (y - k) % n
# x - символ открытого текста
# y - символ шифрованного текста
# n - количсетво символов (мощность алфавита)
# k - ключ (шаг сдвига)
#

print('Программа шифрования/дешифрования сообщений с помощью шифра Цезаря'.center(230))
print('Сперва выберете: шифруем или дешифруем текст? Напечатайте слово close или open ниже:')
direction = input()  # Шифрование или дешифрование
print('Выберите язык вводимого сообщения: английский - напечатайте en, или русский - напечатайте ru:')
language = input()  # Выбор языка en/ru
print('Выберите шаг сдвига шифра. Ниже введите число:')
shift_step = int(input())  # Шаг сдвига
print('И, наконец, введите или вставьте сам текст сообщения:')
user_message = input()  # Вводимый текст

if language == 'en':
    alphabet_lenght = 26
    alph_lower = [chr(i) for i in range(97, 123)]
    alph_upper = [chr(i) for i in range(65, 91)]
elif language == 'ru':
    alphabet_lenght = 32
    alph_lower = [chr(i) for i in range(1072, 1104)]
    alph_upper = [chr(i) for i in range(1040, 1072)]


def decryption_caesar(message, step):  # Расшифрование английского текста
    decrypted_message = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                eng_character = alph_upper.index(message[i])
                # расшифрованный символ upper
                x = (eng_character - step) % alphabet_lenght
                decrypted_message += alph_upper[x]
            elif message[i].islower():
                eng_character = alph_lower.index(message[i])
                # расшифрованный символ lower
                x = (eng_character - step) % alphabet_lenght
                decrypted_message += alph_lower[x]
        else:
            decrypted_message += message[i]
    return decrypted_message


def encryption_caesar(message, step):  # Расшифрование английского текста
    encrypted_message = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                eng_character = alph_upper.index(message[i])
                # расшифрованный символ upper
                x = (eng_character + step) % alphabet_lenght
                encrypted_message += alph_upper[x]
            elif message[i].islower():
                eng_character = alph_lower.index(message[i])
                # расшифрованный символ lower
                x = (eng_character + step) % alphabet_lenght
                encrypted_message += alph_lower[x]
        else:
            encrypted_message += message[i]
    return encrypted_message


print('Результат:', decryption_caesar(user_message, shift_step))
print('Результат:', encryption_caesar(user_message, shift_step))
