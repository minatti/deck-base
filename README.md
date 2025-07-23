# 🃏 Projeto Anki - Deck Base Personalizado com CrowdAnki

Este projeto tem como objetivo criar uma estrutura base de baralho (deck) personalizada para o Anki, utilizando o plugin **CrowdAnki**. Ele serve como ponto de partida para criação, organização e versionamento de decks de estudos via Git, especialmente útil para quem deseja automatizar ou padronizar a geração de cartões para concursos, ensino superior e treinamentos profissionais

---

## 📁 Estrutura do Projeto

deck-base/
├── deck.json # Arquivo principal do deck no padrão CrowdAnki
└── README.md # Documentação do projeto


---

## 📌 Tecnologias e Ferramentas

- **Anki** (versão 2.1.x ou superior)
- **CrowdAnki** (plugin para importar/exportar decks via JSON)
- **VS Code** (para edição dos arquivos JSON)
- **Git** (para versionamento)
- **Linux** (ambiente utilizado no desenvolvimento)
- **Python** (para criar o script de automação do processo)
---

## 🛠️ Como usar

1. **Instale o plugin CrowdAnki** no Anki:
   - Vá em "Tools" > "Add-ons" > "Get Add-ons..."
   - Cole o código do CrowdAnki: `1788670778`
   - Reinicie o Anki.

2. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/deck-base.git
   cd deck-base
