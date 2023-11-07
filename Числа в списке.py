import sys
if __name__ == '__main__':
    B = int(input("Введите размер списка "))
    A = []
    s = 0
    mi = 100000000000
    for i in range(1, B+1):
        d = int(input("Введите элемент списка "))
        A.append(d)
    for h in range(0, B-1):
        if abs(A[h]) < mi:
            mi=A[h]
    for g in range(1, B-1):
        if A[g-1] < 0:
            s = s + abs(A[g])
    a = int(input("Введите границу а "))
    b = int(input("Введите границу в "))
    for l in range(0, B-1):
        if A[l] >= a and A[l] <= b:
            A.pop(l)
            A.append(0)
    print("Минимальный модуль списка равен", mi,"Сумма модулей равна", s, "Новый список:", A)