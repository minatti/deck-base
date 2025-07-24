import os, json, random, string

# Função para obter o caminho da pasta do baralho
def caminho_baralho():
    PASTA_BASE = os.path.abspath(os.path.dirname(__file__))
    PASTA_BARALHO = os.path.join(PASTA_BASE, "data")

    if not os.path.exists(PASTA_BARALHO):
        os.makedirs(PASTA_BARALHO)
        print(f"Pasta '{PASTA_BARALHO}' criada.")
    PASTA_BARALHO = os.path.join(PASTA_BARALHO, "deck.json")

    return PASTA_BARALHO


# Função para gerar um GUID aleatório
def gerar_guid(tamanho=10):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+<>?/{}[]|"
    return ''.join(random.choices(caracteres, k=tamanho))


# Função para gerar questões de teste
def gerar_questoes_teste():
    questoes = [
        {
            "tipo": "multipla_escolha",
            "pergunta": "Qual das alternativas abaixo representa um tipo de dado imutável em Python?",
            "alternativas": {
                "A": "list",
                "B": "set",
                "C": "tuple",
                "D": "dict",
                "E": "bytearray"
            },
            "correta": "C",
            "explicacao": "A `tuple` é um tipo imutável em Python, ao contrário das listas e dicionários que são mutáveis.",
            "tags": ["conhecimento-especifico-python"]
        },
        {
            "tipo": "multipla_escolha",
            "pergunta": "Qual é o resultado da expressão 2 ** 3 em Python?",
            "alternativas": {
                "A": "5",
                "B": "6",
                "C": "7",
                "D": "8",
                "E": "9"
            },
            "correta": "D",
            "explicacao": "O operador `**` realiza exponenciação. 2 elevado a 3 é igual a 8.",
            "tags": ["conhecimento-especifico-python"]
        }
    ]
    
    notas = []
    for q in questoes:
        pergunta_formatada = q["pergunta"] + "\n" + "\n".join([
            f"{letra}) {texto}" for letra, texto in q["alternativas"].items()
        ])
        resposta_formatada = f"Resposta correta: {q['correta']}\n{q['explicacao']}"
        
        nota = {
            "__type__": "Note",
            "fields": [
                pergunta_formatada,
                resposta_formatada
            ],
            "guid": gerar_guid(),
            "note_model_uuid": "c22ea8b0-6815-11f0-b5a7-0ff2d2f8b4fb",
            "tags": q["tags"]
        }
        notas.append(nota)
    
    return notas

def main():
    print("Iniciando o backend do deck base...")
    caminho = caminho_baralho()
    
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados_baralho = json.load(arquivo)
                
    dados_baralho["notes"] = gerar_questoes_teste()


    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_baralho, arquivo, ensure_ascii=False, indent=4)

    print(f"Deck gerado com sucesso em: {caminho}")

if __name__ == "__main__":
    main()