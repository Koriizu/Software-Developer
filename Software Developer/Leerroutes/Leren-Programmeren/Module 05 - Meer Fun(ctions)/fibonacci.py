def Fibonaccibreken(getal):
    fibonacci = [0,1]
    for index in range(2, getal):
        fibonacci.append(fibonacci[index-1] + fibonacci[index-2])
    return fibonacci


def guldensnede(fibonacci):
    Laatste = fibonacci[-1]
    Een_A_Laatste = fibonacci[-2]
    return Laatste / Een_A_Laatste

print(Fibonaccibreken(10))
print(guldensnede(Fibonaccibreken(10)))
print(guldensnede(Fibonaccibreken(30)))
print(guldensnede(Fibonaccibreken(42)))
print(guldensnede(Fibonaccibreken(10000)))
print(guldensnede(Fibonaccibreken(20000)))