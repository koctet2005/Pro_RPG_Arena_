import pygame
import os
import random


pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('data/c245b81d72ab0bb.wav')
pygame.mixer.music.play(-1)

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    image.set_colorkey((0, 255, 0))
    return(image)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  150, random.randrange(150, 255, 15), 105)
RED =   (255,   0,   0)
fGreen = GREEN
weapons1 = ['zombie hand:4', 'small sword:5', 'daggers:6']
armor1 = ['wooden armor:2', 'plastic armor:3', 'chain armor:4']
weapons2 = ['magic book:7', 'hook:8', 'knuckle:9']
armor2 = ['iron armor:5', 'magic water armor:6', 'ninja clothes:7']
lvl = 0
damage = 2
armor = 1
life = 100
next_l = 0
money = 0
hpx, hpy = 400, 400
attack = None
x, u = None, None
running_sprite = True
size = width, height = [800, 800]
transportC = None
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    image1_down = load_image('war1_down.png')
    image2_down = load_image('war2_down.png')
    image3_down = load_image('war3_down.png')
    image1_up = load_image('war1_up.png')
    image2_up = load_image('war2_up.png')
    image3_up = load_image('war3_up.png')
    image1_right = load_image('war1_right.png')
    image2_right = load_image('war2_right.png')
    image3_right = load_image('war3_right.png')
    image1_left = load_image('war1_left.png')
    image2_left = load_image('war2_left.png')
    image3_left = load_image('war3_left.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Player.image1_down
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.tik = 0
        self.lvl = 0
        self.damage = damage
        self.armor = armor
        self.life = life

    def update(self, args):
        global lvl
        global damage
        global armor
        global life
        global transportC
        global fGreen
        global next_l
        global hpx, hpy
        global running_sprite
        global attack
        self.lvl = lvl
        self.damage = damage
        self.armor = armor
        self.life = life
        self.money = money
        if running_sprite == True:
            hpx, hpy = self.rect.x, self.rect.y
            self.tik += 1
            if self.tik == 41:
                self.tik = 0
            if go_up == 1:
                if self.tik == 10:
                    self.image = Player.image2_up
                if self.tik == 20:
                    self.image = Player.image1_up
                if self.tik == 30:
                    self.image = Player.image3_up
                if self.tik == 40:
                    self.image = Player.image1_up
                if go_fast == 1:
                    self.rect.y -= 3
                elif go_fast == 0:
                    self.rect.y -= 1
            elif go_down == 1:
                if self.tik == 10:
                    self.image = Player.image2_down
                if self.tik == 20:
                    self.image = Player.image1_down
                if self.tik == 30:
                    self.image = Player.image3_down
                if self.tik == 40:
                    self.image = Player.image1_down
                if go_fast == 1:
                    self.rect.y += 3
                elif go_fast == 0:
                    self.rect.y += 1
            elif go_left == 1:
                if self.tik == 10:
                    self.image = Player.image2_left
                if self.tik == 20:
                    self.image = Player.image1_left
                if self.tik == 30:
                    self.image = Player.image3_left
                if self.tik == 40:
                    self.image = Player.image1_left
                if go_fast == 1:
                    self.rect.x -= 3
                elif go_fast == 0:
                    self.rect.x -= 1
            elif go_right == 1:
                if self.tik == 10:
                    self.image = Player.image2_right
                if self.tik == 20:
                    self.image = Player.image1_right
                if self.tik == 30:
                    self.image = Player.image3_right
                if self.tik == 40:
                    self.image = Player.image1_right
                if go_fast == 1:
                    self.rect.x += 3
                elif go_fast == 0:
                    self.rect.x += 1
            
            if self.rect.x < -32:
                transportC = 'l'
                self.rect.x = width - 1
                lvl += 1
                fGreen = (105, random.randrange(150, 255, 15), 105)
            elif self.rect.x > width:
                transportC = 'r'
                self.rect.x = -31
                lvl += 1
                fGreen = (105, random.randrange(150, 255, 15), 105)
            elif self.rect.y < -46:
                transportC = 'u'
                self.rect.y = height - 1
                lvl += 1
                fGreen = (105, random.randrange(150, 255, 15), 105)
            elif self.rect.y > height:
                transportC = 'd'
                self.rect.y = -45
                lvl += 1
                fGreen = (105, random.randrange(150, 255, 15), 105)
            
            a1 = pygame.font.Font(None, 25)
            b1 = a1.render(f'Level: {self.lvl}', 1, RED)
            xt1 = 700
            yt1 = 10
            screen.blit(b1, (xt1, yt1))
            
            a2 = pygame.font.Font(None, 25)
            b2 = a2.render(f'Damage: {self.damage}', 1, RED)
            xt2 = 550
            yt2 = 10
            screen.blit(b2, (xt2, yt2))
            
            a3 = pygame.font.Font(None, 25)
            b3 = a3.render(f'Armor: {self.armor}', 1, RED)
            xt3 = 400
            yt3 = 10
            screen.blit(b3, (xt3, yt3))
            
            a4 = pygame.font.Font(None, 25)
            b4 = a4.render(f'Life: {self.life}', 1, RED)
            xt4 = 250
            yt4 = 10
            screen.blit(b4, (xt4, yt4))
            
            a5 = pygame.font.Font(None, 25)
            b5 = a5.render(f'Money: {self.money}$', 1, RED)
            xt5 = 100
            yt5 = 10
            screen.blit(b5, (xt5, yt5))
            
            if next_l == 2:
                transportC = None
                next_l = 0
                
        if life <= 0:
            attack = None
            running_sprite = False
            a0 = pygame.font.Font(None, 50)
            b0 = a0.render(f'Game over', 1, RED)
            xt0 = 500
            yt0 = 510
            screen.blit(b0, (xt0, yt0))
        
        if lvl == 21 and money >= 40:
            running_sprite = False
            ag = pygame.font.Font(None, 50)
            bg = ag.render(f'You win', 1, RED)
            xtg = 500
            ytg = 510
            screen.blit(bg, (xtg, ytg))
        elif lvl == 21 and money < 40:
            running_sprite = False
            aq = pygame.font.Font(None, 50)
            bq = aq.render(f'You lose', 1, RED)
            xtq = 500
            ytq = 510
            screen.blit(bq, (xtq, ytq))

class Chest(pygame.sprite.Sprite):
    image1 = load_image('chest1.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Chest.image1
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000

    def update(self, args):
        global transportC
        global next_l
        global lvl
        global weapons1
        global damage
        global money
        global armor
        global x, u
        if running_sprite == True:
            blocks_hit_list = pygame.sprite.spritecollide(self, all_sprites, False)
            if len(blocks_hit_list) > 1:
                if '[<Player sprite(in 1 groups)>, <Chest sprite(in 1 groups)>]' == str(blocks_hit_list):
                    self.rect.x = -1000
                    self.rect.y = -1000
                    if lvl // 10 == 0:
                        j = random.random()
                        if j >= 0.5:
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                x = weapons1[0].split(':')
                            elif 60 < rnd < 90:
                                x = weapons1[1].split(':')
                            elif 90 < rnd < 100:   
                                x = weapons1[2].split(':')

                            if damage < int(x[1]):
                                damage = int(x[1])
                                print('-------------------------')
                                print(f'you picked {x[0]} with damage {x[1]}')
                                print('-------------------------')
                            elif damage >= int(x[1]):
                                m = (int(x[1]) // 2)
                                money += m
                                print('-------------------------')
                                print(f'you find {m}$')
                                print('-------------------------')
                                
                        elif j < 0.5:
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                u = armor1[0].split(':')
                            elif 60 < rnd < 90:
                                u = armor1[1].split(':')
                            elif 90 < rnd < 100:   
                                u = armor1[2].split(':')

                            if armor < int(u[1]):
                                armor = int(u[1])
                                print('-------------------------')
                                print(f'you picked {u[0]} with protection {u[1]}')
                                print('-------------------------')
                            elif armor >= int(u[1]):
                                lm = (int(u[1]) // 2)
                                money += lm
                                print('-------------------------')
                                print(f'you find {lm}$')
                                print('-------------------------')
                    
                    if lvl // 10 == 1 or lvl == 20:
                        j = random.random()
                        if j >= 0.5:
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                x = weapons2[0].split(':')
                            elif 60 < rnd < 90:
                                x = weapons2[1].split(':')
                            elif 90 < rnd < 100:   
                                x = weapons2[2].split(':')

                            if damage < int(x[1]):
                                damage = int(x[1])
                                print('-------------------------')
                                print(f'you picked {x[0]} with damage {x[1]}')
                                print('-------------------------')
                            elif damage >= int(x[1]):
                                m = (int(x[1]) // 3)
                                money += m
                                print('-------------------------')
                                print(f'you find {m}$')
                                print('-------------------------')

                        elif j < 0.5:
                            rnd = random.randint(1, 100)
                            if 0 < rnd < 60:
                                u = armor2[0].split(':')
                            elif 60 < rnd < 90:
                                u = armor2[1].split(':')
                            elif 90 < rnd < 100:   
                                u = armor2[2].split(':')

                            if armor < int(u[1]):
                                armor = int(u[1])
                                print('-------------------------')
                                print(f'you picked {u[0]} with protection {u[1]}')
                                print('-------------------------')
                            elif armor >= int(u[1]):
                                lm = (int(u[1]) // 3)
                                money += lm
                                print('-------------------------')
                                print(f'you find {lm}$')
                                print('-------------------------')
                    
                            
                           
            if transportC != None:
                self.rect.x = random.randrange(40, 730)
                self.rect.y = random.randrange(40, 730)
                next_l += 1
            
        
class Skeletron(pygame.sprite.Sprite):
    image1_down = load_image('skel1_down.png')
    image2_down = load_image('skel2_down.png')
    image3_down = load_image('skel3_down.png')
    image1_up = load_image('skel1_up.png')
    image2_up = load_image('skel2_up.png')
    image3_up = load_image('skel3_up.png')
    image1_right = load_image('skel1_right.png')
    image2_right = load_image('skel2_right.png')
    image3_right = load_image('skel3_right.png')
    image1_left = load_image('skel1_left.png')
    image2_left = load_image('skel2_left.png')
    image3_left = load_image('skel3_left.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Skeletron.image1_down
        self.rect = self.image.get_rect()
        self.rect.x = -400
        self.rect.y = -400
        self.tik = 0
        self.damage = 1
        self.armor = 1
        self.life = 5
        self.k = 0
        self.at = 0
        self.bat = 1
        self.no = 0

    def update(self, args):
        global transportC
        global next_l
        global attack
        global life
        global money
        
        if running_sprite == True:
            blocks_hit_list = pygame.sprite.spritecollide(self, all_sprites, False)
            if len(blocks_hit_list) > 1:
                if '[<Player sprite(in 1 groups)>, <Skeletron sprite(in 1 groups)>]' == str(blocks_hit_list):
                    self.k = 1
            else:
                self.k = 0
            
            if transportC != None:
                self.rect.x = random.randrange(40, 710)
                self.rect.y = random.randrange(40, 710)
                self.damage = (lvl // 5) + 1
                self.armor = (lvl // 10) + 1
                self.life = (lvl // 2) + 5
                next_l += 1
            
            self.tik += 1
            if self.tik == 41:
                self.tik = 0
            if (self.rect.x - 250 < hpx < self.rect.x + 250 and self.rect.y - 250 < hpy < self.rect.y + 250) and self.k == 0:
                if hpx > self.rect.x:
                    self.rect.x += 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_right
                    if self.tik == 40:
                        self.image = Skeletron.image3_right
                elif hpx < self.rect.x:
                    self.rect.x -= 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_left
                    if self.tik == 40:
                        self.image = Skeletron.image3_left
                elif hpy > self.rect.y:
                    self.rect.y += 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_down
                    if self.tik == 40:
                        self.image = Skeletron.image3_down
                elif hpy < self.rect.y:
                    self.rect.y -= 1
                    if self.tik == 20:
                        self.image = Skeletron.image2_up
                    if self.tik == 40:
                        self.image = Skeletron.image3_up
            elif self.k == 1:
                attack = 'skel'
                if attack == 'skel':
                    if self.life <= 0:
                        self.rect.x = 3000
                        self.rect.y = 3000
                        attack = None
                    if args.type == pygame.MOUSEBUTTONDOWN and self.bat == 1:
                        self.bat = 0
                        self.life -= damage
                        print('-------------------------')
                        print(f'you caused damage {damage}')
                        if self.life > 0:
                            print(f'enemy lives {self.life}')
                        else:
                            print(f'enemy dies')
                            print('you find 2$')
                            money += 2
                        print('-------------------------')
                    self.at += 1
                    if self.at == 200:
                        iii = random.randint(0, 100)
                        if armor > iii > 0:
                            life -= self.damage // 2
                            print('-------------------------')
                            print(f'you get damage {self.damage // 2}')
                            print('-------------------------')
                        else:
                            life -= self.damage
                            print('-------------------------')
                            print(f'you get damage {self.damage}')
                            print('-------------------------')
                        self.at = 0
                        self.bat = 1
            elif self.k == 0:
                attack = None
        else:
            self.image = Skeletron.image1_down
                


Player(all_sprites)
Chest(all_sprites)
Skeletron(all_sprites)
pygame.display.set_caption("PythonRPG")
img = pygame.image.load('data\icon.png')
pygame.display.set_icon(img)



go_up = 0
go_down = 0
go_left = 0
go_right = 0
go_fast = 0
fps = 120
running = True
clock = pygame.time.Clock()
 
while running:
    clock.tick(fps)
    screen.fill(fGreen)
    pygame.draw.polygon(screen, BLACK, [[40, 40], [760, 40], [760, 760], [40, 760]], 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                go_up = 1
            if event.key == pygame.K_s:
                go_down = 1
            if event.key == pygame.K_a:
                go_left = 1
            if event.key == pygame.K_d:
                go_right = 1
            if event.key == pygame.K_LSHIFT:
                go_fast = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                go_up = 0
            if event.key == pygame.K_s:
                go_down = 0
            if event.key == pygame.K_a:
                go_left = 0
            if event.key == pygame.K_d:
                go_right = 0
            if event.key == pygame.K_LSHIFT:
                go_fast = 0
    
    all_sprites.draw(screen)
    all_sprites.update(event)
    
    pygame.display.flip()

pygame.quit()