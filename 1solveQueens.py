# Backtraking
# Tempo O(n!)
# Espaço O(n^2)
def solve_n_queens(n):
    def is_safe(tabuleiro, linha, col):
#Verifica se já existe uma rainha na mesma coluna (tabuleiro[r] == col).
#Verifica se já existe uma rainha na mesma diagonal 
        for r in range(linha):
            if tabuleiro[r] == col or abs(tabuleiro[r] - col) == abs(r - linha):
                return False
        return True
    def place_queen(tabuleiro, linha):
        if linha == n:
            print("Solução encontrada:")
            print_tabuleiro(tabuleiro)
            return True  # Parar ao encontrar a primeira solução
        for col in range(n):
            if is_safe(tabuleiro, linha, col):
                tabuleiro[linha] = col
                if place_queen(tabuleiro, linha + 1):
                    return True
                # BACKTRACK
                print(f"Backtracking: removendo rainha na linha {linha}, coluna {col}")
                tabuleiro[linha] = -1
        return False
    def print_tabuleiro(tabuleiro):
        for linha in range(n):
            line = ""
            for col in range(n):
                if tabuleiro[linha] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()
    tabuleiro = [-1] * n
    place_queen(tabuleiro, 0)
solve_n_queens(8)
