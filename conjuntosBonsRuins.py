while True:
    N = int(input())

    if N > 0: 
        conjunto = []
        resposta = 'Conjunto Bom'
        
        for j in range(0,N):
            palavra = str(input())    

            for word in conjunto:
                if len(palavra) >= len(word):
                    for i in range(0,len(word)):
                        if palavra[i] != word[i]:
                            break
                        elif palavra[i] == word[i] and i == len(word)-1:
                            resposta = 'Conjunto Ruim'
                            break
                else:
                    for i in range(0,len(palavra)):
                        if palavra[i] != word[i]:
                            break
                        elif palavra[i] == word[i] and i == len(palavra)-1:
                            resposta = 'Conjunto Ruim'
                            break

                if resposta == 'Conjunto Ruim':
                    break

            #tambem funciona desse jeito conjunto += [palavra]
            conjunto.append(palavra)

        print(resposta)

    else:
        break