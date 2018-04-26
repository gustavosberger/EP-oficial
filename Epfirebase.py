#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:49:43 2018

@author: Gustavo
"""

from firebase import firebase
import json 


firebase = firebase.FirebaseApplication('https://ep-firebase-76b88.firebaseio.com/', None)


#função para testar se uma strig é numero:
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

#se loja for chave em estoque, modifica, se não, cria:
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
print("5-Produtos que estão em falta")
print("6-Valor monetário total do estoque")
print("7-ver menu de opções")
    
#enquanto não escolherem 0, o programa fica repetindo
while escolha!="0":
    
    escolha=input("faça sua escolha: ")
    
    
#opção de menu 1
    if escolha=="1":
        
        #pede o nome do novo produto:
        print ("para cancelar digite: 0")
        produto=input("nome do produto: ")
        #teste se o produto é válido(está no estoque de loja):
        while produto in estoque[loja] and produto!="0":
            print ("este produto já existe")
            produto=input("nome do produto: ")

        #teste se a quantidade inicial é válida (numeral e positivo):
        if produto !="0":
            quantidade_inicial=input("quantidade de {0}: ".format(produto))
            while not quantidade_inicial.isdigit():
                print ("digite apenas numeros!")
                quantidade_inicial=input("quantidade: ")
            quantidade_inicial=int(quantidade_inicial)
            while quantidade_inicial<0:
                print ('digite um valor maior que 0')
                quantidade_inicial=input("quantidade de {0}: ".format(produto))
            
            #pede preço do produto:
            preco=input("digite o preço unitário de {0}: ".format(produto))
            #testa se prço inicial do produto é válido (numero positivo):
            while not isnumber(preco):
                print ("digite apenas numeros!")
                preco=input("preço de {0}: ".format(produto))
            preco=float(preco)
            while preco<0:
                print ('digite um valor maior que 0')
                preco=input("preço de {0}: ".format(produto))
                                    
            #cria dicionario caracteristica como valor de produto, com preço e quantidade como chaves:
            caracteristica={"quantidade":quantidade_inicial,'valor unitario':preco}
            estoque[loja][produto]=caracteristica
            #printa informações do novo produto:
            print ("{0} {1}s foram adicionadas, custando R${2} reais cada".format(quantidade_inicial, produto, "%.2f"%preco))
            
            #cancelamento
        else:
            print("operação cancelada")           
            
            #salva modificações em JSON:
        estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
        with open ('estoque.json','w') as saida:
            saida.write(estoque_json)
        firebase.patch('https://ep-firebase-76b88.firebaseio.com/estoque', estoque)
                
                
                
                
#opção de menu 2
    elif escolha == "2":
        
        #pede um produto para remover:
        print ("para cancelar digite: 0")
        remover= input("Digite o nome do produto que deseja remover: ")
        #testa se produto a ser removido é válido:
        while remover not in estoque[loja] and remover!="0":
            print ("Produto não encontrado")
            remover = input ("Digite um produto válido: ")
            
        #caso não seja cancelado deleta produto:
        if remover !="0":
            if remover in estoque[loja]:
                del estoque [loja][remover]
                print ("{0} foi removido".format(remover))
                
        #cancelamento:
        else:
            print ("operação cancelada")
            
        #salva em JSON:
        estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
        with open ('estoque.json','w') as saida:
            saida.write(estoque_json)
        firebase.patch('https://ep-firebase-76b88.firebaseio.com/estoque', estoque)
            
            
            
#opção de menu 3
    elif escolha == "3":
        
        #pede produto a ser modificado:
        print ("para cancelar digite: 0")
        produto=input('digite o nome do produto: ')
        
        #testa se produto é válido (está no estoque da loja):
        while produto not in estoque[loja] and produto!="0":
            print ('elemento não encontrado')
            produto= input ("digite o nome do produto: ")
            
            
        if produto !="0":
            
            #pede opção de mudança (preço ou quantidade):
            opcao_mudanca= input("Para cancelar digite 0; Para mudar o preço digite 1; Para mudar a quantidade digite 2: ")
            #testa se opção é válida:
            while opcao_mudanca!="0" and opcao_mudanca!="1" and opcao_mudanca!="2":
                print("comando inválido")
                opcao_mudanca= input("Para mudar o preço digite 1; Para mudar a quantidade digite 2: ")
                
            #opçao preço:
            if opcao_mudanca=="1":
                #pede mudança de preço:
                alteracao_preco= input('novo preço unitário de {0}: '.format(produto))    
            #testa se prço inicial do produto é válido (numero positivo):
                while not isnumber(alteracao_preco):
                    print ("digite apenas numeros!")
                    alteracao_preco=input("Novo preço unitário de {0}: ".format(produto))
                alteracao_preco=float(alteracao_preco)
                while alteracao_preco<0:
                    print ('digite um valor maior que 0')
                    alteracao_preco=input("preço de {0}: ".format(produto))
                #preço do produto de uma loja do estoque muda para o novo preço:
                estoque[loja][produto]['valor unitario'] = alteracao_preco
                
            #opçao quantidade:
            elif opcao_mudanca=="2":
                #pede um valor adicional:
                valor_adicional =input('quantidade adicional de {0}: '.format(produto))
                #testa se valor adicional é numero:
                while not isnumber(valor_adicional):
                    print ("digite apenas numeros!")
                    valor_adicional=input("quantidade adicional de {0}: ".format(produto))
                valor_adicional=int(valor_adicional)
                #quantidade de um produto de uma  loja é alterado:
                estoque[loja][produto]['quantidade'] += valor_adicional
                
            #cancelamento:   
            else:
                print ("operaçao cancelada")
            
            #printa o novo estoque:
            print ('novo estoque de {0} é {1}, e seu novo preço é de R${2}'.format(produto,estoque[loja][produto]['quantidade'],"%.2f"%estoque[loja][produto]['valor unitario']))
            
        #cancelamento
        else:
            print("operação cancelada")
        estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
        with open ('estoque.json','w') as saida:
            saida.write(estoque_json)
        firebase.patch('https://ep-firebase-76b88.firebaseio.com/estoque', estoque)
            
            
            
#opção de menu 4
    elif escolha == "4":

        #printa o nome da loja:
        print("Estoque da loja {0}:".format(loja))
        #vai printando todos os produtos da loja e seus preços e quantidades:
        for chave, valor in estoque[loja].items():
            print ("{0} : {1} , R${2}".format(chave, valor["quantidade"], "%.2f"%valor['valor unitario']))



#opção de menu 5
    elif escolha == "5":
        
        #print inicial:
        print("Produtos que estão em falta no estoque:")
        #vai printando itens em falta (quantidade<0):
        for chave,valor in estoque[loja].items():
            if valor["quantidade"] < 0 :
                print (chave)   




#opção de menu 6
    elif escolha == "6":
        
        #cria listinha:
        listinha=[]
        
        #print inicial:
        print("valor monetário total do estoque:")        
        #adiciona valores na listinha:
        for valor in estoque[loja].values():
            if valor["quantidade"] <= 0:
                listinha.append(0)
            elif valor["quantidade"] > 0:
                v = valor["quantidade"] * valor["valor unitario"]
                listinha.append(v)
        #print soma de listinha:
        print('R${0}'.format("%.2f"%sum(listinha)))




#opção de menu 7:
    elif escolha == "7":
        #printa o menuzinho:
        print("0-Sair")
        print("1-Adicionar produto")
        print("2-Remover produto")
        print("3-Modificar produto")
        print("4-Mostrar estoque completo")
        print("5-Produtos que estão em falta")
        print("6-Valor monetário total do estoque")
        print("7-ver menu de opções")
    

#comando inválido:
    elif escolha != "0":
        print ("Comando inválido")
#saudaçoes:
print ("Até a próxima, amigo!")


