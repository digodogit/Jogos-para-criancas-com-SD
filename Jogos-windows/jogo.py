import pygame
from pygame.locals import*
from sys import exit
from random import randint
import runpy
import os
import sys
import subprocess
pygame.init()
        
#configurações da tela
largura=1000
altura=800
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("joguinho")

#fonte
fonte = pygame.font.SysFont('arial', 40, True, False)
fonte1 = pygame.font.SysFont('arial', 20, True, False)

#clock do Jogo
clock = pygame.time.Clock()

#condição para o Jogo
fechar = False
amb = False
esc = False
cas = False
#variaveis pras coisas
cX=400
cY=700
selx=395
sely=400
tamcarta = 200
gap = 20
#sons
somEscolha=pygame.mixer.Sound("sons/selecionar.ogg")
pygame.mixer.Sound.set_volume(somEscolha,0.05)
somConfirmar=pygame.mixer.Sound("sons/confirmar.ogg")
pygame.mixer.Sound.set_volume(somConfirmar,0.05)
somBotao=pygame.mixer.Sound("sons/butao.ogg")
pygame.mixer.Sound.set_volume(somBotao,0.05)
somStar=pygame.mixer.Sound("sons/star2.ogg")
pygame.mixer.Sound.set_volume(somStar,0.05)
#classes
class Personagem:
    exp = 0
    ids = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ids = Personagem.ids
        Personagem.ids += 1
        
    def checkExp(self):
        return f"O personagem {self.nome} tem exatos: {self.exp} de experiência"
            
class Ambiente:
    fonte
    def __init__(self, nome,x,y):
        self.x = x
        self.y = y
        self.nome = nome
ambientes = []
ambientes.append(Ambiente("escola", 250, 200)) 
ambientes[0].fonte=fonte.render('ESCOLA', True, (255,100,100))
ambientes.append(Ambiente("casa", 550, 200))
ambientes[1].fonte=fonte.render('CASA', True, (255,100,100))
voltar = Ambiente("voltar", 400, altura-120)
voltar.fonte=fonte.render('VOLTAR', True, (255,100,100))
vol=(ambientes[0].x-10,ambientes[0].y-20)
class Jogo(Personagem):
    fonte
    
    def __init__(self, ambiente, nome, x, y):
        self.x = x
        self.y = y
        self.nome = nome
        self.ambiente = ambiente
    def Jogar(self, ambiente, nome, ids, exp):
        modulo = f"{self.ambiente}/{self.nome}/{self.nome}.exe"
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
        else:
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
        print(sys._MEIPASS)

        subprocess.Popen(modulo, cwd=sys._MEIPASS)
        #modulo=runpy.run_path(path_name=modulo)
	#Personagem.exp = modulo.Jogar(ids, exp)
jogos = []
jogos1=[]
#voltar.fonte=fonte.render('VOLTAR', True, (255,100,100))
jogos.append(Jogo(ambientes[0].nome,'jogo1', (largura/2)-40,(altura/2)))
jogos[0].fonte =fonte1.render('jogo 1', True, (255,0,0)) 
jogos.append(Jogo(ambientes[0].nome,'jogo2', 100,(altura/2)))
jogos[1].fonte =fonte1.render('jogo 2', True, (255,0,0))
jogos1.append(Jogo(ambientes[1].nome,'jogo1', (largura/2)-40,(altura/2)))
jogos1[0].fonte =fonte1.render('jogo 1', True, (255,0,0)) 
jogos1.append(Jogo(ambientes[1].nome,'jogo2', 100,(altura/2)))
jogos1[1].fonte =fonte1.render('jogo 2', True, (255,0,0))


eu = Personagem("personagem", 18)
eu1 = Personagem("dodoa", 18)
musica = pygame.mixer.music.load("sons\\music1.mp3")
pygame.mixer.music.set_volume(0.015)
pygame.mixer.music.play(-1)
seta = pygame.transform.smoothscale(pygame.image.load_extended("imagens/seta.png"),(76,42))
seta1 = pygame.transform.smoothscale(pygame.image.load_extended("imagens/seta1.png"),(42,76))
memoria = pygame.transform.smoothscale(pygame.image.load_extended("imagens/memoria.png"),(150,150))
dente = pygame.transform.smoothscale(pygame.image.load_extended("imagens/dente.png"),(150,150))
quarto = pygame.transform.smoothscale(pygame.image.load_extended("imagens/quarto.png"),(150,150))
escolaIMG = pygame.transform.smoothscale(pygame.image.load_extended("imagens/escola.png"),(200,200))
casaIMG = pygame.transform.smoothscale(pygame.image.load_extended("imagens/casa.png"),(200,200))
paredeEscola = pygame.image.load_extended("imagens/paredeEscola.png")
paredeCasa = pygame.image.load_extended("imagens/paredeCasa.png")
paredeAmbiente = pygame.image.load_extended("imagens/paredeAmbiente.png")
paredePrincipal = pygame.image.load_extended("imagens/paredePrincipal.png")
escolha1xy = (100,600)
escolha2xy = (100,660)
setaxy = (escolha1xy[0]-75,escolha1xy[1])

while not fechar:
    
    menu=fonte.render('MENU:', True, (255,0,255))
    ambiente=fonte1.render('Ambientes', True, (255,100,100))
    sair=fonte1.render('Sair', True, (255,100,100))
    tela.fill((0,0,0))
    tela.blit(paredePrincipal,(0,0))
    tela.blit(menu,((largura/15),altura/1.5))
    tela.blit(ambiente,escolha1xy)
    tela.blit(sair,escolha2xy)
    tela.blit(seta,setaxy)
    if pygame.event.peek(QUIT)==True:
            fechar = True
    if pygame.event.peek(KEYDOWN)==True:
            if pygame.key.get_pressed()[K_DOWN]==True:
                pygame.event.clear()
                pygame.mixer.Sound.play(somEscolha)
                setaxy = (escolha2xy[0]-75,escolha2xy[1])
            if pygame.key.get_pressed()[K_UP]==True:
                pygame.event.clear()
                pygame.mixer.Sound.play(somEscolha)
                setaxy = (escolha1xy[0]-75,escolha1xy[1])
            if pygame.key.get_pressed()[K_SPACE]==True:
                pygame.event.clear()
                pygame.mixer.Sound.play(somConfirmar)
                if setaxy == (escolha1xy[0]-75,escolha1xy[1]):
                    print ("ambiente selecionado")
                    azul=pygame.transform.smoothscale(pygame.image.load_extended("imagens/azul.png"),(220,220))
                    fechar=True
                    amb = True
                elif setaxy == (escolha2xy[0]-75,escolha2xy[1]):
                    print ("sair selecionado")
                    fechar = True

    pygame.display.update()
    clock.tick(60)

    while amb:
        Nhor = len(ambientes)
        tela.fill((0,0,0))
        tela.blit(paredeAmbiente,(0,0))
        if pygame.event.peek(QUIT)==True:
            fechar = True
            amb = False
           
        if pygame.event.peek(KEYDOWN)==True:
            if pygame.key.get_pressed()[K_RIGHT]==True:
                pygame.mixer.Sound.play(somEscolha)
                #to no ambiente escola
                if vol == (ambientes[0].x-10,ambientes[0].y-20):
                    vol = (ambientes[1].x-10,ambientes[1].y-20)
                pygame.event.clear()
            if pygame.key.get_pressed()[K_LEFT]==True:
                pygame.mixer.Sound.play(somEscolha)
                #to no ambiente casa
                if vol == (ambientes[1].x-10,ambientes[1].y-20):
                    vol = (ambientes[0].x-10,ambientes[0].y-20)
                pygame.event.clear()
            if pygame.key.get_pressed()[K_DOWN]==True:
                pygame.mixer.Sound.play(somEscolha)
                #to no ambiente escola
                if vol == (ambientes[0].x-10,ambientes[0].y-20) or vol == (ambientes[1].x-10,ambientes[1].y-20):
                    vol = (voltar.x-20,voltar.y-10)
                    azul = pygame.transform.smoothscale(pygame.image.load_extended("imagens/azul.png"),(200,60)) 
                pygame.event.clear()
                    
            if pygame.key.get_pressed()[K_UP]==True:
                pygame.mixer.Sound.play(somEscolha)
                if vol == (voltar.x-20,voltar.y-10):
                    vol = (ambientes[0].x-10,ambientes[0].y-20)
                    azul=pygame.transform.smoothscale(pygame.image.load_extended("imagens/azul.png"),(220,220))
                pygame.event.clear()
                    
            if pygame.key.get_pressed()[K_SPACE]==True:
                pygame.mixer.Sound.play(somConfirmar)
                #to no ambiente escola
                if vol == (ambientes[0].x-10,ambientes[0].y-20):
                    print ("escola selecionado")
                    seta1xy = (jogos[0].x-75,jogos[0].y)
                    esc = True
                    
                 #to no ambiente casa   
                elif vol == (ambientes[1].x-10,ambientes[1].y-20):
                    print ("casa selecionado")
                    seta1xy = (jogos[0].x-75,jogos[0].y)
                    cas = True
                    
                elif vol == (voltar.x-10,voltar.y-10):   
                    amb=False
                
                pygame.event.clear()
                
        #quadrados segunda tela
        tela.blit(azul,vol)
        tela.blit(escolaIMG,(ambientes[0].x,ambientes[0].y-10))
        tela.blit(casaIMG,(ambientes[1].x,ambientes[1].y-10))
        
        #textos
        tela.blit(ambientes[0].fonte,(ambientes[0].x,ambientes[0].y+200))
        tela.blit(ambientes[1].fonte,(ambientes[1].x,ambientes[1].y+200))
        tela.blit(voltar.fonte,(voltar.x,voltar.y))
        pygame.display.update()
        
        while esc:
            tela.fill((0,0,0))
            crashed = False
            tela.blit(paredeEscola,(0,0))
            xp = fonte1.render(eu.checkExp(), True, (255,255,255))
            if pygame.event.peek(QUIT)==True:
                esc = False
                amb = False
                fechar = True
                
            if pygame.event.peek(KEYDOWN)==True:
                if pygame.key.get_pressed()[K_SPACE]==True:
                    pygame.mixer.Sound.play(somConfirmar)
                    if seta1xy==(voltar.x,voltar.y+75):
                        pygame.event.clear()
                        esc= False
                        amb= True
                        
                    elif seta1xy==(jogos[0].x-75,jogos[0].y):
                        print("Jogo 1 selecionado")
                        print(jogos[0].nome)
                        pygame.event.clear()
                        jogos[0].Jogar(jogos[0].ambiente,jogos[0].nome, eu1.ids, eu1.exp)
                        eu.checkExp()
                        pygame.event.clear()     
                        
                if pygame.key.get_pressed()[K_UP]==True:
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy == (jogos[1].x-75,jogos[1].y):
                        pass
                        
                    elif seta1xy==(voltar.x,voltar.y+75):
                        seta1xy = (jogos[0].x-75,jogos[0].y)
               
                if pygame.key.get_pressed()[K_LEFT]==True:
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos[0].x-75,jogos[0].y):
                        seta1xy=(jogos[1].x-75,jogos[1].y)
                        
                        
                if pygame.key.get_pressed()[K_DOWN]==True:
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos[0].x-75,jogos[0].y):
                        seta1xy=(voltar.x,voltar.y+75)
                        
                    elif seta1xy==(jogos[2].x-75,jogos[2].y):
                        seta1xy=(jogos[1].x-75,jogos[1].y)
                    else:
                        pass
                    
                if pygame.key.get_pressed()[K_RIGHT]==True:
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos[1].x-75,jogos[1].y):
                        seta1xy=(jogos[0].x-75,jogos[0].y)
                pygame.event.clear()
                        
            #pygame.draw.polygon(tela, (255,255,255),tri,0)       
            tela.blit(seta1,(seta1xy[0]+75,seta1xy[1]-150))
            tela.blit(memoria,(jogos[0].x-50,jogos[0].y-75))
            tela.blit(voltar.fonte,(voltar.x,voltar.y))
            tela.blit(jogos[0].fonte,(jogos[0].x-40,jogos[0].y+90))
            tela.blit(xp, (100,750))
            pygame.display.update()

        while cas:
            tela.fill((0,0,0))
            crashed = False

            tela.blit(paredeCasa,(0,0))
            if pygame.event.peek(QUIT)==True:
                cas = False
                amb = False
                fechar = True
            if pygame.event.peek(KEYDOWN)==True:    
                if pygame.key.get_pressed()[K_UP]==True:
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(voltar.x,voltar.y+75):
                        seta1xy = (jogos1[0].x-75,jogos[0].y)
               
                if pygame.key.get_pressed()[K_LEFT]==True:
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos1[0].x-75,jogos[0].y):
                        seta1xy=(jogos1[1].x-75,jogos[1].y)
                        
                        
                if pygame.key.get_pressed()[K_DOWN]==True:
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos1[0].x-75,jogos[0].y):
                        seta1xy=(voltar.x,voltar.y+75)
                 
                if pygame.key.get_pressed()[K_RIGHT]==True:
                    if seta1xy==(jogos1[1].x-75,jogos[1].y):
                        seta1xy=(jogos1[0].x-75,jogos[0].y)
                        
            
                if pygame.key.get_pressed()[K_SPACE]==True:
                    pygame.mixer.Sound.play(somConfirmar)
                    if seta1xy==(voltar.x,voltar.y+75):
                        pygame.event.clear()
                        cas= False
                        amb= True
                        
                    elif seta1xy==(jogos1[0].x-75,jogos1[0].y):
                        print("Jogo 1 selecionado")
                        print(jogos1[0].nome)
                        pygame.event.clear()
                        jogos1[0].Jogar(jogos1[0].ambiente,jogos1[0].nome, eu1.ids, eu1.exp)
                        eu.checkExp()
                        pygame.event.clear() 

                    elif seta1xy==(jogos1[1].x-75,jogos1[1].y):
                        print("Jogo 2 selecionado")
                        print(jogos1[1].nome)
                        pygame.event.clear()
                        jogos1[1].Jogar(jogos1[1].ambiente,jogos1[1].nome, eu1.ids, eu1.exp)
                        eu.checkExp()
                        pygame.event.clear() 

            tela.blit(seta1,(seta1xy[0]+75,seta1xy[1]-150))
            tela.blit(dente,(jogos1[0].x-50,jogos1[0].y-75))
            tela.blit(voltar.fonte,(voltar.x,voltar.y))
            tela.blit(quarto,(jogos1[1].x-50,jogos1[1].y-75))
            tela.blit(jogos[0].fonte,(jogos[0].x-40,jogos[0].y+90))
            tela.blit(jogos[1].fonte,(jogos[1].x-40,jogos[1].y+90))
            pygame.display.update()
            

    
pygame.quit()

