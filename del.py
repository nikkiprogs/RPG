import sqlite3
conn = sqlite3.connect('player_list.db')
cursor = conn.cursor()

# Пример запроса (вывести все таблицы)
cursor.execute("DELETE FROM users")

# Подтверждение изменений
conn.commit()

# Закрыть соединение
conn.close()