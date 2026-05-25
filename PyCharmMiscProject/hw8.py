import sqlite3

# 1. Подключаемся к базе данных (файл netflix.db )
conn = sqlite3.connect('netflix.db')
cursor = conn.cursor()

# СОЗДАНИЕ ТАБЛИЦ И НАПОЛНЕНИЕ ДАННЫМИ

# Включаем поддержку внешних ключей (FOREIGN KEY) в SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Создаем таблицу пользователей
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

# Создаем таблицу фильмов
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT
)
''')

# Создаем связующую таблицу отзывов
cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER CHECK(rating >= 1 AND rating <= 10),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
)
''')

# Очищаем таблицы перед заполнением (чтобы данные не дублировались при повторном запуске)
cursor.execute("DELETE FROM reviews")
cursor.execute("DELETE FROM movies")
cursor.execute("DELETE FROM users")

# Добавляем 5 пользователей
users_data = [('Арзыбек',), ('Нара',), ('закир',), ('айжамал',), ('Даниял',)]
cursor.executemany("INSERT INTO users (name) VALUES (?)", users_data)

# Добавляем 5 фильмов (обратите внимание, 5-й фильм оставляем без отзывов для Части 2)
movies_data = [
    ('Интерстеллар', 'Научная фантастика'),
    ('Начало', 'Триллер'),
    ('Зеленая миля', 'Драма'),
    ('Шрек', 'Мультфильм'),
    ('Аватар 3', 'Фантастика')  # Этот фильм останется без отзывов
]
cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", movies_data)

# Добавляем 11 отзывов (указываем id пользователей от 1 до 5 и id фильмов от 1 до 4)
reviews_data = [
    (1, 1, 10), (1, 2, 8),   # Арзыбек оценил Интерстеллар и Начало
    (2, 1, 9),  (2, 3, 10),  # Нара оценила Интерстеллар и Зеленую милю
    (3, 2, 7),  (3, 4, 8),   # закир оценил Начало и Шрек потому что он шрек
    (4, 3, 9),  (4, 4, 10),  # Айжамал оценила Зеленую милю и Шрек
    (5, 1, 8),  (5, 2, 9),  (5, 4, 7) # Даниял оценил три фильма
]
cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", reviews_data)

# Сохраняем изменения в базе данных
conn.commit()
print("=== База данных создана и заполнена тестовыми данными ===\n")


# ЗАПРОСЫ С JOIN

print("1. Имя пользователя + фильм + оценка (INNER JOIN):")
cursor.execute('''
    SELECT u.name, m.title, r.rating
    FROM reviews r
    JOIN users u ON r.user_id = u.id
    JOIN movies m ON r.movie_id = m.id
''')
for row in cursor.fetchall():
    print(f"Пользователь: {row[0]} | Фильм: '{row[1]}' | Оценка: {row[2]}")

print("\n2. ВСЕ фильмы, даже без отзывов (LEFT JOIN):")
cursor.execute('''
    SELECT m.title, r.rating
    FROM movies m
    LEFT JOIN reviews r ON m.id = r.movie_id
''')
for row in cursor.fetchall():
    rating_val = row[1] if row[1] is not None else "Нет оценок"
    print(f"Фильм: '{row[0]}' | Оценка: {rating_val}")


# АГРЕГАЦИИ

print("\n📊 3. Статистика по оценкам (Агрегации):")
cursor.execute('''
    SELECT AVG(rating), MAX(rating), MIN(rating)
    FROM reviews
''')
stats = cursor.fetchone()
print(f"Средняя оценка всех фильмов: {stats[0]:.2f}")
print(f"Максимальная оценка: {stats[1]}")
print(f"Минимальная оценка: {stats[2]}")

# Закрываем соединение с базой данных
conn.close()