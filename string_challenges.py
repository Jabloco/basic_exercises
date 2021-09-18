# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'

print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
def vowel_in_word(input_word: str):
    vowel = ('ауоыиэяюёе')
    vowel_count = 0
    for letter in input_word.lower():
        if letter in vowel:
            vowel_count += 1
    print(f'В слове {input_word} {vowel_count} гласных буквы')

vowel_in_word(word)
# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
def first_letter(input_sentence):
    words = sentence.split()
    print('Первые буквы слов:')
    for word in words:
        print(word[0])

first_letter(sentence)


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
def word_midle_len(input_sentence):
    words = sentence.split()
    words_count = len(words)
    letter_count = 0
    for word in words:
        letter_count += len(word)
    midle_len = letter_count / words_count
    print(f'Средняя длина слова в пердложении {int(midle_len)}')  # среднее количество букв наверно не может быть дробным числом

word_midle_len(sentence)