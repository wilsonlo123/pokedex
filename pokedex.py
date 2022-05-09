import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
import sys, urllib
from urllib.request import urlopen

df = pd.read_csv("pokedex_main.csv")
df = df.sort_values(by=['name'])
pokemon = df["name"]
df = df.sort_index()

def getUrl(pokemon):
    url = 'https://www.serebii.net/pokemon/art/' 
    if pokemon["pokedex_number"] < 100 and pokemon["pokedex_number"] < 10:
        url = url + '00' + str(pokemon["pokedex_number"])
        if pokemon["pokedex_number"] == 6 and 'Mega' in pokemon["name"] and 'X' in pokemon["name"]:
            url = url + '-mx.png'
        elif pokemon["pokedex_number"] == 6 and 'Mega' in pokemon["name"] and 'Y' in pokemon["name"]:
            url = url + '-my.png'
        elif 'Mega' in pokemon["name"]:
            url = url + '-m.png'
        else:
            url = url + '.png'
    elif pokemon["pokedex_number"] < 100:
        url = url + '0' + str(pokemon["pokedex_number"])        
        if 'Mega' in pokemon["name"]:
            url = url + '-m.png'
        elif 'Alolan' in pokemon["name"]:
            url = url + '-a.png'
        elif 'Galarian' in pokemon["name"]:
            url = url + '-g.png'
        else:
            url = url + '.png'
    else:     
        url = url + str(pokemon["pokedex_number"]) 
        if pokemon["pokedex_number"] == 150 and 'Mega' in pokemon["name"] and 'X' in pokemon["name"]:
            url = url + '-mx.png'
        elif pokemon["pokedex_number"] == 150 and 'Mega' in pokemon["name"] and 'Y' in pokemon["name"]:
            url = url + '-my.png'        
        elif 'Mega' in pokemon["name"]:
            url = url + '-m.png'
        elif 'Primal' in pokemon["name"]:
            url = url + '-m.png'
        elif 'Alolan' in pokemon["name"]:
            url = url + '-a.png'
        elif pokemon["pokedex_number"] == 555 and 'Zen' in pokemon["name"] and 'Galarian' in pokemon["name"]:
            url = url + '-gz.png'              
        elif 'Galarian' in pokemon["name"]:
            url = url + '-g.png'
        elif 'Therian' in pokemon["name"]:
            url = url + '-s.png'
        elif 'Black' in pokemon["name"]:
            url = url + '-b.png'
        elif 'White' in pokemon["name"]:
            url = url + '-w.png'
        elif 'Resolute' in pokemon["name"]:
            url = url + '-r.png'
        elif 'Pirouette' in pokemon["name"]:
            url = url + '-p.png'
        elif pokemon["name"] == "Ash-Greninja":
            url = url + '-a.png'
        elif 'Blade' in pokemon["name"]:
            url = url + '-b.png'
        elif '10%' in pokemon["name"]:
            url = url + '-10.png'
        elif 'Complete' in pokemon["name"]:
            url = url + '-c.png'
        elif 'Unbound' in pokemon["name"]:
            url = url + '-u.png'
        elif 'Pom-Pom' in pokemon["name"]:
            url = url + '-p.png'
        elif 'Pa' in pokemon["name"] and pokemon["pokedex_number"] == 741:
            url = url + '-pau.png'
        elif 'Sensu' in pokemon["name"]:
            url = url + '-s.png'
        elif 'Midnight' in pokemon["name"]:
            url = url + '-m.png'
        elif 'Dusk' in pokemon["name"] and pokemon["pokedex_number"] == 745:
            url = url + '-d.png'
        elif 'School' in pokemon["name"]:
            url = url + '-s.png'
        elif 'Core' in pokemon["name"]:
            url = url + '-r.png'
        elif 'Mane' in pokemon["name"]:
            url = url + '-dm.png'
        elif 'Wings' in pokemon["name"]:
            url = url + '-dw.png'
        elif 'Ultra' in pokemon["name"] and pokemon["pokedex_number"] == 800:
            url = url + '-m.png'
        elif 'Low Key' in pokemon["name"]:
            url = url + '-l.png'
        elif 'Noice' in pokemon["name"]:
            url = url + '-n.png'
        elif 'Eternamax' in pokemon["name"]:
            url = url + '-e.png'
        elif 'Hangry' in pokemon["name"]:
            url = url + '-h.png'
        elif 'Crowned' in pokemon["name"]:
            url = url + '-c.png'
        elif 'Rapid' in pokemon["name"]:
            url = url + '-r.png'
        elif 'Ice' in pokemon["name"] and pokemon["pokedex_number"] == 898:
            url = url + '-i.png'
        elif 'Shadow' in pokemon["name"] and pokemon["pokedex_number"] == 898:
            url = url + '-s.png'
        elif pokemon["pokedex_number"] == 351 and 'Sunny' in pokemon["name"]:
            url = url + '-s.png'
        elif pokemon["pokedex_number"] == 351 and 'Rainy' in pokemon["name"]:
            url = url + '-r.png'        
        elif pokemon["pokedex_number"] == 351 and 'Snowy' in pokemon["name"]:
            url = url + '-i.png'    
        elif pokemon["pokedex_number"] == 386 and 'Attack' in pokemon["name"]:
            url = url + '-a.png'
        elif pokemon["pokedex_number"] == 386 and 'Defense' in pokemon["name"]:
            url = url + '-d.png' 
        elif pokemon["pokedex_number"] == 386 and 'Speed' in pokemon["name"]:
            url = url + '-s.png'  
        elif pokemon["pokedex_number"] == 413 and 'Sandy' in pokemon["name"]:
            url = url + '-c.png'           
        elif pokemon["pokedex_number"] == 413 and 'Trash' in pokemon["name"]:
            url = url + '-t.png'  
        elif pokemon["pokedex_number"] == 487 and 'Origin' in pokemon["name"]:
            url = url + '-o.png'             
        elif pokemon["pokedex_number"] == 492 and 'Sky' in pokemon["name"]:
            url = url + '-s.png'  
        elif pokemon["pokedex_number"] == 550 and 'Blue-Striped' in pokemon["name"]:
            url = url + '-b.png'            
        elif pokemon["pokedex_number"] == 555 and 'Zen' in pokemon["name"]:
            url = url + '-z.png'  
        elif pokemon["pokedex_number"] == 479 and 'Heat' in pokemon["name"]:
            url = url + '-h.png'
        elif pokemon["pokedex_number"] == 479 and 'Mow' in pokemon["name"]:
            url = url + '-m.png'            
        elif pokemon["pokedex_number"] == 479 and 'Wash' in pokemon["name"]:
            url = url + '-w.png'            
        elif pokemon["pokedex_number"] == 479 and 'Frost' in pokemon["name"]:
            url = url + '-f.png'  
        elif pokemon["pokedex_number"] == 479 and 'Fan' in pokemon["name"]:
            url = url + '-s.png'  
                  
            
        else:
            url = url + '.png'        
    return url    

def show():
    currentMon = combo.currentText()
    result = []
    for i in range(2000):
        if pokemon[i] == currentMon:
            result = df.iloc[i] 
            break
    hp.setText(str(result["hp"])) 
    attack.setText(str(result["attack"]))
    defense.setText(str(result["defense"]))
    spa.setText(str(result["sp_attack"]))
    spd.setText(str(result["sp_defense"]))
    speed.setText(str(result["speed"]))
    species.setText(result["species"])
    type1.setText(result["type_1"])
    type2.setText(result["type_2"])
    ability1.setText(result["ability_1"])
    ability2.setText(result["ability_2"])
    abilityHidden.setText(result["ability_hidden"])
    image = QImage()
    url = getUrl(result)
    data = urlopen(url).read()
    image.loadFromData(data)
    image = QPixmap(image)
    imageLabel.setPixmap(QPixmap(image))
    
app = QApplication (sys.argv)
win = QMainWindow()
win.setGeometry(0,0,1000,700)
win.setWindowTitle("Pokedex")

combo = QtWidgets.QComboBox(win)
combo.setGeometry(50,50,300,50)  
combo.addItems(pokemon)

button = QtWidgets.QPushButton(win)
button.setText("Search")
button.clicked.connect(show)
button.move(50, 100)

label1 = QtWidgets.QLabel(win)
label1.setText("Stats:")
label1.move(50, 300)

hpLabel = QtWidgets.QLabel(win)
hpLabel.setText("HP")
hpLabel.move(50, 350)

attackLabel = QtWidgets.QLabel(win)
attackLabel.setText("Attack")
attackLabel.move(50, 400)

defenseLabel = QtWidgets.QLabel(win)
defenseLabel.setText("Defense")
defenseLabel.move(50, 450)

spaLabel = QtWidgets.QLabel(win)
spaLabel.setText("Special Attack")
spaLabel.move(50, 500)

spdLabel = QtWidgets.QLabel(win)
spdLabel.setText("Special Defense")
spdLabel.setGeometry(50, 550, 150, 25)

speedLabel = QtWidgets.QLabel(win)
speedLabel.setText("Speed")
speedLabel.move(50, 600)

hp = QtWidgets.QLabel(win)
hp.setText(str(0))
hp.move(200, 350) 

attack = QtWidgets.QLabel(win)
attack.setText(str(0))
attack.move(200, 400)

defense = QtWidgets.QLabel(win)
defense.setText(str(0))
defense.move(200, 450)

spa = QtWidgets.QLabel(win)
spa.setText(str(0))
spa.move(200, 500)

spd = QtWidgets.QLabel(win)
spd.setText(str(0))
spd.move(200, 550)

speed = QtWidgets.QLabel(win)
speed.setText(str(0))
speed.move(200, 600)

speciesLabel = QtWidgets.QLabel(win)
speciesLabel.setText("Species:")
speciesLabel.move(500, 46)

species = QtWidgets.QLabel(win)
species.setText("")
species.setGeometry(600, 50, 200, 25)

type1Label = QtWidgets.QLabel(win)
type1Label.setText("Type 1:")
type1Label.move(500, 100)

type2Label = QtWidgets.QLabel(win)
type2Label.setText("Type 2:")
type2Label.move(700, 100)

type1 = QtWidgets.QLabel(win)
type1.setText("")
type1.move(600, 100)

type2 = QtWidgets.QLabel(win)
type2.setText("")
type2.move(800, 100)

imageLabel = QtWidgets.QLabel(win)
imageLabel.setGeometry(400, 200, 500, 500)

ability1Label = QtWidgets.QLabel(win)
ability1Label.setText("Ability 1:")
ability1Label.move(50,150)

ability2Label = QtWidgets.QLabel(win)
ability2Label.setText("Ability 2:")
ability2Label.move(50,200)

abilityHiddenLabel = QtWidgets.QLabel(win)
abilityHiddenLabel.setText("Hidden Ability:")
abilityHiddenLabel.setGeometry(50, 250, 200, 25)

ability1 = QtWidgets.QLabel(win)
ability1.setText("")
ability1.setGeometry(200, 150, 200, 25)

ability2 = QtWidgets.QLabel(win)
ability2.setText("")
ability2.setGeometry(200, 200, 200, 25)

abilityHidden = QtWidgets.QLabel(win)
abilityHidden.setText("")
abilityHidden.setGeometry(200, 250, 200, 25)

win.show()
sys.exit(app.exec_())
    
  