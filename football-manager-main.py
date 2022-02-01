import random

players_dict = dict(StevenConfident={'Name': 'Steven Confident', 'Position': '',
                                     'AttackSkill': 7, 'DefSkill': 3, 'Team': 'Athletico Mince'},
                    DouglasUppity={'Name': 'Douglas Uppity', 'Position': '',
                                   'AttackSkill': 4, 'DefSkill': 6, 'Team': 'Athletico Mince'})


names = ["Farter", "Frank", "Bruce", "Butcher", "Eddie", "Edward", "Russell", "Marion", "Butch",
         "Bobby", "Doug", "Douglas", "Eric", "Terry", "Terrible", "Fantastic", "Michael", "Mike",
         "Timothy", "Leon", "Timmy", "Ericsson", "Knight", "Fishmonger", "Killer", "Ken", "Kenneth",
         "Kevin", "Kev", "Fencepost", "Billy", "Richard", "Scotch", "Beercan", "Davis", "Philip",
         "Arthur", "Clark", "Boozer", "Ronald", "Dick", "Robert"]

positions = ["Forward", "Midfield", "Defence", "Goal"]

towns = ["Altringham", "Bolton", "Chorlton", "Stockport", "Audenshaw", "Blackrod", "Bury", "Oldham",
         "Salford", "Failsworth", "Hyde", "Middleton", "Wigan", "Urmston", "Ramsbottom", "Hindley"]

teamnamecomponents = ["Athletic", "Wanderers", "City", "Town", "United", "Tacklers", "Rovers", "Arsewipes",
                      "Rangers", "County", "Forest", "FC", "Downandouts", "Under 15s", "Kickers", "Bastards"]

teams = ['Athletico Mince']

searchresult = []

#prints through the nested player dictionary and prints in a pretty format

def printdictionary(dictionary):
    for p_id, p_info in dictionary.items():
        print("\nDict ID:", p_id)

        for key in p_info:
            print(key + ':', p_info[key])


# looks for an item in a nested dictionary matching a search, returns them as a list called search result


def dictionarysearch(dictionary, item, search):
    searchresult.clear()
    for p_id, p_info in dictionary.items():
        if p_info[item] == search:
            searchresult.append(p_id)


# takes two arguements into dictionary search


def doubledictionarysearch(dictionary, item, search, item2, search2):
    searchresult.clear()
    for p_id, p_info in dictionary.items():
        if p_info[item] == search and p_info[item2] == search2:
            searchresult.append(p_id)

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


def newplayer(xteam):
    namegen()
    playerskills()
    players_dict[namecode] = {}
    players_dict[namecode]['Name'] = newname
    players_dict[namecode]['Position'] = ''
    players_dict[namecode]['AttackSkill'] = attackskill
    players_dict[namecode]['DefSkill'] = defskill
    players_dict[namecode]['Team'] = xteam


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
        pitchposition = pitchposition+1
        print('and moves to ' + players_dict[defender]['Team'] + '\'s ' +positions[pitchposition])
    else:
        possession = defender
        intercepting = attacker
        pitchposition == 0
        print(players_dict[defender]['Name'] + adject + ' tackles ' + players_dict[attacker]['Name'])


def goal():
    global intercepting
    global pitchposition
    goalareas = ['bottom left corner', 'top left corner', 'right at the keeper', 'bottom right corner', 'top right corner']
    shotposition = randlistitem(goalareas)
    if shotposition != 'right at the keeper':
        keeperdive = ['left', 'right']
        if keeperdive == 0 and (shotposition == goalareas[0] or shotposition == goalareas[1]):
            print('save')
        else:
            print('Goal!')
            pitchposition = 0
            kickoff(players_dict[intercepting]['Team'])
    else:
        print('shot at the keeper!')


def kickoff(kickoff):
    global intercepting
    global matchtimer
    doubledictionarysearch(players_dict, 'Team', kickoff, 'Position', 'Forward')
    possession = randlistitem(searchresult)
    doubledictionarysearch(players_dict, 'Team', awayteam, 'Position', 'Midfield')
    intercepting = randlistitem(searchresult)

    print(players_dict[possession]['Team'] + '\'s ' + players_dict[possession]['Name'] + ' kicks off against '
          + players_dict[intercepting]['Team'] + '\'s ' + players_dict[intercepting]['Name'])

    while matchtimer <= 15:
        while positions[pitchposition] != 'Goal':
            matchtimer = matchtimer+1
            print(matchtimer)
            attack(possession, intercepting)
            if players_dict[possession]['Team'] == hometeam:
                doubledictionarysearch(players_dict, 'Team', awayteam, 'Position', positions[pitchposition])
                intercepting = randlistitem(searchresult)
            else:
                doubledictionarysearch(players_dict, 'Team', hometeam, 'Position', positions[pitchposition])
                intercepting = randlistitem(searchresult)
        goal()

    else:
        print('Halftime!')
        kickoff(awayteam)



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
searchlist = []
max_index = 0
matchtimer = 0

# Makes teams

teamsgen()

# goes through the teams and adds a number of players per team.

for xteam in teams:
    dictionarysearch(players_dict, 'Team', xteam)

    while len(searchresult) <= 19:
        newplayer(xteam)
        dictionarysearch(players_dict, 'Team', xteam)


# assigns 'Goal' position to each team by finding the player with the highest DefSkill,
# however the first goal position is always the first player because of the looping way I've written this.


for xteam in teams:
    dictionarysearch(players_dict, 'Team', xteam)
    searchlist.clear()

    for xplayer in searchresult:
        searchlist.append(players_dict[xplayer]['DefSkill'])
        max_value = max(searchlist)
        max_index = searchlist.index(max_value)

    players_dict[searchresult[max_index]]['Position'] = 'Goal'


# counts how many players in each team have the position Defence, if it's less than or equal to 3 it'll find all players with no position
# it then finds the player with the highest def skill and assigns 'Forward' it loops until there are 3 defenders


doubledictionarysearch(players_dict, 'Team', xteam, 'Position', 'Defence')
while len(searchresult) <= 3:
    for xteam in teams:
        doubledictionarysearch(players_dict, 'Team', xteam, 'Position', '')
        searchlist.clear()

        for xplayer in searchresult:
            searchlist.append(players_dict[xplayer]['DefSkill'])
            max_value = max(searchlist)
            max_index = searchlist.index(max_value)

        players_dict[searchresult[max_index]]['Position'] = 'Defence'
        doubledictionarysearch(players_dict, 'Team', xteam, 'Position', 'Defence')


# counts how many players in each team have the position forward, if it's less than or equal to 3 it'll find all players with no position
# it then finds the player with the highest attack skill and assigns 'Forward' it loops until there are 3 Forwards


doubledictionarysearch(players_dict, 'Team', xteam, 'Position', 'Forward')
while len(searchresult) <= 3:
    for xteam in teams:
        doubledictionarysearch(players_dict, 'Team', xteam, 'Position', '')
        searchlist.clear()

        for xplayer in searchresult:
            searchlist.append(players_dict[xplayer]['AttackSkill'])
            max_value = max(searchlist)
            max_index = searchlist.index(max_value)

        players_dict[searchresult[max_index]]['Position'] = 'Forward'
        doubledictionarysearch(players_dict, 'Team', xteam, 'Position', 'Forward')

# Assigns anyone who doesn't have a position as Midfield

for xteam in teams:
    doubledictionarysearch(players_dict, 'Team', xteam, 'Position', '')

    for xplayer in searchresult:
        players_dict[xplayer]['Position'] = 'Midfield'

#printdictionary(players_dict)

# Starting to model a match

hometeam = randlistitem(teams)
awayteam = randlistitem(teams)
print(hometeam + ' vs ' + awayteam)

kickoff(hometeam)
