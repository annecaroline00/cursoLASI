
a = int(input("Digite o valor de N: "))

def function(N):
    A = 0
    for x in range (0, N):
        A += (N-x)/(x+1)
    return A


print(function(a))


