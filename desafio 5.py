# Guloso mchila ilimitada
# Tempo O(n log n + m) - devido à ordenação dos itens
# Espaço O(n + m) - para armazenar os itens ordenados m = n total de itens add
def mochila_gulosa_ilimitada(capacidade, objetos):
    # Passo 1: Calcular razão valor/peso para cada objeto
    itens = []
    for obj in objetos:
        nome, peso, preco = obj
        razao = preco / peso
        itens.append((razao, nome, peso, preco))
    
    # Passo 2: Ordenar por melhor custo-benefício
    itens.sort(key=lambda x: x[0], reverse=True)
    
    peso_atual = 0
    valor_total = 0
    escolhas = [] # Lista para armazenar os itens escolhidosW
    
    print("\nIniciando preenchimento da mochila:")
    print("-" * 50)
    
    # Passo 3: Selecionar itens enquanto houver espaço
    for item in itens:
        razao, nome, peso, preco = item
        
        # Verificar se o item cabe pelo menos uma vez
        if peso <= capacidade - peso_atual:
            # Calcular quantas unidades cabem
            qtd = (capacidade - peso_atual) // peso
            if qtd > 0:
                # Adicionar todas as unidades de uma vez
                for _ in range(int(qtd)):
                    escolhas.append(nome)
                    peso_atual += peso
                    valor_total += preco
                    print(f"Adicionado: {nome} (peso: {peso}kg, valor: R${preco})")
                    print(f"Peso atual: {peso_atual:.1f}kg | Valor total: R${valor_total}")
                    print("-" * 50)
    
    # Resultado final
    print("\nRESUMO FINAL:")
    print(f"Capacidade utilizada: {peso_atual:.1f}kg de {capacidade}kg")
    print(f"Valor total na mochila: R${valor_total}")
    print("\nItens na mochila:")
    for item in set(escolhas):
        print(f"- {item}: {escolhas.count(item)} unidade(s)")
    
    return escolhas

# Dados dos objetos
objetos = [
    ("Notebook", 2.5, 3000),    # Alto valor, peso médio
    ("Livro", 1.0, 50),          # Baixo valor/peso
    ("Celular", 0.3, 2000),      # Melhor valor/peso
    ("Garrafa", 0.5, 30),        # Baixo valor
    ("Fone de ouvido", 0.2, 150) # Bom valor/peso
]

# Execução do algoritmo
capacidade_mochila = 5  # 5kg
print(f"Capacidade da mochila: {capacidade_mochila}kg")
print("\nObjetos disponíveis:")
for obj in objetos:
    print(f"- {obj[0]}: peso={obj[1]}kg, preço=R${obj[2]}")

mochila_gulosa_ilimitada(capacidade_mochila, objetos)



