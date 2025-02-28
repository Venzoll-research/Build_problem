cmake_minimum_required(VERSION 3.14)
project(testBIND)

# Указываем путь к Python и pybind11
set(Python_ROOT_DIR "C:/Users/37111/AppData/Local/Programs/Python/Python313")
set(pybind11_DIR "${Python_ROOT_DIR}/Lib/site-packages/pybind11/share/cmake/pybind11")

# Поиск компонентов Python
find_package(Python REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

# Отладочные сообщения
message(STATUS "Python include dirs: ${Python_INCLUDE_DIRS}")
message(STATUS "Python libraries: ${Python_LIBRARIES}")

# Создание модуля
pybind11_add_module(example cpp/example.cpp)

# Настройка путей
target_include_directories(example PRIVATE
    ${Python_INCLUDE_DIRS}
    ${pybind11_INCLUDE_DIRS}
)

# Линковка
target_link_libraries(example PRIVATE
    pybind11::module
    Python::Python
)

# Переименование выходного файла (опционально)
set_target_properties(example PROPERTIES SUFFIX ".pyd")