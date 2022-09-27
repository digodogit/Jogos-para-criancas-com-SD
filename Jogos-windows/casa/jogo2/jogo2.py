import pygame
from pygame.locals import*
from sys import exit
import random
import time
from pygame import mouse


def Jogar(ids, exp):
    pygame.init()
    largura=1000
    altura=800
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("prototipo")
    clock = pygame.time.Clock()
    path = sys._MEIPASS
    
    #variaveis 
    fonte = pygame.font.SysFont('arial', 40, True, False)
    brinquedos = False
    principal = False
    ganhou = False
    cores =["verde","azul","vermelho"]
    trofeu = pygame.image.load_extended(f"{path}\\imagens\\trofeu.png")
    class imagens(object):
    
        def __init__(self,nome, position, imagem, cor):
            self.imagem = imagem
            self.position = position
            self.cor = cor
            self.nome = nome
            self.rect = imagem.get_rect()
            self.rect.topleft = self.position
            self.moving = False
            self.start = position

    class logica(object):
        flagA = 0
        flagV = 0
        flagVe = 0
        moving = False
        countFrase = 0
        countFraseBrin = 0
        countFrasePos = 0
        countFraseGanhou = 0
        verde = Rect(50, 165, 250, 50)
        azul = Rect(50, 450, 250, 50)
        vermelho = Rect(50, 315, 250, 50)
        estrela = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\estrela.png")), (75,75))
        trofeu = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\trofeu.png")), (75,75))
        trofeu2 = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\trofeu2.png")), (75,75))
        coisinho = pygame.image.load_extended(f"{path}\\imagens\\coisinho.png")
        proximo = pygame.image.load_extended(f"{path}\\imagens\\proximo.png")
        def __init__(self):
            self.imagem = []
            self.count = []
            
        def cria_imagem (self):
            self.imagem.append(imagens("bola",(300,550),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\bola.png")), (90,90)), "verde"))
            self.imagem.append(imagens("dinossauro",(375,600),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\dino.png")), (90,90)), "azul"))
            self.imagem.append(imagens("robô",(450,475),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\robo.png")), (90,90)), "vermelho"))
            self.imagem.append(imagens("foguete",(600,650),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\foguete.png")), (90,90)), "verde"))
            self.imagem.append(imagens("cubo",(155,500),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\cubo.png")), (90,90)), "verde"))
            self.imagem.append(imagens("boneca",(650,450),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\boneca.png")), (90,90)), "azul"))
            self.imagem.append(imagens("coroa",(600,525),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\coroa.png")), (90,90)), "azul"))
            self.imagem.append(imagens("guitarra",(200,650),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\guitarra.png")), (90,90)), "vermelho"))
            self.imagem.append(imagens("carro",(100,550),pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\carro.png")), (90,90)), "vermelho"))
 
        def personagem(self, tipo):
            Falando = (pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\Personagem2-falando.png")), (272,195)))
            sorrindo = (pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\Personagem2-sorrindo.png")), (272,195)))
            acenando = (pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\Personagem2-acenando.png")), (272,195)))
            feliz = (pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\Personagem2-feliz.png")), (272,195)))
            if tipo == 'falando':
                return Falando 
            if tipo == 'sorrindo':
                return sorrindo
            if tipo == 'acenando':
                return acenando
            if tipo == 'feliz':
                return feliz

        def draw(self, screen, brinquedos, count):
            if brinquedos == True:
                for i in range(0, len(self.imagem)):
                    screen.blit(self.imagem[i].imagem, (self.imagem[i].rect[0],self.imagem[i].rect[1]))

                    if self.imagem[i].moving:
                        screen.blit(pygame.transform.smoothscale((self.imagem[i].imagem), (150,150)), (625,100))
                        vermelho = fonte.render(self.imagem[i].nome,True,(255,0,0))
                        verde = fonte.render(self.imagem[i].nome,True,(0,185,0))
                        azul = fonte.render(self.imagem[i].nome,True,(0,0,255))

                        if self.imagem[i].cor =="vermelho":
                            if len(self.imagem[i].nome)>5:
                                tela.blit(vermelho,(650,250))
                            else:
                                tela.blit(vermelho,(655,250))
                           
                        elif self.imagem[i].cor =="verde":
                            if len(self.imagem[i].nome)>5:
                                tela.blit(verde,(650,250))
                            else:
                                tela.blit(verde,(655,250))
                            
                        elif self.imagem[i].cor =="azul":
                            if len(self.imagem[i].nome)>=5 and len(self.imagem[i].nome)<=7:
                                screen.blit(azul,(650,250))

                            elif len(self.imagem[i].nome)>7:
                                screen.blit(azul,(595,250))

                            elif len(self.imagem[i].nome)>0 and len(self.imagem[i].nome)<=4:
                                screen.blit(azul,(650,250))

                if self.flagV == 3:
                    screen.blit(self.estrela, (350,175))
                    
                if self.flagA == 3:
                    screen.blit(self.estrela, (350,465))
                    
                if self.flagVe == 3:
                    screen.blit(self.estrela, (350,330))
                    
                if len(count)>=9:
                        self.ganhou(self.countFrasePos,tela)

                if self.countFraseBrin<=10:
                    self.frasesBrin(self.countFraseBrin,screen)

            else:
                for i in range(0, len(self.imagem)):
                    if len(count) == 11:
                        screen.blit(self.trofeu2,(575,400))
                        self.frasesPos(self.countFrasePos,screen)
                        if self.imagem[i].cor == "verde":
                            screen.blit(pygame.transform.smoothscale(self.imagem[i].imagem,(50,50)), (180+self.imagem[i].rect.topleft[0]//2,320))
                        elif self.imagem[i].cor == "vermelho":
                            screen.blit(pygame.transform.smoothscale(self.imagem[i].imagem,(50,50)), (180+self.imagem[i].rect.topleft[0]//2,400))
                        elif self.imagem[i].cor == "azul":
                            screen.blit(pygame.transform.smoothscale(self.imagem[i].imagem,(50,50)), (180+self.imagem[i].rect.topleft[0]//2,475))
                    else:
                         screen.blit(pygame.transform.smoothscale(self.imagem[i].imagem,(75,75)), (self.imagem[i].rect.topleft[0]-100,self.imagem[i].rect.topleft[1]+50))
                         if self.countFrase<=6:
                            self.frases(self.countFrase,screen)
        def collide (self, cor, rect):
            if cor =="verde":
                return pygame.Rect.colliderect(rect,self.verde)

            if cor =="azul":
                return pygame.Rect.colliderect(rect,self.azul)

            if cor =="vermelho":
                return pygame.Rect.colliderect(rect,self.vermelho)

        def frases(self,count,screen):
            frases = []
            fonte1 = pygame.font.SysFont('arial', 20, True, False)
            frases.append(fonte1.render('Oi! Bem-vindo ao seu quarto! ', True, (0,0,0)))
            frases.append(fonte1.render('Nossa, os brinquedos estão todos fora do lugar, que bagunça!', True, (0,0,0)))
            frases.append(fonte1.render('Vamos guardar os brinquedos para quando formos brincar novamente?', True, (0,0,0)))
            frases.append(fonte1.render('Assim que tiver tudo organizado teremos uma bela recompensa!', True, (0,0,0)))
            frases.append(fonte1.render('Ótimo, vamos organizar!', True, (0,0,0)))
            frases.append(fonte1.render('Então, para começar, leve o mouse até o armário de brinquedos e clique nele.', True, (0,0,0)))
            if count <=5: 
                if count==0:
                    screen.blit(self.personagem('acenando'),(680,480))
                    screen.blit(self.coisinho,(0,675))

                if count>0 and count<=3 or count==5:
                    screen.blit(self.personagem('falando'),(680,480))
                    screen.blit(self.coisinho,(0,675))

                if count==4:
                    screen.blit(self.personagem('feliz'),(680,480))
                    screen.blit(self.coisinho,(0,675))

                screen.blit(frases[count],(15,695))
                if pygame.mixer.get_busy()== False:
                    screen.blit(self.proximo,(920,760))

        def frasesBrin(self,count,screen):
            frases = []
            fonte1 = pygame.font.SysFont('arial', 20, True, False)
            frases.append(fonte1.render('Agora, vamos organizar os brinquedos por cores?', True, (0,0,0)))
            frases.append(fonte1.render('O armário possui 3 espaços, cada um com uma cor, sendo elas:', True, (0,0,0)))
            frases.append(fonte1.render('Verde, vermelho e azul.', True, (0,0,0)))
            frases.append(fonte1.render('Em cada espaço cabe 3 brinquedos com a mesma cor.', True, (0,0,0)))
            frases.append(fonte1.render('O objetivo é completar os espaços do armário com esses brinquedos.', True, (0,0,0)))
            frases.append(fonte1.render('E assim, ganhar uma linda estrela por cada espaço completado!', True, (0,0,0)))
            frases.append(fonte1.render('Legal! Agora, para mover os brinquedos para o espaço certo, utilize o mouse!', True, (0,0,0)))
            frases.append(fonte1.render('Para isso, clique no brinquedo com o botão esquerdo do mouse e deixe pressionado.', True, (0,0,0)))
            frases.append(fonte1.render('E, com o botão pressionado, mova o mouse até o espaço de mesma cor do brinquedo.', True, (0,0,0)))
            frases.append(fonte1.render('Não se preocupe em errar, o importante é aprendermos a organizar!', True, (0,0,0)))
            frases.append(fonte1.render('Boa sorte e divirta-se!!', True, (0,0,0)))

            if count==0 or count == 5 or count==6:
                    screen.blit(self.personagem('feliz'),(680,480))
                    screen.blit(self.coisinho,(0,675))
            if (count>0 and count<=5) or (count>6 and count<10):
                    screen.blit(self.personagem('falando'),(680,480))
                    screen.blit(self.coisinho,(0,675))
            if count==10:
                    screen.blit(self.personagem('acenando'),(680,480))
                    screen.blit(self.coisinho,(0,675))
            screen.blit(frases[count],(15,695))
            if pygame.mixer.get_busy()== False:
                screen.blit(self.proximo,(920,760))

        def frasesPos(self,count,screen):
            frases = []
            fonte1 = pygame.font.SysFont('arial', 20, True, False)
            frases.append(fonte1.render('Parabéns, você organizou tudo! Merece uma recompensa!', True, (0,0,0)))
            frases.append(fonte1.render('Aqui está, um lindo troféu! Vamos voltar e colocá-lo no quarto!', True, (0,0,0)))
            frases.append(fonte1.render('Perfeito, olha que lindo ficou tudo organizado! Tudo pronto para brincar novamente!', True, (0,0,0)))
            frases.append(fonte1.render('Foi divertido, até a próxima! ', True, (0,0,0)))

            if count<=3:
                if count==0 or count==2:
                    screen.blit(self.personagem('feliz'),(680,480))
                    screen.blit(self.coisinho,(0,675))
                if count==1 or count==3:
                    screen.blit(self.personagem('acenando'),(680,480))
                    screen.blit(self.coisinho,(0,675))
                if pygame.mixer.get_busy()== False:
                    screen.blit(self.proximo,(920,760))
                screen.blit(frases[count],(15,695))

        def sons(self,count):
            sons = []
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\inicio\\1.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\inicio\\2.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\inicio\\3.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\inicio\\4.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\inicio\\5.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\inicio\\6.ogg"))
            if logica.countFrase<6:
                pygame.mixer.Sound.set_volume(sons[count],0.2)
                pygame.mixer.Sound.play(sons[count])
        def sonsPos(self,count):
            sons = []
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\pos\\1.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\pos\\2.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\pos\\3.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\pos\\4.ogg"))
            if count<4:
                pygame.mixer.Sound.set_volume(sons[count],0.2)
                pygame.mixer.Sound.play(sons[count])
        def sonsBrin(self,count):
            sons = []
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\1.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\2.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\3.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\4.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\5.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\6.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\7.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\8.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\9.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\10.ogg"))
            sons.append(pygame.mixer.Sound(f"{path}\\sons\\tutorial\\11.ogg"))
            if logica.countFraseBrin<11:
                pygame.mixer.Sound.set_volume(sons[count],0.2)
                pygame.mixer.Sound.play(sons[count])
        def Elogios(self,screen):
            fonte1 = pygame.font.SysFont('arial', 20, True, False)
            frasesons = []
            frasesons.append((fonte1.render('Está correto! Muito bem!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\elogios\\1.ogg")))
            frasesons.append((fonte1.render('Que lindo está ficando, continue assim!!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\elogios\\2.ogg")))
            frasesons.append((fonte1.render('Incrível, você está indo muito bem!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\elogios\\3.ogg")))
            rando = random.choice(frasesons)
            pygame.mixer.Sound.set_volume(rando[1],0.2)
            pygame.mixer.Sound.play(rando[1])
            oo=True
            while oo:
                pygame.display.flip()
                self.draw(tela,brinquedos,self.count) 
                screen.blit(self.personagem('feliz'),(680,480))
                screen.blit(self.coisinho,(0,675))
                screen.blit(rando[0],(15,695))
                if pygame.mixer.get_busy()== False:
                    screen.blit(self.proximo,(920,760))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.Sound.play(somBotao)
                        oo=False
                   
        def Erros(self,screen):
            fonte1 = pygame.font.SysFont('arial', 20, True, False)
            frasesons = []
            frasesons.append((fonte1.render('ops, tente de novo!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Ops.mp3")))
            frasesons.append((fonte1.render('quase!! tente novamente!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Quase.mp3")))
            frasesons.append((fonte1.render('Não são iguais, tente de novo!!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Nãoiguais.mp3")))
            frasesons.append((fonte1.render('Diferentes... Mas sem problemas, vc consegue!!', True, (0,0,0)),pygame.mixer.Sound(f"{path}\\sons\\erros\\Diferentes.mp3")))
            rando = random.choice(frasesons)
            pygame.mixer.Sound.set_volume(rando[1],0.2)
            pygame.mixer.Sound.play(rando[1])
            oo=True
            while oo:
                pygame.display.flip()
                self.draw(tela,brinquedos,self.count) 
                screen.blit(self.personagem('sorrindo'),(680,480))
                screen.blit(self.coisinho,(0,675))
                screen.blit(rando[0],(15,695))
                if pygame.mixer.get_busy()== False:
                    screen.blit(self.proximo,(920,760))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.Sound.play(somBotao)
                        oo=False
        def mouse_drag(self, screen):
            mouse_rel = mouse.get_rel()

            for i in range(0,len(self.imagem)):
                if self.imagem[i].moving == True:
                    self.imagem[i].rect.move_ip(mouse_rel)

                    if self.collide(self.imagem[i].cor,self.imagem[i].rect) and self.imagem[i].cor =="verde":
                        self.count.append([self.imagem[i].nome, self.imagem[i].cor,self.flagV])
                        self.imagem[i].moving = False
                        self.imagem[i].rect.topleft = 70+(30+self.verde[0])*self.flagV,15+self.verde[1]
                        self.flagV = self.flagV+1

                        if self.flagV ==3:
                            pygame.mixer.Sound.play(somStar)
                            if len(self.count)<=8:
                                self.Elogios(screen)

                        else:
                            pygame.mixer.Sound.play(somConfirmar)
                       
                    if self.collide(self.imagem[i].cor,self.imagem[i].rect) and self.imagem[i].cor =="azul":
                        self.count.append([self.imagem[i].nome, self.imagem[i].cor,self.flagA])
                        self.imagem[i].moving = False
                        self.imagem[i].rect.topleft = 70+(30+self.azul[0])*self.flagA,15+self.azul[1]
                        self.flagA = self.flagA+1
                        if self.flagA ==3:
                            pygame.mixer.Sound.play(somStar)
                            if len(self.count)<=8:
                                self.Elogios(screen)
                        else:
                            pygame.mixer.Sound.play(somConfirmar)

                    if self.collide(self.imagem[i].cor,self.imagem[i].rect) and self.imagem[i].cor =="vermelho":
                        self.count.append([self.imagem[i].nome, self.imagem[i].cor,self.flagVe])
                        self.imagem[i].moving = False
                        self.imagem[i].rect.topleft = 70+(30+self.vermelho[0])*self.flagVe,15+self.vermelho[1]
                        self.flagVe = self.flagVe+1     
                        if self.flagVe ==3:
                            pygame.mixer.Sound.play(somStar)
                            if len(self.count)<=8:
                                self.Elogios(screen)
                        else:
                            pygame.mixer.Sound.play(somConfirmar)
                        
        def mouse_button_down(self):
            mouse_pos = mouse.get_pos()

            for i in range(0,len(self.imagem)):
                if self.imagem[i].rect.collidepoint(mouse_pos):
                    if not self.collide(self.imagem[i].cor,self.imagem[i].rect):
                        self.imagem[i].start = (self.imagem[i].rect[0],self.imagem[i].rect[1])
                        self.imagem[i].moving = True
    
        def mouse_button_up(self, screen):
            for i in range(0,len(self.imagem)):
                if not self.collide(self.imagem[i].cor,self.imagem[i].rect): 
                        (self.imagem[i].rect[0],self.imagem[i].rect[1]) = self.imagem[i].start
                        self.imagem[i].moving = False
                        

        def ganhou(self, count, screen):
            self.frasesPos(self.countFrasePos,screen)
            if self.countFrasePos == 1:
                screen.blit(pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\trofeu.png")), (250,250)),(575,100))
                pygame.mixer.Sound.play(somStar)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mixer.get_busy()== False:
                    logica.countFrasePos=logica.countFrasePos+1
                    logica.sonsPos(logica.countFrasePos)
                    self.count.append('')
        
    modelo = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\modelo2.png")), (238*1.25,365*1.25))
    placa = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\placa.png")), (238*1.25,250//2))
    modelo2 = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\modelo22.png")), (238//1.5,365//1.5))
    placa2 = pygame.transform.smoothscale((pygame.image.load_extended(f"{path}\\imagens\\placa.png")), (238//1.5,250//3.5))
    recModelo = Rect(200, 300, 238//1.5,365//1.5)
    parede = pygame.image.load_extended(f"{path}\\imagens\\parede.png")
    parede2 = pygame.image.load_extended(f"{path}\\imagens\\parede2.png")
    joysticks = pygame.image.load_extended(f"{path}\\imagens\\inicio.png")
    closeIMG = pygame.image.load_extended(f"{path}\\imagens\\fechar.png")
    inicializar = True
    inicfechar= False
    
    #sons
    somEscolha=pygame.mixer.Sound(f"{path}\\sons\\selecionar.ogg")
    pygame.mixer.Sound.set_volume(somEscolha,0.05)
    somConfirmar=pygame.mixer.Sound(f"{path}\\sons\\confirmar.ogg")
    pygame.mixer.Sound.set_volume(somConfirmar,0.05)
    somBotao=pygame.mixer.Sound(f"{path}\\sons\\butao.ogg")
    pygame.mixer.Sound.set_volume(somBotao,0.05)
    somStar=pygame.mixer.Sound(f"{path}\\sons\\star2.ogg")
    pygame.mixer.Sound.set_volume(somStar,0.07)
    logica = logica()
    while inicializar:
        tela.fill((0,0,0))
        tela.blit(joysticks,(0,0))
        tela.blit(logica.proximo,(920,760))
        for event in pygame.event.get():
            if event.type == QUIT:
                return exp

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(somConfirmar)
                pygame.event.clear()
                inicfechar= True
                inicializar = False
        pygame.display.update()

    while inicfechar:
        tela.fill((0,0,0))
        tela.blit(closeIMG,(0,0))
        tela.blit(logica.proximo,(920,760))
        for event in pygame.event.get():
            if event.type == QUIT:
                return exp
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(somConfirmar)
                pygame.event.clear()
                inicfechar= False
                principal = True
        pygame.display.update()
    
    logica.cria_imagem()
    logica.sons(logica.countFrase)
    
    while principal:
        tela.fill((0,0,0))
        tela.blit(parede,(0,0))
        tela.blit(pygame.transform.smoothscale((modelo), (238//1.5,365//1.5)),(200,300))
        tela.blit(placa2, (200,215))
        logica.draw(tela,brinquedos,logica.count) 
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.stop()
                return exp
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
                if logica.countFrase<6 and pygame.mixer.get_busy()== False:
                    pygame.mixer.Sound.play(somBotao)
                    logica.countFrase=logica.countFrase+1
                    logica.sons(logica.countFrase)

                elif logica.countFrase==6  and len(logica.count)<11 and pygame.mixer.get_busy()== False:
                    mouse_rect = Rect(mouse_position[0],mouse_position[1],50,50) 
                    print (pygame.Rect.colliderect(mouse_rect,recModelo))
                    if pygame.Rect.colliderect(mouse_rect,recModelo):
                        pygame.mixer.Sound.play(somConfirmar)
                        principal = False
                        brinquedos = True
                        logica.sonsBrin(logica.countFraseBrin)
                        print(logica.countFrase)
                elif logica.countFrase==6  and len(logica.count)==11 and pygame.mixer.get_busy()== False:
                        logica.countFrasePos=logica.countFrasePos+1
                        logica.sonsPos(logica.countFrasePos)
                       
        pygame.display.flip()
        clock.tick(60)

        while brinquedos:
            tela.fill((0,0,0)) 
            tela.blit(parede2,(0,0))
            tela.blit(modelo, (50,135))
            tela.blit(placa, (50,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return exp

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if logica.countFraseBrin<11 and pygame.mixer.get_busy()==False:
                        pygame.mixer.Sound.play(somBotao)
                        logica.countFraseBrin=logica.countFraseBrin+1
                        logica.sonsBrin(logica.countFraseBrin)

                    elif logica.countFraseBrin==11:
                        pygame.mixer.Sound.play(somBotao)
                        logica.mouse_button_down()

                elif event.type == pygame.MOUSEBUTTONUP:
                    if len(logica.count)==8:
                        logica.sonsPos(logica.countFrasePos)
                    logica.mouse_button_up(tela)
                    

                elif  event.type==pygame.MOUSEMOTION:
                    logica.mouse_drag(tela)

            #print(len(logica.count))
            logica.draw(tela,brinquedos,logica.count)
            if len(logica.count) == 11:
                principal = True
                brinquedos = False
            pygame.display.flip()
            clock.tick(60)
    pygame.mixer.stop()
    pygame.quit()
    return exp
Jogar(1,1)

