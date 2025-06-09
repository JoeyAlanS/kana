def subset_sum_zero_verbose(nums):
    result = []

    def backtrack(start, path, current_sum):
        print(f"Explorando caminho: {path} | Soma atual: {current_sum}")
        
        # verifica se a soma do subconjunto é igual a zero
        if current_sum == 0 and path:
            print(f">>> Subconjunto encontrado: {path}")
            result.append(path[:])
        for i in range(start, len(nums)):
            print(f"Incluindo {nums[i]} no caminho")
            path.append(nums[i])

            # aqui ocorre o backtracking
            backtrack(i + 1, path, current_sum + nums[i])
            print(f"Removendo {nums[i]} do caminho")
            path.pop()

    backtrack(0, [], 0)
    return result

# Exemplo de uso
nums = [-7, -3, -2, 5, 8]
print("Iniciando busca de subconjuntos com soma 0...")
subconjuntos = subset_sum_zero_verbose(nums)
print("\nTodos os subconjuntos cuja soma é 0:")
for s in subconjuntos:
    print(s)
