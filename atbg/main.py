from cs50 import SQL
from time import sleep
from helpers import isfloat
db = SQL("sqlite:///atbg.db")

#parameter variables
player = {"i": [], "onme": []}
scrollspeed = .03


def start_menu():
    print("""    Start - "s"
    Options - "o" """)
    while(True):
        x = input("")
        if x == "s":
            print("type 'help' for keywords")
            while progress != 100:
                scroll( prompt() )
            scroll("You Win.")
        if x == "o":
            optionmenu()
            

def prompt():
    #promts user for input
    inpt = input("")
    
    #standardizes synonym verbs and splits into 5 word list
    standardedtxt = standardizer(inpt)
    phrase = str(standardedtxt)
    #if two word phrase
    if len(phrase.split()) == 2:
        objs = db.execute("SELECT name FROM objects")
        for obj in objs:
            if obj["name"] in phrase:
                action = phrase.split()[0]
                returnvar = db.execute("SELECT * FROM objects WHERE name = :name", name = obj["name"])
                
                if action in returnvar[0] and returnvar[0]["minreq"] <= progress <= returnvar[0]["maxreq"]:
                    return evaluate(returnvar[0][action], phrase)
                    
                    
    elif "use " in phrase and "on " in phrase:
        words = phrase.split()
        reqcheq1 = db.execute("SELECT id, minreq, maxreq FROM objects WHERE name=:sub", sub=words[1])
        reqcheq2 = db.execute("SELECT id, minreq, maxreq FROM objects WHERE name=:sub", sub=words[3])


        if len(reqcheq1) == 1 and len(reqcheq2) == 1:
            quote = db.execute("SELECT * FROM usetabel WHERE id = :idd", idd=reqcheq1[0]["id"])
            if len(quote) == 1:
                if quote[0][words[3]] != None and reqcheq1[0]["minreq"] <= progress <= reqcheq1[0]["maxreq"] and reqcheq2[0]["minreq"] <= progress <= reqcheq2[0]["maxreq"]:
                    return evaluate(quote[0][words[3]], phrase)
        
        
    #grabs quote from phrase database
    quote = db.execute("SELECT quote, minreq, maxreq FROM phrases WHERE phrase = :command", 
        command=phrase)
    
    #returns quote
    if len(quote) == 1 and quote[0]["minreq"] <= progress <= quote[0]["maxreq"]:
        return evaluate(quote[0]["quote"], phrase)
        
    #reprompts user is unknown command occurs
    return "What was that?"
    
def standardizer(text):
    actions = ["see","feel","grab","hear","make","place","smell","taste","use","wear","open","halfs","hole","enter"]
    for action in actions:
        words = db.execute("SELECT name FROM :table", table=action)
        for word in words:
            if word["name"] in text:
                text = text.replace(word["name"], action, 1)
    return text

def scroll(text):
    for i in text:
        print(i, end='')
        sleep(scrollspeed)
    sleep(.2)
    print("")

def evaluate(quote, phrase):
    #one word commands
    if quote == "look":
        return db.execute("SELECT quote FROM roomdescrip WHERE id = :idd", idd=progress + 1)[0]["quote"]
    elif quote == "i":
        return player["i"]
    elif quote == "p":
        return "Progress = " + str(progress)
    
    #sets subject
    subject = ""
    if "use" in phrase:
        subject = phrase.split()[1]
    else:
        subject = phrase.split()[len(phrase.split()) - 1]
    global progress
    
    #checks if usable
    if ("cut" in phrase or "use" in phrase) and (not subject in player["i"]) and not "use box" in phrase:
        return "You need to be holding that first."
        
    
    #conditional things                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    if "open the box" in quote and progress == 0:
        progress = 1
    elif "open the box" in quote:
        return "You can't open something that has been opened already."
    
    if ("cut the box" in quote and "saw" in player["i"]) or ("use box on saw" == phrase):
        progress = 2
    
    if "make a whole" in quote:
        progress = 3
        
    if "enter the hole" in quote and "saw" in player["i"]:
        player["i"].remove("saw")
        progress = 4
        return quote + "\nYou also feel lighter, as if something is not with you."
    elif "enter the hole" in quote:
        progress = 4
        
    if "use that" == phrase:
        progress = 5
    
        
    
    #handles inventory phrases
    if "grab box" == phrase or "grab that" == phrase or "grab hole" == phrase :
        return "That is too heavy to carry around with you, don't ya think?"
    elif "grab" in phrase and not subject in player["i"]:
        player["i"].append(subject)
    elif "grab" in phrase:
        return "You are already holding that"
        
    if "place" in phrase and  subject in player["i"]:
        player["i"].remove(subject)
    elif "place" in phrase and  subject in player["onme"]:
        player["onme"].remove(subject)
    elif "place" in phrase:
        return "You don't have that"
      
    if "wear saw" == phrase or "wear box" == phrase or "wear hole" == phrase or "wear that" == phrase:
        return quote
    elif "wear" in phrase and not subject in player["onme"]:
        player["onme"].append(subject)
    elif "wear" in phrase:
        return "You are already wearing that"
        
    return quote

def optionmenu():
    print("""    Type "scroll" to set scroll speed.
    Type "exit" to go back to the main menu """)
    while True:
        option = input()
        if option == "scroll":
            inpt = input("Set scroll speed: ")
            if isfloat(inpt):
                scrollspeed = inpt
            else:
                print("That wasn't a number.")
        if option == "exit":
            print("""    Start - "s"
    Options - "o" """)
            return

progress = 0
start_menu()
"""Welcome! I see that simple puzzle solving was too easy for you, so I've taken it upon myself to change this room into something that you can never win!
Welcome to the Trivia Room!
Yeah! this time you will lose.
Do you want to year the rules?
(y/n)
I will ask you five questions, get three right, and you win, which by the way will never happen.
Question One: What popular movie focuses on cartoon characters in a world with normal humans?
A: The Adventures of Rocky and Bullwinkle
B: Who Framed Rodger Rabbit
C: Looney Tunes: Back in Action
D: Space Jam
Question Two: What concept is being challenged when a tree falls in a forest with no one there to here it?
A: Senses
B: State of being
C: Knowledge
D: Life
Question Three: What is the first letter of the alphabet?
A: B
B: C
C: A
D: D
Question Four: What property of equality was demonstrated by three of the options in the previous question?
A: Reflexive
B: Mitochondria
C: Transitive
D: Congruence
Question Five: What was the thirty seventh letter in pneumonoultramicroscopicsilicovolcanoconiosis
A:C
B:O
C:A
D:N
"""