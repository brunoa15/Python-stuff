#mdc por algoritmo euclidiano

def mdc(a, b):
    if a<b:
        c = a
        a = b
        b = c
    
    r = a%b
    
    if r == 0:
        return b
    else:
        return mdc(b,r)

print(mdc(635,1400))