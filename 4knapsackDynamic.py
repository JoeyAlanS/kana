# Algoritmo de mochila (Knapsack) usando programação dinâmica busca maior valor total sem repetir
# Tempo: O(n * capacidade)
## Espaço: O(n * capacidade) - para armazenar a tabela de resultados

def knapsack_dp(capacidade, itens):
    n = len(itens) #percorre a lista de itens e ver qtd
    #faz uma matriz/tabela para armazenar os resultados
    #esta todas as combinações possíveis de itens para cada capacidade, garantindo que o valor total seja o maior possível.
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    #contrucao da matriz 
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            #verifica se o peso do item atual é menor ou igual à capacidade atual
            #se for menor ou igual, calcula o maximo entre o item atual + valor da mochila sem o item atual
            #se for maior, mantém o valor da mochila sem o item atual
            if itens[i-1]['peso'] <= w:
                #No seu código, a matriz dp guarda o melhor valor possível para cada combinação de itens e capacidades, preenchendo a tabela de forma incremental. Isso torna o algoritmo muito mais eficiente do que tentar todas as combinações possíveis (força bruta).
                dp[i][w] = max(itens[i-1]['preco'] + dp[i-1][w - itens[i-1]['peso']], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    # Rastrear quais itens foram selecionados
    w = capacidade
    mochila = []
    # percorre a tabela dp de baixo para cima
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            mochila.append(itens[i-1])
            print(f"Item '{itens[i-1]['nome']}' escolhido (DP).) Peso: {itens[i-1]['peso']} kg")
            print(f"Preço: R$ {itens[i-1]['preco']}")
            w -= itens[i-1]['peso']

    valor_total = dp[n][capacidade]
    print(f"\nValor total na mochila (DP): R$ {valor_total}")
    return mochila
if __name__ == "__main__":
    itens = [
        {"nome": "Notebook", "peso": 3, "preco": 2000},
        {"nome": "Livro", "peso": 1, "preco": 100},
        {"nome": "Garrafa", "peso": 2, "preco": 150},
        {"nome": "Fone", "peso": 1, "preco": 250}
    ]
    capacidade = 4

    print("=== Melhor escolha de itens ===")
    knapsack_dp(capacidade, itens)