import sqlite3


class University:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('students.db')
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                age INTEGER)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS grades (
                                id INTEGER PRIMARY KEY,
                                student_id INTEGER,
                                subject TEXT,
                                grade REAL,
                                FOREIGN KEY (student_id) REFERENCES students(id))''')

        self.conn.commit()

    def add_student(self, name, age):
        self.cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def add_grade(self, student_id, subject, grade):
        self.cur.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)",
                         (student_id, subject, grade))
        self.conn.commit()

    def get_students(self, subject=None):
        if subject:
            self.cur.execute('''SELECT students.name, students.age, grades.subject, grades.grade
                                FROM students
                                INNER JOIN grades ON students.id = grades.student_id
                                WHERE grades.subject = ?''', (subject,))
        else:
            self.cur.execute('''SELECT students.name, students.age, grades.subject, grades.grade
                                FROM students
                                INNER JOIN grades ON students.id = grades.student_id''')

        return self.cur.fetchall()


# Пример использования
u1 = University('Urban')

# Добавление студентов
u1.add_student('Дмитрий', 46)  # id - 1
u1.add_student('Евгений', 24)  # id - 2
u1.add_student('Илья', 26)  # id - 3
u1.add_student('Евгения', 25)  # id - 4

# Добавление оценок
u1.add_grade(1, 'Python', 4.5)
u1.add_grade(1, 'Java', 4.0)
u1.add_grade(2, 'PHP', 4.3)
u1.add_grade(2, 'Python', 4.5)
u1.add_grade(3, 'Java', 4.2)
u1.add_grade(3, 'Python', 4.0)
u1.add_grade(4, 'PHP', 4.1)
u1.add_grade(4, 'Java', 4.0)

# Получение списка студентов
print(u1.get_students())
print(u1.get_students('Python'))

# Закрытие соединения с базой данных
u1.conn.close()
