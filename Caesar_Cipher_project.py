print('Программа шифрования/дешифрования сообщений с помощью шифра Цезаря'.center(230))
print('Сперва выберете: шифруем или дешифруем текст? Напечатайте слово close или open ниже:'.center(230))
direction = input()  # Шифрование или дешифрование
print('Выберите язык вводимого сообщения: английский - напечатайте en, или русский - напечатайте ru:'.center(230))
language = input()  # Выбор языка en/ru
print('Выберите шаг сдвига шифра. Ниже введите число:'.center(230))
shift_step = int(input())  # Шаг сдвига
print('И, наконец, введите или вставьте сам текст сообщения:'.center(230))
user_message = input()  # Вводимый текст

# Логика выбора языка и выбор длины алфавита: 
if language == 'en':
    alphabet_lenght = 26
    alph_lower = [chr(i) for i in range(97, 123)]
    alph_upper = [chr(i) for i in range(65, 91)]
elif language == 'ru':
    alphabet_lenght = 32
    alph_lower = [chr(i) for i in range(1072, 1104)]
    alph_upper = [chr(i) for i in range(1040, 1072)]


def decryption_caesar(message, step):  # Расшифрование 
    decrypted_message = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                eng_character = alph_upper.index(message[i])
                # расшифрованный символ upper
                x = (eng_character - step) % alphabet_lenght # Формула для расшифрования
                decrypted_message += alph_upper[x]
            elif message[i].islower():
                eng_character = alph_lower.index(message[i])
                # расшифрованный символ lower
                x = (eng_character - step) % alphabet_lenght
                decrypted_message += alph_lower[x]
        else:
            decrypted_message += message[i]
    return decrypted_message


def encryption_caesar(message, step):  # Шифрование 
    encrypted_message = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                eng_character = alph_upper.index(message[i])
                # расшифрованный символ upper
                x = (eng_character + step) % alphabet_lenght # Формула для шифрования
                encrypted_message += alph_upper[x]
            elif message[i].islower():
                eng_character = alph_lower.index(message[i])
                # расшифрованный символ lower
                x = (eng_character + step) % alphabet_lenght
                encrypted_message += alph_lower[x]
        else:
            encrypted_message += message[i]
    return encrypted_message

if direction == 'open':
    print('Результат:'.center(200), decryption_caesar(user_message, shift_step).center(220))
elif direction == 'close':
    print('Результат:'.center(200), encryption_caesar(user_message, shift_step).center(220))
