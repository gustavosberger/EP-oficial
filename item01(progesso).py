#menuzinho das op��es

print(1-adicionar produto)
print(2-remover produto)
print(3-modificar produto)
print(4-mostrar estoque completo)


#estoque da loja
estoque={}

#definindo escolha do menu
escolha=1

#enquanto n�o escolherem 0, o programa fica repetindo
while escolha!=0:
    escolha=int(input("fa�a sua escolha:"))
    
#op��o de menu 1
    if escolha==1:
        produto=input("nome do produto:")
        while produto in estoque:
            print ("este produto j� existe")
            produto=input("nome do produto:")
        quantidade_inicial=int(input("quantidade:"))
        while quantidade_inicial<0:
            print ("a quantidade inicial n�o pode ser negativa")
            quantidade_inicial=int(input("quantidade:"))
        caracteristica={"quantidade":quantidade_inicial}
        estoque[produto]=caracteristica
        print ("{0} {1}s foram adicionadas".format(quantidade_inicial, produto))
        
#op��o de menu 3
    elif escolha == 3:
        produto=input('digite o nome do produto - ')
        if produto in estoque:
            valor_adicional = int(input('quantidade do produto - '))
            estoque[produto]['quantidade'] += valor_adicional
            print ('novo estoque de {0} � {1}'.format(produto,estoque[produto]['quantidade']))
        else:
            print ('elemento n�o encontrado')
        