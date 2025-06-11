# Brute Force para encontrar subconjuntos que somam zero
# Tempo: O(2^n)
# Espaço: O(n x 2^n) - para armazenar os subconjuntos
def subset(lista):
    #calcula o tamanho da lista qtd de elementos
    n = len(lista)
    achou = False

    # Aqui entra força bruta
    for i in range(1, 2**n):#gera todos os subconjuntos se n = 5 iual a 32 - 1 = 15 
        subconjunto = []
        # Constrói o subconjunto com base nos bits ligados de i
        for j in range(n):
            #operador de bits >> para dieireta e & para verificar se o bit está ligado
            if (i >> j) & 1:
                subconjunto.append(lista[j])
        # Verifica se soma do subconjunto é zero
        if sum(subconjunto) == 0:
            print(f"subconjunto que soma zero: {subconjunto}")
            achou = True
    if not achou:
        print("nenhum subconjunto soma zero.")

# input
entrada = input("")
numeros = list(map(int, entrada.split()))
print(numeros)
subset(numeros)
