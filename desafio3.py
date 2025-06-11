# desafio3.py > mochila_gulosa.py
# Tempo: O(n log n) - devido à ordenação dos objetos
# Espaço: O(n) - para armazenar os objetos e suas propriedades
class Objeto:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor
        self.ratio = valor / peso if peso != 0 else 0

def mochila_gulosa(capacidade, objetos):
    # Ordenar os objetos pela melhor razão valor/peso (decrescente)
    objetos_ordenados = sorted(objetos, key=lambda obj: obj.ratio, reverse=True)

    peso_total = 0
    valor_total = 0
    mochila = []

    print(f"\nCapacidade da mochila: {capacidade} kg\n")
    print("Escolhas realizadas:")

    for obj in objetos_ordenados:
        if peso_total + obj.peso <= capacidade:
            mochila.append(obj)
            peso_total += obj.peso
            valor_total += obj.valor
            print(f"V Escolhido: {obj.nome} (Peso: {obj.peso}, Valor: R${obj.valor})")
        else:
            print(f"X Ignorado: {obj.nome} (Peso: {obj.peso}, Valor: R${obj.valor}) - Excederia a capacidade")

    print(f"\nPeso total: {peso_total} kg")
    print(f"Valor total: R${valor_total:.2f}")
    print("\nObjetos na mochila:", [obj.nome for obj in mochila])

# Exemplo de uso:
if __name__ == "__main__":
    objetos = [
        Objeto("Notebook", 3, 3000),
        Objeto("Livro", 1.5, 100),
        Objeto("Celular", 0.5, 1500),
        Objeto("Garrafa", 2, 60),
        Objeto("Fone de ouvido", 0.3, 250)
    ]
    
    capacidade_mochila = 5  # em quilos
    mochila_gulosa(capacidade_mochila, objetos)