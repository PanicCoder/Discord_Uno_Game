import asyncio
import json
import discord
import subprocess
client=discord.Client()
players_json={'players':[]}
players=[]
game=False
@client.event
async def on_ready():
    print("ok")
@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.lower() =="uno.start" and str(message.author)=="The Great Depression#3355" and game==False:
        await start_game()
    if message.content.lower() == "uno.join" and game == False:
        await get_players(message)
    if message.content.lower().startswith("u."):
        text = message.content.split("u.")
        await get_input(text[-1]+"*"+str(message.author))
    if message.content.lower() == "uno.end" and str(message.author)=="The Great Depression#3355":
        quit()
async def get_players(message):
    already_in=False
    if not len(players) == 0:
        for player in players:
            if message.author == player:
                already_in=True
        if not already_in:
            players_json["players"].append(str(message.author))
            players.append(message.author)
            await send_join_message()
            await get_profile_picture(message)
        else:
            await send_message(players[-1],"You are already in")
    else:
        players_json["players"].append(str(message.author))
        players.append(message.author)
        await send_join_message()
        await get_profile_picture(message)
    write_players()
def write_players():
    jsonString = json.dumps(players_json)
    jsonFile = open(r"D:\Python\Uno\json_files\players.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
def format_cards(spieler):
    cards_to_format = read_cards()[spieler]
    for c in cards_to_format:
        if c.split("_")[-1] != "blue" and c.split("_")[-1] != "red" and c.split("_")[-1] != "yellow" and c.split("_")[-1] != "green":
            pass
        else:
            pass
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
                if deck[0] !="No" and deck[1] !="Entry":
                    cards.append(deck)
        return cards
    except Exception:
        return -1
async def update():
    while True:
        if await read_instructions() == None:
            pass
        elif len(players)<=1:
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
async def get_profile_picture(message):
    pl_number=0
    picture = await message.author.avatar_url.read()
    for a in range(len(players)):
        if players[a] == message.author:
            pl_number=a
    file = open(r"D:\Python\Uno\Player_Pictures\P_"+str(pl_number+1)+'.png','wb')
    file.write(picture)
    file.close()
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
    await name.send(text)
async def send_cards(spieler):
    cards_player=""
    spieler=int(spieler)-1
    if read_cards() == -1:
        pass
    else:
        cards=read_cards()  
        for a in range(len(cards[spieler])):
            cards_player +=cards[spieler][a]+ "   "
        await send_message(players[spieler],cards_player)
async def send_join_message():
    await players[-1].send("You are in!")
async def start_game():
    if len(players_json["players"])>=2 and len(players_json["players"]) <=4:
        file = open(r"D:\Python\Uno\json_files\player_input.txt","w")
        file.write("True")
        file.close()
        write_players()
        subprocess.Popen(args=r"D:\Python\Uno\game_engine.py",shell=True)
        global game
        game=True
    else:
        print("es müssen min. 2 oder max 4 spieler sein!")
if __name__=="__main__":
    client.loop.create_task(update())
    client.run("ODM4NzM5NTQwMDU4NzAxOTI1.YI_fEQ.ZF4BC2w6-nRbWUfygLDcIoT732g")