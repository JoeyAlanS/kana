def knapsack_dp(capacidade, itens):
    n = len(itens)
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    # Construir tabela DP
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if itens[i-1]['peso'] <= w:
                dp[i][w] = max(itens[i-1]['preco'] + dp[i-1][w - itens[i-1]['peso']], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    # Rastrear quais itens foram selecionados
    w = capacidade
    mochila = []
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