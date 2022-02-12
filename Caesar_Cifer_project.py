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





direction = input() # Шифрование или дешифрование
language = input() # Выбор языка en/ru
shift_step = int(input()) # Шаг сдвига
user_message = input() # Вводимый текст

if language == 'en':
    alphabet_lenght = 26
    alph_lower = [chr(i) for i in range(97, 123)]
    alph_upper = [chr(i) for i in range(65, 91)]
elif language == 'ru':
    alphabet_lenght = 32
    alph_lower = [chr(i) for i in range(1072, 1104)]
    alph_upper = [chr(i) for i in range(1040, 1072)]



def decryption_caesar (message, step): # Расшифрование английского текста
    decrypted_message = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                eng_character = alph_upper.index(message[i]) 
                x = (eng_character - step) % alphabet_lenght # расшифрованный символ upper
                decrypted_message += alph_upper[x]
            elif message[i].islower():
                eng_character = alph_lower.index(message[i])
                x = (eng_character - step) % alphabet_lenght # расшифрованный символ lower
                decrypted_message += alph_lower[x]
        else:
            decrypted_message += message[i]
    return decrypted_message

def encryption_caesar (message, step): # Расшифрование английского текста
    encrypted_message = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                eng_character = alph_upper.index(message[i]) 
                x = (eng_character + step) % alphabet_lenght # расшифрованный символ upper
                encrypted_message += alph_upper[x]
            elif message[i].islower():
                eng_character = alph_lower.index(message[i])
                x = (eng_character + step) % alphabet_lenght # расшифрованный символ lower
                encrypted_message += alph_lower[x]
        else:
            encrypted_message += message[i]
    return encrypted_message


#print(decryption_caesar(user_message, shift_step))
print(encryption_caesar(user_message, shift_step))