# Скрипт для подсчета накоплений со школьных обедов. 
### Сделал за пару :)
Не знаю, должно ли быть так по условию, но я сделал так, чтобы мой скрипт не считал деньги со дней, в которых нет пар. Также, деньги со дней без пар не учитываются и в варианте для теста ниже.

## Предлагаю свой вариант для теста (исход: не накопил)
### Вводимые данные:
**Проезд:** 30 RUB

**Цель:** 50000 RUB

**Дают на проезд:** 50 RUB

**На обед:** 200 RUB

**Разница за проезд:** 20

## Таким образом получается: 
### Подсчет первого семестра:
>(200 + 20) * 4 дня = 880 - в неделю

>(200+20) * 2 дня * 1 неделю = 440 - экзамены

>(880 * 16 недель) + 440 = 14520 RUB (всего)

### Подсчет второго семестра
>(200 + 20) * 2 дня = 440 - в неделю

>(200 + 20) * 3 дня * 1 неделю = 660 - экзамены

>(440 * 23 недели) + 660 = 10780 RUB (всего)

### Итого:
**Всего накоплено**: 25300 RUB

**Исход:** не накопил

## Вариант для теста (исход: накопил)
### Вводимые данные:
**Проезд:** 30 RUB

**Цель:** 20000 RUB

**Дают на проезд:** 50 RUB

**На обед:** 200 RUB

**Разница за проезд:** 20

## Таким образом получается: 

Из первого теста можно отметить, что за первый семестр мы получаем 14520 RUB. Тогда:

> 17 недель * 7 дней = 119 дней - это 14520 RUB

> 119 дней + 14 дней = 133 дня - прибавили каникулы

Итого: за 133 дня мы имеем 14520 RUB

Далее, так как мы получаем во втором семестре по 440 рублей в неделю на протяжении 23 недель без экзаменов, то за второй семестр мы получаем 10120, 
тогда:

> 14520 + 10120 = 24640 RUB за 40 недель

Следовательно мы пересчитали 4640 RUB за второй семестр:

> 4640 RUB / 440 RUB =~ 10 полных недель

Теперь считаем, сколько дней мы пересчитали во втором семестре:

> 23 недели - 10 недель = 13 недель (кол-во недель, которое понадобилось для накопления нужной суммы)

> 13 недель * 440 RUB = 5720 RUB (Сумма за 13 недель второго семестра)

> 14520 RUB + 5720 RUB = 20240 RUB

> 20240 RUB - 20000 RUB = 240 RUB

Получается, что мы пересчитали 1 день равный 220 рублям. Так как до последнего прибыльного дня (Четверга 2 семестра) 3 дня с конца недели (С Воскресенья по Четверг) значит:

> 133 + 13*7 - 3 = 221 день

### Итого:

**Исход:** накопил за 221 день. Это 13-ая неделя 2-ого семестра.
