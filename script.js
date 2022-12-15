const student = "Грошелев Кирилл Дмитриевич"; // Очевидно, что здесь ваши личные Фамилия, Имя и Отчество

document.getElementById("student").innerHTML = student;


//Кол-во недель обучения всего (по полугодиям)
const total_work_weeks = [17, 24]; 


// Информация о кол-ве занятий по дням недели (по полугодиям)
const lessons = [{
  lessons: [4, 1, 2, 5, 2, 2, 0], 
  exams: [0, 2, 0, 2, 0, 0, 0]
}, 
{
  lessons: [1, 4, 4, 2, 5, 0, 0], 
  exams: [2, 0, 2, 0, 2, 0, 0]
}];

// Кол-во дней каникул
const holidays = [2*7, 0]

// Кол-во полугодий
let semesters = lessons.length;


// Ввод данных для подсчета
let ride_coast = +prompt('Стоимость проезда: ', 30);
let console_coast = +prompt('Стоимость приставки: ', 20000);

let ride_increase = +prompt('Сумма денег, которую дает мама на проезд (мин. ' + ride_coast + '): ', 50);
let lunch_increase = +prompt('Сумма денег, которую дает мама на обед: ', 200);

// Просить пользователя ввести новую сумму за проезд от мамы, пока она меньше стоимости проезда
while (ride_coast > ride_increase) {
  ride_increase = +prompt('Введите корректную сумму, которую дает мама на проезд (мин. ' + ride_coast + '): ');
}

// Разница между стоимостью проезда и суммой за проезд от мамы
const ride_difference = ride_increase - ride_coast

// Подсчет суммы элементов списка (нужно для счета суммы недель из total_work_weeks)
function count_list_sum(list) {
  sum = 0
  for (let week in list) {
    sum = sum + Number(week)
  }
  return sum
}

// Функция по подсчету финансов
function count_money(lessons, semesters, total_work_weeks, lunch_increase, ride_difference) {
  // Объявление переменных, которые будутиспользоваться для вывода данных о подсчете
  let money_increase = 0
  let days_count = 0
  let output_dict = {}

  // Цикл по семестрам
  for (let semester = 0; semester < semesters; ++semester) {

    // Цикл по неделям
    for (let week = 0; week < total_work_weeks[semester]-1; ++week) {
      lessons_list = lessons[semester].lessons;

      // Цикл по урокам
      for (let lesson = 0; lesson < lessons_list.length; ++lesson) {
        lesson_count = lessons_list[lesson];
        
        // Проверка на наличие денег на приставку
        if (console_coast <= money_increase) {
          output_dict = {semester: semester, days: days_count, money: money_increase, week: week}
          return output_dict
        }

        // Пропуск итерации, если пар больше 3 или их вообще нет
        if ((lesson_count > 3) || (lesson_count <= 0)) {
          if (lesson_count > 0) {
            money_increase = money_increase + ride_difference;
          }
          days_count = days_count + 1;
          continue
        }
        

        // Добавить дневную сумму денег к общей
        money_increase = money_increase + lunch_increase + ride_difference

        days_count = days_count + 1;
        

      }
    }

    lessons_list = lessons[semester].exams;
    // Цикл по сессиям 
    for (let lesson = 0; lesson < lessons_list.length; ++lesson) {
      lesson_count = lessons_list[lesson];
      
       // Проверка на наличие денег на приставку
       if (console_coast <= money_increase) {
        output_dict = {semester: semester, days: days_count, money: money_increase, week: total_work_weeks[semester]}
        return output_dict
      }

      // Проверка дня по условию
      if ((lesson_count > 3) || (lesson_count <= 0)) {
        if (lesson_count > 0) {
          money_increase = money_increase + ride_difference;
        }
        days_count = days_count + 1;

        continue
      }
      

      // Добавить дневную сумму денег к общей
      money_increase = money_increase + lunch_increase + ride_difference;

      days_count = days_count + 1;
      
    }
  
  // Учет каникул 
  days_count = days_count + holidays[semester]

  
} 
  // Вывод всех данных, на случай если итерация закончилась
  output_dict = {semester: semesters, days: days_count, money: money_increase, week: count_list_sum(total_work_weeks)}
  return output_dict

}

let money_data = count_money(lessons, semesters, total_work_weeks, lunch_increase, ride_difference)

if (money_data.money >= console_coast) {
  alert('На приставку накопить удалось за ' + Number(money_data.days) + ' дней! Это ' + (Number(money_data.week)+1) + "-ая неделя " + (Number(money_data.semester)+1) + "-ого семестра");
}
else {
  alert('Накопить не удалось, но за все время было накоплено ' + Number(money_data.money) + ' рублей!');
}