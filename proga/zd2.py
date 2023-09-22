a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())
try:
    print((a * b - c) / (f - d))
except Exception as e:
    if str(e) == "division by zero":
        print("Делить на ноль нельзя")
    else:
        print("Какая то другая ошибка")