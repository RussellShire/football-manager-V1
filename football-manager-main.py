import random

players_dict = dict(StevenConfident={'Name': 'Steven Confident', 'Position': 'forward',
                                     'AttackSkill': 7, 'DefSkill': 3, 'Team': 'Athletico Mince'},
                    DouglasUppity={'Name': 'Douglas Uppity', 'Position': 'forward',
                                   'AttackSkill': 4, 'DefSkill': 6, 'Team': 'Athletico Mince'})


names = ["Farter", "Frank", "Bruce", "Butcher", "Eddie", "Edward", "Russell", "Marion", "Butch",
         "Bobby", "Doug", "Douglas", "Eric", "Terry", "Terrible", "Fantastic", "Michael", "Mike",
         "Timothy", "Leon", "Timmy", "Ericsson", "Knight", "Fishmonger", "Killer", "Ken", "Kenneth",
         "Kevin", "Kev", "Fencepost", "Billy", "Richard", "Scotch", "Beercan", "Davis", "Philip",
         "Arthur", "Clark", "Boozer"]

positions = ["forward", "midfield", "defence", "goal"]

towns = ["Altringham", "Bolton", "Chorlton", "Stockport", "Audenshaw", "Blackrod", "Bury", "Oldham",
         "Salford", "Failsworth", "Hyde", "Middleton", "Wigan", "Urmston", "Ramsbottom", "Hindley"]

teamnamecomponents = ["Athletic", "Wanderers", "City", "Town", "United", "Tacklers", "Rovers", "Arsewipes",
                      "Rangers", "County", "Forest", "FC", "Downandouts", "Under 15s", "Kickers", "Bastards"]

teams = ['Athletico Mince']


# Dice, returns a random number between parameters, low and high


def dice(low, high):
    return int(random.randint(low, high))


# quick function to use the dice to return a random item from a list


def randlistitem(mylist):
    return mylist[dice(0, len(mylist)-1)]


# takes a random town and adds it to a random second part and adds it to the teams list
# it pops the town/teamnamecomponent from their lists until there are none left


def teamsgen():
    while len(towns) > 0:
        firstpart = randlistitem(towns)
        towns.pop(towns.index(firstpart))
        secondpart = randlistitem(teamnamecomponents)
        teamnamecomponents.pop(teamnamecomponents.index(secondpart))
        teams.append(firstpart + ' ' + secondpart)


# Randomly picks a first name from the names list using a dice roll on the number of names in the list (minus 1)
# Randomly picks a last name using the same method, checks if they are the same name, if so rep:eats the process
# For Loop checks if the name already exists and re-runs the roll if so.
# Namecode is without a space so it can be a dict key


def namegen():
    global newname
    global namecode
    firstname = list(names)[dice(0, (len(names)-1))]
    lastname = list(names)[dice(0, (len(names)-1))]
    if firstname == lastname:
        namegen()
    else:
        newname = firstname + ' ' + lastname
        namecode = firstname+lastname
        for x in players_dict.keys():
            if newname == x:
                namegen()
    return


# generates a total skill by taking a number then randomly adding between -2 and 4
# randomly chooses a number between 1 and Total Skill minus 1 for the attack skill
# (so there will always be some left over for the next skill)
# defskill is total skill minus attack skill, aka the leftover.
# This will have to get more complicated as more skills are added
# At the moment I'm using global variables, which is bad practice but I'm not sure how else to take the data out


def playerskills():
    global attackskill
    global defskill
    totalskill = 10 + dice(-2, 4)
    attackskill = dice(1, totalskill-1)
    defskill = totalskill - attackskill
    return


# Creates a new player and stats and adds them to the players dictionary
# every time it's called with the unique ID Player+1. Position and name are currently blank


def newplayer():
    namegen()
    playerskills()
    teamsgen()
    players_dict[namecode] = {}
    players_dict[namecode]['Name'] = newname
    players_dict[namecode]['Position'] = ''
    players_dict[namecode]['AttackSkill'] = attackskill
    players_dict[namecode]['DefSkill'] = defskill
    players_dict[namecode]['Team'] = randlistitem(teams)

def adjective(attk, defn):
    global adject
    if abs(attk-defn) <= 1:
        adject = ' narrowly'
    else:
        if abs(attk-defn) >= 4:
            adject = ' easily'
         

# Takes two player ids and pits attack skill verses defence skill (with dice rolls for some randomness


def attack(attacker, defender):
    global possession
    global intercepting
    global pitchposition
    global attk
    global defn
    attk = players_dict[attacker]['AttackSkill']+dice(-1, 9)
    defn = players_dict[defender]['DefSkill']+dice(-1, 9)
    adjective(attk, defn)
    if attk > defn:
        print(players_dict[attacker]['Name'] + adject + ' dribbles past ' + players_dict[defender]['Name'])
        pitchposition = +1
        print('and moves to '+positions[pitchposition])
    else:
        possession = defender
        intercepting = attacker
        print(players_dict[defender]['Name'] + adject + ' tackles ' + players_dict[attacker]['Name'])


newname = ''
namecode = ''
attackskill = ''
defskill = ''
pitchposition = 0
possession = ''
intercepting = ''
adject = ''
attk = ''
defn = ''


# Makes players

while len(players_dict.keys()) < 100:
    newplayer()

possession = 'StevenConfident'
intercepting = 'DouglasUppity'


#prints through the nested player dictionary and prints in a pretty format

for p_id, p_info in players_dict.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])
