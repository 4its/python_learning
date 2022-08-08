import re

# text = """100 ИНФ Информатика 213 МАТ Математика 156 АНГ Английский"""
# text2 = """ИНФ Информатика 213 МАТ Математика 156"""
# text3 = """100 ИНФ\tИнформатика 213 МАТ\tМатематика 156 АНГ\tАнглийский"""
# text4 = "<body>Пример жадного соответствия регулярных выражений</body>"


# a = re.split('\s+',text)
# print(a)
# print(type(a))  #посмотрим тип переменной
# print(a[2])     # слово Информатика
# reg_1 = re.compile('\s+')
# reg_2 = re.compile('\d+')

# qqq = re.compile('\s+')   # тут создан шаблон!
# a = qqq.split(text)
# print(a)
# print(type(a))  #посмотрим тип переменной
# print(a[2])     # слово Информатика
#
# a = reg_1.split(text)
# print('a',a)
# b = reg_2.findall(text)
# print('b',b)
# c=reg_2.search(text)
#
# print('c',c)
# print('c',c.start())
# print('c',c.end())
# print(text[c.start():c.end()])

# d = reg_1.sub(' ',text3)
# print('d',d)
#
# a = re.findall('[0-9]+',text)
# print(a)
# b = re.findall('[А-ЯЁ]{3}',text)
# print(b)
# c = re.findall('[а-яА-ЯёЁ]{4,}',text)
# print(c)
#
# print(re.findall('<.*>',text4))     # жадный шаблон
# print(re.findall('<.*?>',text4))    # ленивый шаблон
#
# text = 'python.org'
#
# text = '10, Янв 2018'
# print(re.findall('\d+',text))
# print(re.findall('\D+',text))
# print(re.findall('[а-яА-ЯёЁ]+',text))
# print(re.findall('\w+',text))
# print(re.findall('\W+',text))