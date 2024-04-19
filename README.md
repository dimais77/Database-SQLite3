# Database-SQLite3

## Файл main.py:

Cоздан класс University со следующими атрибутами и методами:  
name - имя университета  
add_student(name, age) - метод добавления студента.  
add_grade(sudent_id, subject, grade) - метод добавления оценки.  
get_students(subject=None) - метод для возврата списка студентов в формате [(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)], 
где subject, если не является None(по умолчанию) и если такой предмет существует, выводит студентов только по этому предмету.

## База данных students.db

В базе данных 2 таблицы: students и grades  
В таблице students следующие поля: id, name, age  
В таблице grades следующие поля: id, student_id, subject, grade  

Описание полей:  
id - в обоих таблицах обязательно PRIMARY KEY  
name - STR  
age - INT  
subject - STR  
grade - FLOAT  
student_id - INT (или внешний ключ)  
