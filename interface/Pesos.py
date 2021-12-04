

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.valor1    = valor1        # valor do nó na árvore
        self.valor2    = valor2        # custo do caminho até o nó atual
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):
        
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


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
            str.append(aux.estado)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        
        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca1(object):
    
    def custo_uniforme(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]
                v1 = v2

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            visitado[j][1]=v1
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1 , v1, atual)
                    l2.inserePos_X(novo, v1, v1, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      
    
    
    def greedy(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                ind1 = nos.index(grafo[ind][i][0])

                # HEURÍSTICA DO NÓ ATUAL ATÉ O OBJETIVO
                v2 = atual.valor2 + grafo[ind][i][1]
                ind2 = nos.index(fim)
                v1 = h[ind2][ind1]

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1]=v1

                        break
                
                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)
                    return linha
                    
        return "Caminho não encontrado"      

    
    def a_estrela(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                ind1 = nos.index(grafo[ind][i][0])

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]
                ind2 = nos.index(fim)
                v1 = v2 + h[ind2][ind1]
                
                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1]=v1
                        break
                
                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)
                        
                    
        return "Caminho não encontrado"      

nos = ["Vila Romana", "Vila Batista", "Vila Maria", "Vila Paulo Romeu",
       "Vila Canevari", "Centro", "Itagaçaba", "Jardim America","Jardim Europa", "Vila Ana Rosa", "Regina Celia", "KM4","Vila Biondi", "Comerciarios", "Vila Juvenal","Parque Primavera","Cecap","Vila Brasil"]

grafo = [
            [["Vila Paulo Romeu",11],["Vila Canevari",15],["KM4",20]], #Vila Romana                 
            [["Vila Canevari",40], ["Centro",66],["Regina Celia",90]], #Vila Batista
            [["Itagaçaba",100], ["Jardim America",120], ["Vila Ana Rosa",130]], #Vila maria
            [["Vila Romana",50],["Vila Canevari",10], ["Centro",140], ["Cecap",160]], #Vila Paulo Romeu
            [["Vila Romana",43],["Vila Batista",70], ["Vila Paulo Romeu",80]], #Vila canevari
            [["Vila Batista",97],["Vila Paulo Romeu",91],["Jardim America",87],["Regina Celia",79]], #Centro
            [["Vila Maria",151],["Jardim America",170], ["Vila Biondi",174]], #Itagaçaba
            [["Vila Maria",152], ["Centro",200],["Itagaçaba",168], ["KM4",190],["Vila Biondi",105]],#Jardim America
            [["Vila Ana Rosa",71], ["Comerciarios",209],["Parque Primavera",158]], #Jardim Europa
            [["Vila Maria",75], ["Jardim Europa",160],["Regina Celia",117],["Vila Juvenal",90],["Parque Primavera",58]], #Vila Ana rosa
            [["Vila Batista",100], ["Centro",130],["Vila Ana Rosa",74]], #Regina celia
            [["Vila Romana",71],["Jardim America", 103],["Vila Juvenal",78]], #km4
            [["Itagaçaba",115], ["Jardim America",128],["Comerciarios",129],["Vila Juvenal",131],["Cecap",134]],#Vila Biondi
            [["Jardim Europa",136], ["Vila Biondi",138], ["Vila Juvenal",143],["Cecap",148], ["Vila Brasil",177]], #Comerciarios
            [["Vila Ana Rosa",122],["KM4",91],["Vila Biondi",20],["Comerciarios",250],["Vila Brasil",211]], #Vila Juvenal
            [["Jardim Europa",185], ["Vila Ana Rosa",169]], #Parque primavera
            [["Vila Paulo Romeu",76],["Vila Biondi", 163],["Comerciarios",169]], #Cecap
            [["Comerciarios",127],["Vila Juvenal",37]] #Vila Brasil
           
       ]


h = [
     [0,11,15,20,60,30,90,86,10,110,70,35,74,95,56,90,88,97],
     [95,0,30,94,63,30,92,87,100,150,71,32,78,83,55,90,88,99],
     [55,21,0,66,77,91,87,48,89,78,68,102,132,100,90,23,91,244],
     [100,15,13,0,64,36,90,86,10,110,70,35,89,95,56,90,88,97],
     [14,15,20,30,0,90,86,36,104,120,72,35,46,55,59,36,73,71],
     [15,30,105,200,61,0,94,123,14,5,73,39,22,83,57,98,43,109],
     [111,15,22,60,30,86,0,106,110,70,35,57,95,56,90,88,97,60],
     [102,18,20,61,30,90,10,0,85,71,39,33,91,56,103,81,99,65],
     [9,18,20,62,30,90,86,10,0,110,75,35,70,95,109,90,88,97],
     [11,15,200,60,30,93,86,120,110,0,70,35,79,95,56,90,88,97],
     [17,140,21,62,77,72,160,201,115,230,0,31,124,116,20,138,160,170],
     [140,152,29,61,180,91,87,107,110,240,350,0,49,133,158,176,89,190],
     [112,15,209,123,79,90,86,10,188,70,35,77,0,95,56,99,88,97],
     [300,155,45,360,9,91,330,107,113,70,35,73,95,0,56,90,88,97],
     [290,16,22,220,31,137,86,10,110,79,359,73,91,57,0,99,129,197],
     [349,157,29,126,316,10,11,101,116,3,356,42,41,61,94,0,15,81],
     [12,13,21,69,301,67,36,65,160,171,351,173,33,76,91,22,0,179],
     [168,39,209,237,31,55,80,129,170,380,47,75,263,264,221,67,92,0],
    
     ]

sol1 = busca1()
caminho = []






