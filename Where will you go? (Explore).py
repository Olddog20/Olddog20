dragon = True
end = True
import time
smallmonsterremains = 'null'
forestentry = False
characterDefintion = {'Health': 100,'Money':0, 'Inventory': []}
def cave():
    answervalidcave1 = False
    while answervalidcave1 == False:
        answervalidcave1 = True
        print ("Inside the cave there is a small monster to your left, and a dark passage to your right. Which way will you go?")
        response = input().upper()
        
        
        if response == "LEFT":

           return response

        elif response == "RIGHT":
            return response
        else:
            print("Invalid response. Please try again")
            time.sleep(0.5)
            answervalidcave1 = False
def River():
    response = 'null'
    answervalid = False
    while answervalid == False:
        answervalid = True

        force = False
        print ("You are at a river. To your right is a cave. Left is a forest. Your status is %s Which direction will you go?" % (characterDefintion))

        response = input ().upper()
        
        if response == "LEFT":

           return response

        elif response == "RIGHT":
            return response
        else:
            print("Invalid response. Please try again")
            time.sleep(0.5)
            answervalid = False
def Battle_End(n, m):
    print ("You defeated the monster! You got %s gold." %(n))
    time.sleep(1)
    if m == 'null':
        print ("Unfortunately, the monster did not drop any items")
        time.sleep(1)
    else:
        print ("The monster dropped %s! You added it to your inventory." % (m))
        time.sleep(1)
    
    
    
        
    

def forest():
    answervalidforest = False
    
    while answervalidforest == False:

        answervalidforest = True
           
        print ("You are in the Forest, you find a fork in the road. Will you go left or right?")

        b = input ().upper()
        
        if b == "RIGHT":
            return b
        elif b == "LEFT":
            return b
        else:
            print ("Invalid response. Please try again")
            answervalidforest = False
def founditem(item, description):
    print ("You found a %s in a chest!" % (item))
    time.sleep(0.5)
    print ("It %s!" % (description))
    time.sleep(0.5)
    characterDefintion['Inventory'].append(item)
    print ("Your inventory now contains %s!" % (characterDefintion['Inventory']))
    time.sleep(0.5)
def Battle(monsterhp,monsterhp2,q,damage):
    criticalhit = damage + damage
    Flee = False
    while 'wooden sword' not in characterDefintion['Inventory']:
        import random
        battlevalue = random.randint (1, 101)
        print ("The monster is at %s/%s health. Will you punch or flee?" % (monsterhp,monsterhp2))
        d = input ().upper()
        if d == "PUNCH":
            monsterhp = monsterhp - 5
            time.sleep(0.5)
            
            print ("The monster is at %s/%s hp." % (monsterhp,monsterhp2))
            time.sleep(0.5)
            if battlevalue < 50:
                print ("The monster tried to hit you and missed!")
                time.sleep(0.5)
                if monsterhp > 0:
                    punch = False
                    battle1 = True
                else:
                    smallmonsterremains = random.randint (1, 5)
                    if smallmonsterremains == 1 or smallmonsterremains == 2 or smallmonsterremains == 3:
                        Battle_End(20,'a small monster leg')
                    else:
                        Battle_End(20,'a small monster eye')

            elif battlevalue > 50:
                print ("The monster hit you, and you lost %s health."% (damage))
                time.sleep(0.5)
                characterDefintion['Health'] = characterDefintion['Health'] - damage
                if chacterDefintion['Health'] <= 0:
                    print ("You died! In your last moments you see a giant monster above you. It makes some sort of sound and calls a bunch of smaller monsters over. They start eating you.....")
                    time.sleep(1)
                    print ("The end!")
                    sys.exit()
                    
                print ("You have %s hp." % (characterDefintion['Health']))
                time.sleep(0.5)
                if monsterhp > 0:
                    punch = False
                    battle1 = True
                else:
                    smallmonsterremains = random.randint (1, 5)
                    if smallmonsterremains == 1 or smallmonsterremains == 2 or smallmonsterremains == 3:
                        Battle_End(20,'a small monster leg')
                    else:
                        Battle_End(20,'a small monster eye')
            elif battlevalue == 50:
                print ("The monster landed a critical hit! You lost %s hp.")
                time.sleep(0.5)
                characterDefintion['Health'] = characterDefintion['Health'] - damage
                if chacterDefintion['Health'] <= 0:
                    print ("You died! In your last moments you see a giant monster above you. It makes some sort of sound and calls a bunch of smaller monsters over. They start eating you.....")
                    time.sleep(1)
                    print ("The end!")
                    sys.exit()
                print ("You have %s hp." % (hp))
               
                if monsterhp > 0:
                    punch = False
                    battle1 = True
                else:
                    smallmonsterremains = random.randint (1, 5)
                    if smallmonsterremains == 1 or smallmonsterremains == 2 or smallmonsterremains == 3:
                        Battle_End(20,'a small monster leg')
                        break
                    else:
                        Battle_End(20,'a small monster eye')
                        break
                        

        elif d == "FLEE":
            print ("You fled from the battle and went back to the %s." %(q))
            Flee = True
            dragon = True

        

        if Flee == True:
            Flee = False
            break
    while 'wooden sword' in characterDefintion['Inventory']:
        import random
        battlevalue = random.randint (1, 101)
        time.sleep(0.5)
        print ("The monster is at %s/%s Health. Will you attack or flee" % (monsterhp,monsterhp2))
        e = input ().upper()
        if e == "ATTACK":
            monsterhp = monsterhp - 10
            time.sleep(0.5)
            print ("The monster is at %s hp." % (monsterhp))
            if battlevalue > 50:
                print ("The monster hit you, and you lost %s health."% (damage))
                time.sleep(0.5)
                characterDefintion['Health'] = characterDefintion['Health'] - damage
                if characterDefintion['Health'] <= 0:
                    print ("You died! In your last moments you see a giant monster above you. It makes some sort of sound and calls a bunch of smaller monsters over. They start eating you.....")
                    time.sleep(1)
                    print ("The end!")
                    sys.exit()
                print ("You have %s hp." % (characterDefintion['Health']))
                time.sleep(0.5)
                if monsterhp > 0:
                    punch = False
                    battle1 = True
                else:
                    smallmonsterremains = random.randint (1, 5)
                    if smallmonsterremains == 1 or smallmonsterremains == 2 or smallmonsterremains == 3:
                        Battle_End(20,'a small monster leg')
                    else:
                        Battle_End(20,'a small monster eye')
                
                                    
            elif battlevalue == 50:
                print ("the monster landed a critical hit! You lost %s hp."%(criticalhit))
                time.sleep(0.5)
                hp = hp - 10
                if chacterDefintion['Health'] <= 0:
                    print ("You died! In your last moments you see a giant monster above you. It makes some sort of sound and calls a bunch of smaller monsters over. They start eating you.....")
                    time.sleep(1)
                    print ("The end!")
                    sys.exit()
                print ("You have %s hp." % (hp))
                time.sleep(0.5)
                if monsterhp > 0:
                    punch = False
                    battle1 = True
                else:
                    smallmonsterremains = random.randint (1, 5)
                    if smallmonsterremains == 1 or smallmonsterremains == 2 or smallmonsterremains == 3:
                        Battle_End(20,'a small monster leg')
                    else:
                        Battle_End(20,'a small monster eye')
            else:
                print ("The monster tried to hit you and missed!")
                if monsterhp > 0:
                    punch = False
                    battle1 = True
                else:
                    smallmonsterremains = random.randint (1, 5)
                    if smallmonsterremains == 1 or smallmonsterremains == 2 or smallmonsterremains == 3:
                        Battle_End(20,'a small monster leg')
                        break
                    else:
                        Battle_End(20,'a small monster eye')
                        break

            


        elif e == "FLEE":
            print ("You fled from the battle and went back to the intersection")
            time.sleep(0.5)
            Flee = True
            dragon = True

        

        if Flee == True:
            Flee = False
            break
        
    
answervalid = False
answervalidforest = False
fist = True
woodsword = False
metalsword = False
answervalidcave1 = False
money = 0
monsterhp1 = 20
hp = 100
import random
battlevalue = random.randint (1, 101)
import sys
battle1 = True
Flee = False

while True:


    a = River()
          
        
    if a == "RIGHT":
        if 'torch' not in characterDefintion['Inventory']:
            time.sleep(0.5)
            print ("It's to dark to go in without a torch.")
            time.sleep(1)
        elif 'torch' in (characterDefintion['Inventory']):
            while True:
                while end == True:
                    time.sleep(0.5)
                    response = cave()
                    if (response == "RIGHT"):
                        if 'wooden sword' not in characterDefintion['Inventory']:
                            answervalidcave1 = False
                            founditem('wooden sword', 'increases your attack power up to ten!')
                            print ("You decide to go back to the intersection")
                            time.sleep(1)
                        else:
                            print ("You already went to the chest! There's nothing there so you decide to go back to the intersection")
                    elif (response == "LEFT"):
                           Battle(20,20,'Cave',5)
                           while dragon == True:
                               print ('''You here the roar of an angry bigger monster coming....
perhaps it's a good idea to start going a little faster.....''')
                               time.sleep(1)
                               print ("You here some roaring in the right tunnel. Sounds almost like a dragon....")
                               time.sleep(2)
                               print ("Will you go right or left?")
                               response = input().upper()
                               if response == "RIGHT":
                                   Battle (100,100,'Intersection',40)
                               elif response == "LEFT":
                                    print ("You run away as fast as you can! You somehow find you way out of the way cave, into a dragons den.")
                                    time.sleep(1)
                                    print ("It's filled with treasure")
                                    time.sleep(1)
                                    print ("A shadow falls on the wall in front of you you")
                                    time.sleep(2)
                                    print("You slowly turn around.....")
                                    time.sleep(3)
                                    print("The end!(For now!)")
                                    sys.exit()
                       
                       
                        
                            
        
             
    elif a == "LEFT" and forestentry == False:
        response = forest()
        if (response == "RIGHT"):
            print ("You found a small chest with a torch and some money inside. A mysterious force teleports you out of the forest and blocks you from going into the forest again.")
            forestentry = True
            money = money + 10
            founditem('torch', 'lets you see in dark places!')
            answervalid = False
        elif (response == "LEFT"):
            print ("You found a huge chest with a torch and lots of money! A mysterious force teleports you and blocks you from going back into the forest")
            forestentry = True
            money = money + 30
            founditem('torch', 'lets you see in dark places!')
            answervalid = False

    elif a == "LEFT" and forestentry == True:
        print ("A mysterious force blocks your path. You decide to go back to the begining")
        answervalid = False

        
