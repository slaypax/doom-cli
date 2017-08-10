import click
import requests

d_server = 'http://localhost:6666'

@click.group()
def cli():
	pass

@cli.command()
def iddqd():
    '''
    Toggle Godmode
    '''
    url = d_server + "/api/player"
    request_player = requests.request("get", url)
    player_state = request_player.json()
    if player_state['cheatFlags'] == {}:
        payload = "{\"cheatFlags\":{\"CF_GODMODE\": true}}"
        response = requests.request("PATCH", url, data=payload)
    else: 
        payload = "{\"cheatFlags\":{\"CF_GODMODE\": false}}"
        response = requests.request("PATCH", url, data=payload)

@cli.command(short_help="Retrive doomguy's state")
def get_player():
    '''
    Retreive state data on the player character.
    '''
    url = d_server + "/api/player"
    response = requests.request("get", url)
    print(response.json())

@cli.command(short_help="Fire the selected Weapon")
def shoot():
    '''
    Does what you think it does. 
    '''
    url = d_server + "/api/player/actions"
    payload = "{\"type\": \"shoot\"}"
    response = requests.request("POST", url, data=payload)
    print("Bam!")

@cli.command(help="Change level to the desired Episode/Level. Values will vary by WAD.", short_help="Change Episode/Level")
@click.option('--episode', prompt="Episode:")
@click.option('--mission', prompt="Mission:")
def level(episode, mission):
    url = d_server + "/api/world"
    payload = "{ \"episode\": " + episode + ",\"map\":" +  mission + "}"
    response = requests.request("PATCH", url, data=payload)
    print(response)

@cli.command(short_help="Change weapon")
@click.argument('weapon')
def change_weapon(weapon):
    '''
    Switches the player character's weapon to the weapon assinged the number provided. Only works for guns already picked up. Type IDKFA in game for weapons to try this out.
    \b\n
    List of Weapons:\n
    1 - Pistol\n
    2 - Shotgun\n
    3 - Chaingun\n
    4 - Rocket Launcher\n
    5 - Plasma Rifle\n
    6 - BFG9K\n
    7 - Chainsaw\n
    8 - Super Shotgun\n
    '''
    url = d_server + "/api/player"
    payload = "{\"weapon\":" + weapon + "}"
    response = requests.request("PATCH", url, data=payload)
    if response.status_code == 400:
        print("You don't have that weapon!")
    else:
        print("Equipped")

@cli.command(short_help="spawns monsters")
@click.option('--monster', prompt="What kind of monster would you like?")
def spawn_monster(monster):
    '''
    \b
    List of Monsters:\n
    - IMP\n
    - FORMER HUMAN\n
    - FORMER HUMAN SERGEANT\n
    - BARON OF HELL\n
    - PAIN ELEMENTAL\n
    - HEAVY WEAPON DUDE\n
    - ARCH-VILE\n
    - CACODEMON\n
    - ARACHNOTRON\n
    - DEMON\n
    - LOST SOUL\n
    - CYBER-DEMON\n
    '''
    url = d_server + "/api/world/objects"
    payload = "{\"distance\": 400,\"angle\": 90,\"type\":" + "\"" + monster.upper() + "\"" + "}"
    response = requests.request("POST", url, data=payload)
    monster_state = response.json()
    monster_id = monster_state['id']
    print(monster)
    print(monster_id)


#Moving doesn't really work yet. I can't figure out why I can't update player position. 
#@cli.command()
#def move():
#    url = d_server + "/api/player"
#    request_player = requests.request("get", url)
#    player_state = request_player.json()
#    x_current = player_state["position"]["x"]
#    x_new = str(int(round(x_current + 10)))
#    payload = "{'position': {'x': 90.279648, 'y': 750.198547, 'z': 160}}"
#    response = requests.request("PATCH", url)
#    print(response.json())