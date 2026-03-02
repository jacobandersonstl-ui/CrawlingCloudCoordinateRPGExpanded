print("PRE-ALPHA BUILT VERSION 0.0.3 NOTHING IS CONFIRMED TO STAY. EXPECT CHANGES IN THE FULL RELEASE")
#CrawlingCloudCoordinateRPG_Ev2
input("\nWelcome to CrawlingCloudCoordinateRPG_Ev2! This is the full story version of the original CrawlingCloudStoryEngine. Please play the previous game by me, CrawlingCloudCoordinateRPG, even though it's not very good. I'd personally appreciate if you went back and checked out my other projects! Have Fun!")


x = 0
y = 0
main_story_chapter = 0
name = None
gender = None
job = None
stamina = 5
health = 100
potions = 0
move = None
password = None
chapter_4_complete = False

def passowrd_opening():
    global password
    password = input("\nWAIT! If you're starting from a password save, then please type it in now. If not, then just hit  Enter to start a new game! Password: ")
    if password == "lcabbahabkst":
        input("\nPassword Accetped. You will start at character creation because this script doesn't remember what you entered last time. Press Enter.")
        opening()
    elif password == "abahbsctlkab":
        input("\nPassword Accetped. You will start at character creation because this script doesn't remember what you entered last time. Press Enter.")
        opening()
    elif password == "bbckshatalba":
        input("\nPassword Accetped. You will start at character creation because this script doesn't remember what you entered last time. Press Enter.")
        opening()
    else:
        opening()

def opening():
    print("opening working")
    global x, y, main_story_chapter, name, gender, job, stamina
    input("\nYou wake up in your tent in the middle of the woods.")
    input("\nYou stand and go to your mirror.")
    name = input("\nWhat is your name? Type here: --> ")
    gender = input("\nAre you male or female? Type Here: --> ").strip().upper()
    job = input("\nAnd your job/proffession? You can choose: Engineer, chef, military man/woman, or blacksmith. Type Here: --> ").strip().upper()
    print("\n")
    print("Okay, you are", name, "and you are a ", gender, "who does ", job, "for work?")
    char_create_y_n = input("\nIs this information correct? Yes or No: --> ").lower().strip()
    if char_create_y_n == "yes":
        input("\nOkay! Lets Move on!")
        if char_create_y_n == "yes" and password == "abahbsctlkab":
            input("\nWell, you're back off onto your adventure. Good Luck Kid.")
            chapter_2()
        elif char_create_y_n == "yes" and password == "bbckshatalba":
            input("\nWell, you're back off onto your adventure. Good Luck Kid.")
            chapter_3()
        else:
            chapter_1()
    elif char_create_y_n == "no":
        input("\nLets restart then."), opening()

def chapter_1():
    print("c1 working")
    global x, y, main_story_chapter, stamina, health, potions, move
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
        move = input("So,  where too? W (North), A (West), S (South), or D (East)? ! space = 5 meters").strip()
        
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
            quit_y_n = input("\nAre you sure you want to quit? Y/N: ").upper().strip()
            if quit_y_n == "Y":
                input("\nWAIT! Wtite this password down so you can get back to this level when you return: lcabbahabkst")
                print("\nOk, Bye!")
                chapter_playing = False
                quit()
            elif quit_y_n == "N":
                input("\nThen Let's get you back in there!")

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
            print("\n" + "="*140)
            print("                As you walk into the barren streets of Yirelem, you see the giant marble buildings. Let's get to the castle.")
            print("="*140)
            print("\n"*2)

            input("\nPress Enter to Proceed.")

            print("\n" + "="*125)
            print("                Act I End")
            print("="*125)
            print("\n"*2)

            input("\nPress Enter to begin Chapter II")

            chapter_playing = False
            chapter_2()


def chapter_2():
    global x, y, main_story_chapter
    chapter_2_playing = True
    print("c2 working")
    main_story_chapter = 2
    chapter_3()

def chapter_3():
    print("c3 working")
    global x, y, main_story_chapter
    chapter_3_playing = True
    main_story_chapter = 3
    ending()

def ending():
    global x, y, main_story_chapter, chapter_4_complete
    print("ending working")
    chapter_4_playing = True
    main_story_chapter = 4
    chapter_4_complete = True

while True:
    if main_story_chapter == 0:
        passowrd_opening()
    elif main_story_chapter == 4 and chapter_4_complete == True:
        input("\nThank you for playing The Crawling CLoud Pre-Alpha Version 0.0.3. This is my first serious game project I've published on GitHub and really want to thank everyone for their support. Stay tuned for future alphas/betas and eventually the FULL RELEASE!!!")
        quit()