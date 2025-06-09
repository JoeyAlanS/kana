import itertools
import math

def distancia(cidade1, cidade2):#Cálculo de Distância Euclidiana
    return math.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

# Função que calcula a distância total de uma rota (incluindo retorno à cidade inicial)
def total_distancia(rota):
    dist = 0
    for i in range(len(rota) - 1):
        dist += distancia(rota[i], rota[i + 1])
    dist += distancia(rota[-1], rota[0]) 
    return dist

cidades = [
    (0, 0), (1, 5), (2, 3), (5, 2), (6, 6),
    (8, 3), (7, 7), (3, 8), (9, 9), (4, 4)
]

melhor_rota = None               # Variável para armazenar a melhor rota encontrada
melhor_distancia = float('inf')   # Inicializa a melhor distância com infinito

for perm in itertools.permutations(cidades):
    dist = total_distancia(perm)
    if dist < melhor_distancia:
        melhor_distancia = dist
        melhor_rota = perm

print("Melhor rota encontrada:")
for i in range(len(melhor_rota)):
    print(f"Cidade {i + 1}: {melhor_rota[i]}")
print(f"Distância total: {melhor_distancia:.2f}")

print("\nDetalhes da rota:")
for i in range(len(melhor_rota)):
    cidade_from = melhor_rota[i]
    cidade_to = melhor_rota[(i + 1) % len(melhor_rota)] 
    d = distancia(cidade_from, cidade_to)
    print(f"De {cidade_from} para {cidade_to}: {d:.2f}")
