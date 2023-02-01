
import pygame
from pygame.locals import*
from sys import exit
import random
import os
import sys



def Jogar(ids,exp):
    pygame.init()
    pygame.mixer.init()
    #configurações da tela
    largura=1000
    altura=800
    tela = pygame.display.set_mode((largura,altura))
    fonte1 = pygame.font.SysFont('arial', 20, True, False)
    pygame.display.set_caption("prototipo: Jogo da memória")
    #clock do jogo
    clock = pygame.time.Clock() 
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
    for joystick in joysticks:
        print(joystick.get_name()) 
        joystick.init() 

    class joysticksFalso(object):
        def __init__(self):
            pass
        def get_button(self,numero):
            pass
    if len(joysticks)==0:
        joystick = joysticksFalso()

    if getattr(sys, 'frozen', False):
        path = sys._MEIPASS
    else:
        path = os.path.dirname(os.path.abspath(__file__))

    class estrela(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.sprites=[]
            self.sprites.append(pygame.image.load_extended(f"{path}\\imagens\\estrela0.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}\\imagens\\estrela1.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}\\imagens\\estrela2.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}\\imagens\\estrela3.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}\\imagens\\estrela4.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}\\imagens\\estrela5.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}\\imagens\\estrela6.png")) 
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = 85, 0

        def update(self):
            self.atual += 1
            self.image = self.sprites[self.atual]
            
    #Idendifica qual carta está revelada ou não       
    def cartarevelação(val):
        cartarevelada = []
        for i in range (Nhor):
            cartarevelada.append([val]*Nver)
        return cartarevelada

    #Responsavel por pegar as letras e entregar sua devida posição.
    def cartarandomica(tipo):
        #pega todas as letras disponiveis pra fruta ou animal
        icones = []
        if tipo == 'animal':
            for letra in letrasAn:
                icones.append(letra)
        elif tipo == 'fruta':
            for letra in letrasFr:
                icones.append(letra)

        #Aleatoriza e adiciona apenas o numero necessario de letras.
        random.shuffle(icones)
        num = int((Nhor)*((Nver)/2))
        icones = icones[:num]*2
        random.shuffle(icones)
        quadro=[]
        #entrega a posição de cada letra para ser colocado no jogo.
        for x in range(Nhor):
            coluna = []
            for y in range(Nver):
                coluna.append(icones[0])
                del icones[0]
            quadro.append(coluna)
            random.shuffle(quadro)
        return quadro

    #Transforma a posição em coordenadas para ser posto na tela.
    def ecdacarta(cartax, cartay):
        esquerda = cartax*(tamcarta+gap)+margemx
        cima = cartay*(tamcarta+(gap*2))+margemy
        return(esquerda, cima)

    #Responsavel por pegar a carta selecionada e sua coordenadas.
    def pegarcarta(x, y):
        for cartax in range(Nhor):
            for cartay in range(Nver):
                esquerda, cima = ecdacarta(cartax, cartay)
                rectcarta = pygame.Rect(esquerda, cima, tamcarta, tamcarta)
                if rectcarta.collidepoint(x,y):
                    return (cartax, cartay)
        return (None, None)
    
    #Desenha as cartas.
    def desenhaicone(letra, cartax, cartay):
        esquerda, cima = ecdacarta(cartax, cartay)
        tela.blit(azul,(esquerda+quarto,cima+quarto))
        tela.blit(letra,(esquerda+quarto,cima+quarto))
            
    ##pega o valor de x e y da carta armazenada.
    def getletra(quadro, cartax, cartay):
        return quadro[cartax][cartay]

    #Função utilizada para cobrir as cartas no quadro.
    def desenhocobrircarta(quadro, cartas, cobrir):
        for carta in cartas:
            #Mostra a carta a partir de sua posição.
            esquerda, cima = ecdacarta(carta[0],carta[1])
            pygame.draw.rect(tela, (0,0,0), ((esquerda+quarto),(cima+quarto), tamcarta, tamcarta))
            letra= getletra(quadro,carta[0],carta[1])
            desenhaicone(letra,carta[0],carta[1])
            #cobre a carta usando o quadro por segundos estabelecido.
            if cobrir > 0:
                pygame.draw.rect(tela,(255,255,255), ((esquerda+quarto),(cima+quarto),cobrir,tamcarta))
        pygame.display.update()
        clock.tick(60)

    #Revela a carta selecionada
    def revelarcarta(quadro, cartarevelar):
        desenhocobrircarta(quadro,cartarevelar,0)

    #Inicia a função de cobrir a carta pra cada carta. 
    def cobrircarta(quadro, cartacobrir,carta):
        for coberto in range(0,tamcarta):
            desenhocobrircarta(quadro, cartacobrir,coberto)

    #Pega todas as cartas e suas coordenadas e desenha elas no quadro.     
    def desenhaquadro(quadro, carta):
        todas_as_estrelas.draw(tela)
        tela.blit(pygame.image.load_extended(f"{path}\\imagens\\dica.png"),(0,0))
        #Usa o numero de quantas cartas terão na horizontal e vertical e aplica suas coordenadas.
        for cartax in range(Nhor):
            for cartay in range(Nver):
                esquerda, cima = ecdacarta(cartax, cartay)
                #se a carta não foi revelada deixa coberta.
                if not carta[cartax][cartay]:
                    pygame.draw.rect(tela,(255,255,255), ((esquerda+quarto),(cima+quarto), tamcarta, tamcarta))
                else:
                    #pega uma coordenada, adiciona uma letra e desenha
                    letra = getletra(quadro, cartax, cartay)
                    desenhaicone(letra, cartax, cartay)

    #Inicia o jogo   
    def iniciojogo(quadro):
        tela.blit(escola,(0,0))
        #cartas iniciam cobertas
        cartarevelada = cartarevelação(False)
        cartas = []
        for x in range(Nhor):
            for y in range(Nver):
                cartas.append((x,y))

        #desenha as cartas(cobertas) a partir da função desenhaquadro
        desenhaquadro(quadro,cartarevelada)

        #Frases dos tutoriais
        frases = []
        frases.append((fonte1.render('Então, vamos la!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\tutorial\\1.ogg")))
        frases.append((fonte1.render('Atrás dessas cartas brancas temos letras escondidas', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\tutorial\\2.ogg")))
        frases.append((fonte1.render('Se conseguirmos achar 2 cartas com a mesma letra', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\tutorial\\3.ogg")))
        frases.append((fonte1.render('Iremos conhecer diversas coisas legais e mais uma bela estrelinha!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\tutorial\\4.ogg")))
        frases.append((fonte1.render('Então, quando as cartas se virarem, olhe para elas e tente memorizar onde as letras estão... ok?', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\tutorial\\5.ogg")))
        frases.append((fonte1.render('Vamos lá! ', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\tutorial\\6.ogg")))
        frases.append((fonte1.render('Muito bem, agora vamos ao jogo!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\tutorial\\7.ogg")))
        frases.append(('',''))
        i = 0
        pygame.mixer.Sound.set_volume(frases[i][1],0.4)
        pygame.mixer.Sound.play(frases[i][1])
        while i< len(frases):
            if i < 5:
                tela.blit(eufalando,(680,480))
                tela.blit(coisinho,(0,675))
                tela.blit(frases[i][0],(15,695))
                if pygame.mixer.get_busy()== False:
                        tela.blit(proximo,(920,760))
                
            elif i==5:
                #Revela todas as cartas
                revelarcarta(quadro, cartas)
                tela.blit(eufeliz,(680,480))
                tela.blit(coisinho,(0,675))
                tela.blit(frases[i][0],(15,695))
                if pygame.mixer.get_busy()== False:
                        tela.blit(proximo,(920,760))
            elif i==6:
                tela.blit(eufalando,(680,480))
                tela.blit(coisinho,(0,675))
                tela.blit(frases[i][0],(15,695))
                tela.blit(proximo,(920,760))
                pygame.time.wait(1000)
                #Cobre novamente todas as cartas
                cobrircarta(quadro, cartas,cartarevelada)
                pygame.display.update()
                i+=1

            if pygame.event.peek(QUIT)==True:
                pygame.mixer.stop()
                return exp
            if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0)):
                    if pygame.mixer.get_busy()== False:
                        pygame.mixer.Sound.play(somBotao)
                        i+=1
                        if i<7:
                            pygame.mixer.Sound.set_volume(frases[i][1],0.4)
                            pygame.mixer.Sound.play(frases[i][1])
                    pygame.event.clear()

            pygame.display.update()

    #Sons do instrutor
    def somtutorial(i):
        somtutorial = []
        somtutorial.append(pygame.mixer.Sound(f"{path}\\sons\\escolha\\1.ogg"))
        somtutorial.append(pygame.mixer.Sound(f"{path}\\sons\\escolha\\2.ogg"))
        somtutorial.append(pygame.mixer.Sound(f"{path}\\sons\\escolha\\3.ogg"))
        pygame.mixer.Sound.set_volume(somtutorial[i],0.4)
        pygame.mixer.Sound.play(somtutorial[i])

    #Frases do instrutor
    def frasetutorial(contador):
        frases = []
        frases.append(fonte1.render('Oi! Vamos nos divertir no jogo da memória?', True, (0,0,0)))
        frases.append(fonte1.render('Primeiro vamos escolher o que iremos aprender hoje!', True, (0,0,0)))
        frases.append(fonte1.render('escolha entre "animal" ou "fruta"', True, (0,0,0)))

        
        if contador == 0 :
            tela.blit(euoi,(680,480))
            
        else:
            tela.blit(eufalando,(680,480))
        tela.blit(coisinho,(0,675))
        tela.blit(frases[contador],(15,695))
        if pygame.mixer.get_busy()== False:
                    tela.blit(proximo,(920,760))
    #Frases de elogios
    def fraseselogio():
        frases = []
        frases.append((fonte1.render('Que perfeito!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\elogios/perfeito.ogg")))
        frases.append((fonte1.render('ótima jogada, parabéns!!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\elogios/jogada.ogg")))
        frases.append((fonte1.render('Acertou! Você foi incrível!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\elogios/incrivel.ogg")))
        frases.append((fonte1.render('Muito bem!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\elogios/muitobem.ogg")))

        oo = True
        rando = random.choice(frases)
        pygame.mixer.Sound.set_volume(rando[1],0.4)
        pygame.mixer.Sound.play(rando[1])
        while oo:
            tela.blit(euoi,(720,480))
            tela.blit(estrela1,(680,480))
            tela.blit(coisinho,(0,675))
            tela.blit(rando[0],(15,695))
            if pygame.mixer.get_busy()== False:
                tela.blit(proximo,(920,760))
            pygame.display.update()
            if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0)) and pygame.mixer.get_busy()== False:
                    pygame.mixer.Sound.play(somBotao)
                    pygame.event.clear()
                    oo = False
    #Frases de erros
    def fraseserro():
        frases = []
        frases.append((fonte1.render('ops, tente de novo!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Ops.ogg")))
        frases.append((fonte1.render('quase!! tente novamente!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Quase.ogg")))
        frases.append((fonte1.render('Não são iguais, tente de novo!!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Nãoiguais.ogg")))
        frases.append((fonte1.render('Diferentes... Mas sem problemas, vc consegue!!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Diferentes.ogg")))
        oo = True
        rando = random.choice(frases)
        pygame.mixer.Sound.set_volume(rando[1],0.4)
        pygame.mixer.Sound.play(rando[1])
        while oo:
            if pygame.mixer.get_busy()== False:
                tela.blit(proximo,(920,760))
            pygame.display.update()
            if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0)) and pygame.mixer.get_busy()== False:
                    pygame.mixer.Sound.play(somBotao)
                    pygame.event.clear()
                    oo = False
            tela.blit(eutriste,(680,480))
            tela.blit(coisinho,(0,675))
            tela.blit(rando[0],(15,695))

    #Responsavel por mostrar o trofeu apos todas as cartas serem reveladas
    def ganhar():
        tela.blit(euoi,(680,480))
        tela.blit(coisinho,(0,675))
        tela.blit(trofeu,(660,150))
        oo = True
        while oo:
            pygame.display.update()
            if pygame.event.peek(QUIT)==True:
                    return exp
            if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0)):
                    pygame.event.clear()
                    oo = False
                    pygame.time.wait(2000)
                    return exp
        pygame.display.update()

    #Checa se todas as cartas foram descobertas
    def GANHOU(cartarevelada):
        for i in cartarevelada:
            if False in i:
                return False
        return True

    #Utilizado para revelar as cartas novamente caso necessario
    def cobrir2(quadro,cartass):
        cartas = []
        for x in range(Nhor):
            for y in range(Nver):
                cartas.append((x,y))

        revelarcarta(quadro, cartas)
        pygame.time.wait(2000)
        if not cartass:
            cobrircarta(quadro, cartas,cartass)
            
                
    #variaveis do jogo
    Nhor = 4 # numero de cartas horizontal
    Nver = 3 # numero de cartas vertical
    tamcarta = 75 #tamanho da carta
    quarto = int(tamcarta*0.25) #variaveis de ajustes
    meio = int(tamcarta*0.5)#variaveis de ajustes
    gap = 50 #gap entre cartas
    margemx = int((largura - (Nhor*(tamcarta+gap)))/6)
    margemy = int((altura - (Nver*(tamcarta+gap)))/3)
    euoi = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\Personagem2acenando.png")), (272,195)),True,False)
    eufalando = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\Personagem2-falando.png")), (272,195)),True,False)
    eutriste = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\Personagem-2sorrindo.png")), (272,195)),True,False)
    eufeliz = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\feliz.png")), (272,195)),True,False)
    coisinho = pygame.image.load_extended(f"{path}\\imagens\\coisinho.png")
    proximo = pygame.image.load_extended(f"{path}\\imagens\\proximo.png")
    estrela1 = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\estrela.png")), (75,75))
    azul = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\vermelho.png"),(75,75))
    escola = pygame.image.load_extended(f"{path}\\imagens\\escola.png")
    trofeu = pygame.image.load_extended(f"{path}\\imagens\\trofeu.png")
    joysticks = pygame.image.load_extended(f"{path}\\imagens\\inicio.png")
    closeIMG = pygame.image.load_extended(f"{path}\\imagens\\fechar.png")

    #sons
    somEscolha=pygame.mixer.Sound(f"{path}\\sons\\selecionar.ogg")
    pygame.mixer.Sound.set_volume(somEscolha,0.05)
    somConfirmar=pygame.mixer.Sound(f"{path}\\sons\\confirmar.ogg")
    pygame.mixer.Sound.set_volume(somConfirmar,0.05)
    somBotao=pygame.mixer.Sound(f"{path}\\sons\\butao.ogg")
    pygame.mixer.Sound.set_volume(somBotao,0.05)
    somStar=pygame.mixer.Sound(f"{path}\\sons\\star2.ogg")
    pygame.mixer.Sound.set_volume(somStar,0.05)

    #animais
    aguia = pygame.image.load_extended(f"{path}\\imagens\\animal\\aguia.png")
    borboleta = pygame.image.load_extended(f"{path}\\imagens\\animal\\borboleta.png")
    coruja = pygame.image.load_extended(f"{path}\\imagens\\animal\\coruja.png")
    leão = pygame.image.load_extended(f"{path}\\imagens\\animal\\leão.png")
    elefante = pygame.image.load_extended(f"{path}\\imagens\\animal\\elefante.png")
    gato = pygame.image.load_extended(f"{path}\\imagens\\animal\\gato.png")
    guaxinim = pygame.image.load_extended(f"{path}\\imagens\\animal\\guaxinim.png")
    macaco = pygame.image.load_extended(f"{path}\\imagens\\animal\\macaco.png")
    panda = pygame.image.load_extended(f"{path}\\imagens\\animal\\panda.png")
    tartaruga = pygame.image.load_extended(f"{path}\\imagens\\animal\\tartaruga.png")

    #fruta
    abacaxi = pygame.image.load_extended(f"{path}\\imagens\\fruta\\abacaxi.png")
    banana = pygame.image.load_extended(f"{path}\\imagens\\fruta\\banana.png")
    cereja = pygame.image.load_extended(f"{path}\\imagens\\fruta\\cereja.png")
    kiwi = pygame.image.load_extended(f"{path}\\imagens\\fruta\\kiwi.png")
    laranja = pygame.image.load_extended(f"{path}\\imagens\\fruta\\laranja.png")
    maça = pygame.image.load_extended(f"{path}\\imagens\\fruta\\maça.png")
    morango = pygame.image.load_extended(f"{path}\\imagens\\fruta\\morango.png")
    pera = pygame.image.load_extended(f"{path}\\imagens\\fruta\\pera.png")
    uva = pygame.image.load_extended(f"{path}\\imagens\\fruta\\uva.png")

    #letras
    A = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\A.png"),(75,75))
    B = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\B.png"),(75,75))
    C = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\C.png"),(75,75))
    E = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\E.png"),(75,75))
    G = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\G.png"),(75,75))
    K = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\K.png"),(75,75))
    L = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\L.png"),(75,75))
    M = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\M.png"),(75,75))
    P = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\P.png"),(75,75))
    T = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\T.png"),(75,75))
    U = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\U.png"),(75,75))

    #animais = [aguia, borboleta, letrauja, leão, elefante, gato]
    letrasAn = [A, B, C, E, G, L, M, P, T]
    letrasFr = [A, B, C, K, L, M, P, U]
    letraFrM = [maça, morango]
    letraAmG = [gato, guaxinim]
    assert len(letrasAn)*len(letrasAn)*2 >= Nhor*Nver
    todas_as_estrelas = pygame.sprite.Group()
    estrelas = estrela()
    todas_as_estrelas.add(estrelas)
    
    xc = 101
    yc = 159
    iniciar = False
    fechar = True
    close = False
    inicializar = True
    inicfechar= False
    
    while inicializar:
        tela.fill((0,0,0))
        tela.blit(joysticks,(0,0))
        tela.blit(proximo,(920,760))
        for event in pygame.event.get():
            if event.type == QUIT:
                return exp
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or joystick.get_button(0):
                    pygame.mixer.Sound.play(somConfirmar)
                    pygame.event.clear()
                    inicfechar= True
                    inicializar = False
        pygame.display.update()
    while inicfechar:
        tela.fill((0,0,0))
        tela.blit(closeIMG,(0,0))
        tela.blit(proximo,(920,760))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.stop()
                return exp
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or joystick.get_button(0):
                    pygame.mixer.Sound.play(somConfirmar)
                    pygame.event.clear()
                    inicfechar= False
                    iniciar = True
        pygame.display.update()
    fonte = pygame.font.SysFont('arial', 40, True, False)
    ganhou=fonte.render('GANHOU TUDO', True, (255,0,255))
    escolha1=fonte.render('ANIMAL', True, (255,255,255))
    escolha2=fonte.render('FRUTA', True, (255,255,255))
    tipo = ''
    escolha1xy = (150,400)
    escolha2xy = (150,500)
    brancoxy = (escolha1xy[0]-75,escolha1xy[1])
    branco2 = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\seta.png"),(76,42))
    conto = 0
    tutu = True
    contador = 0
    somtutorial(contador)
    
    while iniciar:
        tela.fill((0,0,0))
        tela.blit(escola,(0,0))
        tela.blit(escolha1,escolha1xy)
        tela.blit(escolha2,escolha2xy)
        tela.blit(branco2,brancoxy)
        
        #frasetutorial(contador)
        frasetutorial(contador)
        if pygame.event.peek(QUIT)==True:
            pygame.mixer.stop()
            return exp

        if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
            if (pygame.key.get_pressed()[K_DOWN]==True) or joystick.get_button(12):
                pygame.event.clear()
                pygame.mixer.Sound.play(somEscolha)
                brancoxy = (escolha2xy[0]-75,escolha2xy[1])
            if (pygame.key.get_pressed()[K_UP]==True) or  joystick.get_button(11):
                pygame.event.clear()
                pygame.mixer.Sound.play(somEscolha)
                brancoxy = (escolha1xy[0]-75,escolha1xy[1])
            if (pygame.key.get_pressed()[K_SPACE]==True) or joystick.get_button(0):
                pygame.event.clear()
                if contador < 2:
                    if pygame.mixer.get_busy()== False:
                        pygame.mixer.Sound.play(somBotao)
                        contador=contador+1
                        somtutorial(contador)
                else:
                    pygame.mixer.Sound.play(somConfirmar)
                    if brancoxy == (escolha1xy[0]-75,escolha1xy[1]):
                        tipo = 'animal'
                    elif brancoxy == (escolha2xy[0]-75,escolha2xy[1]):
                        tipo = 'fruta'
                    
                    fechar = False
                    iniciar = False
        pygame.display.update()     
                
    #chamadas de funções para o inicio do jogo
    principalquadro=cartarandomica(tipo)
    cartarevelação1 = cartarevelação(False)                
    selecionado = None
    iniciojogo(principalquadro)

    while not fechar:

        tela.fill((0,0,0))
        tela.blit(escola,(0,0))
        pygame.draw.rect(tela,(255,255,0),(xc-5,yc-5,tamcarta+10,tamcarta+10))
        desenhaquadro(principalquadro, cartarevelação1)
        espaço = False
        if pygame.event.peek(QUIT)==True:
                    return exp
        if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
            if (pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0)):
                pygame.mixer.Sound.play(somConfirmar) 
                pygame.event.clear()
                espaço = True
            if pygame.key.get_pressed()[K_a]==True:
                cobrir2(principalquadro,cartarevelação1)
                pygame.event.clear()

            #Vai para carta a direita
            if pygame.key.get_pressed()[K_RIGHT]==True or  joystick.get_button(14):
                pygame.mixer.Sound.play(somEscolha)
                pygame.event.clear()
                if xc<=Nhor*margemx+tamcarta:
                    xc+=125
            if (pygame.key.get_pressed()[K_LEFT]==True or  joystick.get_button(13)):
                pygame.mixer.Sound.play(somEscolha)
                pygame.event.clear()
                if xc>=gap+margemx:
                    pygame.mixer.Sound.play(somEscolha)
                    xc-=125
            if (pygame.key.get_pressed()[K_DOWN]==True or  joystick.get_button(12)):
                pygame.event.clear()
                if yc>=margemy and yc<=Nver*(margemy)+tamcarta:
                    pygame.mixer.Sound.play(somEscolha)
                    yc+=gap+125      
            if (pygame.key.get_pressed()[K_UP]==True or joystick.get_button(11)):
                pygame.mixer.Sound.play(somEscolha)
                pygame.event.clear()
                if yc>=margemy+(tamcarta) and yc<=margemy*Nver+tamcarta+gap:
                    yc-=(125+gap)
                    
        
        if GANHOU(cartarevelação1):
            desenhaquadro(principalquadro, cartarevelação1)
            ganhar()
            pygame.display.update()
            return exp
        #Passa as coordenadas da carta pega para 2 variaeis
        cartax, cartay = pegarcarta(xc, yc)
        #Checa se não existe valor e se a carta ja foi relevada ou não
        if cartax != None and cartay != None  :
            if not cartarevelação1[cartax][cartay] and espaço:
                revelarcarta(principalquadro,[(cartax,cartay)])
                cartarevelação1[cartax][cartay]=True
                #Se é a primeira carta a ser selecionada, vai para outra variavel
                if selecionado == None:
                    selecionado =(cartax, cartay)
                    print(selecionado)
                else:
                    #Checa se as letras são iguais ou diferentes
                    letra1 = getletra(principalquadro,selecionado[0],selecionado[1])
                    letra2 = getletra(principalquadro, cartax, cartay)
                    if letra1 != letra2:
                        fraseserro()
                        pygame.time.wait(1000)
                        cobrircarta(principalquadro,[(selecionado[0],selecionado[1]),(cartax,cartay)],cartarevelação1)
                        cartarevelação1[selecionado[0]][selecionado[1]]= False
                        cartarevelação1[cartax][cartay] = False
                        pygame.event.clear()
                    #Se são iguais irá mostrar o animal ou fruta referente a letra        
                    elif letra1==letra2:
                        conto+=1
                        pygame.mixer.Sound.play(somStar)
                        if tipo == 'animal':
                            if letra1 == A:
                                tela.blit(aguia,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == B:
                                tela.blit(borboleta,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == C:
                                tela.blit(coruja,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == L:
                                tela.blit(leão,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == E:
                                tela.blit(elefante,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == G:
                                tela.blit(random.choice(letraAmG),(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == M:
                                tela.blit(macaco,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == P:
                                tela.blit(panda,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == T:
                                tela.blit(tartaruga,(660,150))
                                pygame.display.update()
                                fraseselogio()
                            estrelas.update()

                        if tipo =='fruta':
                            if letra1 == A:
                                tela.blit(abacaxi,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == B:
                                tela.blit(banana,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == C:
                                tela.blit(cereja,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == L:
                                tela.blit(laranja,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == K:
                                tela.blit(kiwi,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == M:
                                tela.blit(random.choice(letraFrM),(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == P:
                                tela.blit(pera,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            elif letra1 == U:
                                tela.blit(uva,(665,150))
                                pygame.display.update()
                                fraseselogio()
                            estrelas.update()
                                    

                    selecionado = None 
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    return exp
Jogar(1,1)


