def operations(a, b):
    sum = a + b
    res = a - b
    mult = a * b
    try:
        div = a / b
    except ZeroDivisionError:
        div = "No se puede dividir por cero"

    return sum, res, mult, div

a = 1
b = 0

res = operations(a, b)
print("Suma:", res[0])
print("Resta:", res[1])
print("Multiplicación:", res[2])
print("División:", res[3])
