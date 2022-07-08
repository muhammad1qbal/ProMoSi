import pygame, sys, time
from pygame.locals import *
import math
pygame.init()
clock = pygame.time.Clock()
#color
putih1 = (210,210,234)
WHITE = 250,250,250
BLUE=(0,0,255)
BLACK = (0 , 0 , 0)  
GREEN = (0 , 255 , 0)
RED   = (255,   0,   0)
DARKRED    = (128,   0,   0)
YELLOW     = (215, 215,   0)
BLUE1 = (85, 85, 255)
GREEN1 = (65, 255, 65)


WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
#image
truck = pygame.image.load('truck.png')
truck = pygame.transform.scale(truck, (161,97))
arrow = pygame.image.load('arrow.png')
arrow = pygame.transform.scale(arrow, (30,20))
arrowd = pygame.image.load('arrowd.png')
arrowd = pygame.transform.scale(arrowd, (20,30))
arrowl = pygame.image.load('arrowl.png')
arrowl = pygame.transform.scale(arrowl, (30,20))
arrowu = pygame.image.load('arrowu.png')
arrowu = pygame.transform.scale(arrowu, (20,30))
slide1 = pygame.image.load('slide1.png')
slide1 = pygame.transform.scale(slide1, (621,317))
slide2 = pygame.image.load('slide2.png')
slide2 = pygame.transform.scale(slide2, (621,317))
slide3 = pygame.image.load('slide3.png')
slide3 = pygame.transform.scale(slide3, (621,317))

background_image = pygame.image.load("1.jpg")
background_image = pygame.transform.scale(background_image, (1000,600))
start_ticks=pygame.time.get_ticks()

#Setting font-size
teks = True
bahasa = "eng"
font1 = pygame.font.Font(None,25)
font2 = pygame.font.Font(None,25)
font3 = pygame.font.Font(None,23)
font4 = pygame.font.Font(None, 20)
font5 = pygame.font.SysFont("Candara", 50)
font6 = pygame.font.SysFont("verdana", 25)
font7 = pygame.font.SysFont("Arial", 35)

def kalimat():
  fontObj = pygame.font.Font('freesansbold.ttf', 16)
  # making text Surface for various labels
  if bahasa == "eng" or bahasa == "ega":
    kalimat1 = fontObj.render('O = fire | M = move | R = reset | Q/W = degree | V = hide vektor | tab = hide instruction | f=show slide |', True, BLACK)
    kalimat2 = fontObj.render('UP/DOWN = initial velocity', True, BLACK)
    if bahasa == "eng":
      vb = v0; vlang = " m/s"
      vc = 50
    elif bahasa == "ega":
      vb = round(2.237*v0,3); vlang = " miles/hour"
      vc = round(2.237*50,3)
    kalimat3 = fontObj.render('Initial Velocity = '+str(vb) + vlang + " | degree = "+ str(sb) + " | Truck = "+ str(vc) + vlang +" | g = 9.8 m/s^2 ", True, BLACK)
  if bahasa == "ina":
    kalimat1 = fontObj.render('O = tembak | M = jalan | R = ulang | Q/W = derajat',True, BLACK)
    kalimat2 = fontObj.render('UP/DOWN = kecepatan awal', True, BLACK)
    vb = round(3.6*v0, 3); vlang = "km/jam"
    vc = round(3.6*50, 3)
    kalimat3 = fontObj.render('Kecepatan Awal bola = '+str(vb) + vlang + " | derajat = " + str(sb) + " | Truk = "+ str(vc) + vlang, True, BLACK)

  instructionsRect = kalimat1.get_rect()
  instructionsRect.left = 20
  instructionsRect.bottom =+ 30
  
  instructionsRect2 = kalimat2.get_rect()
  instructionsRect2.left = 20
  instructionsRect2.bottom =+ 50
  instructionsRect3 = kalimat3.get_rect()
  instructionsRect3.left = 20
  instructionsRect3.bottom = + 70

  # draw instructions
  screen.blit(kalimat1, instructionsRect)
  screen.blit(kalimat2, instructionsRect2)
  screen.blit(kalimat3, instructionsRect3)


screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('ProMoSi - Truck')

#inisiasi
v=0;x=0;t=0;c=0;degrees=0;k=0;k2=0;g=9.8;ts=0; rot = 0; v0=0;rot_speed = 0;sb=0;m=0;yPos=-163;ui=0;sd=0;v1=0;v2=0;yPos1=0;yPos2=0;xPos1=0;xPos2=0;xPos=0;h=0;hh=0;vex=0;i=0
mulai = 0; sudut = 0; v3=-50;v4=50;v5=-50;v6=50;v7=-50;v8=50;v9=-50;v10=50;v11=-50;v12=50;f=0
vek1=[-100];vek2=[];vek3=[];vek4=[];vek=[];run=[0]
showSine=True
ekor=False
move=False
bolagerak = False
vektor = False
formula = False
pause = False
is_arrow_has_not_been_set = True
is_arrow_has_not_been_set2 = True
is_arrow_has_not_been_set3 = True
is_arrow_has_not_been_set4 = True
is_arrow_has_not_been_set5 = True
is_right= True
is_left= True
posRecord =[] # keeps track of the ball positions for drawing the waves 
moncong = pygame.Surface((58 , 5.33))   
moncong.set_colorkey(BLACK)  
moncong.fill(GREEN)   
image = moncong.copy()  
rect = image.get_rect()  

while True:
  for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
          pygame.quit()
          sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_w:
            sudut = 2
        if event.key == K_q:
            sudut = 1 
        if event.key == K_UP:
              mulai=1
          
        if event.key == K_DOWN:
              mulai=2
              
        #TOMBOL BAHASA
        if event.key == K_1:
            bahasa = "eng"
        if event.key == K_2:
            bahasa = "ega"
        if event.key == K_3:
            bahasa = "ina"
      if event.type == KEYUP:
          mulai=0; sudut = 0
            
          if event.key == K_m:
              move=not move
              bolagerak = not bolagerak
              dx=1
          if event.key == K_o:
             c=0.1
             x=1
             ekor=not ekor
          if event.key == K_r:
              move=False; bolagerak = False
              is_arrow_has_not_been_set=True;is_arrow_has_not_been_set2 = True;is_arrow_has_not_been_set3 = True
              is_arrow_has_not_been_set4 = True;is_arrow_has_not_been_set5 = True
              t=0;c=0;v=0;yPos=0;xPos=0;xPos1=0;xPos2=0;yPos1=0;yPos2=0; position = (0, 350);k=0; posRecord =[]; ui = 0
              vek1=[];vek2=[];v3=-50;v4=50;v5=-50;v6=50;v7=-50;v8=50;v9=-50;v10=50;v11=-50
              ekor=False  
          if event.key == K_TAB:
            teks = not teks
          if event.key == K_v:
            vektor = not vektor
          if event.key == K_f:
            f+=1
          if f==4:
              f=0
          if event.key == K_p:
            pause = not pause
  #5 Detik Pertama RL
  seconds = (pygame.time.get_ticks()-start_ticks)/1000
  if seconds < 5:
      pygame.draw.rect(screen, BLACK, (0,0,WINDOWWIDTH,WINDOWHEIGHT))
      textG = font5.render("ProMoSi: Truck Version", True, GREEN1)
      textH = font6.render("Projectile Motion Simulation v2", True, BLUE1)
      textW = font7.render("Created by", True, WHITE)
      textN = font6.render("1. Muhammad Iqbal 2. Raden M. Jachfikri 3. Aziz Setiawan", True, putih1)
      textP = font1.render("Please wait...", True, WHITE)
      screen.blit(textG, [(WINDOWWIDTH/2-250), WINDOWHEIGHT/2-150])
      screen.blit(textH, [(WINDOWWIDTH/2-190), WINDOWHEIGHT/2-50])
      screen.blit(textW, [(WINDOWWIDTH/2)-70, WINDOWHEIGHT/2-10])
      screen.blit(textN, [(WINDOWWIDTH/2)-315, (WINDOWHEIGHT/2)+30])
      screen.blit(textP, [(WINDOWWIDTH/2)-50, WINDOWHEIGHT-60])
  else:
    if mulai ==1:
      v0+=0.5
    if mulai ==2:
      v0-=0.5
      if v0 <=-0.5:
            v0 =0
    if sudut == 1:
      rot -= 1
      sb+=1
      if rot<=235 and rot>-1:
        rot=235
        sb=135
    if sudut == 2:
      rot += 1
      sb-=1
      if rot>=0 and rot<=100:
       rot=0
       sb=0
    if not move:
      v=0
    if not bolagerak:
      uv = 0
    if move:
      v=5
    if bolagerak:
      uv = 5
    #formula  
    t+=c
    k+=v
    ui += uv
    run.append(t)
    screen.blit(background_image, [0, 0])
    rect.center = (46+k, 437)
    old_center = rect.center
    rot = (rot) % 360
    if teks:
      kalimat()
    if f==1:
      screen.blit(slide1, (340,30))
    if f==2:
      screen.blit(slide2, (340,30))
    if f==3:
      screen.blit(slide3, (340,30))
      
    yPos1=yPos;xPos1=xPos
    #if not pause:
      #print('x')
    xPos=int(-33*math.sin(math.radians(rot-270)))+44+ui-(v0*math.sin(math.radians(rot-270))*t)
    #print(ui,v0)
    yPos=int(-33*math.cos(math.radians(rot-270)))-(163+(v0*math.cos(math.radians(rot-270))*t-0.5*(g)*t**2))
    yPos2=yPos;xPos2=xPos
    vek.append((xPos,yPos))  
    #red line
    if ekor:
        posRecord.append((int(xPos), int(yPos) + WINDOWHEIGHT))
    pygame.draw.circle(screen, RED, (int(xPos), int(yPos) + WINDOWHEIGHT), 6)
    for x, y in posRecord:
        pygame.draw.circle(screen, DARKRED, (x, y), 2)
    if yPos >= -109 :  
        yPos =-109 ;c=0;
    #vektor
    if not vektor:
      if t==0.1:
        v1=xPos;v2=yPos
        
      if t>0:

        if is_arrow_has_not_been_set:
          is_arrow_has_not_been_set = False
          if round(xPos2,3)>round(xPos1,3):
            is_right = False;is_left=True
          if round(xPos2,3)<round(xPos1,3):
            is_left = False;is_right=True
          if yPos2 > yPos1:        
            is_down = True        
          else:
            is_down = False
          if round(xPos1,3)==round(xPos2,3):
            is_left=True;is_right=True

        if not is_right:
          screen.blit(arrow, (v1,v2 + WINDOWHEIGHT-10))
        if not is_left:
          screen.blit(arrowl, (v1-20,v2 + WINDOWHEIGHT-10))
        if is_down:
          screen.blit(arrowd, (v1-10,v2 + WINDOWHEIGHT))
        else:
          screen.blit(arrowu, (v1-9,v2 + WINDOWHEIGHT-29))
      
      if round(xPos2,3)>round(xPos1,3) and yPos1< yPos2 and c==0.1:
        if is_arrow_has_not_been_set2:
          v3=xPos;v4=yPos
          is_arrow_has_not_been_set2 = False
      screen.blit(arrow, (v3,v4 + WINDOWHEIGHT-10))

      if round(xPos2,3)<round(xPos1,3) and yPos1< yPos2 and c==0.1:
        if is_arrow_has_not_been_set2:
          v5=xPos;v6=yPos
          is_arrow_has_not_been_set2 = False
      screen.blit(arrowl, (v5-20,v6 + WINDOWHEIGHT-10))

      if xPos2==xPos1 and yPos1< yPos2 and yPos<-120 and c==0.1:
        if is_arrow_has_not_been_set3:
          v7=xPos;v8=yPos
        if yPos <-300:
          v7=0;v8=0
        is_arrow_has_not_been_set3 = False
      screen.blit(arrowd, (v7-10,v8 + WINDOWHEIGHT))

      if yPos >= -109 :
        screen.blit(arrowd, (xPos-10,yPos + WINDOWHEIGHT))  
        yPos =-109 ;c=0;
        bolagerak = False ; move=False
        if xPos2>xPos1:
          if is_arrow_has_not_been_set4:
            v9=xPos;v10=yPos
          is_arrow_has_not_been_set4 = False

        if xPos2<xPos1:
          if is_arrow_has_not_been_set5:
            v11=xPos;v12=yPos
          is_arrow_has_not_been_set5 = False
      screen.blit(arrow, (v9,v10 + WINDOWHEIGHT-7))
      screen.blit(arrowl, (v11-30,v12 + WINDOWHEIGHT-7))      

    moncong2 = pygame.transform.rotate(moncong , rot)  
    rect = moncong2.get_rect()   
    rect.center = old_center 
    screen.blit(moncong2 , rect)
    position = (0 +k, 404)
    screen.blit(truck, position)




  pygame.display.update()
  clock.tick(30)

