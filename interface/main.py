from flask import Flask, render_template, request
from Pesos import *


app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    
    if request.method == "GET":
        return  render_template("index.html")

    else:
        origem = request.form.get("origem")
        destino = request.form.get("destino")
        metodo = request.form.get("metodo")

    if origem  == '':
            return '<h1> Coloque uma origem</h1>'

    if destino  == '':
            return '<h1> Coloque um destino</h1>'
    
    else:
        class No(object):
            def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
                self.pai       = pai
                self.valor1    = valor1
                self.valor2    = valor2
                self.anterior  = anterior
                self.proximo   = proximo
            
        class lista(object):
            head = None
            tail = None

            # INSERE NO INÍCIO DA LISTA
            def inserePrimeiro(self, v1, v2, p):
                novo_no = No(p, v1, v2, None, None)
                if self.head == None:
                    self.tail = novo_no
                    self.head = novo_no
                else:
                    novo_no.proximo = self.head
                    self.head.anterior = novo_no
                    self.head = novo_no

            # INSERE NO FIM DA LISTA
            def insereUltimo(self, v1, v2, p):

                novo_no = No(p, v1, v2, None, None)

                if self.head is None:
                    self.head = novo_no
                else:
                    self.tail.proximo = novo_no
                    novo_no.anterior   = self.tail
                self.tail = novo_no

            # REMOVE NO INÍCIO DA LISTA
            def deletaPrimeiro(self):
                if self.head is None:
                    return None
                else:
                    no = self.head
                    self.head = self.head.proximo
                    if self.head is not None:
                        self.head.anterior = None
                    else:
                        self.tail = None
                    return no

            # REMOVE NO FIM DA LISTA
            def deletaUltimo(self):
                if self.tail is None:
                    return None
                else:
                    no = self.tail
                    self.tail = self.tail.anterior
                    if self.tail is not None:
                        self.tail.proximo = None
                    else:
                        self.head = None
                    return no

            def vazio(self):
                if self.head is None:
                    return True
                else:
                    return False
                
            def exibeLista(self):
                
                aux = self.head
                str = []
                while aux != None:
                    temp = []
                    temp.append(aux.valor1)
                    temp.append(aux.valor2)
                    str.append(temp)
                    aux = aux.proximo
                
                return str
            
            def exibeCaminho(self):
                
                atual = self.tail
                caminho = []
                while atual.pai is not None:
                    caminho.append(atual.valor1)
                    atual = atual.pai
                caminho.append(atual.valor1)
                caminho = caminho[::-1]
                return caminho
            
            def exibeCaminho1(self,valor):
                        
                atual = self.head
                while atual.valor1 != valor:
                    atual = atual.proximo
            
                caminho = []
                atual = atual.pai
                if atual is None:
                    #caminho.append(valor)
                    return caminho
                print(atual)
                while atual.pai is not None:
                    caminho.append(atual.valor1)
                    atual = atual.pai
                caminho.append(atual.valor1)
                return caminho

            def primeiro(self):
                return self.head
            
            def ultimo(self):
                return self.tail

        class busca(object):

            def amplitude(self, inicio, fim):

                # manipular a FILA para a busca
                l1 = lista()

                # cópia para apresentar o caminho (somente inserção)
                l2 = lista()

                # insere ponto inicial como nó raiz da árvore
                l1.insereUltimo(inicio,0,None)
                l2.insereUltimo(inicio,0,None)

                # controle de nós visitados
                visitado = []
                linha = []
                linha.append(inicio)
                linha.append(0)
                visitado.append(linha)

                while l1.vazio() == False:
                    # remove o primeiro da fila
                    atual = l1.deletaPrimeiro()
                    if atual is None: break

                    ind = nos.index(atual.valor1)

                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafo[ind])):

                        novo = grafo[ind][i]
                        flag = True  # pressuponho que não foi visitado

                        # controle de nós repetidos
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.valor2+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.valor2+1
                                break
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.valor2 + 1, atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)

                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor2+1)
                            visitado.append(linha)

                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("Fila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho

                return "caminho não encontrado"


            def profundidade(self, inicio, fim):  
                
                caminho = []

                # manipular a FILA para a busca
                l1 = lista()

                # cópia para apresentar o caminho (somente inserção)
                l2 = lista()

                # insere ponto inicial como nó raiz da árvore
                l1.insereUltimo(inicio,0,None)
                l2.insereUltimo(inicio,0,None)

                # controle de nós visitados
                visitado = []
                linha = []
                linha.append(inicio)
                linha.append(0)
                visitado.append(linha)


                while l1.vazio() == False:
                    # remove o primeiro da fila
                    atual = l1.deletaUltimo()
                    if atual is None: break

                    ind = nos.index(atual.valor1)

                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafo[ind])-1,-1,-1):

                        novo = grafo[ind][i]
                        #print("\tFilho de atual: ",novo)
                        flag = True  # pressuponho que não foi visitado

                        # para cada conexão verifica se já foi visitado
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.valor2+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.valor2+1
                                break
                            
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.valor2 + 1, atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)

                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor2+1)
                            visitado.append(linha)

                            # verifica se é o objetivo
                            if novo == fim:
                                caminho += l2.exibeCaminho()
                                #print("Árvore de busca:\n",l2.exibeLista())
                                return caminho

                return "caminho não encontrado"


            def profundidade_limitada(self, inicio, fim, limite):
                
                caminho = [] 

                # manipular a FILA para a busca
                l1 = lista()

                # cópia para apresentar o caminho (somente inserção)
                l2 = lista()

                # insere ponto inicial como nó raiz da árvore
                l1.insereUltimo(inicio,0,None)
                l2.insereUltimo(inicio,0,None)

                # controle de nós visitados
                visitado = []
                linha = []
                linha.append(inicio)
                linha.append(0)
                visitado.append(linha)


                while l1.vazio() == False:
                    # remove o primeiro da fila
                    atual = l1.deletaUltimo()
                    if atual is None: break

                    if atual.valor2 < limite:
                        ind = nos.index(atual.valor1)
            
                        # varre todos as conexões dentro do grafo a partir de atual
                        for i in range(len(grafo[ind])-1,-1,-1):
            
                            novo = grafo[ind][i]
                            #print("\tFilho de atual: ",novo)
                            flag = True  # pressuponho que não foi visitado
            
                            # para cada conexão verifica se já foi visitado
                            for j in range(len(visitado)):
                                if visitado[j][0]==novo:
                                    if visitado[j][1]<=(atual.valor2+1):
                                        flag = False
                                    else:
                                        visitado[j][1]=atual.valor2+1
                                    break
                                
                            
                            # se não foi visitado inclui na fila
                            if flag:
                                l1.insereUltimo(novo, atual.valor2 + 1, atual)
                                l2.insereUltimo(novo, atual.valor2 + 1, atual)
            
                                # marca como visitado
                                linha = []
                                linha.append(novo)
                                linha.append(atual.valor2+1)
                                visitado.append(linha)
            
                                # verifica se é o objetivo
                                if novo == fim:
                                    caminho += l2.exibeCaminho()
                                    #print("Árvore de busca:\n",l2.exibeLista())
                                    return caminho

                return "caminho não encontrado"


            def aprofundamento_iterativo(self, inicio, fim):
                
                for limite in range(len(nos)):
                    caminho = []
            
                    # manipular a FILA para a busca
                    l1 = lista()
            
                    # cópia para apresentar o caminho (somente inserção)
                    l2 = lista()
            
                    # insere ponto inicial como nó raiz da árvore
                    l1.insereUltimo(inicio,0,None)
                    l2.insereUltimo(inicio,0,None)
            
                    # controle de nós visitados
                    visitado = []
                    linha = []
                    linha.append(inicio)
                    linha.append(0)
                    visitado.append(linha)
            
            
                    while l1.vazio() is not None:
                        # remove o primeiro da fila
                        atual = l1.deletaUltimo()
                        if atual is None: break
            
                        if (atual.valor2) < limite:
                            ind = nos.index(atual.valor1)
                
                            # varre todos as conexões dentro do grafo a partir de atual
                            for i in range(len(grafo[ind])-1,-1,-1):
                
                                novo = grafo[ind][i]
                                #print("\tFilho de atual: ",novo)
                                flag = True  # pressuponho que não foi visitado
                
                                # para cada conexão verifica se já foi visitado
                                for j in range(len(visitado)):
                                    if visitado[j][0]==novo:
                                        if visitado[j][1]<=(atual.valor2+1):
                                            flag = False
                                        else:
                                            visitado[j][1]=atual.valor2+1
                                        break
                                    
                                
                                # se não foi visitado inclui na fila
                                if flag:
                                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                                    l2.insereUltimo(novo, atual.valor2 + 1, atual)
                
                                    # marca como visitado
                                    linha = []
                                    linha.append(novo)
                                    linha.append(atual.valor2+1)
                                    visitado.append(linha)
                
                                    # verifica se é o objetivo
                                    if novo == fim:
                                        caminho += l2.exibeCaminho()
                                        #print("Árvore de busca:\n",l2.exibeLista())
                                        return caminho

                return "caminho não encontrado"

            def bidirecional(self, inicio, fim):

                # listas para a busca a partir da origem - busca 1
                l1 = lista()      # busca na FILA
                l2 = lista()      # cópia da árvore completa

                # listas para a busca a partir da destino -  busca 2
                l3 = lista()      # busca na FILA
                l4 = lista()      # cópia da árvore completa

                # cria estrutura para controle de nós visitados
                visitado = []

                l1.insereUltimo(inicio,0,None)
                l2.insereUltimo(inicio,0,None)
                linha = []
                linha.append(inicio)
                linha.append(1)
                visitado.append(linha)
                
                l3.insereUltimo(fim,0,None)
                l4.insereUltimo(fim,0,None)
                linha = []
                linha.append(fim)
                linha.append(2)
                visitado.append(linha)
                
                while True:
                    
                    # EXECUÇÃO DO PRIMEIRO AMPLITUDE - BUSCA 1
                    flag1 = True
                    while flag1:
                        
                        atual = l1.deletaPrimeiro()
                        if atual==None:
                            break
                        ind = nos.index(atual.valor1)
                        for i in range(len(grafo[ind])):
                            novo = grafo[ind][i]
                            flag2 = True
                            flag3 = False
                            for j in range(len(visitado)):
                                if visitado[j][0]==novo:
                                    if visitado[j][1] == 1:    # visitado na mesma árvore
                                        flag2 = False
                                    else:                      # visitado na outra árvore
                                        flag3 = True
                                    break
                            # for j
                                
                            if flag2:
                                l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                                l2.insereUltimo(novo, atual.valor2 + 1, atual)
                                print("arvore1:", l2.exibeLista())
                                
                                if flag3:
                                    caminho = []
                                    caminho = l2.exibeCaminho()
                                    #caminho = caminho[::-1]
                                    caminho += l4.exibeCaminho1(novo)
                                    return caminho
                                else:
                                    linha = []
                                    linha.append(novo)
                                    linha.append(1)
                                    visitado.append(linha)
                                # if flag3
                            # if flag2
                        # for i
                        
                        
                        if(l1.vazio()!=True):
                            aux = l1.primeiro()
                            if aux.valor2 == atual.valor2:
                                flag1 = True
                            else:
                                flag1 = False                

                    # EXECUÇÃO DO SEGUNDO AMPLITUDE - BUSCA 2
                    flag1 = True
                    while flag1:
                        atual = l3.deletaPrimeiro()
                        if atual==None:
                            break
                        ind = nos.index(atual.valor1)
                        print("atual",atual.valor1)
                        for i in range(len(grafo[ind])):
                            novo = grafo[ind][i]
                            flag2 = True
                            flag3 = False
                            for j in range(len(visitado)):
                                if visitado[j][0]==novo:
                                    if visitado[j][1] == 2:
                                        flag2 = False
                                    else:
                                        flag3 = True
                                    break
                                
                            if flag2:
                                l3.insereUltimo(novo, atual.valor2 + 1 , atual)
                                l4.insereUltimo(novo, atual.valor2 + 1, atual)
                                print("arvore2:", l4.exibeLista())
                                
                                if flag3:
                                    caminho = []
                                    caminho = l4.exibeCaminho()
                                    caminho = caminho[::-1]
                                    print(caminho)
                                    print(novo)
                                    caminho += l2.exibeCaminho1(novo)
                                    return caminho
                                else:
                                    linha = []
                                    linha.append(novo)
                                    linha.append(2)
                                    visitado.append(linha)
                                
                        if(l3.vazio() != True):
                            aux = l3.primeiro()
                            if(atual.valor2 == aux.valor2):
                                flag1 = True
                            else:
                                flag1 = False

        nos = ["Vila Romana", "Vila Batista", "Vila Maria", "Vila Paulo Romeu",
            "Vila Canevari", "Centro", "Itagaçaba", "Jardim America","Jardim Europa", "Vila Ana Rosa", "Regina Celia", "KM4","Vila Biondi", "Comerciarios", "Vila Juvenal","Parque Primavera","Cecap","Vila Brasil"]

        grafo = [
                    ["Vila Paulo Romeu", "Vila Canevari", "KM4"], #Vila Romana                 
                    ["Vila Canevari", "Centro","Regina Celia"], #Vila Batista
                    ["Itagaçaba", "Jardim America", "Vila Ana Rosa"], #Vila maria
                    ["Vila Romana","Vila Canevari", "Centro", "Cecap"], #Vila Paulo Romeu
                    ["Vila Romana","Vila Batista", "Vila Paulo Romeu"], #Vila canevari
                    ["Vila Batista","Vila Paulo Romeu","Jardim America","Regina Celia"], #Centro
                    ["Vila Maria","Jardim America", "Vila Biondi"], #Itagaçaba
                    ["Vila Maria", "Centro","Itagaçaba", "KM4","Vila Biondi"],#Jardim America
                    ["Vila Ana Rosa", "Comerciarios","Parque Primavera"], #Jardim Europa
                    ["Vila Maria", "Jardim Europa","Regina Celia","Vila Juvenal","Parque Primavera"], #Vila Ana rosa
                    ["Vila Batista", "Centro","Vila Ana Rosa"], #Regina celia
                    ["Vila Romana","Jardim America","Vila Juvenal"], #km4
                    ["Itagaçaba", "Jardim America","Comerciarios","Vila Juvenal","Cecap"],#Vila Biondi
                    ["Jardim Europa", "Vila Biondi", "Vila Juvenal","Cecap", "Vila Brasil"], #Comerciarios
                    ["Vila Ana Rosa","KM4", "Vila Biondi","Comerciarios","Vila Brasil"], #Vila Juvenal
                    ["Jardim Europa", "Vila Ana Rosa"], #Parque primavera
                    ["Vila Paulo Romeu","Vila Biondi","Comerciarios"], #Cecap
                    ["Comerciarios","Vila Juvenal"] #Vila Brasil
                
            ]

        sol = busca()
        sol1 = busca1()
        caminho = []

        """origem = "Vila Biondi"
        destino = "Vila Maria"""


        caminho = sol.amplitude(origem,destino)
        caminho2 = caminho
        caminho2 = sol.profundidade(origem,destino)
        caminho3 = caminho
        caminho3 = sol.profundidade_limitada(origem,destino,2)
        #caminho4 = caminho
        #caminho5 = caminho
        #caminho5 = sol.profundidade_limitada(origem,destino,7)
        caminho6 = caminho
        caminho6 = sol.aprofundamento_iterativo(origem,destino)
        caminho7 = caminho
        caminho7 = sol.bidirecional(origem,destino)


        custos = caminho
        custos = caminho, custo = sol1.custo_uniforme(origem, destino)
        #print("Custo Uniforme: ",caminho[::-1],"\ncusto do caminho: ",custo)
        greedy = caminho
        greedy = caminho, custo = sol1.greedy(origem, destino)
        #print("\nGreedy: ",caminho[::-1],"\ncusto do caminho: ",custo)
        estrela = caminho
        estrela = caminho, custo = sol1.a_estrela(origem, destino)
        #print("\nA estrela: ",caminho[::-1],"\ncusto do caminho: ",custo)


    
    if metodo == 'amplitude':
        return  render_template("index.html", caminho1 = caminho)
    if metodo =='profundidade':
        return  render_template("index.html", caminho2 = caminho2)
    if metodo =='profundidade limitada':
        return  render_template("index.html", caminho3 = caminho3)
    if metodo =='aprofundamento iterativo':
        return  render_template("index.html", caminho6 = caminho6)
    if metodo =='bidirecional':
        return  render_template("index.html", caminho7 = caminho7)
    if metodo == 'custo uniforme':
        return  render_template("index.html", custo = custos)
    if metodo == 'greedy':
        return  render_template("index.html", greedy = greedy)
    if metodo == 'estrela':
        return  render_template("index.html", estrela = estrela)
    
app.run()

