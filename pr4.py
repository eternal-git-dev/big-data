def start():
    result = []
    n = int(input('Введите число:'))
    for i in range(n):
        k = i
        while i != 0:
            result.append(k)
            i = i - 1
    print(*result[:7])

if __name__ == '__main__':
    start()