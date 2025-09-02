# 📚 Sistema de Biblioteca em Python

## Introdução
<h4>Este projeto implementa um sistema de gerenciamento de biblioteca utilizando Python.  
O sistema permite ao usuário cadastrar livros, emprestar e devolver livros, listar todos os livros ou por categoria, atualizar informações e excluir livros.  Ele é construído com orientação a objetos, usando classes para representar livros e a biblioteca, tornando o código organizado, reutilizável e fácil de manter.

O sistema é interativo, apresentando um menu de opções no terminal, permitindo que o usuário realize operações de forma intuitiva.</h4>

---

## ⚙️ Funcionalidades
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

```python
import time
import os
class Livro:
    def __init__(self, titulo, autor, ano, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__categoria = categoria
        self.__disponibilidade = True

    def emprestar(self):
        if self.__disponibilidade == True:
            self.__disponibilidade = False
            print(f"Você emprestou '{self.__titulo}'")
            print()
            os.system("pause")
        else:
            print(f"'{self.__titulo}' já está emprestado!")
            print()
            os.system("pause")

    def devolver(self):
        if self.__disponibilidade == False:
            self.__disponibilidade = True
            print(f"Você devolveu este livro '{self.__titulo}'")
            print()
            os.system("pause")
        else:
            print(f"'{self.__titulo}' já está disponível!")
            print()
            os.system("pause")

    # ---------------- get ------------------------------
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


class Biblioteca:
    def __init__(self):
        self.__livros = [
    Livro("1984", "George Orwell", 1949, "Distopia"),
    Livro("O Senhor dos Anéis", "Tolkien", 1954, "Fantasia"),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Fantasia"),
    Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Clássico"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil"),
    Livro("Moby Dick", "Herman Melville", 1851, "Aventura"),
    Livro("Orgulho e Preconceito", "Jane Austen", 1813, "Romance"),
    Livro("O Hobbit", "Tolkien", 1937, "Fantasia"),
    Livro("O Código Da Vinci", "Dan Brown", 2003, "Suspense"),
    Livro("A Revolução dos Bichos", "George Orwell", 1945, "Satírico"),
    Livro("O Alquimista", "Paulo Coelho", 1988, "Ficção"),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Realismo Mágico"),
    Livro("O Morro dos Ventos Uivantes", "Emily Brontë", 1847, "Romance"),
    Livro("O Grande Gatsby", "F. Scott Fitzgerald", 1925, "Romance"),
    Livro("O Sol é Para Todos", "Harper Lee", 1960, "Romance"),
    Livro("A Menina que Roubava Livros", "Markus Zusak", 2005, "Ficção"),
    Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", 1979, "Ficção Científica"),
    Livro("Alice no País das Maravilhas", "Lewis Carroll", 1865, "Infantil"),
    Livro("Frankenstein", "Mary Shelley", 1818, "Terror"),
    Livro("Drácula", "Bram Stoker", 1897, "Terror"),
    Livro("O Perfume", "Patrick Süskind", 1985, "Suspense"),
    Livro("A Cabana", "William P. Young", 2007, "Ficção"),
    Livro("O Diário de Anne Frank", "Anne Frank", 1947, "Biografia"),
    Livro("Jogos Vorazes", "Suzanne Collins", 2008, "Distopia"),
    Livro("Crepúsculo", "Stephenie Meyer", 2005, "Romance")
]
    # get
    def getLivros(self):
        return self.__livros
    
    # set
    def setLivros(self, livros):
        self.__livros = livros
    
    # ---------------------------------metodos-------------------------------
    def cadastrar(self):
        os.system("cls")
        print("Você está na tela de cadastro de livro.\n")
        print("---------------------------------------------------------\n")
        qtd_livros = int(input("Quantos livros deseja cadastrar?\n-> "))
        for i in range(qtd_livros):
            titulo = input(f"DIGITE O NOME DO {i+1}º LIVRO: ")    
            autor = input(f"DIGITE O AUTOR(A) DO {i+1}º LIVRO: ")
            ano = int(input(f"DIGITE O ANO DO {i+1}º LIVRO: "))
            categoria = input(f"DIGITE A CATEGORIA DO {i+1}º LIVRO: ")
                        
            while True:
                disponibilidade = input("DIGITE s/n PARA A DISPONIBILIDADE DO LIVRO: ").lower()
                if disponibilidade == 's':
                    t_ou_f = True
                    break
                elif disponibilidade == 'n':
                    t_ou_f = False
                    break
                else:
                    print("DIGITE SOMENTE s OU n")
            livro = Livro(titulo, autor, ano, categoria)
            livro.setDisponibilidade(t_ou_f)
            self.__livros.append(livro)
            print("---------------------------------------------------------\n")
            
        print("LIVROS CADASTRADOS COM SUCESSO")
        print()
        os.system("pause")
    
    # --------------------------------------------------------------------------------
    def qual_listar(self):
        while True:
            print("\nVocê está na tela de listar.\n")
            print("---------------------------------------------------------\n")
            print("ESCOLHA UMA OPÇÃO: ")
            qual = int(input("1- LISTAR NORMALMENTE\n2- LISTAR POR CATEGORIA\n3- LISTAR POR AUTOR\n4- LISTAR POR EMPRESTADOS\n5- VOLTAR\n-> "))
            if qual == 1:
                self.listar()
            elif qual == 2:
                self.listar_categoria()
            elif qual == 3:
                self.listar_autor()
            elif qual == 4:
                self.listar_emprestados()
            elif qual == 5:
                break
            else:
                print("Escolha so o 1, 2 ou 3")
                print()
                os.system("pause")
    
    # -----------------------------------------------------------------------------------------
    def listar(self):
        os.system("cls")
        print("Você está na tela listar.\n")
        print("---------------------------------------------------------\n")
        if not self.__livros:
            print("Nenhum livro cadastrado")
            return
            
        for livro in self.__livros:
            status = "Disponível" if livro.getDisponibilidade() else "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) - {livro.getCategoria()} | [{status}]")
        
        print()
        os.system("pause")
    # --------------------------------------------------------------------------------------------
    def listar_categoria(self):
        os.system("cls")
        print("Você está na parte de listar por categoria.\n")
        print("---------------------------------------------------------\n")
        categoria = input("DIGITE A CATEGORIA: ")
        lista_categoria = []
        for livro in self.__livros:
            if livro.getCategoria().lower() == categoria.lower():
                lista_categoria.append(livro)
        
        if not lista_categoria:
            print(f"Nenhum livro encontrado na categoria '{categoria}'")
            return
            
        for livro in lista_categoria:
            if livro.getDisponibilidade() == True:
                status = "Disponivel"
            else:
                status = "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) | [{status}]")
        print()
        os.system("pause")

    def listar_autor(self):
        os.system("cls")
        print("Você está na parte de listar por autor.\n")
        print("---------------------------------------------------------\n")
        autor = input("DIGITE O AUTOR: ")
        lista_autor = []
        
        for livro in self.__livros:
            if livro.getAutor().lower() == autor.lower():
                lista_autor.append(livro)
        
        if not lista_autor:
            print(f"Nenhum livro encontrado com esse '{autor}'")
            return
            
        for livro in lista_autor:
            if livro.getDisponibilidade() == True:
                status = "Disponivel"
            else:
                status = "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getCategoria()} ({livro.getAno()}) | [{status}]")
        os.system("pause")

    def listar_emprestados(self):
        os.system("cls")
        print("Você está na parte de listar por emprestados.\n")
        print("---------------------------------------------------------\n")
        lista_emprestados = []
        for livro in self.__livros:
            if livro.getDisponibilidade() == False:
                lista_emprestados.append(livro)
        
        if not lista_emprestados:
            print(f"Nenhum livro encontrado está emprestado")
            print()
            os.system("pause")
            return
            
        for livro in lista_emprestados:
            print(f"{livro.getTitulo()} - {livro.getCategoria()} - {livro.getAutor()} ({livro.getAno()})")
        print()
        os.system("pause")      
    # -------------------------------------------------------------------
    def atualizar_livros(self):
        atualizar_livro = input("Digite o nome do livro que deseja atualizar: ")

        livro_encontrado = None
        for livro in self.__livros:
            if livro.getTitulo().lower() == atualizar_livro.lower():
                livro_encontrado = livro
                break
        
        if livro_encontrado is None:
            print("Livro não encontrado!")
            return
        
        novo_autor = input("Atualize o autor do livro (Enter para manter atual):\n---> ")
        novo_titulo = input("Atualize o título do livro (Enter para manter atual):\n---> ")
        novo_ano = input("Atualize o ano do livro (Enter para manter atual):\n---> ")
        nova_categoria = input("Atualize a categoria do livro (Enter para manter atual):\n---> ")

        if novo_autor != "":
            livro_encontrado.setAutor(novo_autor)
        if novo_titulo != "":
            livro_encontrado.setTitulo(novo_titulo)
        if novo_ano != "":
            livro_encontrado.setAno(int(novo_ano))
        if nova_categoria != "":
            livro_encontrado.setCategoria(nova_categoria)
        
        print(f"Livro '{livro_encontrado.getTitulo()}' atualizado com sucesso!")
        print()
        os.system("pause")

    def excluir(self):
        titulo = input("Digite o título do livro que deseja excluir: ")
        for livro in self.__livros:
            if livro.getTitulo().lower() == titulo.lower():
                self.__livros.remove(livro)
                print(f"O livro '{titulo}' foi removido com sucesso!")
                time.sleep(2)
                return
        print("Livro não encontrado!")
        print()
        os.system("pause")

    def emprestar_livro(self):
        titulo = input("Digite o título do livro para empréstimo: ")
        for livro in self.__livros:
            if livro.getTitulo().lower() == titulo.lower():
                livro.emprestar() 
                return
        print("Livro não encontrado")
        print()
        os.system("pause")

    def devolver_livro(self):
        titulo = input("Digite o título do livro para devolução: ")
        for livro in self.__livros:
            if livro.getTitulo().lower() == titulo.lower():
                livro.devolver()  
                return
        print("Livro não encontrado")
        print()
        os.system("pause")
```
---
# Explicação
---
## class Livro:

```python

    def __init__(self, titulo, autor, ano, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__categoria = categoria
        self.__disponibilidade = True
```

<h3>Adicionamos titulos, autor, ano e categoria aos tópicos disponiveis do livro
Onde disponibilidade = True, diz que o livro está disponível</h3>

---
<br>
<br>

```python
    def emprestar(self):
        if self.__disponibilidade == True:
            self.__disponibilidade = False
            print(f"Você emprestou '{self.__titulo}'")
            os.system("pause")
        else:
            print(f"'{self.__titulo}' já está emprestado!")
            os.system("pause")
```

<h3>Aqui diz que a disponibilidade esta 'True', ou seja, disponível e agora você vai pegar o livro, então, agora ele está 'False'</h3>

---
<br>
<br>

```python
    def devolver(self):
        if self.__disponibilidade == False:
            self.__disponibilidade = True
            print(f"Você devolveu este livro '{self.__titulo}'")
        else:
            print(f"'{self.__titulo}' já está disponível!")
```


<h3>Aqui diz que a disponibilidade esta 'False', ou seja, Você vai devolver, então, ele volta a ser 'True'</h3>

---
<br>
<br>

```python
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
```


<h3>Utilizamos o comando 'get', para pegar os valores</h3>

---
<br>
<br>

```python
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
```


<h3>Utilizamos o comando 'set', para renovar os valores</h3>

---
<br>
<br>

```python
    class Biblioteca:
    def __init__(self):
        self.__livros = [
    Livro("1984", "George Orwell", 1949, "Distopia"),
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia"),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Fantasia"),
    Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Clássico"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil"),
    Livro("Moby Dick", "Herman Melville", 1851, "Aventura"),
    Livro("Orgulho e Preconceito", "Jane Austen", 1813, "Romance"),
    Livro("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia"),
    Livro("O Código Da Vinci", "Dan Brown", 2003, "Suspense"),
    Livro("A Revolução dos Bichos", "George Orwell", 1945, "Satírico"),
    Livro("O Alquimista", "Paulo Coelho", 1988, "Ficção"),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Realismo Mágico"),
    Livro("O Morro dos Ventos Uivantes", "Emily Brontë", 1847, "Romance"),
    Livro("O Grande Gatsby", "F. Scott Fitzgerald", 1925, "Romance"),
    Livro("O Sol é Para Todos", "Harper Lee", 1960, "Romance"),
    Livro("A Menina que Roubava Livros", "Markus Zusak", 2005, "Ficção"),
    Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", 1979, "Ficção Científica"),
    Livro("Alice no País das Maravilhas", "Lewis Carroll", 1865, "Infantil"),
    Livro("Frankenstein", "Mary Shelley", 1818, "Terror"),
    Livro("Drácula", "Bram Stoker", 1897, "Terror"),
    Livro("O Perfume", "Patrick Süskind", 1985, "Suspense"),
    Livro("A Cabana", "William P. Young", 2007, "Ficção"),
    Livro("O Diário de Anne Frank", "Anne Frank", 1947, "Biografia"),
    Livro("Jogos Vorazes", "Suzanne Collins", 2008, "Distopia"),
    Livro("Crepúsculo", "Stephenie Meyer", 2005, "Romance")
]
```


#### Class biblioteca com 25 livros ja adicionados
---
<br>
<br>

```python
        def getLivros(self):
            return self.__livros
```

#### 'get' para pegar os valores
---
<br>
<br>

```python
        def setLivros(self, livros):
            self.__livros = livros
```

#### 'set' renovar os valores
---
<br>
<br>

```python
        def cadastrar(self):
                print("Você está na tela de cadastro de livro.\n")
                qtd_livros = int(input("Quantos livros deseja cadastrar?\n-> "))
                for i in range(qtd_livros):
                    titulo = input(f"DIGITE O NOME DO {i+1}º LIVRO: ")    
                    autor = input(f"DIGITE O AUTOR(A) DO {i+1}º LIVRO: ")
                    ano = int(input(f"DIGITE O ANO DO {i+1}º LIVRO: "))
                    categoria = input(f"DIGITE A CATEGORIA DO {i+1}º LIVRO: ")
            
            while True:
                disponibilidade = input("DIGITE s/n PARA A DISPONIBILIDADE DO LIVRO: ").lower()
                if disponibilidade == 's':
                    t_ou_f = True
                    break
                elif disponibilidade == 'n':
                    t_ou_f = False
                    break
                else:
                    print("DIGITE SOMENTE s OU n")
            livro = Livro(titulo, autor, ano, categoria)
            livro.setDisponibilidade(t_ou_f)
            self.__livros.append(livro)
            
        print("LIVROS CADASTRADOS COM SUCESSO")
        time.sleep(2)
```

#### Aqui o cadastro funciona diferente, você escolhe um numero e cadastra os livros dependendo da quantidade que você escolheu, e você adiciona a disponibilidade do livro, sim ou não.
---
<br>
<br>

```python
    def qual_listar(self):
        while True:
            print("\nVocê está na tela de listar.\n")
            print("ESCOLHA UMA OPÇÃO: ")
            qual = int(input("1- LISTAR NORMALMENTE\n2- LISTAR POR CATEGORIA\n3- LISTAR POR AUTOR\n4- LISTAR POR EMPRESTADOS\n5- VOLTAR\n-> "))
            if qual == 1:
                self.listar()
            elif qual == 2:
                self.listar_categoria()
            elif qual == 3:
                self.listar_autor()
            elif qual == 4:
                self.listar_emprestados()
            elif qual == 5:
                break
            else:
                print("Escolha so o 1, 2 ou 3")
                time.sleep(1)
```

#### Aqui é um menu de cada tipo de lista (mostrados abaixo).
---
<br>
<br>     

```python
    def listar(self):
        print("Você está na tela listar.\n")
        if not self.__livros:
            print("Nenhum livro cadastrado")
            return
            
        for livro in self.__livros:
            status = "Disponível" if livro.getDisponibilidade() else "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) - {livro.getCategoria()} | [{status}]")
```

#### Caso não há livros, não consegue listar, caso contrario ele lista, com a informação se está disponivel ou não.
---
<br>
<br>

```python
    def listar_categoria(self):
        print("Você está na parte de listar por categoria.\n")
        categoria = input("DIGITE A CATEGORIA: ")
        lista_categoria = []
        
        for livro in self.__livros:
            if livro.getCategoria().lower() == categoria.lower():
                lista_categoria.append(livro)
        
        if not lista_categoria:
            print(f"Nenhum livro encontrado na categoria '{categoria}'")
            return
            
        for livro in lista_categoria:
            if livro.getDisponibilidade() == True:
                status = "Disponivel"
            else:
                status = "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) | [{status}]")
        time.sleep(2)
```

#### Caso não há livros, não consegue listar, caso contrario, ele lista, cada categoria.
---
<br>
<br>

```python
        def listar_autor(self):
        print("Você está na parte de listar por autor.\n")
        autor = input("DIGITE O AUTOR: ")
        lista_autor = []
        
        for livro in self.__livros:
            if livro.getCategoria().lower() == autor.lower():
                lista_autor.append(livro)
        
        if not lista_autor:
            print(f"Nenhum livro encontrado com esse '{autor}'")
            return
            
        for livro in lista_autor:
            if livro.getDisponibilidade() == True:
                status = "Disponivel"
            else:
                status = "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getCategoria()} ({livro.getAno()}) | [{status}]")
        time.sleep(2)
```
#### Caso não há livros, não consegue listar, caso contrario, ele lista, cada autor.
---
<br>
<br>

```python

    def listar_emprestados(self):
        os.system("cls")
        print("Você está na parte de listar por emprestados.\n")
        print("---------------------------------------------------------\n")
        lista_emprestados = []
        for livro in self.__livros:
            if livro.getDisponibilidade() == False:
                lista_emprestados.append(livro)
        
        if not lista_emprestados:
            print(f"Nenhum livro encontrado está emprestado")
            print()
            os.system("pause")
            return
            
        for livro in lista_emprestados:
            print(f"{livro.getTitulo()} - {livro.getCategoria()} - {livro.getAutor()} ({livro.getAno()})")
        print()
        os.system("pause")    
```

#### Caso não há livros, não consegue listar, caso contrario, ele lista os livros emprestados.
---
<br>
<br>

```python
        def atualizar_livros(self):
            atualizar_livro = input("Digite o nome do livro que deseja atualizar: ")
    
            livro_encontrado = None
            for livro in self.__livros:
                if livro.getTitulo() == atualizar_livro:
                    livro_encontrado = livro
                    break
            
            if livro_encontrado is None:
                print("Livro não encontrado!")
                return
            
            novo_autor = input("Atualize o autor do livro (Enter para manter atual):\n---> ")
            novo_titulo = input("Atualize o título do livro (Enter para manter atual):\n---> ")
            novo_ano = input("Atualize o ano do livro (Enter para manter atual):\n---> ")
            nova_categoria = input("Atualize a categoria do livro (Enter para manter atual):\n---> ")
    
            if novo_autor != "":
                livro_encontrado.setAutor(novo_autor)
            if novo_titulo != "":
                livro_encontrado.setTitulo(novo_titulo)
            if novo_ano != "":
                livro_encontrado.setAno(int(novo_ano))
            if nova_categoria != "":
                livro_encontrado.setCategoria(nova_categoria)
```

#### Nesses quatro 'if', ele apenas atualizara caso haver algo escrito senão, ele não renova nada.
---
<br>
<br>

```python
        def emprestar_livro(self):
            titulo = input("Digite o título do livro para empréstimo: ")
            for livro in self.__livros:
                if livro.getTitulo() == titulo:
                    livro.emprestar()
                    return
            print("Livro não encontrado")
```

#### Aqui diz que a disponibilidade esta 'True', ou seja, disponível e agora você vai pegar o livro, então, agora ele está 'False'
---
<br>
<br>

```python
        def devolver_livro(self):
            titulo = input("Digite o título do livro para devolução: ")
            for livro in self.__livros:
                if livro.getTitulo() == titulo:
                    livro.devolver()
                    return
            print("Livro não encontrfado")
```

#### Aqui diz que a disponibilidade esta 'False', ou seja, não está disponível, então, agora ele está 'True'
---
<br>
<br>

```python
        def excluir(self):
            titulo = input("Digite o título do livro que deseja excluir: ")
            for livro in self.__livros:
                if livro.getTitulo() == titulo:
                    Biblioteca.remove(livro)
                    print(f"O livro '{titulo}' foi removido com sucesso!")
                    return
            print("Livro não encontrado!")
```

#### O usuário informa o título, se o livro for encontrado, ele é removido da lista.
---

# 📂 Vamos agora para o menu

```python
import time
import os 
from classes import Biblioteca
biblioteca = Biblioteca()

while True:                   # criação do menu
    os.system("cls")
    print("Bem vindo ao meu menu!")
    print(30*"==")
    time.sleep(1)
    print("Você está no sistema da biblioteca, selecione uma opção.")
    time.sleep(1)

    print("1- CADASTRO DE LIVRO \n2- EMPRESTAR LIVRO \n3- LISTAR \n4- ATUALIZAR \n5- EXCLUIR \n6- DEVOLVER \n0- SAIR")
    time.sleep(1)

    escolha = int(input("--> "))
    time.sleep(1)

    if escolha == 1:        # opção de cadastro
        biblioteca.cadastrar()

    elif escolha == 2:
        biblioteca.emprestar_livro()
        
    elif escolha == 3:
        biblioteca.qual_listar()
        
    elif escolha == 4:
        biblioteca.atualizar_livros()

    elif escolha == 5:
        biblioteca.excluir()
    
    elif escolha == 6:
        biblioteca.devolver_livro()

    elif escolha == 0:
        print("SAINDO...")
        time.sleep(1)
        os.system("pause")

        break

    else:
        print("ESCOLHA INVALIDA")
        time.sleep(1)
        os.system("pause")

```
#### Agora para o menu, temos as bibliotecas importadas, time e os, para a estética do código, o menu te da opções de cadastrar livro, emprestar um livro, devolver os livros,  escolher o tipo da lista, atualizar os livros, excluir livros e sair do sistema, cada escolha vai a uma função ja explicada
#### Caso você coloque uma opção que não existe ele te integra:
```python
ESCOLHA INVÁLIDA
```
## Bibliotecas Python que usamos:

### Neste projeto, utilizamos algumas bibliotecas padrão do Python:

- `os` → Permite interagir com o sistema operacional, como pausar a execução do programa.  
- `time` → Permite manipular o tempo, por exemplo, para pausar a execução por alguns segundos.
