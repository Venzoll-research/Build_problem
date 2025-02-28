#include <pybind11/pybind11.h> //vs code подчёркивает эту строку

int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(example, m) {
    m.def("add", &add, "Складывает два числа");
}