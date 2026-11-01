# Projeto Agenda de Contatos

Projeto de uma agenda de contatos em Python, executada no terminal.

- **Autor:** Alef
- **Versão:** 1.0
- **Data:** 01-11-2026

## Descrição

Aplicação de linha de comando (CLI) para gerenciar contatos. Cada contato possui
**nome**, **telefone**, **e-mail** e **endereço**, e os dados ficam armazenados em
memória durante a execução do programa (em um dicionário).

> Observação: os contatos **não são salvos em arquivo**. Ao encerrar o programa, os
> dados são perdidos.

## Funcionalidades

O menu principal oferece as seguintes opções:

1. **Adicionar contato** (`Add Contact`)
2. **Visualizar contato** (`View Contact`)
3. **Editar contato** (`Edit Contact`)
4. **Excluir contato** (`Delete Contact`)
5. **Listar todos os contatos** (`List All Contacts`)
6. **Sair** (`Exit`)

Regras de comportamento:

- O nome do contato é usado como chave única; nomes repetidos são recusados.
- Adicionar, visualizar, editar e excluir pedem o nome do contato.
- Entradas inválidas no menu (não numéricas ou fora do intervalo 1–6) exibem uma
  mensagem de erro e o menu é mostrado novamente.

## Estrutura do projeto

```
agenda_contatos/
├── agenda_contatos.py   # Ponto de entrada: loop principal e leitura do menu
├── menu.py              # Módulo com a classe ContactBook (regras da agenda)
└── README.md
```

- **`agenda_contatos.py`** — inicia o programa, exibe o menu e direciona a escolha
  do usuário para o método correspondente.
- **`menu.py`** — define a classe `ContactBook`, que guarda os contatos no
  atributo `contact_book` (um dicionário) e implementa os métodos de
  adicionar, visualizar, editar, excluir e listar contatos.

## Requisitos

- Python 3.x

Não há dependências externas — o projeto usa apenas a biblioteca padrão do Python.

## Como executar

1. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   # .venv\Scripts\activate       # Windows
   ```

2. Execute o programa a partir da pasta do projeto:

   ```bash
   cd agenda_contatos
   python3 agenda_contatos.py
   ```

3. Use o menu digitando o número da opção desejada (1 a 6).

## Exemplo de uso

```
Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
Enter your choice: 1
Enter contact name: Maria
Enter contact phone: 99999-0000
Enter contact email: maria@email.com
Enter contact address: Rua das Flores, 10
Contact added successfully!
```

## Possíveis melhorias futuras

- Persistir os contatos em arquivo (JSON/CSV) ou banco de dados (SQLite).
- Validar formato de telefone, e-mail e campos vazios.
- Buscar contatos por parte do nome.
- Permitir nomes com espaços (usando identificadores únicos).
