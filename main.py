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

# функция input() с расширенными параметрами
class ModernInput(object):
    def __init__(self, text: str, integer: bool = False, range_input: tuple[int] = (), *args, **kwargs):
        self.text = text
        self.current_text = self.text
        self.is_integer = integer
        self.range_input = range_input
        self.type = int if (self.is_integer) else str
        self.max_value = 999999
        self.value = None
        self.__format_range()

    def __sub__(self, other):
        pass

    # вывод значения сразу после инициализации класса
    def __new__(cls, *args, **kwargs):
        obj = super(ModernInput, cls).__new__(cls)
        obj.__init__(*args, **kwargs)
        return obj.__show()

    def __int__(self):
        try:
            return int(self.value)
        except:
            return 0

    def __str__(self):
        return str(self.value)

    def __format_range(self):
        self.range_input = self.range_input[0:2]
        try:
            if self.range_input and self.range_input[1] == 0:
                self.range_input = (self.range_input[0], self.max_value)
        except:
            pass

    def __value_in_range(self, value: int):
        if self.is_integer and self.range_input:
            return value in iter(range(*self.range_input))
        return True

    def __show(self):
        try:
            data = self.type(input(self.current_text))
            if not self.__value_in_range(data):
                self.current_text = 'Значение выходит за рамки! ' + self.text
                return self.__show()
            self.value = data
            return data
        except:
            self.current_text = 'Данные введены некорректно! ' + self.text
            return self.__show()

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
        self.weekdays_codes = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

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

    # вывод сокращенного названия дня недели
    def get_weekday_string(self, day: int):
        try:
            return self.weekdays_codes[day]
        except:
            return '??'

    # вывод полного названия дня недели
    def get_weekday_name(self, day: int):
        try:
            return self.weekdays[day]
        except:
            return '??'

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

    # добавление финансов к общей сумме (только проезд)
    def add_from_ride(self):
        self.__money += self.ride_differance

    # вывод изменений в подсчетах
    def log(self, lesson: int, week: int, semester: int, is_exam: bool = False):
        return print(f'Day {self.days}: {self.money} RUB | {"EXAM" if is_exam else "LESSON"} | WEEKDAY {self.get_weekday_string(lesson)} | WEEK {week+1} | SEMESTER {semester+1}')


    # проверить, является ли день выходным
    def is_weekend(self, day_index: int, semester: int, exam: bool = False):
        try:
            if exam:
                lessons = self.get_exams_list(semester)

            else:
                lessons = self.get_lessons_list(semester)

            return lessons[day_index] <= 0
        except Exception as e:
            print(f'Ошибка проверка дня на выходной: {str(e)}')
            return False

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
                    if self.goal_complete:
                        return MoneyData(money=self.money, days=self.days, week=week, is_exam=False, lesson=index, complete=True,
                                         semester=semester)

                    if not self.__check_lessons(lesson):
                        if not self.is_weekend(index, semester, False):
                            self.add_from_ride()
                        self.add_day()
                        continue


                    self.add_to_money()
                    self.add_day()

                    self.log(index, week, semester)


            for index, exam in enumerate(self.get_exams_list(semester)):
                if self.goal_complete:
                    return MoneyData(money=self.money, days=self.days, week=total_work_weeks[semester], is_exam=True,
                                     lesson=index, complete=True, semester=semester)



                if not self.__check_lessons(exam):
                    if not self.is_weekend(index, semester, True):
                        self.add_from_ride()
                    self.add_day()
                    continue

                self.add_to_money()
                self.add_day()

                self.log(index, self.total_work_weeks[semester], semester, True)

            self.add_holidays(semester)

        return MoneyData(money=self.money, days=self.days, week=self.week_sum, is_exam=False, lesson=0, complete=False,
                         semester=self.semesters-1)



# Ввод данных
ride_coast = ModernInput('Стоимость проезда: ', True)
console_coast = ModernInput('Стоимость приставки: ', True)

ride_increase = ModernInput(f'Сумма денег, которую дает мама на проезд (мин. {ride_coast}): ', True, range_input=(ride_coast, 0))
lunch_increase = ModernInput('Сумма денег, которую дает мама на обед: ', True)

# Разница между прибавкой за проезд от мамы и стоимостью проезда
ride_differance = ride_increase - ride_coast

# инициализация класса для подсчета и вызов функции подсчета
money_counter = MoneyCounter(lessons, ride_differance, console_coast, lunch_increase, total_work_weeks, holidays)
money = money_counter.predict()

if money.complete:
    print(f'Вы успешно накопили на свою цель за {money.days} дней! Это {money_counter.get_weekday_name(money.lesson).lower()} {money.week+1}-ой недели {money.semester+1}-ого семестра во время {"обычных занятий" if not money.is_exam else "экзаменов"}! ')
else:
    print(f'Увы, но накопить не удалось( Но за все время было накоплено {money.money} RUB!')




