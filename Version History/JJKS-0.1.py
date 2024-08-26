import math
import random

print("Welcome to JJK Skirmish")
print("Currently in beta build V0.1")
print("NEW CHARACTERS: Yuji Itadori, Panda, Mai Zen'in, Nanami")
print("")
print("Produced by AUG__DOG")
print("Collaborators; Inifitygames, ZigZagFabricGuy")
print("")

print("Disclaimer: I do not own any of the rights to this content, this is a fan made game, made without the consent of the creator")

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
      stunBuild=100
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
  class passive():
    class SukunasVessel():
      #playerAttack=playerAttack+25
      #playerAbility5=abilities.domainExpansion.malevolentShrine
      #playerCE=playerCE+1000
      #playerLives=2
      abilityID="Sukunas Vessel"
    class cursedCorpse():
      #playerLives=3
      #playerCE=playerCE+500
      abilityID="Cursed Corpse"
    class overtime():
      #playerCE=900
      def overtimeActivate():
        if playerHealth<=40:
          #playerCE=1300
          #playerHealth=playerHealth+40
          #playerAttack=65
          while playerHealth<250:
            overtimeTurn=1
            if playerTurn=="True":
              overtimeTurn=overtimeTurn+1
          if overtimeTurn==5:
            #playerCE=200
            #playerHealth=150
            #playerAttack=45
            john=3
      abilityID="Overtime" 
    class zenin():
      #playerHealth=playerHealth+50
      #playerAttack=playerAttack+15
      #playerSpeed=playerSpeed+20
      abilityID="Zen'in Heritage"
      
class characters():
  class JujustsuHigh():
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
      passive=abilities.passive.SukunasVessel
      ability1=abilities.cursedControl.divergentFist
      ability2=abilities.cursedTechnique.dismantle
      ability3=abilities.cursedControl.blackFlash
      ability4=abilities.domainExpansion.malevolentYapping
    class Panda():
      rank="2"
      difficulty="Medium"
      description="With 3 lives, Panda is a tank on the battle field, swapping between cores will allow you to deal massive damage and build tons of stun on your opponent"
      health=350
      attack=45
      defense=40
      speed=35
      cursedEnergy=800
      passive=abilities.passive.cursedCorpse
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
      defense=10
      speed=45
      cursedEnergy=1000
      passive=abilities.passive.overtime
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
      passiveAbility=abilities.passive.zenin
      ability1=abilities.cursedControl.cursedBullet
      ability2=abilities.cursedWeapons.rubberBullet
      ability3=abilities.cursedWeapons.rapidFire
      ability4=abilities.cursedTechnique.creation
    class megumiFushiguro():
      rank="2"
      difficulty="Easy"
      Health=150
      attack=35
      defense=15
      speed=40
      cursedEnergy=750
      passiveAbility=abilities.passive.zenin
      ability1=abilities.cursedTechnique.TSFrogs
      ability2=abilities.cursedTechnique.TSDogs
      ability3=abilities.cursedTechnique.TSNue
      ability4=abilities.cursedTechnique.TSElephant

def playerSelect():
  
