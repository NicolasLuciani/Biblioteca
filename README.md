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


<h2> Vamos ao código</h2>

class Livro:
    def __init__(self, titulo, autor, ano, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__categoria = categoria
        self.__disponibilidade = True

<h3>Adicionamos titulos, autor, ano e categoria aos tópicos disponiveis do livro
Onde está disponibilidade = True, diz que o livro está disponível</h3>

<h3>Emprestar</h3>

    def emprestar(self):
        if self.__disponibilidade == True:
            self.__disponibilidade = False
            print(f"Você emprestou '{self.__titulo}'")
        else:
            print(f"'{self.__titulo}' já está emprestado!")

<h3>Aqui diz que a disponibilidade esta 'True', ou seja, disponível e agora você vai pegar o livro, então, agora ele está 'False'</h3>

    def devolver(self):
        if self.__disponibilidade == False:
            self.__disponibilidade = True
            print(f"Você devolveu este livro '{self.__titulo}'")
        else:
            print(f"'{self.__titulo}' já está disponível!")
            
<h3>Aqui diz que a disponibilidade esta 'False', ou seja, Você vai devolver, então, ele volta a ser 'True'</h3>

    # ---------------- get ------------------------------

<h3>Utilizamos o comando 'get', para pegar os valores</h3>

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAno(self):
        return self.__ano

    def getCategoria(self):
        return self.__categoria

    def getDisponibilidade(self):
        return self.__disponibilidade

    # ---------------- set -------------------------

<h3>Utilizamos o comando 'set', para renovar os valores</h3>
    
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setAno(self, ano):
        self.__ano = ano

    def setCategoria(self, categoria):
        self.__categoria = categoria

    def setDisponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade


