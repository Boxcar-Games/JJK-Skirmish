import math
import random

#These are some global variables that I needed while coding Kugisaki, feel free to remove them if needed - Night#
#player globals#
global playerHealth
global playerMaxHealth
global playerAttack
global playerDefense
global playerSpeed
global playerCE
global playerLives
global playerA1
global playerA2
global playerA3
global playerA4
global playerA5
global playerEnemyNails
#computer globals#
global compHealth
global compMaxHealth
global compAttack
global compDefense
global compSpeed
global compCE
global compLives
global compA1
global compA2
global compA3
global compA4
global compA5
global compEnemyNails


#Kugisaki has two abilities that fall under cursed weapons:Hammer Strike and Ranged Nail - Night#
#Kugisaki also has two abilities that fall under cursed technique: Hairpin and resonance -Night#

class abilities():
  class cursedControl():
    class divergentFist():
      damage=40
      stunBuild=40
      cursedConsumption=50
      critChance="13"
      abilityID="Divergent Fist"
    class blackFlash():
      damage=100
      stunBuild=60
      cursedConsumption=250
      critChance="40"
      abilityID="Black Flash"
    class coreBlast():
      damage=100
      stunBuild=20
      cursedConsumption=200
      abilityID="Core Blast"
    class spottedDullBlade():
      damage=40
      stunBuild=10
      cursedConsumption=75
      critChance="50"
      abilityID="Spotted Dull Blade"
    class wrappedFist():
      damage=55
      stunBuild=60
      cursedConsumption=100
      critChance="35"
      abilityID="Wrapped Fist"
    class cursedBullet():
      damage=30
      stunBuild=15
      cursedConsumption=10
      critChance="55"
      abilityID="Cursed Bullet"
  class cursedTechnique():
    class playerSDhairPin():
      damage=30
      stunBuild=40
      cursedConsumption=150
      critChance="50"
      abilityID="Strawdoll Technique: Hairpin"
      def playerFinalDamage():      
        playerFinalDamage=abilities.cursedTechnique.playerSDhairPin.damage+((playerSelectNobara.playerEnemyNails)*30)
    class playerSDresonance():
      damage=30
      stunBuild=75
      cursedConsumption=300
      critChance="100"
      abilityID="Strawdoll Technique: Resonance"
      def playerFinalDamage():
        playerFinalDamage=abilities.cursedTechnique.playerSDresonance.damage+((compMaxHealth-compHealth)*0.20)
    class compSDhairPin():
      damage=30
      stunBuild=40
      cursedConsumption=150
      critChance="50"
      abilityID="Strawdoll Technique: Hairpin"
      def compFinalDamage():       
        compFinalDamage=abilities.cursedTechnique.compSDhairPin.damage+((compSelectNobara.compEnemyNails)*30)
    class compSDresonance():
      damage=30
      stunBuild=75
      cursedConsumption=300
      critChance="100"
      abilityID="Strawdoll Technique: Resonance"
      def compFinalDamage():
        compFinalDamage=abilities.cursedTechnique.compSDresonance.damage+((playerMaxHealth-playerHealth)*0.20)
    class dismantle():
      damage=80
      stunBuild=5
      cursedConsumption=150
      critChance="25"
      abilityID="Dismantle"
    class coreShiftSister():
      damage=35
      stunBuild=20
      cursedConsumption=100
      critChance="40"
      abilityID="3rd Core"
    class coreShiftPanda():
      damage=50
      stunBuild=40
      cursedConsumption=50
      critChance="20"
      abilityID="First Core"
    class coreShiftGorilla():
      damage=80
      stunBuild=90
      cursedConsumption=250
      critChance="35"
      abilityID="Second Core"
    class ratio73():
      damage=85
      stunBuild=5
      cursedConsumption=150
      critChance="80"
      abilityID="Ratio 7:3"
    class collapse():
      damage=65
      stunBuild=100
      cursedConsumption=120
      critChance="80"
      abilityID="Collapse"
    class creation():
      damage=200
      stunBuild=200
      cursedConsumption=400
      critChance="100"
      abilityID="Creation"
    class TSFrogs():
      damage=10
      stunBuild=150
      cursedConsumption=25
      critChance="35"
      abilityID="Ten Shadows: Frogs"
    class TSDogs():
      damage=60
      stunBuild=50
      cursedConsumption=60
      critChance="45"
      abilityID="Ten Shadows: Demon Dogs"
    class TSNue():
      damage=80
      stunBuild=100
      cursedConsumption=100
      critChance="75"
      abilityID="Ten Shadows: Nue"
    class TSElephant():
      damage=120
      stunBuild=125
      cursedConsumtption=200
      critChace="25"
      abiltyID="Ten Shadows: Elephant, Maximum Form"
  class cursedWeapons():
    class rangedNail():
      damage=20
      stunbuild=15
      cursedConsumption=40
      critChance="30"
      abilityID="Ranged Nail"
    class hammerStrike():
      damage=20
      stunbuild=45
      cursedConsumption=20
      critChance="10"
      abilityID="Hammer Stike"
    class rubberBullet():
      damage=5
      stunBuild=45
      cursedConsumption=0
      critChance="70"
      abilityID="Rubber Bullets"
    class rapidFire():
      damage=45
      stunBuild=25
      cursedConsumption=0
      critChance="80"
      abilityiD="Rapid Fire"
  class domainExpansion():
    class malevolentYapping():
      damage=45
      stunBuild=200
      cursedConsumption=450
      critChance="10"
      abilityID="Benevolent Shrine"
      abilityVL="I am you"
    class malevolentShrine():
      damage=300
      stunBuild=20
      cursedConsumption=800
      critChance="50"
      abilityID="Malevolent Shrine"
      abilityVL="Domain Expansion: Malevolent Shrine"
    class mountainOfIron():
      damage=80
      stunBuild=40
      cursedConsumption=400
      
      
class characters():
  class JujutsuHigh():
    class ItadoriYuji():
      rank="Special Grade"
      difficulty="Easy"
      description="Yuji is able to do mass amounts of damage quickly while also building stun, his divergent fist and black flash ensure a quick end to any encounters, while being sukunas vessel allows him to access domain expansions, capable of taking down even the strongest cursed spirits"
      health=200
      attack=340
      defense=15
      speed=50
      cursedEnergy=1350
      lives=1
      ability1=abilities.cursedControl.divergentFist
      ability2=abilities.cursedTechnique.dismantle
      ability3=abilities.cursedControl.blackFlash
      ability4=abilities.domainExpansion.malevolentYapping
      ability5=abilities.domainExpansion.malevolentYapping
    class Panda():
      rank="2"
      difficulty="Medium"
      description="With 3 lives, Panda is a tank on the battle field, swapping between cores will allow you to deal massive damage and build tons of stun on your opponent"
      health=350
      attack=45
      defense=40
      speed=35
      cursedEnergy=800
      lives=3
      ability1=abilities.cursedTechnique.coreShiftPanda
      ability2=abilities.cursedTechnique.coreShiftSister
      ability3=abilities.cursedTechnique.coreShiftGorilla
      ability4=abilities.cursedControl.coreBlast
    class Nanami():
      rank="1"
      difficulty="Medium"
      description="Nanami is a grade 1 sorcerer, his 7:3 ratio make him deadly to most targets, that combined with his passive 'Overtime', make for a deadly combo on the field"
      health=250
      attack=50
      defense=25
      speed=45
      cursedEnergy=1000
      lives=1
      ability1=abilities.cursedControl.spottedDullBlade
      ability2=abilities.cursedControl.wrappedFist
      ability3=abilities.cursedTechnique.collapse
      ability4=abilities.cursedTechnique.ratio73
    class MaiZenin():
      rank="1"
      difficulty="Hard"
      health=100
      attack=25
      defense=25
      speed=40
      cursedEnergy=500
      lives=1
      ability1=abilities.cursedControl.cursedBullet
      ability2=abilities.cursedWeapons.rubberBullet
      ability3=abilities.cursedWeapons.rapidFire
      ability4=abilities.cursedTechnique.creation
    class megumiFushiguro():
      rank="2"
      difficulty="Easy"
      health=150
      attack=35
      defense=15
      speed=40
      cursedEnergy=750
      lives=1
      ability1=abilities.cursedTechnique.TSFrogs
      ability2=abilities.cursedTechnique.TSDogs
      ability3=abilities.cursedTechnique.TSNue
      ability4=abilities.cursedTechnique.TSElephant
    class nobaraKugisaki():
      rank="3"
      difficulty="Medium"
      health=150
      attack=20
      defense=20
      speed=35
      lives=1
      cursedEnergy=700
      ability1=abilities.cursedWeapons.rangedNail
      ability2=abilities.cursedWeapons.hammerStrike
      ability3a=abilities.cursedTechnique.playerSDhairPin
      ability4a=abilities.cursedTechnique.playerSDresonance
      ability3b=abilities.cursedTechnique.compSDhairPin
      ability4b=abilities.cursedTechnique.compSDresonance
  class CursedSpirits():
    class Jogo():
      rank="Special Grade"
      difficulty="Medium"
      health=175
      attack=20
      defense=35
      speed=45
      cursedEnergy=1150
      lives=1
      #ability1
      #ability2
      #ability3
      
#I decided to add Nobara to this list, you can remove her if this causes problems - Night#
def playerSelectYuji():
  playerCharacter="Yuji Itadori"
  playerHealth=characters.JujutsuHigh.ItadoriYuji.health
  playerAttack=characters.JujutsuHigh.ItadoriYuji.attack
  playerDefense=characters.JujutsuHigh.ItadoriYuji.defense
  playerSpeed=characters.JujutsuHigh.ItadoriYuji.speed
  playerCE=characters.JujutsuHigh.ItadoriYuji.cursedEnergy
  playerLives=characters.JujutsuHigh.ItadoriYuji.lives
  playerA1=characters.JujutsuHigh.ItadoriYuji.ability1
  playerA2=characters.JujutsuHigh.ItadoriYuji.ability2
  playerA3=characters.JujutsuHigh.ItadoriYuji.ability3
  playerA4=characters.JujutsuHigh.ItadoriYuji.ability4
  playerA5=characters.JujutsuHigh.ItadoriYuji.ability5
  return
def playerSelectPanda():
  playerCharacter="Panda"
  playerHealth=characters.JujutsuHigh.Panda.health
  playerAttack=characters.JujutsuHigh.Panda.attack
  playerDefense=characters.JujutsuHigh.Panda.defense
  playerSpeed=characters.JujutsuHigh.Panda.speed
  playerCE=characters.JujutsuHigh.Panda.cursedEnergy
  playerLives=characters.JujutsuHigh.Panda.lives
  playerA1=characters.JujutsuHigh.Panda.ability1
  playerA2=characters.JujutsuHigh.Panda.ability2
  playerA3=characters.JujutsuHigh.Panda.ability3
  playerA4=characters.JujutsuHigh.Panda.ability4
  return
def playerSelectNanami():
  playerCharacter="Nanami"
  playerHealth=characters.JujutsuHigh.Nanami.health
  playerAttack=characters.JujutsuHigh.Nanami.attack
  playerDefense=characters.JujutsuHigh.Nanami.defense
  playerSpeed=characters.JujutsuHigh.Nanami.speed
  playerCE=characters.JujutsuHigh.Nanami.cursedEnergy
  playerLives=characters.JujutsuHigh.Nanami.lives
  playerA1=characters.JujutsuHigh.Nanami.ability1
  playerA2=characters.JujutsuHigh.Nanami.ability2
  playerA3=characters.JujutsuHigh.Nanami.ability3
  playerA4=characters.JujutsuHigh.Nanami.ability4
  return
def playerSelectMai():
  playerCharacter="Mai Zen'in"
  playerHealth=characters.JujutsuHigh.MaiZenin.health
  playerAttack=characters.JujutsuHigh.MaiZenin.attack
  playerDefense=characters.JujutsuHigh.MaiZenin.defense
  playerSpeed=characters.JujutsuHigh.MaiZenin.speed
  playerCE=characters.JujutsuHigh.MaiZenin.cursedEnergy
  playerLives=characters.JujutsuHigh.MaiZenin.lives
  playerA1=characters.JujutsuHigh.MaiZenin.ability1
  playerA2=characters.JujutsuHigh.MaiZenin.ability2
  playerA3=characters.JujutsuHigh.MaiZenin.ability3
  playerA4=characters.JujutsuHigh.MaiZenin.ability4
  return

def compSelectYuji():
  compCharacter="Yuji Itadori"
  compHealth=characters.JujutsuHigh.ItadoriYuji.health
  compAttack=characters.JujutsuHigh.ItadoriYuji.attack
  compDefense=characters.JujutsuHigh.ItadoriYuji.defense
  compSpeed=characters.JujutsuHigh.ItadoriYuji.speed
  compCE=characters.JujutsuHigh.ItadoriYuji.cursedEnergy
  compLives=characters.JujutsuHigh.ItadoriYuji.lives
  compA1=characters.JujutsuHigh.ItadoriYuji.ability1
  compA2=characters.JujutsuHigh.ItadoriYuji.ability2
  compA3=characters.JujutsuHigh.ItadoriYuji.ability3
  compA4=characters.JujutsuHigh.ItadoriYuji.ability4
  compA5=characters.JujutsuHigh.ItadoriYuji.ability5
  print("Yuji Itadori")
  return
def compSelectPanda():
  compCharacter="Panda"
  compHealth=characters.JujutsuHigh.Panda.health
  compAttack=characters.JujutsuHigh.Panda.attack
  compDefense=characters.JujutsuHigh.Panda.defense
  compSpeed=characters.JujutsuHigh.Panda.speed
  compCE=characters.JujutsuHigh.Panda.cursedEnergy
  compLives=characters.JujutsuHigh.Panda.lives
  compA1=characters.JujutsuHigh.Panda.ability1
  compA2=characters.JujutsuHigh.Panda.ability2
  compA3=characters.JujutsuHigh.Panda.ability3
  compA4=characters.JujutsuHigh.Panda.ability4
  print("Panda")
  return
def compSelectNanami():
  compCharacter="Nanami"
  compHealth=characters.JujutsuHigh.Nanami.health
  compAttack=characters.JujutsuHigh.Nanami.attack
  compDefense=characters.JujutsuHigh.Nanami.defense
  compSpeed=characters.JujutsuHigh.Nanami.speed
  compCE=characters.JujutsuHigh.Nanami.cursedEnergy
  compLives=characters.JujutsuHigh.Nanami.lives
  compA1=characters.JujutsuHigh.Nanami.ability1
  compA2=characters.JujutsuHigh.Nanami.ability2
  compA3=characters.JujutsuHigh.Nanami.ability3
  compA4=characters.JujutsuHigh.Nanami.ability4
  print("Nanami")
  return
def compSelectMai():
  compCharacter="Mai Zen'in"
  compHealth=characters.JujutsuHigh.MaiZenin.health
  compAttack=characters.JujutsuHigh.MaiZenin.attack
  compDefense=characters.JujutsuHigh.MaiZenin.defense
  compSpeed=characters.JujutsuHigh.MaiZenin.speed
  compCE=characters.JujutsuHigh.MaiZenin.cursedEnergy
  compLives=characters.JujutsuHigh.MaiZenin.lives
  compA1=characters.JujutsuHigh.MaiZenin.ability1
  compA2=characters.JujutsuHigh.MaiZenin.ability2
  compA3=characters.JujutsuHigh.MaiZenin.ability3
  compA4=characters.JujutsuHigh.MaiZenin.ability4
  print("Mai Zen'in")
  return
def playerSelectNobara():
  playerCharacter="Nobara Kugisaki"
  playerHealth=characters.JujutsuHigh.nobaraKugisaki.Health
  playerMaxHealth=characters.JujutsuHigh.nobaraKugisaki.Health
  playerAttack=characters.JujutsuHigh.nobaraKugisaki.attack
  playerDefense=characters.JujutsuHigh.nobaraKugisaki.defense
  playerSpeed=characters.JujutsuHigh.nobaraKugisaki.speed
  playerCE=characters.JujutsuHigh.nobaraKugisaki.cursedEnergy
  playerLives=characters.JujutsuHigh.nobaraKugisaki.lives
  playerA1=characters.JujutsuHigh.nobaraKugisaki.ability1
  playerA2=characters.JujutsuHigh.nobaraKugisaki.ability2
  playerA3=characters.JujutsuHigh.nobaraKugisaki.ability3a
  playerA4=characters.JujutsuHigh.nobaraKugisaki.ability4a
  playerStunlevel=0
  playerEnemyNails=0
  return


#This is just a little thing that I made as a placeholder, you may remove if necessary - Night#

def compCharacterChoice():
  compCharacterChoice=random.randint(1,5)
  if compCharacterChoice == 1:
    print("Enemy is Yuji Itador")
    compSelectYuji
  elif compCharacterChoice == 2:
    print("Enemy is Panda")
    compSelectPanda
  elif compCharacterChoice == 3:
    print("Enemy is Nanami")
    compSelectNanami
  elif compCharacterChoice == 4:
    print("Enemy is Mai Zenin")
    compSelectMai
  elif compSelectNanami == 5:
    print("Enemy is Nobara")
    compSelectNobara
    return


#Placeholder character selection for Player#
playerCharacterChoice=input("enter  1 for Yuji, enter 2 for Panda, enter 3 for Nanami, enter 4 for Mai, enter 5 for Nobara")
playerCharacterChoice=int(playerCharacterChoice)
if playerCharacterChoice == 1:
  print("You chose Yuji Itadori")
  playerSelectYuji
  compCharacterChoice
elif playerCharacterChoice == 2:
  print("You chose Panda")
  playerSelectPanda
  compCharacterChoice
elif playerCharacterChoice == 3:
  print("You chose Nanami")
  playerSelectNanami
  compCharacterChoice
elif playerCharacterChoice == 4:
  print("You chose Mai Zenin")
  playerSelectMai
  compCharacterChoice
elif playerCharacterChoice == 5:
  print("You chose Nobara Kugisaki")
  playerSelectNobara
  compCharacterChoice
else:
  print("Please try again")

def overTimeExec():
  playerCE=1400
  playerHealth=playerHealth+40
  playerAttack=65
  
def combatLoopYuji():
  return
def combatLoopPanda():
  return
def combatLoopNanami():
  return
def combatLoopMai():
  return
  

  
  
  
  
  
