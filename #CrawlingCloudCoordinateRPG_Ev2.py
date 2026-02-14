#CrawlingCloudCoordinateRPG_Ev2
input("\nWelcome to CrawlingCloudCoordinateRPG_Ev2! This is the full story version of the original CrawlingCloudStoryEngine. Please play the previous game by me, CrawlingCloudCoordinateRPG, even though it's not very good. I'd personally appreciate if you went back and checked out my other projects! Have Fun!")


x = -31
y = 35
main_story_chapter = 0
name = None
gender = None
job = None
stamina = 5
health = 100
potions = 0

def opening():
    print("opening working")
    global x, y, main_story_chapter, name, gender, job, stamina
    input("\nYou lay asleep in your bed......... AHHH! Well, you're awake now.")
    input("\nYOo stand and go to your mirror.")
    name = input("\nWhat is your name? Type here: --> ")
    gender = input("\nAre you male or female? Type Here: --> ").strip().upper()
    job = input("\nAnd your job/proffession? You can choose: Engineer, chef, military man/woman, or blacksmith. Type Here: --> ").strip().upper()
    print("Okay, you are", name, "and you are a ", gender, "who does ", job, "for work?")
    char_create_y_n = input("\nIs this information correct? Yes or No: --> ").lower().strip()
    if char_create_y_n == "yes":
        input("\nOkay! Lets Move on!")
        chapter_1()
    elif char_create_y_n == "no":
        input("\nLets restart then."), opening()

def chapter_1():
    print("c1 working")
    global x, y, main_story_chapter, stamina, health, potions
    main_story_chapter = 1

    chapter_playing = True
    car_searched = False
    robot_2058_found = False

    print("\n" + "="*50)
    print("                Act I: Where am I?")
    print("="*50)
    print("\n"*2)

    while chapter_playing:
        print("Status Bar: Health:", health, "Potions:", potions, "X:", x, "Y:", y, "Name:", name, "Stamina:", stamina, ". You can go North, East, South, or West with the W, A, S, and D keys. You can use potions with the P key.")
        move = input("So,  where too? W (North), A (West), S (South), or D (East)?").strip()
        
        if move == "N":
            print("Ok! Going North!")
            y += 2
            stamina -= 1
            #moves += 1
        elif move == "E":
            print("Ok! Going East!")
            x += 2
            stamina -= 1
            #moves += 1
        elif move == "S":
            print("Ok! going South!")
            y -= 2
            stamina -= 1
            #moves += 1
        elif move == "W":
            print("Ok! Going West!")
            x -= 2
            stamina -= 1
            #moves += 1
        elif move == "n":
            print("Ok! Going North!")
            y += 1
            if stamina < 5:
                stamina += 1
            #moves += 1
        elif move == "e":
            print("Ok! Going East!")
            x += 1
            if stamina < 5:
                stamina += 1
            #moves += 1
        elif move == "s":
            print("Ok! going South!")
            y -= 1
            if stamina < 5:
                stamina += 1
            #moves += 1
        elif move == "w":
            print("Ok! Going West!")
            x -= 1
            if stamina < 5:
                stamina += 1
            #moves += 1
        elif move == "Q":
            print("Ok! Bye!")
            quit()
        if stamina < 0:
            stamina = 0

        #Events
        if x == 14 and y == 7 and not car_searched:
            input("\n[!] EVENT [!]")
            input("\nYou found an old, broken down car.")
            if job == "ENGINEER":
                input("You tear the thing apart and manage to find a few potions stuffed in a bag under the drivers seat. +5 Potions!")
                potions += 5
            else:
                input("\nYou couldn't salvage anything from the car. -1 stamina.")
                stamina -= 1
            car_searched = True
        
        if x == 21 and y == 27 and not robot_2058_found:
            input("\n[!] EVENT [!]")
            input("\nYou found an old, rusty robot buried in dirt. It must've been there since 2058. 50 years is a long time.")
            input("\nBack on the journey though! We need to get to the capital!")
            robot_2058_found = True

        if x > 50:
            x = 50
            input("The fog is way to thick to go East.")
        if y > 50:
            y = 50
            input("The fog is way to thick to go North.")
        if x < -50:
            x = -50
            input("The fog is way to thick to go West.")
        if y < -50:
            y = -50
            input("The fog is way to thick to go South.")

        if x == -31 and y == 35:
            print("\n" + "="*50)
            print("                You made it to the Capital, hooray!")
            print("="*50)
            print("\n"*2)

            input("\n")
            
            print("\n" + "="*50)
            print("                Act I End")
            print("="*50)
            print("\n"*2)
            chapter_playing = False
            chapter_2()


def chapter_2():
    global x, y, main_story_chapter
    print("c2 working")
    main_story_chapter = 2
    chapter_3()

def chapter_3():
    print("c3 working")
    global x, y, main_story_chapter
    main_story_chapter = 3
    ending()

def ending():
    global x, y, main_story_chapter
    print("ending working")
    main_story_chapter = 4

while True:

    if main_story_chapter == 0:
        opening()
    elif main_story_chapter == 4:
        quit()