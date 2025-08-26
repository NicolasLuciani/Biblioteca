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

import time # importei a biblioteca time
import os # importei a biblioteca os
from classes import cadastrar, emprestar, qual_listar, atualizar_livros, excluir 
# importei todas as classe do arquivo classes



while True:                   # criação do menu
    os.system("cls")
    print("Bem vindo ao menu!")
    print(30*"=")
    time.sleep(1)
    print("Você está no sistema da biblioteca, selecione uma opção.")
    time.sleep(1)

    print("1- CADASTRO DE LIVRO \n2- EMPRESTAR LIVRO \n3- LISTAR \n4- ATUALIZAR \n5- EXCLUIR \n0- S")
    time.sleep(1)

    escolha = int(input("--> "))
    time.sleep(1)
    

    if escolha == 1:        # opção de cadastro
        cadastrar()

    elif escolha == 2:
        emprestar()
        
    elif escolha == 3:
        qual_listar()
        
    elif escolha == 4:
        atualizar_livros()

    elif escolha == 5:
        excluir()

    elif escolha == 0:
        print("SAINDO...")
        time.sleep(1)
        os.system("pause")

        break

    else:
        print("ESCOLHA INVALIDA")
        time.sleep(1)
        os.system("pause")
