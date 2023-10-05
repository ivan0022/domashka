a = input()

c1 = a.count('(')
c2 = a.count(')')

if c1 == c2:
    print('всё хорошо')
elif c1 > c2:
    print(f"Не хватает {c1 - c2} закрывающей скобки!")
elif c1 < c2:
    print(f"Не хватает {c1 - c2} открывающей скобки!")