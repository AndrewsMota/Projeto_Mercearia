from model import *
import os.path  

class ProdutoDal:
    @classmethod
    def salvar(cls, produto: Produto):

        if os.path.exists('produtos.txt'):
            with open('produtos.txt', 'r') as arquivo:
                for line in arquivo:
                    for word in line.split():
                        if str(produto.nome) == word:
                            print(f'O produto {produto.nome}  já consta em nosso sistema ')
                            return   
                
        with open('produtos.txt', 'a') as arquivo:           
            arquivo.write(produto.nome + " " + str(produto.preco) + " " + (produto.categoria)+ " \n" )
            

                
                        
    @classmethod        
    def alterar(cls, produto, novo_produto):
        with open('produtos.txt', 'r') as arquivo:
            lista_condicao = arquivo.read().split(" ")
            
            if produto not in lista_condicao:
                return(print(f"{produto} não consta na base de dados"))
            
        
        ProdutoDal.remover(produto)
        ProdutoDal.salvar(novo_produto)
        
    @classmethod
    def remover(cls, produto):
        data = ""
        
        with open('produtos.txt', 'r') as arquivo:
            lista_produto = arquivo.read().splitlines()
            
            for line in lista_produto:
                if produto not in line:
                    data += line + "\n"                    
        
        with open('produtos.txt', 'w') as arquivo:
            arquivo.write(data)
                     
        

class FornecedorDal:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'w') as arquivo:
            arquivo.write(fornecedor.categoria + " " + fornecedor.cnpj + " " + fornecedor.nome + " " + fornecedor.telefone)

class ClienteDal:
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open('cliente.txt', 'w') as arquivo:
            arquivo.write(cliente.cpf + " " + cliente.email + " " + cliente.nome + " " + cliente.telefone)
            
class FuncionarioDal:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'w') as arquivo:
            arquivo.write(funcionario.clt + " " + funcionario.cpf + " " + funcionario.email + " " + funcionario.endereco + " " + funcionario.idade + " " + funcionario.nome + " " + funcionario.telefone)

