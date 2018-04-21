
import json 

#fun��o para testar se uma strig � numero:
def isnumber(valor):
    try:
        float(valor)
    except ValueError:
        return False
    return True

#abrindo arquivo JSON
with open ('estoque.json','r') as entrada:
    a = json.loads(entrada.read())
    
#Estoque recebe JSON:
estoque=a

#pede nome da loja:
loja=input("digite o nome loja: ")

#se loja for chave em estoque, modifica, se n�o, cria:
if loja in estoque:
    print ("modificando a loja {0}".format(loja))
elif loja not in estoque:
    estoque[loja]={}
    print ("criando loja {0}".format(loja))

#definindo escolha do menu
escolha=1

#menuzinho:
print("0-Sair")
print("1-Adicionar produto")
print("2-Remover produto")
print("3-Modificar produto")
print("4-Mostrar estoque completo")
print("5-Produtos que est�o em falta")
print("6-Valor monet�rio total do estoque")
print("7-ver menu de op��es")
    
#enquanto n�o escolherem 0, o programa fica repetindo
while escolha!="0":
    
    escolha=input("fa�a sua escolha: ")
    
    
#op��o de menu 1
    if escolha=="1":
        
        #pede o nome do novo produto:
        print ("para cancelar digite: 0")
        produto=input("nome do produto: ")
        #teste se o produto � v�lido(est� no estoque de loja):
        while produto in estoque[loja] and produto!="0":
            print ("este produto j� existe")
            produto=input("nome do produto: ")

        #teste se a quantidade inicial � v�lida (numeral e positivo):
        if produto !="0":
            quantidade_inicial=input("quantidade de {0}: ".format(produto))
            while not quantidade_inicial.isdigit():
                print ("digite apenas numeros!")
                quantidade_inicial=input("quantidade: ")
            quantidade_inicial=int(quantidade_inicial)
            while quantidade_inicial<0:
                print ('digite um valor maior que 0')
                quantidade_inicial=input("quantidade de {0}: ".format(produto))
            
            #pede pre�o do produto:
            preco=input("digite o pre�o unit�rio de {0}: ".format(produto))
            #testa se pr�o inicial do produto � v�lido (numero positivo):
            while not isnumber(preco):
                print ("digite apenas numeros!")
                preco=input("pre�o de {0}: ".format(produto))
            preco=float(preco)
            while preco<0:
                print ('digite um valor maior que 0')
                preco=input("pre�o de {0}: ".format(produto))
                                    
            #cria dicionario caracteristica como valor de produto, com pre�o e quantidade como chaves:
            caracteristica={"quantidade":quantidade_inicial,'valor unitario':preco}
            estoque[loja][produto]=caracteristica
            #printa informa��es do novo produto:
            print ("{0} {1}s foram adicionadas, custando R${2} reais cada".format(quantidade_inicial, produto, "%.2f"%preco))
            
            #cancelamento
        else:
            print("opera��o cancelada")           
            
            #salva modifica��es em JSON:
        estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
        with open ('estoque.json','w') as saida:
            saida.write(estoque_json)
                
                
                
                
#op��o de menu 2
    elif escolha == "2":
        
        #pede um produto para remover:
        print ("para cancelar digite: 0")
        remover= input("Digite o nome do produto que deseja remover: ")
        #testa se produto a ser removido � v�lido:
        while remover not in estoque[loja] and remover!="0":
            print ("Produto n�o encontrado")
            remover = input ("Digite um produto v�lido: ")
            
        #caso n�o seja cancelado deleta produto:
        if remover !="0":
            if remover in estoque[loja]:
                del estoque [loja][remover]
                print ("{0} foi removido".format(remover))
                
        #cancelamento:
        else:
            print ("opera��o cancelada")
            
        #salva em JSON:
        estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
        with open ('estoque.json','w') as saida:
            saida.write(estoque_json)
            
            
            
            
#op��o de menu 3
    elif escolha == "3":
        
        #pede produto a ser modificado:
        print ("para cancelar digite: 0")
        produto=input('digite o nome do produto: ')
        
        #testa se produto � v�lido (est� no estoque da loja):
        while produto not in estoque[loja] and produto!="0":
            print ('elemento n�o encontrado')
            produto= input ("digite o nome do produto: ")
            
            
        if produto !="0":
            
            #pede op��o de mudan�a (pre�o ou quantidade):
            opcao_mudanca= input("Para cancelar digite 0; Para mudar o pre�o digite 1; Para mudar a quantidade digite 2: ")
            #testa se op��o � v�lida:
            while opcao_mudanca!="0" and opcao_mudanca!="1" and opcao_mudanca!="2":
                print("comando inv�lido")
                opcao_mudanca= input("Para mudar o pre�o digite 1; Para mudar a quantidade digite 2: ")
                
            #op�ao pre�o:
            if opcao_mudanca=="1":
                #pede mudan�a de pre�o:
                alteracao_preco= input('novo pre�o unit�rio de {0}: '.format(produto))    
            #testa se pr�o inicial do produto � v�lido (numero positivo):
                while not isnumber(alteracao_preco):
                    print ("digite apenas numeros!")
                    alteracao_preco=input("Novo pre�o unit�rio de {0}: ".format(produto))
                alteracao_preco=float(alteracao_preco)
                while alteracao_preco<0:
                    print ('digite um valor maior que 0')
                    alteracao_preco=input("pre�o de {0}: ".format(produto))
                #pre�o do produto de uma loja do estoque muda para o novo pre�o:
                estoque[loja][produto]['valor unitario'] = alteracao_preco
                
            #op�ao quantidade:
            elif opcao_mudanca=="2":
                #pede um valor adicional:
                valor_adicional =input('quantidade adicional de {0}: '.format(produto))
                #testa se valor adicional � numero:
                while not isnumber(valor_adicional):
                    print ("digite apenas numeros!")
                    valor_adicional=input("quantidade adicional de {0}: ".format(produto))
                valor_adicional=int(valor_adicional)
                #quantidade de um produto de uma  loja � alterado:
                estoque[loja][produto]['quantidade'] += valor_adicional
                
            #cancelamento:   
            else:
                print ("opera�ao cancelada")
            
            #printa o novo estoque:
            print ('novo estoque de {0} � {1}, e seu novo pre�o � de R${2}'.format(produto,estoque[loja][produto]['quantidade'],"%.2f"%estoque[loja][produto]['valor unitario']))
            
        #cancelamento
        else:
            print("opera��o cancelada")
        estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
        with open ('estoque.json','w') as saida:
            saida.write(estoque_json)
            
            
            
            
#op��o de menu 4
    elif escolha == "4":

        #printa o nome da loja:
        print("Estoque da loja {0}:".format(loja))
        #vai printando todos os produtos da loja e seus pre�os e quantidades:
        for chave, valor in estoque[loja].items():
            print ("{0} : {1} , R${2}".format(chave, valor["quantidade"], "%.2f"%estoque[loja][produto]['valor unitario']))



#op��o de menu 5
    elif escolha == "5":
        
        #print inicial:
        print("Produtos que est�o em falta no estoque:")
        #vai printando itens em falta (quantidade<0):
        for chave,valor in estoque[loja].items():
            if valor["quantidade"] < 0 :
                print (chave)   




#op��o de menu 6
    elif escolha == "6":
        
        #cria listinha:
        listinha=[]
        
        #print inicial:
        print("valor monet�rio total do estoque:")        
        #adiciona valores na listinha:
        for valor in estoque[loja].values():
            if valor["quantidade"] <= 0:
                listinha.append(0)
            elif valor["quantidade"] > 0:
                v = valor["quantidade"] * valor["valor unitario"]
                listinha.append(v)
        #print soma de listinha:
        print('R${0}'.format("%.2f"%sum(listinha)))




#op��o de menu 7:
    elif escolha == "7":
        #printa o menuzinho:
        print("0-Sair")
        print("1-Adicionar produto")
        print("2-Remover produto")
        print("3-Modificar produto")
        print("4-Mostrar estoque completo")
        print("5-Produtos que est�o em falta")
        print("6-Valor monet�rio total do estoque")
        print("7-ver menu de op��es")
    

#comando inv�lido:
    elif escolha != "0":
        print ("Comando inv�lido")
#sauda�oes:
print ("At� a pr�xima, amigo!")