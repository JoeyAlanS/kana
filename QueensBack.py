def mostrar_tabuleiro(tabuleiro, tamanho):
    for linha in range(tamanho):
        texto = ""
        for coluna in range(tamanho):
            if tabuleiro[linha][coluna] == 1:
                texto += "Q "  
            else:
                texto += ". "  
        print(texto)
    print("\n") 

def posicao_segura(tabuleiro, linha, coluna, tamanho): # linhas diagonais direita e esquerda
    for i in range(linha):
        if tabuleiro[i][coluna] == 1:
            return False 

    i, j = linha - 1, coluna - 1
    while i >= 0 and j >= 0:
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = linha - 1, coluna + 1
    while i >= 0 and j < tamanho:
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True  

def resolver_n_rainhas(tabuleiro, linha, tamanho):
    if linha == tamanho:
        print("Solução encontrada:")
        mostrar_tabuleiro(tabuleiro, tamanho)
        return True # encontrou solução

    for coluna in range(tamanho):
        if posicao_segura(tabuleiro, linha, coluna, tamanho):
            tabuleiro[linha][coluna] = 1 
            if resolver_n_rainhas(tabuleiro, linha + 1, tamanho):# linha que define backetracking
                return True  #encontrou solução
            
            tabuleiro[linha][coluna] = 0 # aqui ocorre o backtracking
            print(f"Backtracking: removendo rainha de ({linha}, {coluna})")
    
    return False  #nao encontrou solução

N = 8 

tabuleiro = [[0 for _ in range(N)] for _ in range(N)]


resolver_n_rainhas(tabuleiro, 0, N)
