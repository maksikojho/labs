# TODO  Напишите функцию count_letters
def count_letters(text):
    dict = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict
def calculate_frequency(letters):
    global main_str
    all_let = 0
    for i in main_str:
        if i.isalpha():
            all_let += 1
    freqs = {}
    for letter in letters:
        freqs[letter] = '%.2f' % (letters[letter] / all_let)
    return freqs
# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letters = {}

letters = count_letters(main_str)
freqs = calculate_frequency(letters)
for i in freqs:
    print(f'{i}: {freqs[i]}')
# TODO Распечатайте в столбик букву и её частоту в тексте
