import sys
import os

# Добавляем папку build в путь
build_dir = os.path.join(os.path.dirname(__file__), "build")
sys.path.append(build_dir)

# Импорт библиотеки
import example

# Тестирование
print(example.add(10, 20))  # Должно вывести 30