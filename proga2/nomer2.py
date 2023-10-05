spisok = []
while True:
    a = input ('Введите число')
    if a == '':
        break
    else:
        spisok.append(int(a))
spisok.sort(Key = lambda x: int(str(x)[0]), reverse = True)
for i in range( 0 , len(spisok)):
    print(spisok[i], end = ' ')