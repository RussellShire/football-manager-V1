# football-manager-V1
Old School Football Manager, a text based Python game to push basic concepts and practice managing complexity.

Overview:
The eventual aim of this project would be a Football manager style game but with an old school twist. Drinking at half time, bribing officials, shouting at players and most importantly, big brown coats
However, my initial aim is to get a single match automated before adding in any gameplay elements.

Some notes:
I'm trying to keep this Python only, because I'm learning but also because it's an interesting restriction. This means I'm using nested dictionaries to store data instead of the obvious solution of MySQL
I'll probably refactor later to add MySQL. As a result of using dictionaries it's actually influenced a lot of what I've been doing, which will make refactoring very annoying.
I've also started without modules because I was keen to get something working, this is clearly a terrible idea I'll come to regret and need to fix later.
I'm using simulated dice rolls using rand to make things happen in an unpredictable way.
There is an over reliance on Global variables because I'm generating a lot of things in functions that then need to be passed to other functions. I am aware this is bad pratice and I'll need to fix eventually.

How it works:

- Player and team generation:
The main 'database' is nested dictionary 'players_dict' where the keys are players names with the space removed. The items are various attributes like, position, team and skills.
Players and team names are randomly generated using random dice rolls the length of the list. Players can have any two names, there are no duplicate players but names can be used over and over.
Teams take one name from the town list and one name from the secondnamepart list ('United' or 'FC' etc). Names are popped from these lists as they're generated so there can only be a set amount of teams.

Players positions are assigned based on their stats, the player in a team with the highest defence is the Goal keeper. The top three players for attack skill are forwards, 
the top three for defence skill are defenders, the rest are assigned as mid field - theoretically with a balanced set of skills.

This is done using doubledictionarysearch, that creates a temporary list called searchresult of all the players in a team who don't have a position assigned. 
There is then a second list of skills created. There are while loops that keep assigning positions and for loops that cycle through teams and players until every position is filled.

- A match:
The pitch is split up into postions, forward, midfield, defence and goal. A forward faces off against a forward, the two players are assigned as possession or intercepting.
There is then a skills test (with some dice roll modifiers to their base skills to add some randomness) the player in possession has their attack skill against the intercepting player's defence skill
If the player in position is victorious they will then move forward to the next pitch position (ie. from forward to midfield) to challenge a player in that position.
If the intercepting player is succesful they become the player in possession.

There is also a little function to see how big the gap in skills between players were that adds adjectives 'narrowly' or 'easily' into the print statement.
This is just for flavour and because I could.

The idea is that this will keep playing out until one or the other team makes it to the Goal position, at which point there will be some form of shot taken. This isn't coded yet.
I would also like to add passing into the game so that the player in possession can move the ball to other players (ideally one with a higher attack skill).
Once a goal happens or fails to happen then possession should change, a score should be recorded and the loop repeats.

There also needs to be some sort of counter of how many moves have been made to decide when half-time and full time occurs. 
Eventually there will also be fouls and special skills to add more variety to the game play.

