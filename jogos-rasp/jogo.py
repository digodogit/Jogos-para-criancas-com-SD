import pygame
from pygame.locals import*
from sys import exit
from random import randint
import runpy
import os
import sys
import subprocess
import random
#Inicialização do pygame
pygame.init()

#Variaveis de largura e altura de tela
largura=1000
altura=800

#Inicialização do display de tela
tela = pygame.display.set_mode((largura,altura))

#Inicialização do Clock 
clock = pygame.time.Clock()
pygame.display.set_caption("prototipo: jogos para criança com SD")

#fonte
fonte = pygame.font.SysFont('arial', 40, True, False)
fonte1 = pygame.font.SysFont('arial', 20, True, False)
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    print(joystick.get_name()) 
    joystick.init()  

# Identificador da pasta onde o jogo esta rodando em .exe ou .py
if getattr(sys, 'frozen', False):
    path = sys._MEIPASS
else:
    path = os.path.dirname(os.path.abspath(__file__)) 

class joysticksFalso(object):
        def __init__(self):
            pass
        def get_button(self,numero):
            pass
if len(joysticks)==0:
    joystick = joysticksFalso()

#configurações da tela


#clock do Jogo


#condição para o Jogo
fechar = False
amb = False
esc = False
cas = False

#variaveis de posição
cX=400
cY=700
selx=395
sely=400
tamcarta = 200
gap = 20

#Informa qual som selecionar e passa para uma variavel
somEscolha=pygame.mixer.Sound(f"{path}\\sons\\selecionar.ogg")
#O mesmo para imagem, porem a função usada é diferente
paredeMenu = pygame.image.load_extended(f"{path}\\imagens\\menu.png")
pygame.mixer.Sound.set_volume(somEscolha,0.05)
somConfirmar=pygame.mixer.Sound(f"{path}\\sons\\confirmar.ogg")
pygame.mixer.Sound.set_volume(somConfirmar,0.05)
somBotao=pygame.mixer.Sound(f"{path}\\sons\\butao.ogg")
pygame.mixer.Sound.set_volume(somBotao,0.05)
somStar=pygame.mixer.Sound(f"{path}\\sons\\star2.ogg")
pygame.mixer.Sound.set_volume(somStar,0.05)
#classes
class Personagem(object):
    exp = 0
    ids = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ids = Personagem.ids
        Personagem.ids += 1
        
    def checkExp(self):
        return f"O personagem {self.nome} tem exatos: {self.exp} de experiência"

#Classe de ambiente           
class Ambiente(object):
    fonte = None
    def __init__(self, nome,x,y):
        self.x = x
        self.y = y
        self.nome = nome

#Instancia de ambientes atribuida a um vetor
ambientes = []
ambientes.append(Ambiente("escola", 250, 200)) 
ambientes[0].fonte=fonte.render('ESCOLA', True, (255,0,0))
ambientes.append(Ambiente("casa", 550, 200))
ambientes[1].fonte=fonte.render('CASA', True, (255,0,0))
voltar = Ambiente("voltar", 400, altura-120)
voltar.fonte=fonte.render('VOLTAR', True, (255,0,0))
vol=(ambientes[0].x-10,ambientes[0].y-20)

#Classe jogos
class Jogo(object):
    fonte
    #Construtor
    def __init__(self, ambiente, nome, x, y):
        self.x = x
        self.y = y
        self.nome = nome
        self.ambiente = ambiente
        
    #Função de abrir os jogos
    def Jogar(self):
        if getattr(sys, 'frozen', False):
            modulo = f"{self.ambiente}\\{self.nome}\\{self.nome}.exe"
            subprocess.Popen(modulo, cwd=path)
        else:
            
            modulo = f"{self.ambiente}\\{self.nome}\\{self.nome}.py"
            #Personagem.exp = modulo.Jogar(ids, exp)
            runpy.run_path(path_name=modulo)
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
def cria_brinquedos():
    imagemB=[]
    imagemB.append(pygame.image.load_extended(f"{path}\\imagens\\principal\\spark1.png"))
    imagemB.append(pygame.image.load_extended(f"{path}\\imagens\\principal\\spark2.png"))
    imagemB.append(pygame.image.load_extended(f"{path}\\imagens\\principal\\spark3.png"))
    imagemB.append(pygame.image.load_extended(f"{path}\\imagens\\principal\\estrela.png"))
    imagemB.append(pygame.image.load_extended(f"{path}\\imagens\\principal\\trofeu2.png"))
    for n in range(200): 
        xlar = random.randrange(0, largura) 
        ylar = random.randrange(0, 719) 
        size = random.randint(10,40)
        brinquedoIMG = pygame.transform.smoothscale(random.choice(imagemB), (size,size))
        brinquedinhos.append([xlar, ylar,brinquedoIMG]) 

brinquedinhos = []
def desenha_brinquedos(brinq):
    for i in brinq:
        i[2].set_alpha(150) 
        tela.blit(i[2],(i[0],i[1]))
        i[1] += 1
        if i[1] > 799: 
            ylar = random.randrange(-250, -5) 
            i[1] = ylar
            xlar = random.randrange(largura) 
            i[0] = xlar      
jogos = []
jogos1=[]
#voltar.fonte=fonte.render('VOLTAR', True, (255,100,100))
jogos.append(Jogo(ambientes[0].nome,'jogo1', (largura/2)-40,(altura/2)))
jogos[0].fonte =fonte1.render('jogo da memória', True, (255,0,0)) 
jogos.append(Jogo(ambientes[0].nome,'jogo2', 100,(altura/2)))
jogos[1].fonte =fonte1.render('jogo 2', True, (255,0,0))
jogos1.append(Jogo(ambientes[1].nome,'jogo1', (largura/2)-40,(altura/2)))
jogos1[0].fonte =fonte1.render('Escovar os dentes', True, (255,0,0)) 
jogos1.append(Jogo(ambientes[1].nome,'jogo2', 100,(altura/2)))
jogos1[1].fonte =fonte1.render('Arrumar o quarto', True, (255,0,0))


eu = Personagem("personagem", 18)
eu1 = Personagem("dodoa", 18)
musica = pygame.mixer.music.load(f"{path}\\sons\\music1.mp3")
pygame.mixer.music.set_volume(0.02)
pygame.mixer.music.play(-1)
seta = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\seta.png"),(76,42))
seta1 = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\seta1.png"),(42,76))
memoria = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\memoria.png"),(150,150))
dente = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\dente.png"),(150,150))
quarto = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\quarto.png"),(150,150))
escolaIMG = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\escola.png"),(200,200))
casaIMG = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\casa.png"),(200,200))
paredeEscola = pygame.image.load_extended(f"{path}\\imagens\\paredeEscola.png")
paredeCasa = pygame.image.load_extended(f"{path}\\imagens\\paredeCasa.png")
paredeAmbiente = pygame.image.load_extended(f"{path}\\imagens\\paredeAmbiente.png")
paredePrincipal = pygame.image.load_extended(f"{path}\\imagens\\paredePrincipal.png")
paredeMenu = pygame.image.load_extended(f"{path}\\imagens\\menu.png")
escolha1xy = (100,600)
escolha2xy = (100,660)
setaxy = (escolha1xy[0]-75,escolha1xy[1]-10)
cria_brinquedos()

while not fechar:
    #definição de variavel de fonte
    menu=fonte.render('OPÇÕES:', True, (255,0,255))
    ambiente=fonte1.render('Ambientes de jogos', True, (255,100,100))
    sair=fonte1.render('Sair', True, (255,100,100))
    tela.fill((0,0,0))
    #Aplica as imagens na tela
    tela.blit(paredePrincipal,(0,0))
    desenha_brinquedos(brinquedinhos)
    tela.blit(paredeMenu,(0,0))
    tela.blit(menu,((int(largura/15)),int(altura/1.5)))
    tela.blit(ambiente,escolha1xy)
    tela.blit(sair,escolha2xy)
    tela.blit(seta,setaxy)
    #Identifica um evento de fechar a tela
    if pygame.event.peek(QUIT)==True:
            fechar = True
    #Identifica um evento de teclado ou de controle
    if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
            #Identifica se o botão(seta) para baixo está sendo pressionado
            if pygame.key.get_pressed()[K_DOWN]==True or joystick.get_button(12):
                #limpa o buffer de eventos para não haver conflito
                pygame.event.clear()
                #Aciona o som de escolha                            
                pygame.mixer.Sound.play(somEscolha)
                #Mexe a seta de escolha             
                setaxy = (escolha2xy[0]-75,escolha2xy[1]-10)    

            if pygame.key.get_pressed()[K_UP]==True or joystick.get_button(11):
                pygame.event.clear()
                pygame.mixer.Sound.play(somEscolha)
                setaxy = (escolha1xy[0]-75,escolha1xy[1]-10)
            #Identifica se o espaço(teclado) está sendo pressionado
            if pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0):
                pygame.event.clear()
                pygame.mixer.Sound.play(somConfirmar)

                if setaxy == (escolha1xy[0]-75,escolha1xy[1]-10):
                    print ("ambiente selecionado")
                    azul=pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\azul.png"),(220,220))
                    fechar=True
                    amb = True
                elif setaxy == (escolha2xy[0]-75,escolha2xy[1]-10):
                    print ("sair selecionado")
                    fechar = True
    #Atualiza a tela do jogo
    pygame.display.update()
    #Define a quanto frame por segundo
    clock.tick(60)

    while amb:
        Nhor = len(ambientes)
        tela.fill((0,0,0))
        tela.blit(paredeAmbiente,(0,0))
        desenha_brinquedos(brinquedinhos)
        if pygame.event.peek(QUIT)==True:
            fechar = True
            amb = False
           
        if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
            if pygame.key.get_pressed()[K_RIGHT]==True or joystick.get_button(14):
                pygame.mixer.Sound.play(somEscolha)
                #to no ambiente escola
                if vol == (ambientes[0].x-10,ambientes[0].y-20):
                    vol = (ambientes[1].x-10,ambientes[1].y-20)
                pygame.event.clear()
            if pygame.key.get_pressed()[K_LEFT]==True or joystick.get_button(13):
                pygame.mixer.Sound.play(somEscolha)
                #to no ambiente casa
                if vol == (ambientes[1].x-10,ambientes[1].y-20):
                    vol = (ambientes[0].x-10,ambientes[0].y-20)
                pygame.event.clear()
            if pygame.key.get_pressed()[K_DOWN]==True or joystick.get_button(12):
                pygame.mixer.Sound.play(somEscolha)
                #to no ambiente escola
                if vol == (ambientes[0].x-10,ambientes[0].y-20) or vol == (ambientes[1].x-10,ambientes[1].y-20):
                    vol = (voltar.x-20,voltar.y-10)
                    azul = pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\azul.png"),(200,60)) 
                pygame.event.clear()
                    
            if pygame.key.get_pressed()[K_UP]==True or joystick.get_button(11):
                pygame.mixer.Sound.play(somEscolha)
                if vol == (voltar.x-20,voltar.y-10):
                    vol = (ambientes[0].x-10,ambientes[0].y-20)
                    azul=pygame.transform.smoothscale(pygame.image.load_extended(f"{path}\\imagens\\azul.png"),(220,220))
                pygame.event.clear()
                    
            if pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0):
                pygame.mixer.Sound.play(somConfirmar)
                #Identifica se estamos selecionando o ambiente escola
                if vol == (ambientes[0].x-10,ambientes[0].y-20):
                    print ("escola selecionado")
                    seta1xy = (jogos[0].x-75,jogos[0].y)
                    esc = True
                    
                #Identifica se estamos selecionando o ambiente casa
                elif vol == (ambientes[1].x-10,ambientes[1].y-20):
                    print ("casa selecionado")
                    seta1xy = (jogos1[0].x-75,jogos1[0].y)
                    cas = True
                    
                elif vol == (voltar.x-20,voltar.y-10):
                    vol = (ambientes[0].x-10,ambientes[0].y-20)   
                    amb=False
                    fechar = False
                
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
                
            if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:
                if pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0):
                    pygame.mixer.Sound.play(somConfirmar)
                    if seta1xy==(voltar.x,voltar.y+75):
                        pygame.event.clear()
                        esc= False
                        amb= True
                        
                    elif seta1xy==(jogos[0].x-75,jogos[0].y):
                        print("Jogo 1 selecionado")
                        print(jogos[0].nome)
                        pygame.event.clear()
                        jogos[0].Jogar()
                        eu.checkExp()
                        pygame.event.clear()     
                        
                if pygame.key.get_pressed()[K_UP]==True or joystick.get_button(11):
                    pygame.mixer.Sound.play(somEscolha)
                    if  seta1xy==(voltar.x,voltar.y+75):
                        seta1xy = (jogos[0].x-75,jogos[0].y)
                    else:
                        pass

                if pygame.key.get_pressed()[K_LEFT]==True or joystick.get_button(13):
                    pygame.mixer.Sound.play(somEscolha)
                    pass
                        
                        
                if pygame.key.get_pressed()[K_DOWN]==True or joystick.get_button(12):
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos[0].x-75,jogos[0].y):
                        seta1xy=(voltar.x,voltar.y+75)
                    else:
                        pass
                    
                if pygame.key.get_pressed()[K_RIGHT]==True or joystick.get_button(14):
                    pygame.mixer.Sound.play(somEscolha)
                    pass
                pygame.event.clear()

            #pygame.draw.polygon(tela, (255,255,255),tri,0)       
            tela.blit(seta1,(seta1xy[0]+75,seta1xy[1]-150))
            tela.blit(memoria,(jogos[0].x-50,jogos[0].y-75))
            tela.blit(voltar.fonte,(voltar.x,voltar.y))
            tela.blit(jogos[0].fonte,(jogos[0].x-60,jogos[0].y+90))
            #tela.blit(xp, (100,750))
            pygame.display.update()

        while cas:
            tela.fill((0,0,0))
            crashed = False

            tela.blit(paredeCasa,(0,0))
            if pygame.event.peek(QUIT)==True:
                cas = False
                amb = False
                fechar = True
            if pygame.event.peek(KEYDOWN)==True or pygame.event.peek(JOYBUTTONDOWN)==True:    
                if pygame.key.get_pressed()[K_UP]==True or joystick.get_button(11):
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(voltar.x,voltar.y+75):
                        seta1xy = (jogos1[0].x-75,jogos[0].y)
               
                if pygame.key.get_pressed()[K_LEFT]==True or joystick.get_button(13):
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos1[0].x-75,jogos[0].y):
                        seta1xy=(jogos1[1].x-75,jogos[1].y)
                        
                        
                if pygame.key.get_pressed()[K_DOWN]==True or joystick.get_button(12):
                    pygame.mixer.Sound.play(somEscolha)
                    if seta1xy==(jogos1[0].x-75,jogos[0].y):
                        seta1xy=(voltar.x,voltar.y+75)
                 
                if pygame.key.get_pressed()[K_RIGHT]==True or joystick.get_button(14):
                    if seta1xy==(jogos1[1].x-75,jogos[1].y):
                        seta1xy=(jogos1[0].x-75,jogos[0].y)
                        
            
                if pygame.key.get_pressed()[K_SPACE]==True or joystick.get_button(0):
                    pygame.mixer.Sound.play(somConfirmar)
                    #checa se estamos no em "voltar", caso sim, voltamos para os ambientes
                    if seta1xy==(voltar.x,voltar.y+75):
                        pygame.event.clear()
                        cas= False
                        amb= True
                    #checa se estamos no jogo 1, caso sim, o jogo 1 é iniciado  
                    elif seta1xy==(jogos1[0].x-75,jogos1[0].y):
                        print("Jogo 1 selecionado")
                        print(jogos1[0].nome)
                        pygame.event.clear()
                        #Chamada de função da classe Jogo, que abre o jogo selecionado (jogo 1)
                        jogos1[0].Jogar()
                        pygame.event.clear() 
                    #checa se estamos no jogo 1, caso sim, o jogo 2 é iniciado 
                    elif seta1xy==(jogos1[1].x-75,jogos1[1].y):
                        print("Jogo 2 selecionado")
                        print(jogos1[1].nome)
                        pygame.event.clear()
                        #Chamada de função da classe Jogo, que abre o jogo selecionado (jogo 2)
                        jogos1[1].Jogar()
                        pygame.event.clear() 

            tela.blit(seta1,(seta1xy[0]+75,seta1xy[1]-150))
            tela.blit(dente,(jogos1[0].x-50,jogos1[0].y-75))
            tela.blit(voltar.fonte,(voltar.x,voltar.y))
            tela.blit(quarto,(jogos1[1].x-50,jogos1[1].y-75))
            tela.blit(jogos1[0].fonte,(jogos1[0].x-60,jogos[0].y+90))
            tela.blit(jogos1[1].fonte,(jogos1[1].x-60,jogos[1].y+90))
            pygame.display.update()
            

    
pygame.quit()

