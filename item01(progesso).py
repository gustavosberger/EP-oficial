#menuzinho das opções
print("0- sair")
print("1-adicionar produto")
print("2-remover produto")
print("3-modificar produto")
print("4-mostrar estoque completo")


#estoque da loja
estoque={}

#definindo escolha do menu
escolha=1

#enquanto não escolherem 0, o programa fica repetindo
while escolha!="0":
    escolha=input("faça sua escolha:")
    
#opção de menu 1
    if escolha=="1":
        produto=input("nome do produto:")
        while produto in estoque:
            print ("este produto já existe")
            produto=input("nome do produto:")
        quantidade_inicial=int(input("quantidade:"))
        while quantidade_inicial<0:
            print ("a quantidade inicial não pode ser negativa")
            quantidade_inicial=int(input("quantidade:"))
        caracteristica={"quantidade":quantidade_inicial}
        estoque[produto]=caracteristica
        print ("{0} {1}s foram adicionadas".format(quantidade_inicial, produto))

#opção de menu 2
    elif escolha == "2":
        remover= input("Digite o nome do produto que deseja remover: ")
        while remover not in estoque:
            print ("Produto não encontrado")
            remover = input ("Digite um produto válido: ")
        if remover in estoque:
            del estoque [remover]
            print ("{0} foi removido".format(remover))
        
#opção de menu 3
    elif escolha == "3":
        produto=input('digite o nome do produto: ')
        while produto not in estoque:
            print ('elemento não encontrado')
            produto= input ("digite o nome do produto: ")
        valor_adicional = int(input('quantidade do produto: '))
        estoque[produto]['quantidade'] += valor_adicional
        print ('novo estoque de {0} é {1}'.format(produto,estoque[produto]['quantidade']))
        

#opção de menu 4
    elif escolha == "4":
        print("Estoque:")
        for chave, valor in estoque.items():
            print ("{0} : {1}".format(chave,valor["quantidade"]))
    elif escolha != "0":
        print ("Comando inválido")

print ("Até a próxima, amigo!")