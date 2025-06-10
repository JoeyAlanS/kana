def subset(lista):
    n = len(lista)
    achou = False

    #Aqui entra força bruta
for i in range(1, 2**n):
        subconjunto = []
  # Constrói o subconjunto com base nos bits ligados de i
        for j in range(n):
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
subset(numeros)
