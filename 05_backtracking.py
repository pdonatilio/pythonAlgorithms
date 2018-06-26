# Backtracking Technique in Python


def backtrack(S, vet, K, N):
    if K == N:
        print('{', end=' ')
        for i in range(N):
            if vet[i] == True:
                print('%d' % S[i], end=' ')
        print('}')  # show the partial candidates in a sub array
    else:
        vet[K] = True
        backtrack(S, vet, K + 1, N)
        vet[K] = False
        backtrack(S, vet, K + 1, N)

S = [1, 2, 3]

size_S = len(S)

vet = [False for i in range(size_S)]

backtrack(S, vet, 0, size_S)