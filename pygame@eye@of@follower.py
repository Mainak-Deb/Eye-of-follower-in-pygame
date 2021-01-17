import time,math,random
import pygame,sys
import pygame,sys
from pygame.locals import *
import math

pygame.init()
screenlenth=700
screen=pygame.display.set_mode((screenlenth,screenlenth))
icon=pygame.image.load('Eye-Lens-PNG-File.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("Planetary rotation")

lens=pygame.image.load('Eye-Lens-PNG-File.png')
lens=pygame.transform.scale(lens,(100,100))


x=int(screenlenth/2)
y=int(screenlenth/2)
od=40
ind=20
a=int(screenlenth*2/3)
r=300
ex=0
m=2
ea=0
ma=0
eye_height=80

prev_x=x

def polar_elipse(a,b,t):
    x1=a*math.cos(t*math.pi/180)
    y1=b*math.sin(t*math.pi/180)
    return (x+x1,y+y1)
    
def polar_circle(r,t):
    x1=r*math.cos(t*math.pi/180)
    y1=r*math.sin(t*math.pi/180)
    return (x+x1,y+y1)

def elipse_height(lx,posy):
    h=math.sqrt((1-(lx/a)**2)*(eye_height)**2)
    ly=((posy-y)*(h-(lens.get_width()/2))/y)
    return ly
    
def mod(x):
    if x<0:return (-1*x)
    else: return x
    
running=True

while running:
        screen.fill((255,255,255))  
      
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        mice=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        posx=mice[0]
        posy=mice[1]   
        if(mod(prev_x-posx)>30):colour=(255,0,0)
        else:colour=(255,255,255)
        pygame.draw.circle(screen,colour,(x,y),int(screenlenth/3))
        lens_radius=int(130-(mod(posx-x)/10))

        lens_copy=pygame.transform.scale(lens,(lens_radius,lens_radius))
        lx=((posx-x)*(x-a/4-(lens_copy.get_width()/2))/x)

        
        p=mod(elipse_height(lx,posy))+(lens_copy.get_width()/4)
       
        screen.blit(lens_copy,(int(x-(lens_copy.get_width()/2)+lx),int(y-(lens_copy.get_height()/2)+elipse_height(lx,posy))))
        
      
        b=((screenlenth/3)-p)/ind
        
        for i in range(0,90):
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,i),polar_elipse(a/2,p,i+1),polar_circle(int(screenlenth/3),i+1),polar_circle(int(screenlenth/3),i)])       
            j=i+270
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,j),polar_elipse(a/2,p,j+1),polar_circle(int(screenlenth/3),j+1),polar_circle(int(screenlenth/3),j)])       
            j=i+90
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,j),polar_elipse(a/2,p,j+1),polar_circle(int(screenlenth/3),j+1),polar_circle(int(screenlenth/3),j)])       
            j=i+180
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,j),polar_elipse(a/2,p,j+1),polar_circle(int(screenlenth/3),j+1),polar_circle(int(screenlenth/3),j)])       

            
        
        
        for i in range(od):
              pygame.draw.circle(screen,(0,0,0),(x,y),int((screenlenth/3)+((i*((screenlenth*(1/(2**(.5))-(1/3)))/od)+ex)%((screenlenth*(1/(2**(.5))-(1/3)))))),2)
              if(i<ind):
                  if((p+i*b)>2):pygame.draw.ellipse(screen,(255,255,255),(x-a/2,y-((p+(i*b))),a,2*(p+(i*b))),1)
                  else:pygame.draw.ellipse(screen,(255,255,255),(x-a/2,y-2,a,4))
        
        
        ex+=0.4
        prev_x=posx
        pygame.display.update()       
        
        