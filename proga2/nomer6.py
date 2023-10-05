a = input()
n = int(input()) - 1
ints = []
for c in a:
    try:
        b = int(c)
        ints.append(b)
    except:
        pass
print(f"{n+1}-ая цифра в строке {ints[n]}")