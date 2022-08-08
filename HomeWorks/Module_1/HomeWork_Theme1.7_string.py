print('=== Практическое задание по теме «Строки и форматирование» ===')
print('Задание №1')
# Входные данные Дана строка.
sample = 'Welcome to Python course!'
print('Дана строка: ', sample)
# Выходные данные
# • Сначала выведите третий символ этой строки.
print('1) ', sample[2:3])
# • Во второй строке выведите предпоследний символ этой строки.
print('2) ', sample[len(sample) - 2:len(sample) - 1])
# • В третьей строке выведите первые пять символов этой строки.
print('3) ', sample[:5])
# • В четвертой строке выведите всю строку, кроме последних двух символов.
print('4) ', sample[:len(sample) - 2])
# • В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы
# выводятся начиная с первого).
print('5) ', sample[::2])  # не совсем понял условие...
# • В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print('6) ', sample[1::2])  # не совсем понял условие...
# • В седьмой строке выведите все символы в обратном порядке.
print('7) ', sample[::-1])
# • В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print('8) ', (sample[::2])[::-1])
# • В девятой строке выведите длину данной строки.
print('9) ', len(sample))

print('\nЗадание №2')

# Задание 2
# Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет, имеется ли
# подстрока subst в строке st. В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.
def serch_substr(substr, st):
    substr, st = substr.lower(), st.lower()     #apply lower case to all
    if st.find(substr) >= 1:
        print('Есть контакт!')
    else:
        print('Мимо!')

str1 = 'Welcome to Python course!'  # Нужно делать ввод строки пользователем?
str2 = 'python'                     # Нужно делать ввод строки пользователем?
print('Строка №1: ', str1)        # Проверочные строки
print('Строка №2: ', str2)        # Проверочные строки
serch_substr(str2, str1)

print('\nЗадание №3')

# Задание 3
# Требуется определить индексы первого и последнего вхождения буквы в строке. Для этого нужно написать
# функцию first_last(letter, st), включающую 2 параметра: letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть, то кортеж будет состоять из
# первого и последнего индекса этого символа.
def first_last(letter, st):
    res = []
    if (st.find(letter)) >= 0:
        res.append(st.find(letter))
        if (st.rfind(letter)) >= 0:
            res.append(st.rfind(letter))
    else:
        res = [None, None]
    return tuple(res)

sample = 'Съешь ещё этих мягких французских булок, да выпей же чаю'
print('Имеем строку:      ', sample)
letter = input('Введите букву которую будем искать: ')
print('Ищем идексы буквы: ', letter)
print(first_last(letter, sample))

print('\nЗадание №4')

# Задание 4
# На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в ней.
# Пробелы нужно игнорировать (не учитывать при подсчете). Для выведения результатов вычислений требуется написать
# функцию top3(st). Итог работы функции представить в виде строки: «символ – количество раз, символ – количес-
# тво раз...».
def top3(st):
    print('Default string: ',st)
    str = set(st)    # преобразуем в множество, тем самым исключив повторы
    str.remove(' ')  # исключим пробел!
    d_st = {}        # введем словарь
    for i in str:
        d_st.setdefault(i, st.count(i)) # в словарь дабвим пары "символ":"количество в строке"
    a = (sorted(d_st.values())[::-1])[0:3]      #ограничитель, который возмет 3 самых больших значения ключа из словаря
    b = []
    for i in a:                     # для каждого значения a...
        for j in d_st:              # ... ищем совпадение значения со словарем
            if d_st.get(j)== i:
                b.append(j)
                d_st.pop(j)
                break
    print('«',b[0],'–',a[0],'раз,',b[1],'–',a[1],'раз,',b[2],'–',a[2],'раз »')
st = 'На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в ней'
top3(st)

print('\nЗадание №5')

# Задание 5
# Дан текст, произвольный длины, необходимо вывести слова текста в отсортированном алфавитном порядке.
# Например текст «Это пример сроки», результат работы программы:
# пример
# строки
# это

def inrow(string):
    string = string.lower()             #make all in lower case
    list_string = string.split(' ')     #making a list from words at string by separating it by spaces
    for i in (sorted(list_string)):     #lets iterate SORTED list and print his values
        print(i)

st = 'Это пример сроки'
inrow(st)