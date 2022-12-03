# -*- coding: utf-8 -*-

# недели по семестрам
total_work_weeks = [17, 24]

# пары и экзамены по семестрам
lessons = [{
  "lessons": [4, 1, 2, 5, 2, 2, 0],
  "exams": [0, 2, 0, 2, 0, 0, 0]
},
{
  "lessons": [1, 4, 4, 2, 5, 0, 0],
  "exams": [2, 0, 2, 0, 2, 0, 0]
}]

# каникулы по семестрам
holidays = [2*7, 0]

# интервал между кол-вом минимальных и максимальных пар по условию
lessons_range = (1, 3)

# кол-во семестров
semesters = len(lessons)

# класс для преобразования словаря в объект (чтобы вместо ключей выводить данные по атрибутам)
class MoneyData(object):
    def __init__(self, **kwargs):
        self.data = kwargs

    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        return None


class MoneyCounter:
    # инициализация класса
    def __init__(self, lessons: list[dict], ride_differance: int, goal: int, increase: int, total_work_weeks: list[int], holidays: list[int], lesson_range: tuple[int] = (1, 3)):
        self.lessons = lessons
        self.ride_differance = ride_differance
        self.total_work_weeks = total_work_weeks
        self.goal = goal
        self.holidays = holidays
        self.increase = increase
        self.lessons_range = lesson_range
        self.semesters = len(self.lessons)

        self.__money = 0
        self.__days = 0

    # функция для изменения кортежей
    def __edit_tuple(self, tuple_obj: tuple[int], pos: int, val: int):
        list_tuple = list(tuple_obj)
        list_tuple[pos] += val
        return tuple(list_tuple)

    # проверка условия по кол-ву пар
    def __check_lessons(self, lessons: int):
        lessons_range = self.__edit_tuple(self.lessons_range, 1, 1)
        return lessons in iter(range(*lessons_range))

    # вывод кол-ва дней каникул по семестрам
    def get_holidays(self, semester: int = 0):
        return self.holidays[semester]

    # добавить каникулы по семестрам к общему кол-ву дней
    def add_holidays(self, semester: int):
        self.__days += self.get_holidays(semester)

    # очистка данных прошлого подсчета перед новым
    def __clear_count_data(self):
        self.__money = 0
        self.__days = 0

    # проверка на наличие денег на приставку
    @property
    def goal_complete(self):
        return self.__money >= self.goal

    # вывод списка пар по семестрам
    def get_lessons_list(self, semester: int):
        return self.lessons[semester]['lessons']

    # вывод списка пар на экзаменах по семестрам
    def get_exams_list(self, semester: int):
        return self.lessons[semester]['exams']

    # вывод списка с кол-вом пар в каждом подходящем по условию дне по семестрам
    def get_lessons_per_week(self, semester: int):
        return [lesson for lesson in self.get_lessons_list(semester) if self.__check_lessons(lesson)]

    # вывод списка с кол-вом пар на экзаменах в каждом подходящем по условию дне по семестрам
    def get_exam_lessons(self, semester: int):
        return [exam for exam in self.get_exams_list(semester) if self.__check_lessons(exam)]

    # вывод кол-во недель, не считая экзамены
    def lesson_weeks(self, semester: int):
        return self.total_work_weeks[semester]-1

    # вывод недели, на которой проходит экзамен по семестрам
    def exam_week(self, semester: int):
        return self.lesson_weeks(semester) + 1

    # добавление финансов к общей сумме
    def add_to_money(self):
        self.__money += self.increase + self.ride_differance

    # вывод общего кол-ва недель обучения
    @property
    def week_sum(self):
        return sum(total_work_weeks)

    # вывод общей суммы финансов
    @property
    def money(self):
        return self.__money

    # вывод общего кол-ва дней
    @property
    def days(self):
        return self.__days

    # добавить 1 день к общей сумме дней
    def add_day(self):
        self.__days += 1

    # функция подсчета финансов
    def predict(self):
        self.__clear_count_data()

        for semester in range(self.semesters):
            for week in range(self.lesson_weeks(semester)):
                for index, lesson in enumerate(self.get_lessons_list(semester)):
                    self.add_day()
                    if not self.__check_lessons(lesson):
                        continue

                    if self.goal_complete:
                        return MoneyData(money=self.money, days=self.days, week=week, is_exam=False, lesson=index, complete=True,
                                         semester=semester)

                    self.add_to_money()

            for index, exam in enumerate(self.get_exams_list(semester)):
                self.add_day()
                if not self.__check_lessons(exam):
                    continue

                if self.goal_complete:
                    return MoneyData(money=self.money, days=self.days, week=total_work_weeks[semester], is_exam=True,
                                     lesson=index, complete=True, semester=semester)

                self.add_to_money()

            self.add_holidays(semester)

        return MoneyData(money=self.money, days=self.days, week=self.week_sum, is_exam=False, lesson=0, complete=False,
                         semester=self.semesters-1)



# Ввод данных
ride_coast = int(input('Стоимость проезда: '))
console_coast = int(input('Стоимость приставки: '))

ride_increase = int(input(f'Сумма денег, которую дает мама на проезд (мин. {ride_coast}): '))
lunch_increase = int(input('Сумма денег, которую дает мама на обед: '))

# Просить пользователя ввести сумму за проезд от мамы, пока эта сумма не соответствует условиям
while ride_coast > ride_increase:
    ride_increase = int(input(f'Введите корректную сумму денег, которую дает мама на проезд (мин. {ride_coast}): '))

# Разница между прибавкой за проезд от мамы и стоимостью проезда
ride_differance = ride_increase - ride_coast

# инициализация класса для подсчета и вызов функции подсчета
money_counter = MoneyCounter(lessons, ride_differance, console_coast, lunch_increase, total_work_weeks, holidays)
money = money_counter.predict()

if money.complete:
    print(f'Вы успешно накопили на свою цель за {money.days} дней! Это {money.lesson+1}-ый день {money.week+1}-ой недели {money.semester+1}-ого семестра во время {"обычных занятий" if not money.is_exam else "экзаменов"}! ')
else:
    print(f'Увы, но накопить не удалось( Но за все время было накоплено {money.money} RUB!')




