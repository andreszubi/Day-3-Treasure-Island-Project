from flask import Flask, render_template, request, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

TREASURE_ASCII = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

STORY_NODES = {
    'start': {
        'title': 'Welcome to Treasure Island',
        'text': "Your mission is to find the treasure.\nYou're at a crossroad. Where do you want to go?",
        'options': [
            {'text': 'Go Left', 'value': 'left', 'next': 'lake'},
            {'text': 'Go Right', 'value': 'right', 'next': 'game_over_cave'}
        ],
        'game_over': False,
        'win': False
    },
    'lake': {
        'title': 'The Beautiful Lake',
        'text': "You have crossed a path, which leads you to a beautiful lake surrounded by golden glowing trees with beautiful canopies.\nYou quickly notice that there is an island in the middle of the lake.\nAt the middle of the island you spot a huge house with shining lights gleaming through the windows.\nYou also see that there is a boat to get to the island, however it is very slow.\nWhat will you do?",
        'options': [
            {'text': 'Wait for the boat', 'value': 'wait', 'next': 'house'},
            {'text': 'Swim across', 'value': 'swim', 'next': 'game_over_piranhas'}
        ],
        'game_over': False,
        'win': False
    },
    'game_over_piranhas': {
        'title': 'Game Over!',
        'text': "You slowly get into the water and start swimming towards the island.\nHalfway through, a pack of hungry piranhas spot you and attack you viciously.\n\nGAME OVER!",
        'options': [],
        'game_over': True,
        'win': False
    },
    'house': {
        'title': 'The Mysterious House',
        'text': "Slowly but surely, the boat takes you safely to the island.\nYou go ahead and step into the house.\nYou see that there are 3 doors. One red, one yellow and one blue.\nWhich door will you choose?",
        'options': [
            {'text': 'Red Door', 'value': 'red', 'next': 'game_over_chimera'},
            {'text': 'Yellow Door', 'value': 'yellow', 'next': 'win'},
            {'text': 'Blue Door', 'value': 'blue', 'next': 'game_over_goblins'}
        ],
        'game_over': False,
        'win': False
    },
    'game_over_chimera': {
        'title': 'Game Over!',
        'text': "You have stepped into a room with a chimera!\nThe beast quickly spots you and kills you with its fiery breath.\n\nGAME OVER!",
        'options': [],
        'game_over': True,
        'win': False
    },
    'game_over_goblins': {
        'title': 'Game Over!',
        'text': "You have entered into a humid room, almost like a swamp. When you look around, you spot a group of goblins.\nThey quickly surround you and ask you to hand over all of your money, however you don't have any on you.\nThe goblins become angry and decide to decapitate you.\n\nGAME OVER!",
        'options': [],
        'game_over': True,
        'win': False
    },
    'win': {
        'title': 'Congratulations!',
        'text': "You have entered a room filled with flying fairies.\nThey are friendly and guide you to a chest filled with gold and jewels.\n\nCONGRATULATIONS! YOU WIN!",
        'options': [],
        'game_over': False,
        'win': True
    },
    'game_over_cave': {
        'title': 'Game Over!',
        'text': "You crossed the road and arrived at a dark cave.\nAs you enter the cave, you are greeted by a hungry troll who gobbles you up in one bite.\n\nGAME OVER!",
        'options': [],
        'game_over': True,
        'win': False
    }
}

@app.route('/')
def index():
    session.clear()
    session['current_node'] = 'start'
    return redirect(url_for('play'))

@app.route('/play', methods=['GET', 'POST'])
def play():
    if 'current_node' not in session:
        session['current_node'] = 'start'
    
    if request.method == 'POST':
        choice = request.form.get('choice')
        current_node = session.get('current_node', 'start')
        
        if current_node in STORY_NODES:
            node = STORY_NODES[current_node]
            valid_choice = None
            
            for option in node['options']:
                if option['value'] == choice:
                    valid_choice = option
                    break
            
            if valid_choice:
                session['current_node'] = valid_choice['next']
            else:
                session['current_node'] = 'start'
        
        return redirect(url_for('play'))
    
    current_node_key = session.get('current_node', 'start')
    current_node = STORY_NODES.get(current_node_key, STORY_NODES['start'])
    
    return render_template('game.html', 
                         node=current_node,
                         ascii_art=TREASURE_ASCII if current_node_key == 'start' else None)

@app.route('/restart')
def restart():
    session.clear()
    session['current_node'] = 'start'
    return redirect(url_for('play'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
