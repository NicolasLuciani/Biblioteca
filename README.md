# Sistema de Biblioteca em Python

## Introdução
<h4>Este projeto implementa um sistema de gerenciamento de biblioteca utilizando Python.  
O sistema permite ao usuário cadastrar livros, emprestar e devolver livros, listar todos os livros ou por categoria, atualizar informações e excluir livros.  Ele é construído com orientação a objetos, usando classes para representar livros e a biblioteca, tornando o código organizado, reutilizável e fácil de manter.

O sistema é interativo, apresentando um menu de opções no terminal, permitindo que o usuário realize operações de forma intuitiva.</h4>

---

## Funcionalidades
- Cadastro de livros  
- Empréstimo de livros  
- Devolução de livros  
- Listagem de livros (todos ou por categoria)  
- Atualização de informações de livros  
- Exclusão de livros

## A estrutura dos códigos:
- app.py
- classes.py
- menu.py

## Sistema de Biblioteca

## Classe Livro
**Atributos:**
- `titulo`
- `autor`
- `categoria`
- `disponivel` (boolean)

**Métodos:**
- `__init__(self, titulo, autor, categoria)` → inicializa o livro
- `emprestar(self)` → marca o livro como indisponível
- `devolver(self)` → marca o livro como disponível

---

## Classe Biblioteca
**Atributos:**
- `livros` (lista de objetos `Livro`)

**Métodos:**
- `__init__(self)` → inicializa a lista de livros
- `cadastrar(self, livro)` → adiciona um livro à lista
- `atualizar(self, titulo_antigo, novo_livro)` → atualiza dados de um livro
- `listar(self, categoria=None)` → lista todos os livros ou por categoria
- `excluir(self, titulo)` → remove um livro da lista
