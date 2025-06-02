import sys

N, M = map(int, input().split())

Pokemons = [sys.stdin.readline().strip() for _ in range(N)]

for i in range(M):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(Pokemons[int(question)-1])
    else:
        print(Pokemons.index(question)+1)