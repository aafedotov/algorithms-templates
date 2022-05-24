def PisanoPeriod(m):

    previous = 0
    current = 1
    fib_modulos = []
    fib_modulos.append(previous)
    fib_modulos.append(current)
    i = 1

    while True:

        temp = previous
        previous = current
        current = (temp + current) % m
        fib_modulos.append(current)
        i += 1
        if fib_modulos[i] == 1 and fib_modulos[i - 1] == 0:
            fib_modulos.pop()
            fib_modulos.pop()
            return fib_modulos

if __name__ == '__main__':

    m = int(input())
    k = 10 ** m
    pis = PisanoPeriod(k)
    print(pis)
    n = int(input())
    p = n % k
    print(p)
    print(pis[p])
