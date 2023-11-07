import sys
if __name__ == '__main__':
    p=1
    k=0
    print("Введите 10 чисел")
    A=[]
    for i in range(1, 11):
        a = int(input())
        A.append(a)
    for c in range(0, 10):
        if A[c] > 0 and A[c] % 3 == 0:
            p=p*A[c]
            k=k+1
    print("Произведение равно", p, "количество равно", k)