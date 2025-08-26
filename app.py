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