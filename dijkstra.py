#essa desgraça funciona mas o URI não aceita

lista = []
while True:
    
    try:
        procurado = input()
        if len(lista) == 0:
            lista += [procurado]

        for i in range(0,len(lista)):
            if len(lista) == 0:
                lista+= [procurado]
            elif lista[i] == procurado:
                break
            elif i == len(lista)-1 and lista[len(lista)-1] != procurado:
                lista += [procurado]
    except EOFError:
        break

print(len(lista))
