import pygame,time
from pygame.locals import *
from sys import exit
from random import *
pygame.init()
dim=(40,40)
screen=pygame.display.set_mode((1200,600),0,32)
ship_image=pygame.transform.scale(pygame.image.load('images/ship.png'),dim)
water=pygame.transform.scale(pygame.image.load('images/water.png'),dim)
unknown=pygame.transform.scale(pygame.image.load('images/unknown.png'),dim)
shot=pygame.transform.scale(pygame.image.load('images/shot.png'),dim)
class ship():
    def __init__(self,name,length):
        self.name=name;
        self.length=length;
        self.length_temp=length
def no_cross(ship,board):
    count=0
    if ship.state=='HORIZONTAL':
        for i in range(ship.length):
            if board[ship.ver[1]+i][ship.ver[0]]!='blue':
                count+=1
    elif ship.state=='VERTICAL':
        for i in range(ship.length):
            if board[ship.ver[1]][ship.ver[0]+i]!='blue':
                count+=1
    if count==0:
        return 1;
    else:
        return 0;
def valid(ship,board):
    if ship.state=='HORIZONTAL':
        if 10-ship.ver[1]>=ship.length and no_cross(ship,board):
            return 1;
    elif ship.state=='VERTICAL':
        if 10-ship.ver[0]>=ship.length and no_cross(ship,board):
            return 1;
    else:
        return 0;
def check(board,i,j,ships):
    count_hor1=0
    count_hor2=0
    count_ver1=0
    count_ver2=0
    for k in range(1,j+1):
        if board[i][j-k]=='blue':
            count_hor1+=1
        else:
            break;
    for k in range(j+1,10):
        if board[i][k]=='blue':
            count_hor2+=1
        else:
            break;
    for k in range(1,i+1):
        if board[i-k][j]=='blue':
            count_ver1+=1
        else:
            break
    for k in range(i+1,10):
        if board[k][j]=='blue':
            count_ver2+=1
        else:
            break
    sum_value=0
    for ship in ships:
        if count_hor1+count_hor2+1>=ship.length:
            if count_hor1>=ship.length-1:
                if count_hor2>=ship.length-1:
                    sum_value+=ship.length
                else:
                    sum_value+=count_hor2+1
            else:
                if count_hor2>=ship.length-1:
                    sum_value+=count_hor1+1
                else:
                    sum_value+=max(count_hor1,count_hor2)-1
        if count_ver1+count_ver2+1>=ship.length:
            if count_ver1>=ship.length-1:
                if count_ver2>=ship.length-1:
                    sum_value+=ship.length
                else:
                    sum_value+=count_ver2+1
            else:
                if count_ver2>=ship.length-1:
                    sum_value+=count_ver1+1
                else:
                    sum_value+=max(count_ver1,count_ver2)-1
    return sum_value
def calculate(board,prob,ships):
    for i in range(10):
        for j in range(10):
            if board[i][j]=='blue':
                count=0
                if i+1<=9 and board[i+1][j]=='H':
                    prob[i][j]*=50
                    count+=1
                if i-1>=0 and board[i-1][j]=='H':
                    prob[i][j]*=50
                    count+=1
                if j-1>=0 and board[i][j-1]=='H':
                    prob[i][j]*=50
                    count+=1
                if j+1<=9 and board[i][j+1]=='H':
                    prob[i][j]*=50
                    count+=1
                if count==0:
                    prob[i][j]=check(board,i,j,ships)
            elif board[i][j]=='green' or board[i][j]=='sunk' or board[i][j]=='H':
                prob[i][j]=0
def draw(color,x,y):
    if color=='A' or color=='S' or color=='D' or color=='B' or color=='C' or color=='D' or color=='sunk':
        screen.blit(ship_image,(x,y))
    elif color=='blue':
        screen.blit(unknown,(x,y))
    elif color=='green':
        screen.blit(water,(x,y))
    elif color=='H':
        screen.blit(shot,(x,y))
def display(board,position):
    for i in range(10):
        for j in range(10):
            draw(board[i][j],i*40+position[0],j*40+position[1])
    for j in range(11):
        pygame.draw.line(screen,(0,0,0),(position[0],j*40+position[1]),(position[0]+400,j*40+position[1]),5)
        pygame.draw.line(screen,(0,0,0),(position[0]+(j)*40,position[1]),(position[0]+(j)*40,position[1]+board_size),5)    
prob=[]
hboard1=[]
hboard2=[]
board1=[]
board2=[]
for i in range(10):
    prob.append([0,0,0,0,0,0,0,0,0,0])
for i in range(10):
    hboard1.append([])
    for j in range(10):
        hboard1[i].append('blue')
for i in range(10):
    hboard2.append([])
    for j in range(10):
        hboard2[i].append('blue')
for i in range(10):
    board1.append([])
    for j in range(10):
        board1[i].append('blue')
for i in range(10):
    board2.append([])
    for j in range(10):
        board2[i].append('blue')
size=RESIZABLE
screen=pygame.display.set_mode((1200,600),size,32)
font=pygame.font.SysFont('Algerian',64)
smallfont=pygame.font.SysFont('Algerian',32)
text=''
position1=(220,200)
position2=(700,200)
board_size=400
text_pos=(200,650)
placed_player1=0
AIRCRAFT_CARRIER=ship('Aircraft Carrier',5)
BATTLESHIP=ship('Battleship',4)
SUBMARINE=ship('Submarine',3)
CRUSIER=ship('Cruiser',3)
DESTROYER=ship('Destroyer',2)
CAIRCRAFT_CARRIER=ship('Aircraft Carrier',5)
CBATTLESHIP=ship('Battleship',4)
CSUBMARINE=ship('Submarine',3)
CCRUSIER=ship('Cruiser',3)
CDESTROYER=ship('Destroyer',2)
player1_ships=[AIRCRAFT_CARRIER,BATTLESHIP,SUBMARINE,CRUSIER,DESTROYER]
both_placed=0
ship_number=1
first=0
placed_player2=0
player2_ships=[CAIRCRAFT_CARRIER,CBATTLESHIP,CSUBMARINE,CCRUSIER,CDESTROYER]
move=1
flag=0
player1=5
player2=5
diff=0
while True:
    screen.fill((0,0,0))
    screen.blit(font.render('BATTLESHIPS',True,(255,0,0)),(420,20))
    if player1==0:
        screen.blit(font.render('Player 2 won the war.',True,(255,0,0)),(350,300))
        pygame.display.update()
        break
    elif player2==0:
        screen.blit(font.render('Player 1 won the war.',True,(255,0,0)),(350,300))
        pygame.display.update()
        break
    if flag==0:
        if not placed_player1:
            screen.blit(smallfont.render('Player 1: Place your '+player1_ships[ship_number-1].name,True,(255,0,0)),(300,120))
        elif not placed_player2:
            screen.blit(smallfont.render('Player 2: Place your '+player1_ships[ship_number-1].name,True,(255,0,0)),(300,120))
        elif both_placed:
            if move==1:
                screen.blit(smallfont.render('Player 1: Your move.',True,(255,0,0)),(300,120))
                pygame.draw.rect(screen,(255,255,255),(position2[0]-10,position2[1]-10,board_size+20,board_size+20))
                diff=0
            elif move==2:
                screen.blit(smallfont.render('Player 2: Your move.',True,(255,0,0)),(300,120))
                pygame.draw.rect(screen,(255,255,255),(position1[0]-10,position1[1]-10,board_size+20,board_size+20))
                diff=1
        if not placed_player1:
            display(hboard1,position1)
        if both_placed:
            display(board1,position1)
            display(board2,position2)
        screen.blit(font.render('Player 1',True,(255,0,0)),(position1[0]+30,position1[1]+board_size+10))
        screen.blit(font.render('Player 2',True,(255,0,0)),(position2[0]+30,position2[1]+board_size+10))
    elif flag==1:
        screen.blit(smallfont.render('1. This game is based on a game called Battleships.',True,(255,0,0)),(50,100))
        screen.blit(smallfont.render('2. you have to place your ships without showing it to your opponent.',True,(255,0,0)),(50,100+smallfont.get_linesize()))
        screen.blit(smallfont.render('3. You can place your ships by clicking the buttons on the mouse.',True,(255,0,0)),(50,100+2*smallfont.get_linesize()))       
    for event in pygame.event.get():
        if event.type==quit:
            pygame.display.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_RETURN:
                pygame.display.quit()
                exit()
            if event.key==K_SPACE:
                if size==FULLSCREEN:
                    size=RESIZABLE
                elif size==RESIZABLE:
                    size=FULLSCREEN
                pygame.display.set_mode((1366,768),size,32)
            if event.key==K_h and flag==0:
                flag=1
            elif event.key==K_h and flag==1:
                flag=0            
        if event.type==MOUSEBUTTONDOWN:
            if not placed_player1:
                ship=player1_ships[ship_number-1]
                x,y=pygame.mouse.get_pos()
                if x<position1[0]+board_size and x>position1[0] and y<position1[1]+board_size and y>position1[1]:
                    if event.button==1:
                        ship.state='HORIZONTAL'
                        ship.ver=int((y-position1[1])/40),int((x-position1[0])/40)
                        if valid(ship,hboard1):
                            for i in range(ship.length):
                                hboard1[int((x-position1[0])/40)+i][int((y-position1[1])/40)]=ship.name[0]
                        else:
                            continue
                    elif event.button==3:
                        ship.state='VERTICAL'
                        ship.ver=int((y-position1[1])/40),int((x-position1[0])/40)
                        if valid(ship,hboard1):
                            for i in range(ship.length):
                                hboard1[int((x-position1[0])/40)][int((y-position1[1])/40)+i]=ship.name[0]
                        else:
                            continue;
                    if ship_number<5:
                        ship_number+=1
                    elif ship_number==5:
                        display(hboard1,position1)
                        pygame.draw.rect(screen,(0,0,0),(300,120,600,smallfont.get_linesize()))
                        screen.blit(smallfont.render('Player 1: your ships have been placed',True,(255,0,0)),(300,120))
                        pygame.display.update()
                        time.sleep(0.5)
                        pygame.draw.rect(screen,(0,0,0),(300,120,700,smallfont.get_linesize()))
                        screen.blit(smallfont.render('Now Player 2: place your ships',True,(255,0,0)),(300,120))
                        pygame.display.update()
                        time.sleep(1)
                        ship_number=1
                        placed_player1=1
            elif both_placed:
                if event.type==MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if move==1:
                        if x<position2[0]+board_size and x>position2[0] and y<position2[1]+board_size and y>position2[1]:
                            if event.button==1:
                                if hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]=='A':
                                    ship=CAIRCRAFT_CARRIER
                                elif hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]=='B':
                                    ship=CBATTLESHIP
                                elif hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]=='S':
                                    ship=CSUBMARINE
                                elif hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]=='C':
                                    ship=CCRUSIER
                                elif hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]=='D':
                                    ship=CDESTROYER
                                elif hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]=='blue':
                                    board2[int((x-position2[0])/40)][int((y-position2[1])/40)]='green'
                                    hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]='green'
                                    move=2
                                #elif hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]=='H':
                                    #move=1
                                if hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]!='blue' and hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]!='green' and hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]!='H'and hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]!='sunk':
                                    board2[int((x-position2[0])/40)][int((y-position2[1])/40)]='H'
                                    hboard2[int((x-position2[0])/40)][int((y-position2[1])/40)]='H'
                                    if ship.length>0:
                                        ship.length-=1
                                    if ship.length==0:
                                        player2-=1
                                        for i in range(ship.length_temp):
                                            if ship.state=='HORIZONTAL':
                                                hboard2[ship.ver[1]+i][ship.ver[0]]='sunk'
                                                board2[ship.ver[1]+i][ship.ver[0]]='sunk'
                                            else:
                                                hboard2[ship.ver[1]][ship.ver[0]+i]='sunk'
                                                board2[ship.ver[1]][ship.ver[0]+i]='sunk'  
                                        screen.blit(smallfont.render('Opponent\'s '+ship.name+' has been sunk.',True,(255,0,0)),(300,700))
                                        player2_ships.remove(ship)
                                        display(board2,position2)
                                        pygame.display.update()
                                        time.sleep(1)
    if placed_player1 and not placed_player2: 
        ship=player2_ships[ship_number-1]
        i=randint(0,9)
        j=randint(0,9)
        ship.state=choice(['HORIZONTAL','VERTICAL'])
        ship.ver=(j,i)
        if valid(ship,hboard2):
            for i in range(ship.length_temp):
                if ship.state=='HORIZONTAL':
                    hboard2[ship.ver[1]+i][ship.ver[0]]=ship.name[0]
                else:
                    hboard2[ship.ver[1]][ship.ver[0]+i]=ship.name[0]
            if ship_number<5:
                ship_number+=1
            elif ship_number==5:
                pygame.draw.rect(screen,(0,0,0),(300,120,600,smallfont.get_linesize()))
                screen.blit(smallfont.render('Now it\'s the time of war.',True,(255,0,0)),(300,120))
                pygame.display.update()
                time.sleep(1)
                ship_number=1
                placed_player2=1;
                both_placed=1
    if diff==1:
        lst=[]
        maximum=0
        for i in range(10):
            for j in range(10):
                if prob[i][j]>maximum:
                    maximum=prob[i][j]
                    lst=[(i,j)]
                elif prob[i][j]==maximum:
                    lst.append((i,j))
        (i,j)=choice(lst)
        if hboard1[i][j]=='blue':
            board1[i][j]='green'
            hboard1[i][j]='green'
            move=1
            continue
        elif hboard1[i][j]=='A':
            ship=AIRCRAFT_CARRIER
        elif hboard1[i][j]=='B':
            ship=BATTLESHIP
        elif hboard1[i][j]=='S':
            ship=SUBMARINE
        elif hboard1[i][j]=='C':
            ship=CRUSIER
        elif hboard1[i][j]=='D':
            ship=DESTROYER
        if hboard1[i][j]!='blue' and hboard1[i][j]!='green' and hboard1[i][j]!='H' and hboard1[i][j]!='sunk':
            board1[i][j]='H'
            hboard1[i][j]='H'
            if ship.length>0:
                ship.length-=1
            if ship.length==0:
                for i in range(ship.length_temp):
                    if ship.state=='HORIZONTAL':
                        board1[ship.ver[1]+i][ship.ver[0]]='sunk'
                        hboard1[ship.ver[1]+i][ship.ver[0]]='sunk'
                    else:
                        board1[ship.ver[1]][ship.ver[0]+i]='sunk'
                        hboard1[ship.ver[1]][ship.ver[0]+i]='sunk'
                screen.blit(smallfont.render('Your\'s '+ship.name+' has been sunk.',True,(255,0,0)),(300,700))
                player1-=1
                player1_ships.remove(ship)
                display(board1,position1)
                pygame.display.update()
                time.sleep(1)
    calculate(board1,prob,player1_ships)
    pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                pygame.display.set_mode((1366,768),RESIZABLE,32)
            
