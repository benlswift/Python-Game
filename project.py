import random
import pickle
import pygame
import time

def display_update(text,screen):
    
    #Modified from: https://sivasantosh.wordpress.com/2012/07/18/displaying-text-in-pygame/
    #updates the display - white background & text box
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.fill((255,255,255))
            
    screen.blit(text, textrect)
    pygame.display.update()

def menu():
    #Modified from: http://www.pygame.org/docs/tut/tom/games2.html and: https://sivasantosh.wordpress.com/2012/07/18/displaying-text-in-pygame/
    pygame.init()
    pygame.display.set_mode((900,400))
    screen = pygame.display.set_mode((900,400)) # Set screen size of pygame window
    background = pygame.Surface(screen.get_size())  # Create empty pygame surface
    background.fill((255, 255, 255)) # A white background  
    background = background.convert()
    basicfont = pygame.font.SysFont('Arial', 16)#Font is Arial
    text = basicfont.render("""Welcome - do you have what it takes to master four levels of word puzzles, maths challenges and quiz questions? (click to proceed)""", True, (0, 0, 0))
    display_update(text,screen)
    while True:
        for event in pygame.event.get():
            #When the mouse is clicked the next instruction is shown
            if event.type == pygame.MOUSEBUTTONDOWN:
                background_image = pygame.image.load("background.jpg").convert()
                screen.blit(background_image, [0,0])
                pygame.display.update()

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    text = basicfont.render("""You will now be taken to the game...""", True, (0, 0, 0))
                    display_update(text,screen)
                    pygame.quit()
                    main()
                    
                
                if event.key == pygame.K_2:
                    text = basicfont.render("""You can search for your personal best score...""", True, (0, 0, 0))
                    display_update(text,screen)
                    pygame.quit()
                    name = input("What is your name?\n")
                    find_score(name)
                    menu()
                
                if event.key == pygame.K_3:
                    text = basicfont.render("""You can view the high scores...""", True, (0, 0, 0))
                    display_update(text,screen)
                    pygame.quit()
                    viewhigh()
                    menu()
                    
                    
                if event.key == pygame.K_4:
                    pygame.quit()
                    print("You have exited the game")
    
#The questions are located in a file
def open_file(file_name, mode):
    file = open(file_name, mode)
    return file

#The file is read - this is used in read_file function
#Modified from http://www.delmarlearning.com/companions/content/1435455002/downloads/index.asp chapter 7 trivia_challenge.py
def read_line(file):
    line = file.readline()
    return line
    
def read_file(file):
    
    #The lines of the file are read using the read_line function
    description = read_line(file)
    question = read_line(file)
    #Possible answers are shown
    #read 4 lines
    possible_answer1 = read_line(file)
    possible_answer2 = read_line(file)
    possible_answer3 = read_line(file)
    possible_answer4 = read_line(file)
    correct_answer = read_line(file)
    #correct answer is the first character of the next line
    if correct_answer:
        correct_answer = correct_answer[0]
    answer_description = read_line(file)
    points = read_line(file)
    #The lines read from the file are returned
    return description, question, possible_answer1, possible_answer2, possible_answer3, possible_answer4, correct_answer, answer_description, points
    
def level_one(scorelist):
    #The file is printed
    score = 0
    one_file = open_file("level one.txt", "r")
    description, question, possible_answer1, possible_answer2, possible_answer3, possible_answer4, correct_answer, answer_description, points = read_file(one_file)
    while description:
        #While there is text in the description line the file is printed 
        print(description)
        print(question)
        print(possible_answer1)
        print(possible_answer2)
        print(possible_answer3)
        print(possible_answer4)
        answer = input("What is your answer? ")
        if answer == correct_answer:
            print("Well done. You gained", points," point(s)")
            score += int(points)
            print(answer_description)
        else:
            print("That's wrong!",answer_description)
        print("Score:", score, "\n")
    
    
        description, question, possible_answer1, possible_answer2, possible_answer3, possible_answer4, correct_answer, answer_description, points = read_file(one_file)  
    one_file.close()
    #add level one score to list
    scorelist.append(score)
    print("Your score for Level One is", score,"\n")


def level_two(scorelist):
    score = 0
    two_file = open_file("level two.txt", "r")
    #The file is printed 
    description, question, possible_answer1, possible_answer2, possible_answer3, possible_answer4, correct_answer, answer_description, points = read_file(two_file)
    while description:
        #While there is text in the description line the file is printed 
        print(description)
        print(question)
        print(possible_answer1)
        print(possible_answer2)
        print(possible_answer3)
        print(possible_answer4)
        answer = input("What is your answer? ")
        if answer == correct_answer:
            print("Well done. You gained", points," point(s)")
            score += int(points)
            
            print(answer_description)
        else:
            print("That's wrong!",answer_description)
        print("Score:", score, "\n")
    
    
        description, question, possible_answer1, possible_answer2, possible_answer3, possible_answer4, correct_answer, answer_description, points = read_file(two_file)  
    two_file.close()
    #add level one score to list
    scorelist.append(score)
    print("Your score for Level Two is", score,"\n")


#Bonus question for low scores
def bonus_question(scorelist):
    score = 0
    three_file = open_file("level three.txt", "r")
    #The file is printed 
    description, question, possible_answer1, possible_answer2, possible_answer3, possible_answer4, correct_answer, answer_description, points = read_file(three_file)
    while description:
    #While there is text in the description line the file is printed 
        print(description)
        print(question)
        print(possible_answer1)
        print(possible_answer2)
        print(possible_answer3)
        print(possible_answer4)
        answer = input("What is your answer? ")
        if answer == correct_answer:
            print("Well done. You gained", points," point(s)")
            score += int(points)
            
            print(answer_description)
        else:
            print("That's wrong!",answer_description)
            print("Score:", score, "\n")
    
    
        description, question, possible_answer1, possible_answer2, possible_answer3, possible_answer4, correct_answer, answer_description, points = read_file(three_file)  
    three_file.close()
    #add level one score to list
    scorelist.append(score)
    print("Your score for Level Three is", score,"\n")

    
    
    
# level three is a maths challenge question
#The challenge is generated randomly from a dictionary
def level_three(scorelist):
    challenges = {"I have travelled 1.6Km in 20 mins, how far have I gone after 30mins, in meters?":"2400","What is pi to 3 decimal places?":"3.141","I have a pentagon and a nonagon how many sides do I have?":"14","""
What is 6 to the power of 0?""":"0","My car weighs 2000Kg, I weigh 20x less. How much does the car weigh if I get in, in Kg?":"2100","""It takes 15 minutes to get home on the bus. It's average speed is 20mph, how far
away do I live in miles?""":"5","I want to buy milk & bread at £1.49 & £1.20 respectively. I have 2 50p coins & 4 20p coins, can I afford it?(y/n)":"y","""If I walk 20 meters then stop, walk another 40 meters and then come back.
What is my displacement?""":"0"}
    tries = 0
    score = 0
    print("Here's some tricky maths questions")
    while tries < 5:
        challenge = random.choice(list(challenges))
        print(challenge)
        playeranswer = input("")
        answer = challenges[challenge]
        tries += 1
        if playeranswer == answer:
            score += 3
            print("Well Done\n")
            
        else:
            print("That's wrong, the answer is", answer)
    #add score to list
    scorelist.append(score)
    


def level_four(scorelist):
    #Modified from: http://stackoverflow.com/questions/27732736/pygame-key-pressed Author: Pyboss
    score = 0
    pygame.init()
    pygame.display.set_mode((900,400))
    screen = pygame.display.set_mode((900,400)) # Set screen size of pygame window
    background = pygame.Surface(screen.get_size())  # Create empty pygame surface
    background.fill((255, 255, 255)) # A white background  
    background = background.convert()
    background_image = pygame.image.load("four_welcome.jpg").convert()
    screen.blit(background_image, [0,0])
    pygame.display.update()
    running = True

    while running:
        for event in pygame.event.get():
            #When the mouse is clicked the next instruction is shown
            if event.type == pygame.MOUSEBUTTONDOWN:
                background_image = pygame.image.load("four_q1.jpg").convert()
                screen.blit(background_image, [0,0])
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                #If 8 is pressed an image is displayed
                if event.key == pygame.K_8:
                    score += 2
                    background_image = pygame.image.load("four_q2.jpg").convert()
                    screen.blit(background_image, [0,0])
                    pygame.display.update()
                if event.key == pygame.K_9:
                    score -= 3
                    background_image = pygame.image.load("four_q2WRONG.jpg").convert()
                    screen.blit(background_image, [0,0])
                    pygame.display.update()
                if event.key == pygame.K_LEFT:
                    score += 3
                    background_image = pygame.image.load("four_q3.jpg").convert()
                    screen.blit(background_image, [0,0])
                    pygame.display.update()
                if event.key == pygame.K_RIGHT:
                    score -= 4
                    background_image = pygame.image.load("four_q3WRONG.jpg").convert()
                    screen.blit(background_image, [0,0])
                    pygame.display.update()
                    
                    print("That's the end of level four")
                    #The pygame window closes
                    running = False
                    
                if event.key == pygame.K_f:
                    score += 2
                    background_image = pygame.image.load("four_q4.jpg").convert()
                    screen.blit(background_image, [0,0])
                    pygame.display.update()
                    
                    print("That's the end of level four")
                    
                    running = False
                    
                if event.key == pygame.K_g:
                    score -= 2
                    background_image = pygame.image.load("four_q4WRONG.jpg").convert()
                    screen.blit(background_image, [0,0])
                    pygame.display.update()
                    
                    print("That's the end of level four")
                    
                    running = False
                    
         #To close the window False is called            
        while not running:
            #While running = False the window closes
            pygame.quit()
            #Score is added to list
            scorelist.append(score)
            break


def high_score(total):
    #The highscore is read & if it is beaten it will be replaced
    file = open("highscore.txt", "r")
    highscore = file.readline()
    print ("The high score is",highscore)
    file.close()
    if total > int(highscore):
        file = open("highscore.txt", "w")
        file.write(str(total))
        print("Well done you have beaten the high score!\n Your score of", total, "has beaten", highscore," to be the new highscore!")
        file.close()

def viewhigh():
    #Used as menu option to see high score
    file = open("highscore.txt", "r")
    highscore = file.readline()
    print ("The high score is...", highscore)
    file.close()



#Saves the players score into a file

def score_save(name,total,oldscore):
    #If player hasn't played before their score is saved
    if oldscore == 0:
        print("Your score has been saved for you to beat next time")
        file = open('saved_scores.txt', 'ab+')
        scores = {name:total}
        pickle.dump(scores,file)
        file.close
    elif total > int(oldscore):
        print("You have beaten your previous best!")
        #If new score is better than their last score it is saved
        file = open('saved_scores.txt', 'ab+')
        scores_dict = pickle.load(file)
        #Their past best score is deleted
        del scores_dict[name]
        scores = {name:total}
        pickle.dump(scores,file)
        print (scores)
        file.close
    else:
        print("You didn't beat your previous score!")

def find_score(name):
    #The players last score is found if they have played before
    file = open('saved_scores.txt', 'rb')
    scores_dict = pickle.load(file)
    name = name
    if name in scores_dict:
        oldscore = scores_dict[name]
        print ("You previous best is", oldscore, ",try to beat it!")
        
    else:
        print("You haven't played before!")


def main():
    #A list is created to store scores
    scorelist = []
    oldscore = 0
    name = input("What is your name?")
    find_score(name)
    #start the timer
    start = time.time()
    level_one(scorelist)
    #whether the player moves up a level depends on their score
    total = sum(scorelist)
    if total > 3:
        level_two(scorelist)
        total = sum(scorelist)
    else:
        print("You needed 3 points to continue, you only got", total)
        print("Oh dear, you haven't scored highly enough to progress")
        score_save(total, oldscore, name)
    if total < 10:
            #If the total is less than 10 a bonus level is played - to boost players score
        bonus_question(scorelist)
        total = sum(scorelist)
    level_three(scorelist)
    total = sum(scorelist)
    level_four(scorelist)
    #The scores from each level are added together to give a total score
    total = sum(scorelist)
    print("And that's the end of the game!")
    print("You scored", total, "points")
    #end the timer
    end = time.time()
    #Work out how long it took to finush game
    timer = int(end) - int(start)
    print("And it took you", timer, "seconds to complete the game")
    score_save(name,total,oldscore)
    high_score(total)
    #Ask the user if they want to play again
    again = input("Do you want to play again?(y/n)")
    if again == "y":
        menu()
    else:
        print("Thankyou for playing")
        input("\n\nPress enter to exit")

    
menu()    
main()
