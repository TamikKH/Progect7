#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    proizvedenie = 1
    kolichestvo = 0
    print("Введите 10 чисел")
    list_a = list(map(int, input().split()))
    for c in range(0, 10):
        if list_a[c] > 0 and list_a[c] % 3 == 0:
            proizvedenie = proizvedenie * list_a[c]
            kolichestvo = kolichestvo + 1
    print(f"Произведение равно {proizvedenie}, количество равно {kolichestvo}")