import pygame
from pygame.locals import * #用QUIT
from sys import exit    #用EXIT來QUIT
""" #確認你的顯示器支援哪些screen size
import pygame
pygame.init()
print(pygame.display.list_modes())
 """
pygame.init()
screen = pygame.display.set_mode((1280,720))
background_image_filename = 'check_YES.png' #背景圖片
background = pygame.image.load(background_image_filename).convert()#將背景圖片load進去

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           exit()
    if event.type == KEYDOWN:
        if event.key == K_f:    #當按下F鍵時
            print("fc",Fulscreen)
            Fullscreen = not Fullscreen #如果為視窗模式就變全螢幕，反之
            print("nfc",Fullscreen)
            if Fullscreen:
                screen = pygame.display.set_mode((1280,720), FULLSCREEN)
            else:
                screen = pygame.display.set_mode((1280,720))
 
    screen.blit(background, (0,0))#重新畫上背景
    pygame.display.update()