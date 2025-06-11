#Backtracking 
#Tempo O(2^n)
#Esoaco O(n x 2^n)
def subset_sum_zero_verbose(nums):
    result = []
#path e o subconjunto atual comeca vazio
#se considerado igual a zero armazena em result
    def backtrack(start, path, current_sum):
        print(f"Explorando caminho: {path} | Soma atual: {current_sum}")
        
        # verifica se a soma do subconjunto é igual a zero
        if current_sum == 0 and path:
            print(f">>> Subconjunto encontrado: {path}")
            result.append(path[:])
        for i in range(start, len(nums)):
            #percorre o vetor a partir do indice start
            print(f"Incluindo {nums[i]} no caminho")
            #adiciona o item atual ao caminho
            path.append(nums[i])

            # aqui ocorre o backtracking
            #busca sempre o proximo item do vetor e adiciona a soma atual do subconjunto
            backtrack(i + 1, path, current_sum + nums[i])
            print(f"Removendo {nums[i]} do caminho")
            path.pop()
            #sempre remove o ultimo item do caminho
    backtrack(0, [], 0)
    #start sempre inicia com 0 sendo ele o indice da lista nums
    return result

# Exemplo de uso
nums = [-7, -3, -2, 5, 8]
print("Iniciando busca de subconjuntos com soma 0...")
subconjuntos = subset_sum_zero_verbose(nums)
print("\nTodos os subconjuntos cuja soma é 0:")
#exibe os subconjuntos encontrados
for s in subconjuntos:
    print(s)
