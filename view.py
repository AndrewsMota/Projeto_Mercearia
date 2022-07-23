import time
from controller import *
from model import *



while True:

    print('''

    ===========================   
    |    Menu Principal       |
    |                         |
    |    (1) Cadastro         |
    |    (2) Alteração        |
    |    (3) Remoção          |
    |    (4) Caixa            |
    |    (5) Relatório        |
    |    (9) Sair             |
    |                         |
    ===========================
    ''')

    menu = int(input("Selecione uma opção acima: "))
    
    if menu == 1:
        while True:
            print('''

    ===========================   
    |    Menu Cadastro        |
    |                         |
    |    (1) Produto          |
    |    (2) Fornecedor       |
    |    (3) Cliente          |
    |    (4) Funcionario      |
    |    (5) Sair             |
    |                         |
    ===========================
    ''')
    
            menuCadastro = int(input("Selecione uma opção acima: "))
            
            if menuCadastro == 1:
                while True:
                    nome = str(input("Nome do produto: ")).lower()
                    preco = str(input("Preço do produto: "))
                    categoria = str(input("Categoria do produto: ")).lower()
                    
                    print((f"{nome}\n{preco}\n{categoria}"))
                    

                    confirmar = input("As informações acima estão corretas ? S/N ").lower()
                    if confirmar == "n":
                        print('Insira as informações novamente')
                    elif confirmar == "s":
                        break
                    
                produto = Produto(nome, preco, categoria)
                
                ProdutoDal.salvar(produto)
                print(f' {nome} cadastrado com sucesso! ')
                time.sleep(2)
                    
                    
            
            elif menuCadastro == 2:
                pass
            
            elif menuCadastro == 3:
                pass
            
            elif menuCadastro == 4:
                pass
            
            elif menuCadastro == 5:
                break
            
            else:
                print('Informe uma opção válida ')
                time.sleep(2)
    
    elif menu == 2:
        while True:
            print('''

    ===========================   
    |    Menu Alteração       |
    |                         |
    |    (1) Produto          |
    |    (2) Fornecedor       |
    |    (3) Cliente          |
    |    (4) Funcionario      |
    |    (5) Sair             |
    |                         |
    ===========================
    ''')
    
            menuAlteracao = int(input("Selecione uma opção acima: "))
            
            if menuAlteracao == 1:
                nome = str(input('Insira o nome do produto a ser alterado: ')).lower
                nome_produto = str(input('\nInsira a alteração do nome: ')).lower
                preco = str(input('Insira a alteração do preço: '))
                categoria = str(input('Insira a alteração da categotria: ')).lower
                
                confirmar = input(f"Tem certeza que deseja alterar {nome}? S/N ").lower()
                
                if confirmar == 's':
                    produto = Produto(nome_produto, preco, categoria)
                    ProdutoDal.alterar(nome, produto)
                    print((f" {nome} Alterado para {nome_produto}"))   
            
            elif menuAlteracao == 2:
                pass
            
            elif menuAlteracao == 3:
                pass
            
            elif menuAlteracao == 4:
                pass
            
            elif menuAlteracao == 5:
                break
            
            else:
                print('Informe uma opção válida ')
                time.sleep(2)
    
    elif menu == 3:
        while True:
            print('''

    ===========================   
    |    Menu Remoção         |
    |                         |
    |    (1) Produto          |
    |    (2) Fornecedor       |
    |    (3) Cliente          |
    |    (4) Funcionario      |
    |    (5) Sair             |
    |                         |
    ===========================
    ''')
    
            menuRemocao = int(input("Selecione uma opção acima: "))
            
            if menuRemocao == 1:
                nome = str(input('Insira o nome do produto: '))
                
                confirmar = input(f"Tem certeza que deseja remover {nome}? S/N").lower()
                
                if confirmar == 's':
                    ProdutoDal.remover(nome)
                    print((f" {nome} removido com sucesso! "))    

            
            elif menuRemocao == 2:
                pass
            
            elif menuRemocao == 3:
                pass
            
            elif menuRemocao == 4:
                pass
            
            elif menuRemocao == 5:
                break
            
            else:
                print('Informe uma opção válida ')
                time.sleep(2)
    
    elif menu == 4:
        pass
    
    elif menu == 5:
        pass
    
    elif menu == 6:
        break
       
    else:
        print('Informe uma opção válida !')
        time.sleep(2)
        
    

