# Solução do problema do Cavalo (Knight's Tour) usando backtracking
# Tempo: O(8^(N^2)) - no pior caso, o cavalo pode visitar todas as casas do tabuleiro
# Espaço: O(N^2) - para armazenar o tabuleiro
import time
# Tamanho do tabuleiro
N = 6

# 8 direções do cavalo
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def movimento_valido(x, y, tabuleiro):
    # Verifica se a posição está dentro dos limites do tabuleiro e se ainda não foi visitada
    return 0 <= x < N and 0 <= y < N and tabuleiro[x][y] == -1 # todas as casas começam com -1 indicando que não foram visitadas

def resolver_knight_tour():
    #Cria o tabuleiro inicial, preenchido com -1 (não visitado).
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]
    # Começa na posição (0, 0)
    tabuleiro[0][0] = 0  

#retorno quando o tabuleiro estiver completo
    if backtrack(0, 0, 1, tabuleiro):
        print("Caminho completo.")
        imprimir_tabuleiro(tabuleiro)
    else:
        print("Não existe solução.")

def backtrack(x, y, move_count, tabuleiro):
    # Verifica se todas posições foram visitadas
    if move_count == N * N: 
        return True

    # Tenta os 8 movimentos do cavalo
    for i in range(8):
        proximo_x = x + dx[i]
        proximo_y = y + dy[i]

        if movimento_valido(proximo_x, proximo_y, tabuleiro):
            tabuleiro[proximo_x][proximo_y] = move_count
            #mostrar_tabuleiro(tabuleiro, move_count)
            #time.sleep(0.1)  # Controle de velocidade
#Essa linha faz a chamada recursiva para tentar continuar o caminho do cavalo a partir da nova posição.            
#É o coração do algoritmo de backtracking, pois tenta todas as possibilidades a partir de cada movimento válido.
            if backtrack(proximo_x, proximo_y, move_count + 1, tabuleiro):
                return True
            tabuleiro[proximo_x][proximo_y] = -1  # aqui ocorre o backtrack
    return False
#ordem das casas do tabuleiro que foram visitadas
def imprimir_tabuleiro(tabuleiro):
    print("\nTabuleiro final:")
    for linha in tabuleiro:
        for casa in linha:
            print(f"{casa:2}", end=" ")
        print()

def mostrar_tabuleiro(tabuleiro, passo):
    print(f"\nPasso: {passo}")
    for linha in tabuleiro:
        for casa in linha:
            if casa == -1:
                print("__", end=" ")
            else:
                print(f"{casa:02}", end=" ")
        print()

if __name__ == "__main__":
    resolver_knight_tour()
