import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
NORMAL_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)


    
class Principal(tk.Tk):
    
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        tk.Tk.wm_title(self,"Software Loja")
        
        container= tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
              
        self.frames= {}
        
        
        for F in (StartPage, 
                  PageOne1_1, PageOne1_2, PageOne1_3,
                  PageTwo2_1,
                  PageTree3_1, PageTree3_2, PageTree3_3,
                  PageFour4_1,
                  PageFive5_1,
                  PageSix6_1):
            
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky= "nsew")

        self.show_frame(StartPage)
        

    def show_frame(self, cont):
        
        frame= self.frames[cont]
        frame.tkraise()
  



class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Menu", font= LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button_opcao1= ttk.Button(self,text="Adicionar produto",
                           command=lambda: controller.show_frame(PageOne1_1))
        button_opcao1.pack()
        
        button_opcao2= ttk.Button(self,text="Remover produto",
                           command=lambda: controller.show_frame(PageTwo2_1))
        button_opcao2.pack()
        
        button_opcao3= ttk.Button(self,text="Modificar Produto",
                           command=lambda: controller.show_frame(PageTree3_1))
        button_opcao3.pack()
        
        button_opcao4= ttk.Button(self,text="Mostrar estoque completo",
                           command=lambda: controller.show_frame(PageFour4_1))
        button_opcao4.pack()
        
        button_opcao5= ttk.Button(self,text="Produtos que estão em falta",
                           command=lambda: controller.show_frame(PageFive5_1))
        button_opcao5.pack()
    
        button_opcao6= ttk.Button(self,text="Valor monetário total",
                           command=lambda: controller.show_frame(PageSix6_1))
        button_opcao6.pack()
        
        
        
        self.conteudo_caixa_texto = tk.StringVar()
        
        caixa_texto = tk.Entry(self.window)
        caixa_texto.configure(textvariable=self.conteudo_caixa_texto)
        caixa_texto.grid(row=1, column=0, padx=20, sticky="ew")
        

# =================================== Botão 1 (adicionar produto) =================================== 

class PageOne1_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Digite o nome do produto que deseja adicionar", font= LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1_1= ttk.Button(self,text="Próximo passo",
                           command=lambda: controller.show_frame(PageOne1_2))
        button1_1.pack()
        
        button1_1_2= ttk.Button(self,text="Voltar para o menu principal",
                           command=lambda: controller.show_frame(StartPage))
        button1_1_2.pack()
        
        
class PageOne1_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Digite a quantidade do produto que deseja adicionar", font= LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1_2= ttk.Button(self,text="Próximo",
                           command=lambda: controller.show_frame(PageOne1_3))
        button1_2.pack()
        
        
class PageOne1_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Digite o preço desse produto", font= LARGE_FONT)
        label.pack(pady=10,padx=10)      
        
        button1_3= ttk.Button(self,text="Confirmar produto",
                           command=lambda: controller.show_frame(StartPage))
        button1_3.pack()
        
        
# ===================================  Botão 2 (Remover produto) ===================================       
 
class PageTwo2_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Digite o nome do produto que deseja Remover", font= LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button2_1= ttk.Button(self,text="Confirmar Remoção",
                           command=lambda: controller.show_frame(StartPage))
        button2_1.pack()
        
        button2_1_2= ttk.Button(self,text="Voltar para o menu principal",
                           command=lambda: controller.show_frame(StartPage))
        button2_1_2.pack()
        

# ===================================  Botão 3 (Modificar Produto) ===================================  

class PageTree3_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Digite o nome do produto que deseja Modificar", font= LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button3_1= ttk.Button(self,text="Modificar quantidade",
                           command=lambda: controller.show_frame(PageTree3_2))
        button3_1.pack()
        
        button3_1_2= ttk.Button(self,text="Modificar preço",
                           command=lambda: controller.show_frame(PageTree3_3))
        button3_1_2.pack()
        
        button3_1_3= ttk.Button(self,text="Voltar para o menu principal",
                           command=lambda: controller.show_frame(StartPage))
        button3_1_3.pack()
        
        
class PageTree3_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Modificar quantidade", font= LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button3_2= ttk.Button(self,text="Confirmar modificação",
                           command=lambda: controller.show_frame(StartPage))
        button3_2.pack()
        
        button3_2= ttk.Button(self,text="Voltar",
                           command=lambda: controller.show_frame(PageTree3_1))
        button3_2.pack()

        
class PageTree3_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Modificar preço", font= LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button3_2= ttk.Button(self,text="Confirmar modificação",
                           command=lambda: controller.show_frame(StartPage))
        button3_2.pack()
        
        button3_2= ttk.Button(self,text="Voltar",
                           command=lambda: controller.show_frame(PageTree3_1))
        button3_2.pack()
        
# =================================== Botão 4 (Mostrar Estoque completo) =================================== 
        
class PageFour4_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Ainda não faz nada", font= LARGE_FONT)
        label.pack(pady=10,padx=10)      
        
        button4_1= ttk.Button(self,text="voltar para o menu principal",
                           command=lambda: controller.show_frame(StartPage))
        button4_1.pack()   


# =================================== Botão 5 (Produtos em falta) ===================================            

class PageFive5_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Ainda não faz nada", font= LARGE_FONT)
        label.pack(pady=10,padx=10)      
        
        button5_1= ttk.Button(self,text="voltar para o menu principal",
                           command=lambda: controller.show_frame(StartPage))
        button5_1.pack()    

# =================================== Botão 6 (Valor monetário Total) =================================== 

class PageSix6_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Ainda não faz nada", font= LARGE_FONT)
        label.pack(pady=10,padx=10)      
        
        button6_1= ttk.Button(self,text="voltar para o menu principal",
                           command=lambda: controller.show_frame(StartPage))
        button6_1.pack()  

                          
app= Principal()
app.mainloop()

