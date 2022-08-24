import json

# dictData = {    "ID"        : 210450,
#                 "login"     : "admin",
#                 "name"      : "John Smith",
#                 "password"  : "root",
#                 "phone"     : 5550505,
#                 "email"     : "smith@mail.com",
#                 "online"    : True }
#
# jsonData = json.dumps(dictData, indent=4)
# print(jsonData)
#
# with open("data.json", "w") as file:
#     file.write(jsonData)

# создаем пользовательский класс >>>
# class Test:
#     def __init__(self, title, body):
#         self.title = title
#         self.body = body
#
# # создаем экземпляр класса
# t = Test("Some string", "Here is a bit more text, but still isn't enough")
# # пытаемся сериализовать его в JSON, но...
#
# class TestEncoder(json.JSONEncoder):
#     def default(self, o):
#         return {"TITLE": o.title, "BODY": o.body, "CLASSNAME": o.__class__.__name__}
#
# x = json.dumps(t, cls=TestEncoder)
# print(x)
#
# y = json.loads(x)
# print(y)

# class Figure:
#     def __init__(self, title, form, color):
#         self.title = title
#         self.form = form
#         self.color = color
#
#     def __str__(self):
#         return f"Figure: {self.title}, {repr(self.form)}, {repr(self.color)}"
#
# class Form:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"<Form: {self.name}>"
#
# class Color:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return f"<Color: {self.name}>"
#
# class JSONDataAdapter:
#     @staticmethod
#     def to_json(o):
#         if isinstance(o, Figure):
#             return json.dumps({  "title": o.title,
#                                  "form": o.form.name,
#                                  "color": o.color.name, })
#     @staticmethod
#     def from_json(o):
#         o = json.loads(o)
#         try:
#             form = Form(o["form"])
#             color = Color(o["color"])
#             figure = Figure(o["title"], form, color)
#             return figure
#         except AttributeError:
#             print("Неверная структура")
#
# if __name__ == '__main__':
# # создадим несколько цветов
#     black = Color("Black")
#     yellow = Color("Yellow")
#     green = Color("Green")
# # несколько форм
#     rountt = Form("Rounded")
#     square = Form("Squared") # объекты фигур
#     figure_one = Figure("Black Square", form=square, color=black)
#     figure_two = Figure("Yellow Circle", form=rountt, color=yellow)
#     print("“Отображение объектов”")
#     print(figure_one)
#     print(figure_two)
#     print()
# # преобразуем данные в JSON
#     jone = JSONDataAdapter.to_json(figure_one)
#     jtwo = JSONDataAdapter.to_json(figure_two)
#     print("“Отображение JSON”")
#     print(jone)
#     print(jtwo)
#     print()
# # восстановим объекты
#     restored_one = JSONDataAdapter.from_json(jone)
#     restored_two = JSONDataAdapter.from_json(jtwo)
#     print("Отображение восстановленных объектов")
#     print(restored_one)
#     print(restored_two)

# class Clock:
#     __DAY = 86400 # число секунд в одном дне
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s = self.seconds % 60 # секунды
#         m = (self.seconds // 60) % 60 # минуты
#         h = (self.seconds // 3600) % 24 # часы
#         return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
#
#     @classmethod
#     def __get_formatted(cls, x):
#         return str(x).rjust(2, "0")
#
#     # def __eq__(self, other):
#     #     if not isinstance(other, (int, Clock)):
#     #         raise TypeError("Операнд справа должен иметь тип int или Clock")
#     #     sc = other if isinstance(other, int) else other.seconds
#     #     return self.seconds == sc
#     def __eq__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds == sc
#
#     # def __lt__(self, other):
#     #     if not isinstance(other, (int, Clock)):
#     #         raise TypeError("Операнд справа должен иметь тип int или Clock")
#     #     sc = other if isinstance(other, int) else other.seconds
#     #     return self.seconds < sc
#     def __lt__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds < sc
#
#     def __gt__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds > sc
#
#     def __le__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds <= sc
#
#     @classmethod
#     def __verify_data(cls, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError("Операнд справа должен иметь тип int или Clock")
#         return other if isinstance(other, int) else other.seconds
#
# c1 = Clock(1000)
# c2 = Clock(1000)
# print(c1 < c2)

# from datetime import datetime
# class Event:
#     events = []
#     def __init__(self, date):
#         self.date = date
#         self.add_event(self) \
#
#     @classmethod
#     def add_event(cls, event):
#         cls.events.append(event)
#         cls.sort_events() \
#
#     @classmethod
#     def sort_events(cls):
#         cls.events.sort(key=lambda event: event.date)
#
#     def __repr__(self):
#         return '<Event({})>'.format(self.date.date())
#
# e = Event(datetime(1999, 1, 1))
# e = Event(datetime(2000, 1, 1))
# e = Event(datetime(2022, 8, 23))
# e = Event(datetime(1960, 1, 1))
#
# print(e.events)
# print(Event.events)

# class Foo(object):
#     def __init__(self, score):
#         self.score = score
#     def __lt__(self, other):
#         return self.score < other.score
#
# l = [Foo(3), Foo(1), Foo(2)]
# l.sort()
# print(l)

# def avg(ranks):
#     assert len(ranks) != 0, 'Список ranks не должен быть пустым'
#     return round(sum(ranks)/len(ranks), 2)
# ranks = [62, 65, 75]
# print("Среднее значение:", avg(ranks))
# #Вызов ошибки
# ranks = []
# print("Среднее значение:", avg(ranks))

class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage
    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
                f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"
# Второе условие
class PersonAgeException2(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage
    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
                f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"

class Person:
    def __init__(self, name, age, w):
        self.__name = name # устанавливаем имя
        self.__weight = w
        minage, maxage = 1, 110
        if minage < age < maxage: # устанавливаем возраст, если передано корректное значение
            self.__age = age
        else: # иначе генерируем исключение
            raise PersonAgeException(age, minage, maxage)
        # Проверка второго условия
        if minage < age < maxage: # устанавливаем возраст, если передано корректное значение
            self.__age = age
        else: # иначе генерируем исключение
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f"Имя: {self.__name} Возраст: {self.__age}")

try:
    tom = Person("Tom", 37)
    tom.display_info() # Имя: Tom Возраст: 37
    bob = Person("Bob", -23)
    bob.display_info()
except PersonAgeException as e:
    print(e) # Недопустимое значение: -23. Возраст должен быть в диапазоне от 1 до 110