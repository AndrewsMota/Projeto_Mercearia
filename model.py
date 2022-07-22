import datetime

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria


class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        
        
class Funcionario(Pessoa):
    def __init__(self, clt, nome, cpf, idade, endereco, telefone):
        self.clt = clt
        self.idade = idade
        super(Funcionario, self).__init__(nome, cpf, endereco, telefone)


class Produto:
    def __init__(self,nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
       
        
        
class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria
        
        
        
class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        
        
class Venda:
    def __init__(self, itensVendidos: Produto, vendedor, comprador, quantidadeVendida, data = datetime.date):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data
        
class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, email):
        super(Cliente, self).__init__(nome, cpf, endereco, telefone)