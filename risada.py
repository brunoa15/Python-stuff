risada = str(input())
for i in range(0,len(risada)):
    
    if risada[i] in ['a', 'e', 'i', 'o', 'u']:

        try:
            vogais += risada[i]
        except NameError:
            vogais = risada[i]

try:
    if vogais == vogais[::-1]:
        print('S')
    else:
        print('N')
except NameError:
    print('N')
