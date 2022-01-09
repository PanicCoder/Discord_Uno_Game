import asyncio
import json
import random
import datetime
from time import sleep
import discord
import subprocess
client=discord.Client()
players_json={'players':[]}
players=[]
reactions=["🚫","🔄","🌀","➕","🎴","0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🟥","🟦","🟩","🟨","🆕","☑️"]
name_reation=["skip_","turn_","color_switch_","take_","3_","0_","1_","2_","3_","4_","5_","6_","7_","8_","9_","red","blue","green","yellow"]
reaction_queue=[]
reacted=False
game=False
@client.event
async def on_ready():
    print("ok")
    subprocess.Popen(args=r"D:\Python\Uno\game_engine.py",shell=True)
    client.loop.create_task(update())
@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.lower() =="uno.start" and str(message.author)=="The Great Depression#3355" and game==False:
        await start_game()
    if message.content.lower() == "uno.join" and game == False:
        await get_players(message)
        while True:
            await get_profile_picture(message.author)
            if await get_profile_picture(message.author)!=-1:
                break
    if message.content.lower() == "uno.end" and str(message.author)=="The Great Depression#3355":
        quit()
@client.event
async def on_raw_reaction_add(payload):
    global reaction_queue
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    name = message.channel.recipient
    if str(payload.user_id) == "838739540058701925":
        return
    reaction_queue.append((payload.emoji,name))
    await build_inp_cards(str(name),name)
async def get_players(message):
    if message.author in players:
        await send_message(players[-1],"You are already in")
    else:
        players_json["players"].append(str(message.author))
        players.append(message.author)
        await send_join_message()
    write_players()
def write_players():
    jsonString = json.dumps(players_json)
    jsonFile = open(r"D:\Python\Uno\json_files\players.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
async def sort_after_num(card_list):
    for i in range(len(card_list)-1):
        min = i
        j=i+1
        while j <len(card_list):
            if (card_list[min]>card_list[j]):
                min = j
            j+=1
        temp = card_list[i]
        card_list[i]=card_list[min]
        card_list[min]=temp
    return card_list
async def get_random_player():
    for _ in range(10):
        k=random.randint(0,len(players)-1)
        l=random.randint(0,len(players)-1)
        zw=players_json["players"][k]
        players_json["players"][k]=players_json["players"][l]
        players_json["players"][l]=zw
        zw_=players[k]
        players[k]=players[l]
        players[l]=zw_
async def format_cards(player_cards):
    blue_cards=[]
    red_cards=[]
    sort_cards=[]
    yellow_cards=[]
    green_cards=[]
    sondercards=[]
    for c in player_cards:
        if c.split("_")[0] == "take" or c.split("_")[0] == "color" or c.split("_")[0] == "turn" or c.split("_")[0] == "skip":
            sondercards.append(c)
            sondercards = await sort_after_num(sondercards)
        elif c.split("_")[-1] == "blue":
            blue_cards.append(c)
            blue_cards = await sort_after_num(blue_cards)
        elif c.split("_")[-1] == "yellow":
            yellow_cards.append(c)
            yellow_cards = await sort_after_num(yellow_cards)
        elif c.split("_")[-1] == "green":
            green_cards.append(c)
            green_cards = await sort_after_num(green_cards)
        elif c.split("_")[-1] == "red":
            red_cards.append(c)
            red_cards = await sort_after_num(red_cards)
    sort_cards.append(sondercards)
    sort_cards.append(blue_cards)
    sort_cards.append(yellow_cards)
    sort_cards.append(green_cards)
    sort_cards.append(red_cards)
    for i in range(len(sort_cards)):
        if len(sort_cards[i]) == 0:
            sort_cards[i].append("[]")
    return sort_cards
def read_cards():
    try:
        with open(r"D:\Python\Uno\json_files\player_cards.json", "r") as f:
            cards=[]
            data = json.load(f)
            f.close()
        if data == "":
            return -1
        else:
            for deck in data:
                if deck[0] !="No":
                    cards.append(deck)
        return cards
    except Exception:
        return -1
async def update():
    while True:
        if await read_instructions() == None:
            pass
        else:
            instruction = await read_instructions()
            if instruction[0] == "1.":
                await send_cards(instruction[-1])
                await clear_instruction()
            elif instruction[0]=="2.":
                await send_message(players[int(instruction[1])-1],instruction[-1])
                await clear_instruction()
        await asyncio.sleep(1)
async def get_profile_picture(author):
    pl_number=0
    picture = await author.avatar_url.read()
    for a in range(len(players)):
        if players[a] == author:
            pl_number=a
    try:
        file = open(r"D:\Python\Uno\Player_Pictures\P_"+str(pl_number+1)+'.png','wb')
        file.write(picture)
        file.close()
    except Exception:
        return -1
async def get_input(text):
    file = open(r"D:\Python\Uno\json_files\player_input.txt","w")
    file.write(text)
    file.close()
async def read_instructions():
    file = open(r"D:\Python\Uno\json_files\com.txt","r")
    content=file.read()
    file.close()
    zw = content.split(" ")
    return zw
async def clear_instruction():
    file = open(r"D:\Python\Uno\json_files\com.txt","w")
    file.write("")
    file.close()
async def send_message(name,text):
    mes = await name.send(text)
    return mes
async def do_reactions(name,reaction):
    await name.add_reaction(reaction)
async def build_inp_cards(name,un_name):
    global reaction_queue
    start=False
    restart=False
    my_card=""
    c_cards=[]
    for i in range(len(reaction_queue)):
        c_cards.append(reaction_queue[i][0])
    if c_cards == []:
        return
    else:
        for element in c_cards:
            if str(element) == '☑️' :
                start=True
                break
            elif str(element)=="🆕":
                restart=True
                break
    if start:
        reaction_queue=[]
        for element in c_cards:
            for i in range(len(reactions)-2):
                if str(element) == str(reactions[i]):
                   my_card+=name_reation[i]
        m_card=my_card.split("_")
        try:
            if m_card[2] =="blue" or m_card[2] =="red" or m_card[2] =="green" or m_card[2] =="yellow":
                if m_card[0] == "take" and m_card[1] == "4":
                    my_card="take_four "+m_card[2]
                if m_card[0]=="color" and m_card[1]=="switch":
                    my_card="color_switch "+m_card[2]
        except IndexError:
            pass
        await get_input(my_card+"*"+str(name))
    if restart:
        reaction_queue=[]
        await get_new_reactions(un_name)
async def get_new_reactions(name):
    await send_cards(players.index(name)+1)
async def send_cards(spieler):
    cards_player=cards_from_player=blue=red=green=yellow=extra=form=""
    spieler=int(spieler)-1
    if read_cards() == -1:
        pass
    else:
        cards=read_cards()  
        cards_player = await format_cards(cards[spieler])
        for b in cards_player[1]:
            blue += " | " +b
        for r in cards_player[4]:
            if len(red)==0:
                red+=r
            else: 
                red += " | "+r
        for y in cards_player[2]:  
            if len(yellow)==0:
                yellow +=y
            else:
                yellow+=" | "+y
        for g in cards_player[3]: 
            if len(green)==0:
                green+=g
            else:
                green +=" | "+g
        for e in cards_player[0]:
            if len(extra)==0:
                extra+=e 
            else:
                extra += " | "+e
        cards_from_player=blue+"  /|\  "+red+"  /|\  "+green+"  /|\  "+yellow+"  /|\  "+extra+" | "
        element_save=""
        i=0
        num_spaces=[]
        for element in cards_from_player:
            if element_save =="\\" and element==" ":
                num_spaces.append(i)
                i=0
            element_save=element
            i+=1
        form="Blue"+"-"*(num_spaces[0]-len("Blue"))+"Red"+"-"*(num_spaces[1]-len("Red"))+"Green"+"-"*(num_spaces[2]-len("Green"))+"Yellow"+"-"*(num_spaces[3]-len("Yellow"))+"Extra"
        to_use_re = await get_needed_reations(cards_from_player)
        mes = await send_message(players[spieler],form+"\n"+cards_from_player)
        for re in reactions:
            if re in to_use_re:
                await do_reactions(mes,re)
async def get_needed_reations(cards):
    c_list=cards.split(" /|\ ")
    pieces=[]
    end_pieces=[]
    reactions_to_use=[]
    for element in c_list:
        pieces.append(element.split(" "))
    for element in pieces:
        for e in element:
            end_pieces.append(e.split("_"))
    for element in end_pieces:
        for i in range(len(element)):
            for k in range(len(name_reation)):
                if element[i] == "four":
                    reactions_to_use.append("4️⃣")
                    for g in range(14,18):
                        reactions_to_use.append(reactions[g])
                if element[i] == "color":
                    reactions_to_use.append("🌀")
                    for g in range(14,18):
                        reactions_to_use.append(reactions[g])
                if element[i]+"_" == name_reation[k] or element[i] == name_reation[k]:
                    if reactions[k] not in reactions_to_use:
                        reactions_to_use.append(reactions[k])
    reactions_to_use.append("🆕")
    reactions_to_use.append("☑️")
    if len(reactions_to_use)<20:
        reactions_to_use.append("🎴")
    else:
         reactions_to_use.append("3️⃣")
    return reactions_to_use
async def send_join_message():
    await players[-1].send("You are in!")
async def start_game():
    file = open(r"D:\Python\Uno\json_files\player_input.txt","w")
    file.write("True")
    file.close()
    await asyncio.sleep(1)
    if len(players_json["players"])>=2 and len(players_json["players"]) <=4:
        await get_random_player()
        for i in range(len(players)):
            await get_profile_picture(players[i])
        write_players()
        global game
        game=True
    else:
        print("es müssen min. 2 oder max 4 spieler sein!")
if __name__=="__main__":
    client.run("ODM4NzM5NTQwMDU4NzAxOTI1.YI_fEQ.ZF4BC2w6-nRbWUfygLDcIoT732g")