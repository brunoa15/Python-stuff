C = int(input())

for i in range(0,C):
    B,E = input().split(' ')

    for j in range(int(B)+1,int(E)+1):
        B += str(j)

    for j in range(len(B)-1,-1,-1):
        B += B[j]

    print(B)