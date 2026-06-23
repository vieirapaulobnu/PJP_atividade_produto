from modelos import Produto, listar_produtos

def exibir_menu():
    print("=======================")
    print("MENU DE PRODUTOS")
    print("0 - Sair")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("=======================")

def cadastrar():
    nome = input("Digite o nome: ")
    preco = float(input("Digite o preço:"))
    categoria = input("Digite a categoria: ") 

    produto = Produto(nome, preco, categoria)
    produto.salvar()

def mostrar():
    for produto in listar_produtos():
        produto.exibir()

    while True:
        opcao = input("Digite uma opção: ")

        if opcao == "0":
            break
        elif opcao == "1":
            cadastrar()
        elif opcao == "2":
            mostrar()
        else:
            print("Opção inválida! Tente novamente.")