import os

# Função para obter o caminho da pasta do baralho
def caminho_baralho():
    PASTA_BASE = os.path.abspath(os.path.dirname(__file__))
    PASTA_BARALHO = os.path.join(PASTA_BASE, "data")

    if not os.path.exists(PASTA_BARALHO):
        os.makedirs(PASTA_BARALHO)

    PASTA_BARALHO = os.path.join(PASTA_BARALHO, "deck.json")

    return PASTA_BARALHO

def main():
    print("Iniciando o backend do deck base...")
    print("Caminho do baralho:", caminho_baralho())


if __name__ == "__main__":
    main()