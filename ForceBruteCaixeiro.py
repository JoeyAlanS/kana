import itertools
import math

# Calcula a distância Euclidiana entre duas cidades
def distancia(cidade1, cidade2):
    return math.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

# Calcula a distância total de um caminho
def total_distancia(route):
    dist = 0
    for i in range(len(rota) - 1):
        dist += distancia(rota[i], rota[i + 1])
    dist += distancia(rota[-1], rota[0])  # Volta para a cidade de origem
    return dist

# Definindo as coordenadas das cidades
cities = [
    (0, 0), (1, 5), (2, 3), (5, 2), (6, 6),
    (8, 3), (7, 7), (3, 8), (9, 9), (4, 4)
]

melhor_rota = None
melhor_distancia = float('inf')

# FORÇA BRUTA: gera todas as permutações possíveis
for perm in itertools.permutations(cities):
    # --> Esta linha define que o problema é de FORÇA BRUTA por PERMUTAÇÃO
    dist = total_distancia(perm)
    if dist < melhor_distancia:
        melhor_distancia = dist
        melhor_rota = perm

# Exibe a melhor rota encontrada
print("Melhor rota encontrada:")
for i in range(len(melhor_rota)):
    print(f"Cidade {i + 1}: {melhor_rota[i]}")
print(f"Distância total: {best_distancia:.2f}")

# Mostrar cadeia de cidades e distância entre cada par
print("\nDetalhes da rota:")
for i in range(len(best_rota)):
    city_from = melhor_rota[i]
    city_to = melhor_rota[(i + 1) % len(melhor_rota)]  # Volta à origem
    d = distancia(city_from, city_to)
    print(f"De {city_from} para {city_to}: {d:.2f}")
