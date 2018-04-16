#menuzinho das opções

print(1-adicionar produto)
print(2-remover produto)
print(3-modificar produto)
print(4-mostrar estoque completo)


#estoque da loja
estoque={}

#definindo escolha do menu
escolha=1

#enquanto não escolherem 0, o programa fica repetindo
while escolha!=0:
    escolha=int(input("faça sua escolha:"))
    
#opção de menu 1
    if escolha==1:
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
        
#opção de menu 3
    elif escolha == 3:
        produto=input('digite o nome do produto - ')
        if produto in estoque:
            valor_adicional = int(input('quantidade do produto - '))
            estoque[produto]['quantidade'] += valor_adicional
            print ('novo estoque de {0} é {1}'.format(produto,estoque[produto]['quantidade']))
        else:
            print ('elemento não encontrado')
        