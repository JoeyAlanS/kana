def print_board(board, N):
    for row in range(N):
        line = ""
        for col in range(N):
            if board[row][col] == 1:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

# Verifica se é seguro colocar uma rainha na posição (row, col)
def safe(board, row, col, N):
    # Verifica coluna acima
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Verifica diagonal superior esquerda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Verifica diagonal superior direita
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True

# Função principal de backtracking
def solve_n_queens(board, row, N):
    if row >= N:
        print("Solução encontrada:")
        print_board(board, N)
        return True  # Encontrou uma solução

    for col in range(N):
        # TENTATIVA de colocar a rainha
        if safe(board, row, col, N):
            board[row][col] = 1  # Coloca a rainha
            # --> Esta linha define que o problema é de BACKTRACKING
            if solve_n_queens(board, row + 1, N):
                return True  # Encontrou uma solução
            # BACKTRACKING: remove a rainha
            board[row][col] = 0  # <-- Aqui ocorre o BACKTRACKING
            print(f"Backtracking: removendo rainha de ({row}, {col})")
    return False  # Não encontrou solução nesta configuração

# Execução
N = 8  # Você pode alterar para qualquer valor de N >= 4
board = [[0 for _ in range(N)] for _ in range(N)]
solve_n_queens(board, 0, N)
