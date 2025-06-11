pendrive = 99  # capacidade em MB

# Lista de PDFs: (nome, páginas, tamanho)
pdfs = [
    ("PDF_A", 500, 50),  # 10
    ("PDF_B", 400, 30),  # 13,333
    ("PDF_C", 300, 10),  # 30
    ("PDF_D", 200, 60),  # 3,33
    ("PDF_E", 100, 25)   # 4
]

# Calcula as páginas por MB e ordena
pdfs.sort(key=lambda x: x[1] / x[2], reverse=True)

capacidade = 0
print("Arquivos escolhidos:")
for nome, paginas, tamanho in pdfs:
    if capacidade + tamanho <= pendrive:
        print(nome)
        capacidade += tamanho
