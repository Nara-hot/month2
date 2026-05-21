import sqlite3


# Функция для создания базы данных и таблицы
def init_db():
    # Подключаемся к базе (если файла нет, он создастся автоматически)
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Создаем таблицу products
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS products
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       name
                       TEXT
                       NOT
                       NULL,
                       price
                       REAL
                       NOT
                       NULL,
                       quantity
                       INTEGER
                       NOT
                       NULL
                   )
                   ''')

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()


# 1️⃣ CREATE — добавление товара
def create_product(name, price, quantity):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO products (name, price, quantity)
                   VALUES (?, ?, ?)
                   ''', (name, price, quantity))

    conn.commit()
    print(f"Товар '{name}' успешно добавлен!")
    conn.close()


# 2️⃣ READ — получение всех данных
def read_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    print("\n--- Список всех товаров ---")
    if not products:
        print("База данных пуста.")
    for product in products:
        print(f"ID: {product[0]} | Название: {product[1]} | Цена: {product[2]} руб. | Количество: {product[3]} шт.")
    print("---------------------------\n")

    conn.close()



def update_product(product_id, new_price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('''
                   UPDATE products
                   SET price = ?
                   WHERE id = ?
                   ''', (new_price, product_id))

    conn.commit()
    print(f"Цена товара с ID {product_id} успешно обновлена до {new_price}!")
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE ID = ?', (product_id,))

    conn.commit()
    print(f"Товар с ID {product_id} успешно удален!")
    conn.close()

if __name__ == '__main__':
    init_db()

    print("Проверка CREATE:")
    create_product("Ноутбук", 45000.0, 5)
    create_product("Мышка", 1200.5, 15)
    create_product("Клавиатура", 2500.0, 8)

    read_products()

    print("Проверка UPDATE:")
    # Меняем цену мышки (у нее ID должен быть 2)
    update_product(2, 1499.9)
    read_products()

    print("Проверка DELETE:")
    # Удаляем клавиатуру (ID 3)
    delete_product(3)

    read_products()