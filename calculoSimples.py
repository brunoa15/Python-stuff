a,b,c = input().split(" ")
x,y,z = input().split(" ")

precoA = int(b) * float(c)
precoB = int(y) * float(z)

total = precoA + precoB
print('VALOR A PAGAR: R$ %.2f' % total)