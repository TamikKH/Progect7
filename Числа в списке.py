#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    s = 0
    min_a = 999999999999999999999999999999999
    list_a = list(map(int, input("Ведите строку чисел через пробел ").split()))
    for i in range(0, len(list_a)):
        if abs(list_a[i]) < min_a:
            min_a = abs(list_a[i])
    for i in range(1, len(list_a)):
        if list_a[i-1] < 0:
            s = s + abs(list_a[i])
    a = int(input("Введите границу а "))
    b = int(input("Введите границу в "))
    for i in range(0, len(list_a)):
        if a <= list_a[i] <= b:
            list_a.pop(i)
            list_a.append(0)
    print(f"Минимальный модуль списка равен {min_a}, Сумма модулей равна {s}, Новый список: {list_a}")