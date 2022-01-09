import json
from pygame.constants import *
from win32api import GetSystemMetrics
import pygame
import random
import time
pygame.init()
pygame.display.set_caption("UNO")
Height=GetSystemMetrics(1)
Width=GetSystemMetrics(0)
screen = pygame.display.set_mode((Width,Height),pygame.RESIZABLE)
fps = 60
cards = ['0_yellow','1_yellow','2_yellow','3_yellow','4_yellow','5_yellow','6_yellow','7_yellow','8_yellow','9_yellow','1_yellow','2_yellow','3_yellow','4_yellow','5_yellow','6_yellow','7_yellow','8_yellow','9_yellow',
                    '0_green','1_green','2_green','3_green','4_green','5_green','6_green','7_green','8_green','9_green','1_green','2_green','3_green','4_green','5_green','6_green','7_green','8_green','9_green',
                    '0_red','1_red','2_red','3_red','4_red','5_red','6_red','7_red','8_red','9_red','1_red','2_red','3_red','4_red','5_red','6_red','7_red','8_red','9_red',
                    '0_blue','1_blue','2_blue','3_blue','4_blue','5_blue','6_blue','7_blue','8_blue','9_blue','1_blue','2_blue','3_blue','4_blue','5_blue','6_blue','7_blue','8_blue','9_blue',
                    'take_2_yellow','take_2_yellow','take_2_green','take_2_green','take_2_red','take_2_red','take_2_blue','take_2_blue',
                    'turn_yellow','turn_yellow','turn_green','turn_green','turn_red','turn_red','turn_blue','turn_blue',
                    'skip_yellow','skip_yellow','skip_green','skip_green','skip_red','skip_red','skip_blue','skip_blue',
                    'color_switch','color_switch','color_switch','color_switch','take_four','take_four','take_four','take_four',
]
jString = json.dumps({'players':[]})
jFile = open(r"D:\Python\Uno\json_files\players.json", "w")
jFile.write(jString)
jFile.close()
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
    screen.blit(pygame.transform.scale(pygame.image.load('D:\\Python\\Uno\\Spielkarten\\waitingroom.png'), (Width,Height)), (0,0))
    try:
        file=open(r"D:\Python\Uno\json_files\players.json","r")
        d = json.load(file)
        file.close()
        pic_pos=()
        for a in range(len(d["players"])):
            if a == 0:
                pic_pos=(520,300)
            elif a == 1:
                pic_pos = (1285,315)
            elif  a == 2:
                pic_pos = (110,375)
            elif a == 3:
                pic_pos = (1575,425)
            screen.blit(pygame.transform.scale(pygame.image.load(r"D:\Python\Uno\Player_Pictures\P_"+str(a+1)+'.png'),(100,100)), pic_pos)
    except Exception:
        pass
    pygame.display.flip()
    try:
        file = open(r"D:\Python\Uno\json_files\player_input.txt","r")
        content = file.read()
        file.close()
        if content == "True":
            time.sleep(5)
            file=open(r"D:\Python\Uno\json_files\players.json","r")
            data = json.load(file)
            file.close()
            max_player = len(data["players"])
            time.sleep(1)
            break
    except Exception:
        pass
played_cards=[]
player_deck=[
    ['No','Entry'],
    ['No','Entry'],
    ['No','Entry'],
    ['No','Entry']
]
if max_player >=1:
    player_deck[0]=[]
if max_player >=2:
    player_deck[1]=[]
if max_player >=3:
    player_deck[2]=[]
if max_player >=4:
    player_deck[3]=[]
want_to_play=""
interupt = False
reverse=False
switch=""
class comunication():
    def __init__(self):
        self.text=""
    def write_file(self,path,com):
        file = open(path,"w")
        file.write(com)
        file.close()
    def read_file(self,path):
        if path.split(".")[-1] == "txt":
            file = open(path,"r")
            content=file.read()
            file.close()
            return content
        elif path.split(".")[-1]=="json":
            file=open(r"D:\Python\Uno\json_files\players.json")
            data = json.load(file)
            file.close()
            return data
    def reset_file(self,path):
        file = open(path,"w")
        file.write("")
        file.close()
    def write_cards(self):
        jsonString = json.dumps(player_deck)
        jsonFile = open(r"D:\Python\Uno\json_files\player_cards.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    def reset_json(self,path):
        jsonString = json.dumps("")
        jsonFile = open(path, "w")
        jsonFile.write(jsonString)
        jsonFile.close()
class card():
    def __init__(self):
        self.pywin=pywind()
        self.x=None
        self.x_safe=None
        self.card_valid = False
        self.valid_input = None
    def place_first_card(self):
        played_cards.append(cards[-1])
        del cards[-1]
    def reshuffle(self,cards,played_cards):
        if not len(cards) > 2:
            cards=played_cards
            played_cards=[]
            self.shuffle()
            print("reshuffle")
        else:
            pass
    def shuffle(self):
        for _ in range(1000):
            random.shuffle(cards)
    def get_new_card(self,player,turn):
        player_deck[player-1].append(cards[0])
        sp=0
        if turn ==1:
            sp = spieler
        else: 
            if max_player ==2:
                if spieler == 1:
                    sp=spieler+1
                else:
                    sp=spieler-1  
            else: 
                if not reverse:
                    if spieler +1 > max_player:
                        sp=1
                    else:
                        sp=spieler+1
                else:
                    if spieler -1 < 0:
                        sp=max_player
                    else:
                        sp=spieler-1 
        com.write_file(r"D:\Python\Uno\json_files\com.txt","2. "+str(sp)+" Du_hast_die_Karte_"+cards[0]+"_gezogen")
        time.sleep(2)
        del cards[0]
    def get_valid_input(self,player):
        return self.valid_input
    def place_card(self,player):
        self.x = want_to_play
        self.x_safe = self.x
        try: 
            self.x_safe = int(self.x_safe)
        except ValueError:
            pass
        if self.x_safe == 3:
            self.get_new_card(player,1)
        else:
            for i in range(len(player_deck[spieler-1])):
                if self.x == player_deck[spieler-1][i-1]:
                    self.pywin.draw_card(self.x)
                    played_cards.append(self.x)
                    del player_deck[spieler-1][i-1]
                    self.card_valid=True
                    self.valid_input=True
                    break
            if not self.card_valid:
                com.write_file(r"D:\Python\Uno\json_files\com.txt","2. "+str(spieler)+" Diese_Karte_ist_nicht_in_deinem_deck_enthalten")
                time.sleep(1)
                self.valid_input = False
            else:
                self.card_valid = False
    def get_four_cards(self,spieler):
        if not reverse:
            for i in range(r.get_more_four()):
                if spieler +1 > max_player:
                    c.get_new_card(1,2)
                else:
                    c.get_new_card(spieler + 1,2)
        else:
            for i in range(r.get_more_four()):
                if spieler  > 1:
                    c.get_new_card(spieler - 1,2)
                else:
                    c.get_new_card(max_player,2)
    
    def get_more_cards(self,spieler,more_four):
        for _ in range(4):
            if not reverse:
                if spieler +1 > max_player:
                    c.get_new_card(1,2)
                else:
                    c.get_new_card(spieler + 1,2)
            else:
                if spieler  > 1:
                    c.get_new_card(spieler -1,2)
                else:
                    c.get_new_card(max_player,2)
        for _ in range(more_four-4):
            cards.append(player_deck[spieler-1][-1])
            del player_deck[spieler-1][-1]
            if not reverse:
                if spieler  +1 > max_player:
                    c.get_new_card(1,2)
                else:
                    c.get_new_card(spieler+1,2)
            else:
                if spieler >1:
                    c.get_new_card(spieler -1,2)
                else:
                    c.get_new_card(max_player,2)
                    
    def get_two_cards(self,spieler):
        if not reverse:
            for _ in range(r.get_more_two()):
                if spieler +1 > max_player:
                    c.get_new_card(1,2)
                else:
                    c.get_new_card(spieler + 1,2)
        else:
            for _ in range(r.get_more_two()):
                if spieler  > 1:
                    c.get_new_card(spieler - 1,2)
                else:
                    c.get_new_card(max_player,2)
    def get_more_two_cards(self,spieler,more_two):
        for _ in range(2):
            if not reverse:
                if spieler +1 > max_player:
                    c.get_new_card(1,2)
                else:
                    c.get_new_card(spieler + 1,2)
            else:
                if spieler  > 1:
                    c.get_new_card(spieler -1,2)
                else:
                    c.get_new_card(max_player,2)
        for _ in range(more_two-2):
            cards.append(player_deck[spieler-1][-1])
            del player_deck[spieler-1][-1]
            if not reverse:
                if spieler  +1 > max_player:
                    c.get_new_card(1,2)
                else:
                    c.get_new_card(spieler+1,2)
            else:
                if spieler >1:
                    c.get_new_card(spieler -1,2)
                else:
                    c.get_new_card(max_player,2)
class players():
    def __init__(self):
      pass
    def give_cards(self):
        i=0
        while i < 28:
            if max_player >= 1:
                player_deck[0].append(cards[i])
                del cards[i]
            if max_player >=2:
                player_deck[1].append(cards[i+1])
                del cards[i+1]
            if max_player >=3:
                player_deck[2].append(cards[i+2])
                del cards[i+2]
            if max_player>=4:
                player_deck[3].append(cards[i+3])
                del cards[i+3]
            i+=4
class rules():
    def __init__(self):
        self.com=comunication()
        self.count=1
        self.is_color_set=True
        self.is_four=False
        self.last_four=False
        self.last_valid_card=True
        self.won_game = False
        self.last_card=""
        self.valid_card = None
        self.want_to_play=""
        self.more_four=4
        self.more_two=2
        self.color=[]
    def get_valid_card(self):
        return self.valid_card
    def check_won(self):
        if len(player_deck[0])==0 or len(player_deck[1])==0 or len(player_deck[2])==0 or len(player_deck[3])==0:
            self.won_game = True
        else:
            self.won_game= False
    def won(self):
        self.check_won()
        return self.won_game
    def get_more_four(self):
        return self.more_four
    def get_more_two(self):
        return self.more_two
    def set_color(self):
        if self.is_color_set:
            self.is_color_set=False
        else:
            self.is_color_set=True
    def check_card(self,switch):
        self.valid_card=False
        if self.get_last_played_card() == "No card has been played yet":
            self.valid_card = True
        else:
            zw = want_to_play.split("_")
            if self.count==1  and self.last_valid_card==True:
                self.color = self.last_card.split("_")
            if self.count !=1:
                self.count+=1
            if switch !="":
                if self.is_four:
                    self.color=["four",switch]           
                else:
                    self.color=[switch]
                self.count=0
            if self.last_card=="take_four":
                self.is_four=True
            else:
                self.is_four=False
            if self.color[-1] != "blue" and self.color[-1] != "green" and self.color[-1] != "red" and self.color[-1] != "yellow":
                self.more_two=2
                self.valid_card=True
            elif  zw[-1]=="four" and self.color[0]=="four" and not self.is_color_set:
                    self.more_four+=4
                    self.valid_card=True
            elif zw[-1] != "blue" and zw[-1] != "green" and zw[-1] != "red" and zw[-1] != "yellow":
                self.more_two=2
                self.valid_card=True
            else:
                if self.color[-1]== zw[-1]:
                    self.more_four=4
                    try:
                        if zw[1] =="2" and self.color[1]=="2":
                            self.more_two+=2
                        else:
                            self.more_two=2
                        self.valid_card=True
                    except IndexError:
                        self.more_two=2
                        self.valid_card=True
                else:
                    self.valid_card=False
                    if self.color[0]==zw[0]:
                        self.more_four=4
                        if zw[1] =="2" and self.color[1]=="2":
                            self.more_two+=2
                        else:
                            self.more_two=2
                        self.valid_card=True
                    else:
                        self.valid_card=False
                        self.com.write_file(r"D:\Python\Uno\json_files\com.txt","2. "+str(spieler)+" Die_Karte_kann_nicht_auf_die_letzte_gespielt_werden")
                        time.sleep(1)
        self.last_valid_card=self.valid_card
    def get_last_played_card(self):
        try:
            self.last_card = played_cards[-1]
            return self.last_card
        except IndexError:
            return "No card has been played yet"       
class pywind():
    def __init__(self):
        self.com = comunication()
        self.screen = pygame.display.set_mode((Width,Height),pygame.RESIZABLE)
        self.font = pygame.font.SysFont('arial', 32)
        self.name_font = pygame.font.SysFont('inkfree',32)
        self.clock = pygame.time.Clock()
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color_side_cards=pygame.Color('deeppink4')
        self.colour = self.color_inactive
        self.board_color = pygame.Color('indianred4')
        self.innerboard_color=pygame.Color('lightseagreen')
        self.name_color = pygame.Color('firebrick4')
        self.name_pos = (Width/11.9,(Height-1000))
        self.pic_pos = (Width/10,(Height-950))
        self.uno_pos = (Width/10,(Height-750))
        self.uno_pic_scale = (182,117)
        self.pic_scale = (150,150)
        self.done = False
        self.uno_player=[0,0,0,0]
        self.question=""
        self.name=""
        self.wish_color=""
        self.question_pos=(0,0)
        self.card_scale=(175,300)
    def show_question(self,name,question):
        self.question=question
        self.name=name
        if question != " Am Zug ist!":
            self.question_pos=((Width/3.5,30))
        else:
            self.question_pos=((Width/2.1,30))
        text_surface= self.font.render(self.question,False,self.color_active)
        text_surface_name=self.name_font.render(name,False,self.name_color)
        self.screen.blit(text_surface,self.question_pos)
        self.screen.blit(text_surface_name,(Width/2.25,75))
        self.screen.blit(pygame.transform.scale(pygame.image.load(r"D:\Python\Uno\Player_Pictures\P_"+str(spieler)+'.png'), self.pic_scale), ((Width/2.15,120)))
    def get_inputpy(self):
        self.text = ''
        self.done=False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    self.com.reset_json(r"D:\Python\Uno\json_files\player_cards.json")
                    self.com.reset_file(r"D:\Python\Uno\json_files\Start_game.txt")
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.com.reset_json(r"D:\Python\Uno\json_files\player_cards.json")
                        self.com.reset_file(r"D:\Python\Uno\json_files\Start_game.txt")
                        quit()
            self.screen.fill((30, 30, 30))
            self.draw_background()
            self.show_question(self.name,self.question)
            if reverse:
                self.draw_reverse()
            self.draw_wish_color(self.wish_color)
            self.draw_inner_board()
            self.draw_card_stack()
            self.draw_card(card_to_play = played_cards[-1] if played_cards[-1]!=None else "")
            self.draw_board()
            self.draw_player_picture()
            self.draw_uno(self.uno_player)
            pygame.display.flip()
            self.clock.tick(60)
            if com.read_file(r"D:\Python\Uno\json_files\player_input.txt") != "":
                self.done=True
        self.text = com.read_file(r"D:\Python\Uno\json_files\player_input.txt").split("*")[0]
        return self.text
    def draw_board(self):
        pygame.draw.rect(self.screen,self.board_color,(Width/3,Height/3.4,675,450),4)
        pygame.draw.rect(self.screen,self.innerboard_color,(Width/1.85,(Height/3.4)+75,175,300),3)
        pygame.draw.rect(self.screen,self.innerboard_color,(Width/2.5,(Height/3.4)+75,175,300),3)
    def draw_inner_board(self):
        pygame.draw.rect(self.screen,(30,30,30),(Width/3,Height/3.4,675,450),0)
    def draw_card(self,card_to_play):
        if not card_to_play == "":
            path='D:\\Python\\Uno\\Spielkarten\\'+card_to_play+'.png' 
            card_to_drawn=pygame.image.load(path)
            self.screen.blit(pygame.transform.scale(card_to_drawn, self.card_scale), (Width/1.85,(Height/3.4)+75))
    def draw_card_stack(self):
        self.screen.blit(pygame.transform.scale(pygame.image.load('D:\\Python\\Uno\\Spielkarten\\Card_Back.png'), self.card_scale), (Width/2.5,(Height/3.4)+75))
    def draw_reverse(self):
        self.screen.blit(pygame.transform.scale(pygame.image.load('D:\\Python\\Uno\\Spielkarten\\reverse_arrow.png'), (75,75)), (Width/2.4,(Height-900)))
    def draw_wish_color(self,wish_color):
        if not wish_color =="":
            self.screen.blit(pygame.transform.scale(pygame.image.load('D:\\Python\\Uno\\Spielkarten\\'+wish_color+'.png'),(75,75)),(Width/1.75,(Height-900)))
    def draw_background(self):
        self.screen.blit(pygame.transform.scale(pygame.image.load('D:\\Python\\Uno\\Spielkarten\\background.jpg'),(Width,Height)),(0,0))
    def draw_player_picture(self): 
        data = com.read_file(r"D:\Python\Uno\json_files\players.json")
        for a in range(max_player):
            text=data["players"][a].split("#")
            if a == 0:
                self.name_pos = (Width/11.9,(Height-1000))
                self.pic_pos = (Width/10,(Height-950))
            elif a == 1:
                self.name_pos = (Width/1.3,(Height-1000))
                self.pic_pos = (Width/1.25, (Height-950))
            elif  a == 2:
                self.name_pos = (Width/1.3,(Height-275))
                self.pic_pos = (Width/1.25, (Height-225))
            elif a == 3:
                self.name_pos = (Width/11.9,(Height-275))
                self.pic_pos = (Width/10,(Height-225))
            text_surface= self.name_font.render(text[0]+"["+str(len(player_deck[a]))+"]",False,self.name_color)
            self.screen.blit(text_surface,self.name_pos)
            self.screen.blit(pygame.transform.scale(pygame.image.load(r"D:\Python\Uno\Player_Pictures\P_"+str(a+1)+'.png'), self.pic_scale), self.pic_pos)
    def draw_uno(self,pl):
        check=False
        self.set_uno_player()
        for pla in range(len(pl)):
            if pla == 0 and pl[pla] == 1:
                self.uno_pos=(Width/10,(Height-750))
                check=True
            if pla == 1 and pl[pla] == 1:
                self.uno_pos=(Width/1.25,(Height-750))
                check=True
            if pla == 2 and pl[pla] == 1:
                self.uno_pos=(Width/1.25,(Height-100))
                check=True
            if pla == 3 and pl[pla] == 1:
                self.uno_pos=(Width/10,(Height-100))
                check=True
            if check:
                self.screen.blit(pygame.transform.scale(pygame.image.load('D:\\Python\\Uno\\Spielkarten\\uno.png'),self.uno_pic_scale),self.uno_pos)
    def draw_winner_screen(self,reverse,spieler):
        self.screen.fill((30, 30, 30))
        self.screen.blit(pygame.transform.scale(pygame.image.load('D:\\Python\\Uno\\Spielkarten\\crown.png'),(250,150)),(Width/2-100,Height/2-200))
        winner=spieler
        data = self.com.read_file(r"D:\Python\Uno\json_files\players.json")
        text=data["players"][winner-1].split("#")
        self.screen.blit(pygame.transform.scale(pygame.image.load(r"D:\Python\Uno\Player_Pictures\P_"+str(winner)+'.png'), self.pic_scale),(Width/2-50,Height/2-50))
        text_surface= self.name_font.render(text[0],False,self.name_color)
        self.screen.blit(text_surface,(Width/2-100,Height/2+125))
        pygame.display.flip()
        time.sleep(15)
        pygame.quit()
    def set_wish_color(self,col):
        self.wish_color = col
    def set_uno_player(self):
        for count in range(max_player):
            if len(player_deck[count])== 1:
                self.uno_player[count]=1
            else:
                self.uno_player[count]=0
if __name__ == "__main__":
    com=comunication()
    c = card()
    p =players()
    r = rules()
    c.shuffle()
    p.give_cards()
    c.place_first_card() 
    inp = pywind()
    spieler = 1
    spieler_name=""
    second_time=False
    while not r.won():
        c.reshuffle(cards=cards,played_cards=played_cards)
        while True:
            want_to_play_sondercard=["",""]
            spieler_name=com.read_file(r"D:\Python\Uno\json_files\player_cards.json")["players"][spieler-1]
            if not interupt:
                com.write_cards()
                com.write_file(r"D:\Python\Uno\json_files\com.txt","1. "+str(spieler))
            time.sleep(1)
            com.reset_file(r"D:\Python\Uno\json_files\player_input.txt")
            k=None
            spieler_safe = spieler
            inp.show_question(name = str(com.read_file(r"D:\Python\Uno\json_files\player_cards.json")["players"][spieler-1].split("#")[0]),question=" Am Zug ist!")        
            want_to_play=inp.get_inputpy()
            check = want_to_play.split(" ")
            if len(check)>1:
                if check[-1] == "blue" or check[-1] == "yellow" or check[-1] == "green" or check[-1] == "red":
                    want_to_play_sondercard=[check[0],check[-1]]
                    want_to_play=check[0]
                else:
                    interupt=True
                    continue
            if spieler_name != com.read_file(r"D:\Python\Uno\json_files\player_input.txt").split("*")[-1]:
                for player_ in range(len(com.read_file(r"D:\Python\Uno\json_files\player_cards.json")["players"])):
                    if com.read_file(r"D:\Python\Uno\json_files\player_cards.json")["players"][player_] == com.read_file(r"D:\Python\Uno\json_files\player_input.txt").split("*")[-1]:
                        com.write_file(r"D:\Python\Uno\json_files\com.txt","2. "+str(player_+1)+" Du_bist_nicht_am_Zug!")
                        interupt=True
                continue    
            interupt=False
            com.reset_file(r"D:\Python\Uno\json_files\player_input.txt")
            if want_to_play !="3_":
                r.check_card("")
                k=r.get_valid_card()
            elif second_time:
                second_time=False
            else:
                c.get_new_card(spieler,1)
                second_time = True
                com.write_cards()
                com.write_file(r"D:\Python\Uno\json_files\com.txt","1. "+str(spieler))
                continue
            if k:
                inp.set_wish_color("")
                c.place_card(spieler)
                if not c.get_valid_input(spieler):
                    continue
                if want_to_play_sondercard[0] == "take_four":
                    h=want_to_play_sondercard[-1]
                    if h == "red" or h == "yellow" or h == "blue" or h=="green":
                        r.set_color()
                        r.check_card(h)
                        inp.set_wish_color(h)
                    else:
                        com.write_file(r"D:\Python\Uno\json_files\com.txt","2. "+str(spieler)+" Diese_Farbe_steht_nicht_zur_auswahl!")
                        continue
                    r.set_color()
                    if r.get_more_four()==4:
                        c.get_four_cards(spieler)
                    else:
                        ki=r.get_more_four()
                        c.get_more_cards(spieler,ki)
                elif want_to_play == "take_2_blue" or want_to_play == "take_2_yellow" or want_to_play == "take_2_red" or want_to_play == "take_2_green" :
                    if r.get_more_two() ==2:
                        c.get_two_cards(spieler)
                    elif r.get_more_two() <=16:
                        ku=r.get_more_two()
                        c.get_more_two_cards(spieler,ku)
                elif want_to_play == "turn_blue" or want_to_play == "turn_yellow" or want_to_play == "turn_red" or want_to_play == "turn_green":
                    if reverse:
                        reverse=False
                    elif max_player >2:
                        reverse=True
                    else:
                        spieler-=1
                elif want_to_play == "skip_blue" or want_to_play == "skip_yellow" or want_to_play == "skip_red" or want_to_play == "skip_green":
                    if max_player >2:
                        if reverse:
                            if spieler-1<1:
                                spieler = max_player
                            else:
                                spieler-=1
                        else:
                            if spieler+1>max_player:
                                spieler = 1
                            else:
                                spieler+=1
                    else:
                        spieler-=1
                elif want_to_play_sondercard[0] == "color_switch":
                    h=want_to_play_sondercard[-1]
                    if h == "red" or h == "yellow" or h == "blue" or h=="green":
                        r.check_card(h)
                        inp.set_wish_color(h)
                    else:
                        com.write_file(r"D:\Python\Uno\json_files\com.txt","2. "+str(spieler)+" Diese_Farbe_steht_nicht_zur_auswahl!")
                        continue
                if c.get_valid_input(spieler_safe) == False:
                    pass
                else:
                    break
            else:
                if want_to_play == "3_":
                    break
                else:
                    pass
        if reverse:
            if spieler>1:
                spieler=spieler-1
            else:
                spieler=max_player
        else:
            if spieler<max_player:
                spieler+=1
            else:
                spieler = 1
        second_time=False
    inp.draw_winner_screen(reverse,spieler_safe)
    com.reset_json(r"D:\Python\Uno\json_files\players.json")
    com.reset_file(r"D:\Python\Uno\json_files\Start_game.txt")
   