import pygame
from pygame.locals import*
from sys import exit
import random

def Jogar(ids,exp):
    pygame.init()
    #configuraÃ§Ãµes da tela
    largura=1000
    altura=800
    tela = pygame.display.set_mode((largura,altura))
    fonte = pygame.font.SysFont('arial', 20, True, False)
    fonte1 = pygame.font.SysFont('arial', 20, True, False)
    limpou=fonte.render('VOCÊ GANHOU UMA ESTRELA!!', True, (255,0,255))

    #clock do jogo
    clock = pygame.time.Clock()
    
    path = "casa/jogo1/"
    eu = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/Personagem2 - feliz.png")), (272,195)),True,False)
    euoi = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/Personagem2acenando.png")), (272,195)),True,False)
    eufalando = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/Personagem2-falando.png")), (272,195)),True,False)
    eutriste = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/Personagem-2sorrindo.png")), (272,195)),True,False)
    eufeliz = pygame.transform.flip(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/Personagem2 - feliz.png")), (272,195)),True,False)
    coisinho = pygame.image.load_extended(f"{path}imagens/coisinho.png")
    proximo = pygame.image.load_extended(f"{path}imagens/proximo.png")
    boca=pygame.image.load_extended(f"{path}imagens/boca.png")
    estrela1=pygame.transform.smoothscale(pygame.image.load_extended(f"{path}imagens/estrela.png"),(75,75))
    estrelavazio=pygame.transform.smoothscale(pygame.image.load_extended(f"{path}imagens/estrelavazio.png"),(75,75))
    parabens = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}imagens/parabens.png"),(200,50))
    trofeu=pygame.image.load_extended(f"{path}imagens/trofeu.png")
    pia=pygame.image.load_extended(f"{path}imagens/pia.png")
    seta=pygame.transform.flip(pygame.image.load_extended(f"{path}imagens/seta.png"),False,True)
    parede = pygame.image.load_extended(f"{path}imagens/parede.png")
    fundo = pygame.image.load_extended(f"{path}imagens/fundo.png")
    joysticks = pygame.image.load_extended(f"{path}imagens/inicio.png")
    closeIMG = pygame.image.load_extended(f"{path}imagens/fechar.png")
    #sons
    somEscolha=pygame.mixer.Sound("sons/selecionar.ogg")
    pygame.mixer.Sound.set_volume(somEscolha,0.05)
    somConfirmar=pygame.mixer.Sound("sons/confirmar.ogg")
    pygame.mixer.Sound.set_volume(somConfirmar,0.05)
    somBotao=pygame.mixer.Sound("sons/butao.ogg")
    pygame.mixer.Sound.set_volume(somBotao,0.05)
    somStar=pygame.mixer.Sound("sons/star2.ogg")
    pygame.mixer.Sound.set_volume(somStar,0.07)
    class personagem(object):
    
        def __init__(self):
            self.imagem = []
            self.numero =[]
        def criar_personagem(self):
            self.numero = ["2","3","4","5","6","7"]
            escolhido = random.choice(self.numero)
            self.imagem.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/personagens/{escolhido}/feliz.png")), (310,310)))
            self.imagem.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/personagens/{escolhido}/acenando.png")), (310,310)))
            self.imagem.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/personagens/{escolhido}/triste.png")), (310,310)))

        def desenhar(self, tela, gesto):
            if gesto == "feliz":
                tela.blit(self.imagem[0], (200,400))
            if gesto == "acenando":
                tela.blit(self.imagem[1], (400,400))
            if gesto == "triste":
                tela.blit(self.imagem[2], (600,400))


    class copo(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.sprites=[]
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/copovazio.png")), (90,85)))
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/copo.png")), (90,85)))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = 430, 515

        def update(self):
            self.atual += 1
            if self.atual == 1:
                self.image = self.sprites[1]
                self.rect.topleft = 300, 480
            elif self.atual== 2:
                self.image = self.sprites[0]
                self.rect.topleft = 430, 515
    class estrela(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.sprites=[]
            self.sprites.append(pygame.image.load_extended(f"{path}imagens/estrela0.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}imagens/estrela1.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}imagens/estrela2.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}imagens/estrela3.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}imagens/estrela4.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}imagens/estrela5.png"))
            self.sprites.append(pygame.image.load_extended(f"{path}imagens/estrela6.png")) 
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = 85, 50

        def update(self):
            self.atual += 1
            self.image = self.sprites[self.atual]
    class escova(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.sprites=[]
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/escovaver.png")), (80,120)))
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/escova.png")), (120,80)))
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/escova1.png")), (120,80)))
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/escova2.png")), (120,80)))
            #self.sprites.append(pygame.image.load_extended(f"{path}imagens/escova2.png"))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = 430, 480

        def update(self):
            self.atual += 1
            if self.atual == 1:
                self.image = self.sprites[self.atual]
                self.rect.topleft = 280, 475
            elif self.atual == 2:
                self.image = self.sprites[self.atual]
                self.rect.topleft = 280, 475
            elif self.atual == 3:
                self.rect.topleft = 310, 430
            elif self.atual == 4:
                self.image = self.sprites[3]
            elif self.atual >= 5:
                self.image = self.sprites[0]
                self.rect.topleft = 430, 480
            else:
                pass
        def updatevolta(self):
            self.atual -=1
            self.image = self.sprites[2]
        
        def frente(self):
            self.rect[0]+=20
            pygame.display.update()
        def tras(self):
            self.rect[0]-=20
            pygame.display.update()
    class pasta(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.sprites=[]
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/pasta.png")), (110,85)))
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/pastaab.png")), (110,85)))
            self.sprites.append(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}imagens/pastaab2.png")), (110,85)))
            #self.sprites.append(pygame.image.load_extended(f"{path}imagens/escova2.png"))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = 150, 512

        def update(self):
            self.atual += 1
            if self.atual == 1:
                self.image = self.sprites[self.atual]
                self.rect.topleft = 190, 450
            elif self.atual == 2:
                self.image = self.sprites[self.atual]
                self.rect.topleft = 190, 450
            elif self.atual == 3:
                self.image = self.sprites[0]
                self.rect.topleft = 150, 512
            elif self.atual == 4:
                self.rect.topleft = 150, 512
            else:
                pass

    fechar = True
    telaboca = False

    #instancias
    todas_as_escovas = pygame.sprite.Group()
    escovas = escova()
    todas_as_escovas.add(escovas)
    todas_as_pastas = pygame.sprite.Group()
    pastas = pasta()
    todas_as_pastas.add(pastas)
    todas_as_estrelas = pygame.sprite.Group()
    estrelas = estrela()
    todas_as_estrelas.add(estrelas)
    todas_os_copos = pygame.sprite.Group()
    copos = copo()
    todas_os_copos.add(copos)
    personagem = personagem()
    personagem.criar_personagem()
    nada = (pygame.image.load_extended(f"{path}imagens/nada.png"))
    tudo = []
    tudo.append((pygame.image.load_extended(f"{path}imagens/sujeiraesc.png"),"esquerda cima"))
    tudo.append((pygame.image.load_extended(f"{path}imagens/sujeiraesc.png"),"esquerda baixo"))
    tudo.append((pygame.image.load_extended(f"{path}imagens/sujeira.png"), "meio cima"))
    tudo.append((pygame.image.load_extended(f"{path}imagens/sujeira.png"), "meio baixo"))
    tudo.append((pygame.image.load_extended(f"{path}imagens/sujeiradir.png"),"direita cima"))
    tudo.append((pygame.image.load_extended(f"{path}imagens/sujeiradir.png"), "direita baixo"))

    count = 0
    fonte = pygame.font.SysFont('arial', 40, True, False)
    contador=fonte.render(f'ACERTOS: {count}', True, (255,0,255))
    sim = False
    stack = 0
    posx = 100
    posy = 100
    distancia = 75
    margem = int((800-(2*(100+distancia)))/2)
    vari=0

    def fraseselogio(count):
        frases = []
        frases.append((fonte1.render('Isso, Parabéns! vamos para o próximo! '  , True, (0,0,0)),pygame.mixer.Sound(f"{path}sons/elogios/parabens.mp3")))
        frases.append((fonte1.render('Muito bem! Os seus dentes estão ficando limpos! '  , True, (0,0,0)),pygame.mixer.Sound(f"{path}sons/elogios/muitobem.mp3")))  
        frases.append((fonte1.render('Você é incrível, continue limpando! '  , True, (0,0,0)),pygame.mixer.Sound(f"{path}sons/elogios/continue.mp3")))
        fim = fonte1.render('Demais! Você limpou tudo e coletou as estrelas, parabéns! '  , True, (0,0,0))
        fim2 = fonte1.render('Agora vamos pôr a escova de volta! '  , True, (0,0,0))
       
        oo = True
        rando = random.choice(frases)
        pygame.mixer.Sound.set_volume(rando[1],0.2)
        pygame.mixer.Sound.play(rando[1])
        while oo:
            pygame.display.update()
            if pygame.event.peek(KEYDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True) and pygame.mixer.get_busy()== False:
                    pygame.mixer.Sound.play(somBotao)
                    pygame.event.clear()
                    oo = False
            if pygame.mixer.get_busy()== False:
                tela.blit(proximo,(920,760))
            if count == 6:
                tela.blit(eufeliz,(680,480))
                tela.blit(coisinho,(0,675))
                tela.blit(fim,(15,695))
            if count==7:
                tela.blit(eufeliz,(680,480))
                tela.blit(coisinho,(0,675))
                tela.blit(fim,(15,695))
            else:
                tela.blit(eufeliz,(680,480))
                tela.blit(coisinho,(0,675))
                tela.blit(rando[0],(15,695))

    def somtutoboca(i):
        somtutorial = []
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/boca/2.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/boca/3.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/boca/4.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/boca/5.mp3"))
        pygame.mixer.Sound.set_volume(somtutorial[i],0.2)
        pygame.mixer.Sound.play(somtutorial[i])

    def frasetutorial(i):
        frases = [] 
        frases.append(fonte1.render('Nossa, está tudo sujo, vamos limpar?! '  , True, (0,0,0)))
        frases.append(fonte1.render('Ótimo! Para remover todas precisamos escolher a sujeira correta e mover a escova'  , True, (0,0,0)))
        frases.append(fonte1.render('utilize as setas do teclado para mover a escova e espaço para selecionar a sujeira'  , True, (0,0,0)))
        frases.append(fonte1.render('Cada vez que você limpar ganhará uma estrela! Não tenha medo em errar!'  , True, (0,0,0)))
        
        
        somtutoboca(i)
        while i< len(frases):
            if i == 0:
                tela.blit(euoi,(680,480))
                
            elif i>=0 and i<=2:
                tela.blit(eufalando,(680,480))
                
            elif i == 3:
                tela.blit(eufeliz,(680,480))
            
            tela.blit(coisinho,(0,675))
            tela.blit(frases[i],(15,695))
            if pygame.mixer.get_busy()== False:
                tela.blit(proximo,(920,760))
            pygame.display.flip()
            if pygame.event.peek(KEYDOWN)==True:
                    if (pygame.key.get_pressed()[K_SPACE]==True):
                        if pygame.mixer.get_busy()== False:
                            pygame.mixer.Sound.play(somBotao)
                            i+=1
                            if i<4:
                                somtutoboca(i)
                            elif i ==4:
                                pygame.event.clear()
                                return i
                        pygame.event.clear()

        
    def ganhou():
        frases = []
        frases.append(fonte1.render('Demais! Você limpou tudo e coletou as estrelas, parabéns! '  , True, (0,0,0)))
        frases.append(fonte1.render('Agora vamos pôr a escova de volta! '  , True, (0,0,0)))
        som = []
        som.append(pygame.mixer.Sound(f"{path}sons/elogios/demais.mp3"))
        som.append(pygame.mixer.Sound(f"{path}sons/elogios/volta.mp3"))
        i=0
        pygame.mixer.Sound.set_volume(som[i],0.2)
        pygame.mixer.Sound.play(som[i])
        oo = True
        while oo:
            if pygame.mixer.get_busy()== False:
                tela.blit(proximo,(920,760))
            pygame.display.update()
            if pygame.event.peek(KEYDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True) and pygame.mixer.get_busy()== False:
                    pygame.mixer.Sound.play(somBotao)
                    pygame.event.clear()
                    i=i+1
                    if i < 1:
                        pygame.mixer.Sound.play(som[i])
                    if i == 2:
                        oo = False


    def somtutorial(contador):
        somtutorial = []
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/1.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/2.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/3.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/4.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/5.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/6.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/7.mp3"))
        pygame.mixer.Sound.set_volume(somtutorial[contador],0.2)
        pygame.mixer.Sound.play(somtutorial[contador])

    def somtutorial1(contador):
        somtutorial = []
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/8.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/9.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/10.mp3"))
        somtutorial.append(pygame.mixer.Sound(f"{path}sons/tutorial/11.mp3"))
        pygame.mixer.Sound.set_volume(somtutorial[contador],0.2)
        pygame.mixer.Sound.play(somtutorial[contador])

    def iniciotutorial(contador):
        frases = []
        frases.append(fonte1.render('oi! Aqui iremos aprender a escovar os dentes! ', True, (0,0,0)))
        frases.append(fonte1.render('primeiro, vamos nos preparar! ', True, (0,0,0)))
        frases.append(fonte1.render('Para começar, vamos pegar a pasta de dente e abrir. ', True, (0,0,0)))
        frases.append(fonte1.render('Isso!! Agora vamos pegar a escova e levar para perto da pasta. ', True, (0,0,0)))
        frases.append(fonte1.render('Depois apertamos a pasta de dente em direção a escova (com pouca força!) ', True, (0,0,0)))
        frases.append(fonte1.render('Fácil né? Hora de levarmos a escova até os dentes! ', True, (0,0,0)))
        frases.append(fonte1.render('Perfeito, muito bem! Hora de escovar!', True, (0,0,0)))
        frases.append(fonte1.render('Após escovar precisamos limpar a boca com água! ', True, (0,0,0)))  
        frases.append(fonte1.render('Coloque um pouco de água na boca (sem engolir) ', True, (0,0,0)))
        frases.append(fonte1.render('Assim mesmo! Agora bocheche por 5 segundos e cuspa a água na pia! ', True, (0,0,0)))
        
        if contador == 0:
            tela.blit(euoi,(680,480))
        elif contador >= 1 and contador <=3:
            tela.blit(eufalando,(680,480))
        elif contador == 4:
            tela.blit(eufeliz,(680,480))
        else:
            tela.blit(eufalando,(680,480))
        tela.blit(coisinho,(0,675))
        tela.blit(frases[contador],(15,695))
        if pygame.mixer.get_busy()== False:
                    tela.blit(proximo,(920,760))
        
            
    def fraseserro():
        frases = []
        frases.append(fonte1.render('ops, vamos de novo!', True, (0,0,0)))
        frases.append(fonte1.render('quase! vamos de novo!', True, (0,0,0)))
        frases.append(fonte1.render('Não é essa sujeira, vamos de novo!', True, (0,0,0)))
        oo = True
        rando = random.choice(frases)
        while oo:
            if pygame.mixer.get_busy()== False:
                tela.blit(proximo,(920,760))
            pygame.display.update()
            if pygame.event.peek(KEYDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True):
                    pygame.mixer.Sound.play(somEscolha)
                    pygame.event.clear()
                    oo = False
            tela.blit(eutriste,(680,480))
            tela.blit(coisinho,(0,675))
            tela.blit(rando,(15,695))

    def final(): 
        parabens=fonte1.render('Aqui está sua recompensa!', True, (255,0,0))
        tela.blit(eu,(680,580))
        tela.blit(parabens,(480,150))
        tela.blit(trofeu,(680,200))

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
                if event.key == pygame.K_SPACE:
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
                return exp
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(somConfirmar)
                    pygame.event.clear()
                    inicfechar= False
                    fechar = False
        pygame.display.update()
    contar =0
    somtutorial(contar)
    while not fechar:
            tela.fill((0,0,0))
            tela.blit(parede,(0,0))
            if pygame.event.peek(QUIT)==True:
                return exp

            if pygame.event.peek(KEYDOWN)==True:
                if (pygame.key.get_pressed()[K_SPACE]==True):
                    if pygame.mixer.get_busy()== False:
                        pygame.mixer.Sound.play(somBotao)
                        if contar >6 and contar <10:
                            somtutorial1(contar-6)
                        contar+=1
                        if contar <7:
                            somtutorial(contar)
                        if contar > 2:
                        
                            if escovas.atual == 0 and pastas.atual == 1:
                                #telaboca = True
                                escovas.update()
                            elif escovas.atual == 0:
                                pastas.update()
                        
                            elif escovas.atual == 1:
                                escovas.update()
                                pastas.update()
                            elif escovas.atual == 2:
                                escovas.update()
                                pastas.update()
                                pygame.event.clear()
                            elif escovas.atual == 3 and pastas.atual == 3:
                                ran = random.choice(tudo)
                                countboca = 0
                                
                                telaboca = True
                            else:
                                if contar == 8:
                                    copos.update()
                                if contar ==9:
                                    copos.update()
                    
                    pygame.event.clear()
            print (f"{contar}")
            tela.blit(personagem.imagem[0], (190,290))
            tela.blit(pia,(150,510))
            todas_as_escovas.draw(tela)
            todas_os_copos.draw(tela)
            if contar < 10:
                iniciotutorial(contar)
            todas_as_pastas.draw(tela)
            todas_as_estrelas.draw(tela)
            if contar ==10:
                final()
            pygame.display.update()
            clock.tick(60)

            while telaboca:
                #contador=fonte.render(f'ACERTOS: {count}', True, (255,0,255))
                escolha=fonte.render(f'{ran[1]}', True, (255,255,255))
                tela.fill((0,0,0))
                tela.blit(fundo, (0,0))
                tela.blit(boca, (0,0))

                todas_as_estrelas.draw(tela)
                print(countboca)
                if count<6:
                    tela.blit(escolha, (375,175))
                sujeiras = []
                for x in range(3):
                    for y in range(2):
                         if ((x == 0 or x==2) and (y == 1)):
                            sujeiras.append(((x*(100+distancia)+margem),(y*(50+distancia)+margem+50)))
                         elif x==1:
                            sujeiras.append(((x*(100+distancia)+margem),(y*(75+distancia)+margem+75)))
                         else: 
                            sujeiras.append(((x*(100+distancia)+margem),(y*(50+distancia)+margem+50)))

                 
                for oi in range(len(sujeiras)):    
                    tela.blit(tudo[oi][0],sujeiras[oi])
                
                if pygame.event.peek(QUIT)==True:
                    return exp
                if pygame.event.peek(KEYDOWN)==True:
                    if pygame.key.get_pressed()[K_DOWN]==True:
                        pygame.mixer.Sound.play(somEscolha)
                        if vari%2 == 0:
                            vari += 1
                            pygame.event.clear()
                        else:
                            pass
                    elif pygame.key.get_pressed()[K_UP]==True:
                        pygame.mixer.Sound.play(somEscolha)
                        if vari%2 != 0:
                            vari -= 1
                            pygame.event.clear()
                        else:
                            pass
                    elif pygame.key.get_pressed()[K_RIGHT]==True:  
                        pygame.mixer.Sound.play(somEscolha)
                        if vari==4 or vari==5:
                            pass
                        else:
                            vari+=2
                            pygame.event.clear()
                    elif pygame.key.get_pressed()[K_LEFT]==True:
                        pygame.mixer.Sound.play(somEscolha)
                        if vari==0 or vari==1:
                            pass
                        else:
                            vari-=2
                            pygame.event.clear()

                    if (pygame.key.get_pressed()[K_SPACE]==True):
                        if escovas.rect[0]== sujeiras[vari][0]+50 and escovas.rect[1]==sujeiras[vari][1] and tudo[vari][1]==ran[1]:
                            pygame.mixer.Sound.play(somConfirmar)
                            pygame.event.clear()
                            escovas.update()
                            sim = True
                            
                            stack = 0
                        else: 
                            pygame.event.clear()
                            fraseserro()
                        
                            
                                      
                if ran[1]==None:
                    ran = random.choice(tudo)
                
                
                todas_as_escovas.draw(tela)
                escovas.rect[0] = sujeiras[vari][0]+50
                escovas.rect[1] = sujeiras[vari][1]
                
                if count >= 6:
                    escovas.update()
                    pastas.update()
                    ganhou()
                    print(escovas.atual)
                    somtutorial1(0)
                    telaboca = False

                pygame.display.update()
                if countboca < 3:
                    countboca = frasetutorial(countboca)
                clock.tick(60)

                while sim:
                    tela.fill((0,0,0))
                    tela.blit(fundo, (0,0))
                    tela.blit(boca, (0,0))
                    for oi in range(len(sujeiras)):
                        tela.blit(tudo[oi][0],sujeiras[oi])
                    todas_as_escovas.draw(tela)
                    tela.blit(estrelavazio,(837,260))
                    pygame.draw.rect(tela,(240,203,56),(850,350,50,100))
                    pygame.draw.rect(tela,(0,0,0),(855,355,40,90-stack*9))
                    if stack>=10:
                        tudo[vari] = (pygame.image.load_extended(f"{path}imagens/nada.png"),None)
                        pygame.mixer.Sound.play(somStar)
                        count+=1
                        tela.blit(estrela1,(837,260))
                        tela.blit(parabens,(795,190))
                        fraseselogio(count)
                        estrelas.update()
                        if count<6:
                                ran = random.choice(tudo)
                                escovas.updatevolta()
                        escovas.rect[0]= sujeiras[vari][0]+50
                        escovas.rect[1]= sujeiras[vari][1]
                        
                        sim = False
                        
                    if pygame.event.peek(KEYDOWN)==True:
                        if pygame.key.get_pressed()[K_RIGHT]==True:
                            if escovas.rect[0]<sujeiras[vari][0]+100:
                                escovas.frente()
                                stack+=1
                            pygame.event.clear()
                        if pygame.key.get_pressed()[K_LEFT]==True:
                            if escovas.rect[0]>sujeiras[vari][0]:
                                escovas.tras()
                                stack+=1
                            pygame.event.clear()
                    pygame.display.update()
                    clock.tick(60)
            

    pygame.quit()
    return exp

