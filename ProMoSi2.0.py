import sys, time, pygame, math, random, decimal
import numpy as np
from pygame.locals import *

# WARNA
putih1 = (210,210,234)
BLUE       = (  0,   0, 255)
WHITE      = (255, 255, 255)
DARKRED    = (128,   0,   0)
DARKBLUE   = (  0,   0, 128)
RED        = (255,   0,   0); RED1 = (150, 10, 10)
GREEN      = (  0, 255,   0)
DARKGREEN  = (  0, 128,   0)
YELLOW     = (215, 215,   0)
DARKYELLOW = (128, 128,   0)
BLACK      = (  0,   0,   0)

BGCOLOR = WHITE
Rr = 60
Gr = 60
Br = 60

#ukuran layar & meja
WINDOWWIDTH = int(1100) # width of the program's window, in pixels
WINDOWHEIGHT = 700 # height in pixels
AMPLITUDE = 100 # how many pixels tall the waves with rise/fall.
xmeja, ymeja = (0, 75)
lmeja = WINDOWWIDTH
tmeja = (WINDOWHEIGHT-2*ymeja)

# standard pygame setup code
pygame.init()
clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Projectile Motion Simulation')
fontObj = pygame.font.Font('freesansbold.ttf', 16)
start_ticks=pygame.time.get_ticks()

# INISIASI AWAL & variables that track visibility modes 
g = 9.80665

derajat = 0
pause = False
showSine = True
teks = True
playing = True
bahasa = "eng"
degrees = 30; v0 = 10
gambar = 0
posv = 0; vo = 0
posh = 0
v0p = 0; degp = 0
xPos = 0
yPos = 0
posRecord = {'sin': [], 'cos': [], 'hiampsin': [], 'hifreqsin': []} # keeps track of the ball positions for drawing the waves
mulai = 0
t = 0
loop = False
dr = 1
updown = True
metric = True; metric1 = True
resist = False; c = 12.5; mass = 10
mass1 = 0; c1 = 0


#Setting font-size
font1 = pygame.font.Font(None,25)
font2 = pygame.font.Font(None,25)
font3 = pygame.font.Font(None,23)
font4 = pygame.font.Font(None, 20)
font5 = pygame.font.SysFont("comicsansms", 50)
font6 = pygame.font.SysFont("verdana", 25)
font7 = pygame.font.SysFont("Arial", 35)

print()
print()
print("Simulasi Parabola")
print("untuk media pembelajaran oleh:")
print("- Aziz Setiawan (1302617026)")
print("- Muhammad Iqbal (1302617038)")
print("- Raden Muhammad Jachfikri (1302617066)")
print()
print("Pendidikan Fisika 2017 - Universitas Negeri Jakarta")
print()
print("Versi  2.0 - Update terakhir: 14 November 2019")
  
    
running = True
intro = True
while running:
  # EVENT RL
  # fill the screen to draw from a blank state
  DISPLAYSURF.fill(WHITE)
  for event in pygame.event.get():
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
      running = False
      
    # Klik Mouse untuk memulai
    if event.type == pygame.MOUSEBUTTONDOWN:
      mulai = 1
      pause = False
      
    if event.type == pygame.KEYDOWN:
      if event.key == K_SPACE:
        intro = not intro
      if event.key == K_p:
        pause = not pause
      if event.key == K_8:
        resist = not resist
      

      #TOMBOL NAIKIN MASSA DAN C
    
      if event.key == K_u:
        if resist:
          mass += 1
      if event.key == K_i:
        if resist:
          c += 0.5
      if event.key == K_j:
        if resist:
          mass -= 1
          if mass <= 1:
            mass = 1
      if event.key == K_k:
        if resist:
          c -= 0.5
          if c <= 0.5:
            c = 0.5

      #TOMBOL BAHASA
      if event.key == K_1:
          bahasa = "eng"
      if event.key == K_2:
          bahasa = "ina"
      if event.key == K_3:
        metric = not metric
      if event.key == K_BACKSPACE:
        metric1 = not metric1

      # Tombol Mengatur Sudut
      if event.key == K_w:
        if updown:
          degrees += 1
        if not updown:
          degp = 1
      if event.key == K_s:
        if updown:
          degrees  -= 1
        if not updown:
          degp = 2

      # Tombol Mengatur Kecepatan Awal
      if event.key == K_e:
        if updown:
          v0 += 1
        if not updown:
          v0p = 1
      if event.key == K_d:
        if updown:
          v0 -= 1
        if not updown:
          v0p = 2

      # Tombol untuk posisi awal bola
      if event.key == K_UP:
        if updown:
          mulai = 1
          yPos -= 91.8
        elif not updown:
          mulai = 1
          posv = 1
      if event.key == K_DOWN:
        if updown:
          mulai = 1
          yPos += 91.8
        elif not updown:
          mulai = 1
          posv = 2
      if event.key == K_LEFT:
        if updown:
          mulai = 1
          xPos -= 91.8
        elif not updown:
          mulai = 1
          posh = 1
      if event.key == K_RIGHT:
        if updown:
          mulai = 1
          xPos += 91.8
        elif not updown:
          mulai = 1
          posh = 2
        
      # Tombol untuk mengulang
      if event.key == K_r:
        mulai = 0
      if event.key == K_o:
        mulai = 1
        xPos = xbola; yPos = ybola; t = 0; dtt = 0
      if event.key == K_u:
        posRecord = {'sin': [], 'cos': [], 'hiampsin': [], 'hifreqsin': []}


      # Tombol Jejak/Teks/Updown:
      if event.key == K_q:
        showSine = not showSine
      if event.key == K_TAB:
        teks = not teks
      if event.key == K_LSHIFT or event.key == K_RSHIFT:
        updown = not updown
    
    if event.type == pygame.MOUSEBUTTONUP:
      mulai = 2
      posv = 0; posh = 0
      t = time.time()
      
    if event.type == pygame.KEYUP:
      posh = 0; posv = 0; v0p = 0; degp = 0
    
        
  #5 Detik Pertama RL
  seconds = (pygame.time.get_ticks()-start_ticks)/1000
  if intro:
      pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,WINDOWWIDTH,WINDOWHEIGHT))
      textG = font5.render("SIMULASI PARABOLA", True, YELLOW)
      textH = font6.render("Pengembangan Media Pembelajaran", True, YELLOW)
      textW = font7.render("Created by", True, WHITE)
      textN = font6.render("Muhammad Iqbal, Raden M. Jachfikri, and Aziz Setiawan", True, putih1)
      textP = font1.render("press SPACE", True, WHITE)
      DISPLAYSURF.blit(textG, [(WINDOWWIDTH/2-270), WINDOWHEIGHT/2-150])
      DISPLAYSURF.blit(textH, [(WINDOWWIDTH/2-230), WINDOWHEIGHT/2-50])
      DISPLAYSURF.blit(textW, [(WINDOWWIDTH/2)-70, WINDOWHEIGHT/2-10])
      DISPLAYSURF.blit(textN, [(WINDOWWIDTH/2)-350, (WINDOWHEIGHT/2)+30])
      DISPLAYSURF.blit(textP, [(WINDOWWIDTH/2)-50, WINDOWHEIGHT-60])
  elif not intro:
    # draw the horizontal middle line and the amplitude lines
    pygame.draw.rect(DISPLAYSURF, putih1, (xmeja,ymeja,lmeja,tmeja))
    for n in range(0,9):
      pygame.draw.line(DISPLAYSURF, BLACK, (0, WINDOWHEIGHT-75-91.8*n), (WINDOWWIDTH, WINDOWHEIGHT-75-91.8*n))
    for n in range(0, 19):
      pygame.draw.line(DISPLAYSURF, BLACK, (n*91.8, 75), (n*91.8, WINDOWHEIGHT-75))


    # Keadaan Awal Bola / Diam
    if mulai == 0:
      vx = 0; vy = 0
      xPos = 0
      yPos = -75
      xbola = xPos
      ybola = yPos
      m = 0
      dt = 0;dtt = 0
      posRecord = {'sin': [], 'cos': [], 'hiampsin': [], 'hifreqsin': []}
      kecepx = v0; kecepy = v0

    if v0p == 1:
      v0 += 1
    elif v0p == 2:
      v0 -= 1
    if degp == 1:
      degrees += 1
    elif degp == 2:
      degrees -= 1

    # Persiapan sebelum bergerak
    if mulai == 1:
      if posv == 1:
        yPos -= 1
      if posv == 2:
        yPos += 1
      if posh == 1:
        xPos -= 1
      if posh == 2:
        xPos += 1
      xbola = xPos
      ybola = yPos
      if yPos >= -74:
        yPos = -75
      kecepx = v0; kecepy = v0
      pospos = 0; tpospos = 0

    
    # Bola Bergerak    
    elif mulai == 2:
      if not pause:
        dt = time.time()-t
        #dtt += 0.01091
        if not resist:
          vx = v0*math.cos(math.radians(degrees))
          vy = v0*math.sin(math.radians(degrees))
          kecepx = vx
          kecepy = vy-(g*dt)
          waktutinggi = v0*math.sin(math.radians(degrees))/g
          yPuncak = -((v0**2)*((math.sin(math.radians(degrees)))**2)*91.8/(2*g))+ybola
        elif resist:
          vx = v0*math.cos(math.radians(degrees))*math.exp(-c*dt/mass)
          vy = v0*math.sin(math.radians(degrees))*math.exp(-c*dt/mass) - (m*g/c)*(1-math.exp(-c*dt/mass))
          kecepx = v0*math.cos(math.radians(degrees))*math.exp(-c*dt/mass)
          kecepy = (v0*math.sin(math.radians(degrees))*math.exp(-c*dt/mass) - (m*g/c)*(1-math.exp(-c*dt/mass)))-(g*dt)
          waktutinggi = v0*math.sin(math.radians(degrees))*mass/(c*g)
          yPuncak = -((v0**2)*(math.sin(math.radians(2*degrees)))*91.8/(2*g))+ybola

        # Rumus Parabola
        yPos -= vy-(g*(dt))
        xPos += vx
        posRecord['sin'].append((int(xPos), int(yPos) + WINDOWHEIGHT))
        
      elif pause:
        dtt += 0
        dt += 0; t += 0

    # Bola selesai bergerak
    elif mulai == 3:
      vy = 0; vx = 0; yPos = -75; dtt = 0

    # Batas X dan Y:
    if yPos >= -74 :
      mulai = 3

    # draw variable
    if teks:
      if resist:
        if bahasa == "eng":
          if metric:
            if metric1:
              teksconstant = fontObj.render("c = {:0.1f} kg/s".format(c),True,BLACK)
              teksmassa = fontObj.render("mass = {} kg".format(mass),True,BLACK)
            elif not metric1:
              teksconstant = fontObj.render("c = {:0.3f} tonne/h".format(c*3.6),True,BLACK)
              teksmassa = fontObj.render("mass = {} g".format(mass*1000),True,BLACK)
          elif not metric:
            if metric1:
              teksconstant = fontObj.render("c = {:0.3f} cu ft/s".format(c*0.035),True,BLACK)
              teksmassa = fontObj.render("mass = {:0.3f} pounds".format(mass*2.205),True,BLACK)
            elif not metric1:
              teksconstant = fontObj.render("c = {:0.3f} us tons/h".format(c*3.968),True,BLACK)
              teksmassa = fontObj.render("mass = {:0.4f} us ton".format(mass*0.0011),True,BLACK)
        elif bahasa == "ina":
          if metric:
            if metric1:
              teksconstant = fontObj.render("konstanta = {:0.1f} kilogram/detik".format(c),True,BLACK)
              teksmassa = fontObj.render("massa = {} kilogram".format(mass),True,BLACK)
            elif not metric1:
              teksconstant = fontObj.render("konstanta = {:0.3f} ton/jam".format(c*3.6),True,BLACK)
              teksmassa = fontObj.render("massa = {} gram".format(mass*1000),True,BLACK)
          elif not metric:
            if metric1:
              teksconstant = fontObj.render("konstanta = {:0.3f} kaki kubik/detik".format(c*0.035),True,BLACK)
              teksmassa = fontObj.render("massa = {:0.3f} pon".format(mass*2.205),True,BLACK)
            elif not metric1:
              teksconstant = fontObj.render("konstanta = {:0.3f} us ton/jam".format(c*3.968),True,BLACK)
              teksmassa = fontObj.render("massa = {:0.4f} us ton".format(mass*0.0011),True,BLACK)
        DISPLAYSURF.blit(teksconstant, [300, 30])
        DISPLAYSURF.blit(teksmassa, [300, 50])
      dts = round(dt, 2)
      posx = xPos/91.8
      posy = abs(yPos+75)/91.8
      posbola = abs(ybola+75)
      teksbahasa = fontObj.render("1 = English | 2 = Bahasa Indonesia | 3 = Metric/Imperial | 8 = Drag", True, BLACK)
      # making text Surface for various labels
      if bahasa == "eng":
        kalimat1 = fontObj.render('Q = Toggle waves | P = Pause | Mouse Button = play | W - S = degrees | E - D = Initial Velocity  .', True, BLACK, BGCOLOR)
        kalimat2 = fontObj.render("Angle = "+str(degrees) + ' degrees \t '+"Time = " + str(dts)+" s", True, BLACK)
        kalimat3 =  fontObj.render("TAB = text on/off | R = Reset | O = Back to initial position | Arrows = initial position", True, BLACK)
        #waktu = fontObj.render("Time = " + str(dts)+" s", True, BLACK)
        # METRIC
        if metric:
          if metric1:
            tekskecepatan = fontObj.render("Initial Velocity = {} m/s".format(v0),True,BLACK)
            rposx = posx
            rposy = posy
            poslang = " m"
            tekspos = fontObj.render("(x, y) = ({:0.1f}, {:0.1f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) m/s".format(kecepx, kecepy),True,BLACK)
          elif not metric1:
            tekskecepatan = fontObj.render("Initial Velocity = {:0.1f} km/h".format(3.6*v0),True,BLACK)
            rposx = posx/1000
            rposy = posy/1000
            poslang = " km"
            tekspos = fontObj.render("(x, y) = ({:0.5f}, {:0.5f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) km/h".format(3.6*kecepx, 3.6*kecepy),True,BLACK)
        # IMPERIAL
        elif not metric:
          if metric1:
            rposx = posx/1609.344
            rposy = posy/1609.344
            tekskecepatan = fontObj.render("Initial Velocity = {:0.3f} miles/h".format(2.237*v0),True,BLACK)
            poslang = " miles"
            tekspos = fontObj.render("(x, y) = ({:0.4f}, {:0.4f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) miles/h".format(2.237*kecepx, 2.237*kecepy),True,BLACK)
          elif not metric1:
            tekskecepatan = fontObj.render("Initial Velocity = {:0.3f} feet/s".format(3.281*v0),True,BLACK)
            rposx = posx*39.37
            rposy = posy*39.37
            poslang = " inch"
            tekspos = fontObj.render("(x, y) = ({:0.4f}, {:0.4f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) ft/s".format(3.281*kecepx, 3.281*kecepy),True,BLACK)
        
      elif bahasa == "ina":
        kalimat1 = fontObj.render('Q = Jejak Parabola | P = Berhenti | Tombol Mouse = Mulai | W - S = derajat | E - D = Kecepatan Awal .', True, BLACK, BGCOLOR)
        kalimat2 = fontObj.render("Sudut awal = " + str(degrees) +" derajat \t "+"Waktu = " + str(dts)+" detik", True, BLACK)
        kalimat3 = fontObj.render("TAB = on/off teks | R = Ulang kembali | O = kembali ke posisi awal | Panah = Posisi awal", True, BLACK)
        #waktu = fontObj.render("Waktu = " + str(dts)+" detik", True, BLACK)
        if metric:
          if metric1:
            tekskecepatan = fontObj.render("Kecepatan Awal = {} meter per detik".format(v0),True,BLACK)
            rposx = posx
            rposy = posy
            poslang = " meter"
            tekspos = fontObj.render("(x, y) = ({:0.1f}, {:0.1f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) m/det".format(kecepx, kecepy),True,BLACK)
          elif not metric1:
            tekskecepatan = fontObj.render("Kecepatan Awal = {:0.1f} kilometer per jam".format(3.6*v0),True,BLACK)
            rposx = posx/1000
            rposy = posy/1000
            poslang = " kilometer"
            tekspos = fontObj.render("(x, y) = ({:0.5f}, {:0.5f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) km/jam".format(3.6*kecepx, 3.6*kecepy),True,BLACK)
        # IMPERIAL
        elif not metric:
          if metric1:
            rposx = posx/1609.344
            rposy = posy/1609.344
            tekskecepatan = fontObj.render("Kecepatan Awal = {:0.3f} mil per jam".format(2.237*v0),True,BLACK)
            poslang = " mil"
            tekspos = fontObj.render("(x, y) = ({:0.4f}, {:0.4f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) mil/jam".format(2.237*kecepx, 2.237*kecepy),True,BLACK)
          elif not metric1:
            tekskecepatan = fontObj.render("Kecepatan Awal = {:0.3f} kaki per detik".format(3.281*v0),True,BLACK)
            rposx = posx*39.37
            rposy = posy*39.37
            poslang = " inci"
            tekspos = fontObj.render("(x, y) = ({:0.4f}, {:0.4f}) {:2}".format(rposx, rposy, poslang),True,BLACK)
            tekskecep = fontObj.render("(vx, vy) = ({:0.2f}, {:0.2f}) kaki/det".format(3.281*kecepx, 3.281*kecepy),True,BLACK)

      if bahasa == "eng":
        mh = "y highest = "
        mt = "time at highest y = "
      elif bahasa == "ina":
        mh = "y tertinggi = "
        mt = "waktu pada y tertinggi = "
      
      if mulai == 2 or mulai == 3:
        if kecepy >= 0:
          if metric:
            if metric1:
              pospos = abs(yPos+75)/91.833
            elif not metric1:
              pospos = abs(yPos+75)/(1000*91.833)
          elif not metric:
            if metric1:
              pospos = abs(yPos+75)/(1609.344*91.833)
            elif not metric1:
              pospos = abs(yPos+75)*39.37/91.833
          tpospos = dt
        if kecepy <= 0:
          pospos += 0; tpospos += 0
        tekstinggimaks = fontObj.render("{} {:0.1f} {} || {} {:0.2f} s".format(mh, pospos, poslang, mt, tpospos), True, RED1)  
        DISPLAYSURF.blit(tekstinggimaks, [600,10])
        #if yPos <= yPuncak+10 and yPos >= yPuncak-10:
          #tekstinggimaks = fontObj.render("{} {:0.4f} {} || {} {:0.2f} s".format(mh, pospos, poslang, mt, waktutinggi), True, RED1)
              
        #elif v0 >= 21 or degrees >= 51 or v0 < 0 or degrees < 0 or resist:
          #tekstinggimaks = fontObj.render("{} {:0.4f} {} || {} {:0.2f} s".format(mh, pospos, poslang, mt, waktutinggi), True, RED1)

      instructionsRect2 = kalimat2.get_rect()
      instructionsRect2.left = 20
      instructionsRect2.bottom = WINDOWHEIGHT - 50

      # draw instructions
      DISPLAYSURF.blit(kalimat3, [20, WINDOWHEIGHT-40])
      DISPLAYSURF.blit(kalimat1, instructionsRect2)
      DISPLAYSURF.blit(kalimat2, [10, 30])
      DISPLAYSURF.blit(tekskecepatan, [10, 50])
      DISPLAYSURF.blit(tekspos, [10, 10])
      #DISPLAYSURF.blit(waktu, [130, 30])
      DISPLAYSURF.blit(teksbahasa, [550, 50])
      DISPLAYSURF.blit(tekskecep, [350, 10])
      

    # draw the waves from the previously recorded ball positions
    if showSine:
        sinecolor = (Rr, Gr, Br)
        for x, y in posRecord['sin']:
          pygame.draw.circle(DISPLAYSURF, sinecolor, (x, y), 4)
    if not updown:
      teksshift = fontObj.render("SHIFT", True, YELLOW)
      DISPLAYSURF.blit(teksshift, [WINDOWWIDTH-100, 30])
    if pause:
      if bahasa == "eng":
        tekspause = fontObj.render("PAUSE", True, RED1)
      elif bahasa == "ina":
        tekspause = fontObj.render("BERHENTI", True, RED1)
      DISPLAYSURF.blit(tekspause, [WINDOWWIDTH-120, 10])
      
    pygame.draw.circle(DISPLAYSURF, RED, (int(xPos), int(yPos) + WINDOWHEIGHT), 10)

  # draw the border
  pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)
  clock.tick(100)
  pygame.display.update()

pygame.quit()
print()
print("====== Thank you ======")

      
