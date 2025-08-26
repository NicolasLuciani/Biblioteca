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

#### Class biblioteca

    class Biblioteca:
        def __init__(self):
            self.__livros = []

#### 'get' para pegar os valores
        # get
        def getLivros(self):
            return self.__livros

#### 'set' renovar os valores

        # set
        def setLivros(self, livros):
            self.__livros = livros
        
        # ---------------------------------metodos-------------------------------


#### Aqui o cadastro funciona diferente, você escolhe um numero e cadastra os livros dependendo da quantidade que você escolheu

        def cadastrar(self):
            print("Você está na tela de cadastro de livro.\n")
            qtd_livros = int(input("Quantos livros deseja cadastrar?\n-> "))
            for i in range(qtd_livros):
                titulo = input(f"DIGITE O NOME DO {i+1}º livro: ")    
                autor = input(f"DIGITE O AUTOR(A) DO {i+1}º livro: ")
                ano = int(input(f"DIGITE O ANO DO {i+1}º livro: "))
                categoria = input(f"DIGITE A CATEGORIA DO {i+1}º livro: ")
                
                while True:
                    disponibilidade = input("DIGITE s/n PARA A DISPONIBILIDADE DO livro: ").lower()
                    if disponibilidade == 's':
                        t_ou_f = True
                        break
                    elif disponibilidade == 'n':
                        t_ou_f = False
                        break
                    else:
                        print("DIGITE SOMENTE s ou n")
                livro = Livro(titulo, autor, ano, categoria)
                livro.setDisponibilidade(t_ou_f)
                self.__livros.append(livro)
                
            print("LIVROS CADASTRADOS COM SUCESSO")

        # --------------------------------------------------------------------------------

#### Aqui é um menu de cada tipo de lista
        
        def qual_listar(self):
            while True:
                print("\nVocê está na tela de listar.\n")
                print("ESCOLHA UMA OPÇÃO: ")
                qual = int(input("1- LISTAR NORMALMENTE\n2-LISTAR POR CATEGORIA\n3- VOLTAR\n-> "))
                if qual == 1:
                    self.listar()
                elif qual == 2:
                    self.listar_categoria()
                elif qual == 3:
                    break
                else:
                    print("Escolha so o 1, 2 ou 3")
        
        # -----------------------------------------------------------------------------------------

#### Caso não há livros, e não consegue listar caso contrario, ele lista, com a informação se está disponivel ou não.
        
        def listar(self):
            print("Você está na tela listar.\n")
            if not self.__livros:
                print("Nenhum livro cadastrado")
                return
                
            for livro in self.__livros:
                status = "Disponível" if livro.getDisponibilidade() else "Emprestado"
                print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) - {livro.getCategoria()} | [{status}]")
        
        # --------------------------------------------------------------------------------------------

#### Caso não há livros, e não consegue listar caso contrario, ele lista, cada categoria.
        
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
                status = "Disponível" if livro.getDisponibilidade() else "Emprestado"
                print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) | [{status}]")
        
        # -------------------------------------------------------------------

#### Atualiza os livros com o comando 'set'
        
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
    
        def emprestar_livro(self):
            titulo = input("Digite o título do livro para empréstimo: ")
            for livro in self.__livros:
                if livro.getTitulo().lower() == titulo.lower():
                    livro.emprestar()
                    return
            print("Livro não encontrado")
    
        def devolver_livro(self):
            titulo = input("Digite o título do livro para devolução: ")
            for livro in self.__livros:
                if livro.getTitulo().lower() == titulo.lower():
                    livro.devolver()
                    return
            print("Livro não encontrfado")
    
        def excluir(self):
            titulo = input("Digite o título do livro que deseja excluir: ")
            for livro in self.__livros:
                if livro.getTitulo() == titulo:
                    Biblioteca.remove(livro)
                    print(f"O livro '{titulo}' foi removido com sucesso!")
                    return
            print("Livro não encontrado!")
    
    
