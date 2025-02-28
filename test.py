import sys
import os

# Путь к папке build
build_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "build"))
sys.path.insert(0, build_dir)

# Проверка наличия example.pyd
print("Содержимое build:")
for file in os.listdir(build_dir):
    print(f"  - {file}")

# Импорт модуля
try:
    import example
    print("Успех! Результат:", example.add(10, 20))
except Exception as e:
    print("Ошибка:", e)