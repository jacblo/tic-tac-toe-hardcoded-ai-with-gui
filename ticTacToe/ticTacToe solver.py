#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:11:36 2020

@author: y4
"""

import copy
import random


screen = [[0,0,0],
          [0,0,0],
          [0,0,0]]


def showScreen(screen=screen):
    print("\n"*2)
    show = ""
    for x in screen[0]:
        if x == 0:
            show+="   |"
        elif x == 1:
            show+=" x |"
        elif x == 2:
            show+=" o |"
    show=show[:-1]
    show+="\n-----------\n"
    for x in screen[1]:
        if x == 0:
            show+="   |"
        elif x == 1:
            show+=" x |"
        elif x == 2:
            show+=" o |"
    show=show[:-1]
    show+="\n-----------\n"
    for x in screen[2]:
        if x == 0:
            show+="   |"
        elif x == 1:
            show+=" x |"
        elif x == 2:
            show+=" o |"
    show=show[:-1]
    show=show+"\n"
    print(show)

def checkWinner(screen=screen):
    #x win
    if(screen[0][0]==1 and screen[0][1]==1 and screen[0][2]==1)    or    (screen[1][0]==1 and screen[1][1]==1 and screen[1][2]==1)    or    (screen[2][0]==1 and screen[2][1]==1 and screen[2][2]==1)         or        (screen[0][0]==1 and screen[1][1]==1 and screen[2][2]==1)     or    (screen[2][0]==1 and screen[1][1]==1 and screen[0][2]==1)        or        (screen[0][0]==1 and screen[1][0] == 1 and screen[2][0] == 1) or (screen[0][1]==1 and screen[1][1] == 1 and screen[2][1] == 1) or (screen[0][2]==1 and screen[1][2] == 1 and screen[2][2] == 2):
          return 1
    #o win
    elif(screen[0][0]==2 and screen[0][1]==2 and screen[0][2]==2)    or    (screen[1][0]==2 and screen[1][1]==2 and screen[1][2]==2)    or    (screen[2][0]==2 and screen[2][1]==2 and screen[2][2]==2)         or        (screen[0][0]==2 and screen[1][1]==2 and screen[2][2]==2)     or    (screen[2][0]==2 and screen[1][1]==2 and screen[0][2]==2)        or        (screen[0][0]==2 and screen[1][0] == 2 and screen[2][0] == 2) or (screen[0][1]==2 and screen[1][1] == 2 and screen[2][1] == 2) or (screen[0][2]==2 and screen[1][2] == 2 and screen[2][2] == 2):
          return 2
    else:
        count = 0
        for y in range(len(screen)):
            for x in range(len(screen[y])):
                if screen[y][x] != 0:
                    count += 1
        if count == 9:
            return 3
    return 0

def move(screen = screen,move = 0,player = 0):
    newScreen = copy.deepcopy(screen)
    pos = []
    if move == None:
        return newScreen
    if move <= 2:
        newScreen[2][move] = player
        pos = [2,move]
    elif move >=3 and move <= 5:
        newScreen[1][move-3] = player
        pos = [1,move-3]
    elif move >=6 and move <= 8:
        newScreen[0][move-6] = player
        pos = [0,move-6]
    if screen[pos[0]][pos[1]] == 0:
        return newScreen
    
    
    
def computerMove(screen,player=1):
    #check if first or second turn
    count = 0
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] != 0:
                count += 1
                pos = [y,x]
    if count == 1:
        if screen[1][1] != 0:
            return random.choice([0,1,2,3,5,6,7,8])
        else:
            val = [(pos[0]-2)*-1,(pos[1]-2)*-1]
            return 0 if val==[2,0] else 1 if val==[2,1] else 2 if val==[2,2] else 3 if val==[1,0] else 4 if val==[1,1] else 5 if val==[1,2] else 6 if val==[0,0] else 7 if val==[0,1] else 8 if val==[0,2] else None
    elif count == 0:
        return random.randint(0,8)
    
    #check if full
    elif count == 9:
        return None
    #if not then start algorythm
    choice = 0
    possibilities = []
    #check immediate next moves
    for place in range(9):
        #make move
        testScreen=copy.deepcopy(screen)
        testScreen = move(testScreen,place,player)
        if testScreen == None:
            continue
        result = checkWinner(testScreen)
        if result == player:
            choice = place
            return choice
        else:
            #all possible player moves
            for place2 in range(9):
                testScreen2=copy.deepcopy(testScreen)
                testScreen2 = move(testScreen2,place2,1 if player == 2 else 2)
                if testScreen2 == None:
                    continue
                result2 = checkWinner(testScreen2)
                if result2 == 1 if player == 2 else 2:
                    #save if player will win in a turn
                    #unless you can win first
                    for place3 in range(9):
                        testScreen3=copy.deepcopy(screen)
                        testScreen3 = move(testScreen3,place3,player)
                        if testScreen3 == None:
                            continue
                        result3 = checkWinner(testScreen3)
                        if result3 == player:
                            return place3
                    return place2
                else:
                    possibilities.append([place,testScreen2])
    #if nothing special then endless loop to find all other possible future games and choose fastest one
    for currentScreen in possibilities:
        for place in range(9):
            testScreen=copy.deepcopy(currentScreen[1])
            testScreen = move(testScreen,place,player)
            if testScreen == None:
                continue
            result = checkWinner(testScreen)
            if result == player:
                choice = currentScreen[0]
                break
            else:
                for place2 in range(9):
                    testScreen2=copy.deepcopy(testScreen)
                    testScreen2 = move(testScreen2,place2,1 if player == 2 else 2)
                    if testScreen2 == None:
                        continue
                    result2 = checkWinner(testScreen2)
                    if result2 == 1 if player == 2 else 2:
                        continue
                    else:
                        possibilities.append([currentScreen[0],testScreen2])
    #if you lost basically because there is no case to win
    if choice == 0:
        while True:
            testScreen = copy.deepcopy(screen)
            x = random.randint(0,8)
            if move(testScreen,x,player) != None:
                return x
    return choice









def plVpl(screen = screen):
    print("positions like numpad")
    player1 = 2 if "o" in input("player one do you want to be x or o?(x/o)").lower() else 1
    while True:
        while True:
            showScreen(screen)
            while True:
                movement = input("what position to place player 1?(1-9) ")
                try:int(movement) 
                except:print("not number try again")
                else:break
            nextScreen = move(screen,int(movement)-1,player1)
            if nextScreen == None:
                print("impossible move try again")
            else:
                screen = nextScreen
                break
        
        winner = checkWinner(screen)
        if winner != 0:
            showScreen(screen)
            if winner == 3:
                print("it was a tie")
                break
            print("player ",winner," has won!")
            break
        
        while True:
            showScreen(screen)
            while True:
                movement = input("what position to place player 2?(1-9) ")
                try:int(movement) 
                except:print("not number try again")
                else:break
            nextScreen = move(screen,int(movement)-1,1 if player1 == 2 else 2)
            if nextScreen == None:
                print("impossible move try again")
            else:
                screen = nextScreen
                break
            
        winner = checkWinner(screen)
        if winner != 0:
            showScreen(screen)
            print("player ",winner," has won!")
            break
        
        
        
        
    
def plVco(screen = screen):
    print("positions like numpad")
    player1 = 2 if "o" in input("player do you want to be x or o?(x/o) ").lower() else 1
    first = 1 if "c" in input("player first or computer?(p/c) ") else 2
    while True:
        if first == 1:
            showScreen(screen)
            computeMove = computerMove(screen,1 if player1 == 2 else 2)
            screen = move(screen,computeMove, 1 if player1 == 2 else 2)
            print("computer has gone")
            showScreen(screen)
            
            winner = checkWinner(screen)
            if winner != 0:
                showScreen(screen)
                if winner == player1:
                    print("player has won!")
                elif winner == 2 if player1 == 1 else 1:
                    print("computer has wone. you lose.")
                elif winner == 3:
                    print("it was a tie")
                break
        
        
        
        
        while True:
            print("your turn")
            showScreen(screen)
            while True:
                movement = input("what position to place player?(1-9) ")
                try:int(movement) 
                except:print("not number try again")
                else:break
            nextScreen = move(screen,int(movement)-1,player1)
            if nextScreen == None:
                print("impossible move try again")
            else:
                screen = nextScreen
                break
        
        winner = checkWinner(screen)
        if winner != 0:
            showScreen(screen)
            if winner == player1:
                print("player has won!")
            elif winner == 2 if player1 == 1 else 1:
                print("computer has wone. you lose.")
            elif winner == 3:
                print("it was a tie")
            break
        
        
        if first == 2:
            showScreen(screen)
            computeMove = computerMove(screen,1 if player1 == 2 else 2)
            screen = move(screen,computeMove, 1 if player1 == 2 else 2)
            print("computer has gone")
            showScreen(screen)
            
            winner = checkWinner(screen)
            if winner != 0:
                showScreen(screen)
                if winner == player1:
                    print("player has won!")
                elif winner == 2 if player1 == 1 else 1:
                    print("computer has wone. you lose.")
                elif winner == 3:
                    print("it was a tie")
                break
        

def coVco(screen = screen):
    while True:
        print("computer 1 turn")
        showScreen(screen)
        computeMove = computerMove(screen, 1)
        screen = move(screen,computeMove, 1)
        
        winner = checkWinner(screen)
        if winner != 0:
            showScreen(screen)
            if winner == 1:
                print("computer 1 has won!")
            elif winner == 2:
                print("computer 2 has won!")
            elif winner == 3:
                    print("it was a tie")
            break
        
        print("computer 2 turn")
        showScreen(screen)
        computeMove = computerMove(screen, 2)
        screen = move(screen,computeMove, 2)
        
        winner = checkWinner(screen)
        if winner != 0:
            showScreen(screen)
            if winner == 1:
                print("computer 1 has won!")
            elif winner == 2:
                print("computer 2 has won!")
            elif winner == 3:
                    print("it was a tie")
            break


def play():
    global screen
    while True:
        print("what type of game do you want to play?")
        choice = input("do you want to play computer vs computer if so type cvc.\notherwise do you want to play computer vs player? if so type cvp.\notherwise do you want to play player vs player if so type pvp.\n:").lower()
        if "cvc" in choice:
            coVco()
            break
        elif "cvp" in choice:
            plVco()
            break
        elif "pvp" in choice:
            plVpl()
            break
        else:
            print("not a choice try again.\n\n")
    input("press enter to quit ")


import tkinter
from tkinter import *

def choicePopup(choices,title):
    root = Tk()
    root.resizable(False,False)
    root.geometry("300x130")
    root.title(title)
    canvas = Canvas(root, width = 2, height = 1)
    var= StringVar(root)
    var.set(choices[0])
    w = OptionMenu(root, var, *choices)
    w.grid(row=0)
    w.config(font = ("MS Sans Serif", 20))
    w.config(height = 1, width = 20)
    def click(*args):
        root.destroy()
    btn = Button(root,text="OK", command=click, font = ("MS Sans Serif", 40));btn.grid(row=1);btn.config(height = 1, width = 10)
    root.bind('<Return>', click)
    root.mainloop()
    return var.get()

import pygame
from pygame.locals import *

startAgain=False
def playGUI():  
    global startAgain
    global screen
    symbolScreen = screen
    
    def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

    
    gameType = choicePopup(['player vs player', 'player vs computer', 'computer vs computer'],"Game type")
    
    boardImage = pygame.image.load("Link to tic tac toe graphics/board.png")
    xImage = pygame.image.load("Link to tic tac toe graphics/x.png")
    oImage = pygame.image.load("Link to tic tac toe graphics/o.png")
    oxImages = [oImage,xImage]
    
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    
    positions = [[30,690],[360,690],[690,690]   ,    [30,360],[360,360],[690,360]   ,   [30,30],[360,30],[690,30]]
    sizeSprites=280
    class Button(pygame.sprite.Sprite):
        def __init__(self,pos,numpadPos):
            self.pos = pos
            self.surf = pygame.Surface([0,0])
            self.rect = pygame.Rect(pos[0], pos[1], sizeSprites, sizeSprites)
            self.image = self.surf
            self.set = False
            self.numpadPos = numpadPos
    buttons=[Button(positions[0],0),Button(positions[1],1),Button(positions[2],2),Button(positions[3],3),Button(positions[4],4),Button(positions[5],5),Button(positions[6],6),Button(positions[7],7),Button(positions[8],8)]
    
    class againOrQuit(pygame.sprite.Sprite):
        def __init__(self,pos,size:list,text:str):
            self.pos = pos
            self.size = size
            self.surf = pygame.Surface([0,0])
            self.surf.fill((50,50,50))
            self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
            self.image = pygame.transform.scale(pygame.image.load("Link to tic tac toe graphics/button.png"),size)
            self.text = text
    
    if gameType == 'player vs player':
        player1 = 1 if choicePopup(["o","x"],"x or o") == "o" else 2
        currentPlayer = player1
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')
        font = pygame.font.Font('freesansbold.ttf', 40)
        font2 = pygame.font.Font('freesansbold.ttf', 100)
        font3 = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render('Turn player '+("X" if player1 == 2 else "O"), True, (0,0,0))
        textRect = pygame.Rect(373, 5, 200, 50)
        otherSprites = []
        again = againOrQuit([150,500],[300,300],"Again")
        quitProgram = againOrQuit([550,500],[300,300],"Quit")
        done = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if again.rect.collidepoint(x,y) and done:
                        running = False
                        startAgain = True
                        return
                    elif quitProgram.rect.collidepoint(x,y) and done:
                        running = False
                        pygame.quit()
                        import sys;sys.exit()
                    for button in buttons:
                        if button.rect.collidepoint(x,y) and not button.set:
                            button.set = True
                            button.image = oxImages[currentPlayer-1]
                            text=font.render('Turn player '+("X" if currentPlayer == 1 else "O"), True, (0,0,0))
                            symbolScreen = move(symbolScreen, button.numpadPos, currentPlayer)
                            winner = checkWinner(symbolScreen)
                            if winner != 0:
                                if winner == 3:
                                    for button2 in buttons:
                                        button2.set = True
                                    surf = pygame.Surface((1000,1000))
                                    surf.fill((255,255,255,100))
                                    surf.set_colorkey(-1, RLEACCEL)
                                    otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                                    text = font2.render('It was a tie', True, (0,0,0))
                                    textRect = text.get_rect()
                                    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-20)
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([again.image,again.rect,[False]])
                                    text = font3.render(again.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = again.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                                    text = font3.render(quitProgram.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = quitProgram.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    done = True
                                else:
                                    for button2 in buttons:
                                        button2.set = True
                                    surf = pygame.Surface((1000,1000))
                                    surf.fill((255,255,255,100))
                                    surf.set_colorkey(-1, RLEACCEL)
                                    otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                                    if winner == 2:
                                        text = font2.render('Player X has won!', True, (0,0,0))
                                    else:
                                        text = font2.render('Player O has won!',True, (0,0,0))
                                    textRect = text.get_rect()
                                    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-20)
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([again.image,again.rect,[False]])
                                    text = font3.render(again.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = again.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                                    text = font3.render(quitProgram.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = quitProgram.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    done = True
                            currentPlayer = 1 if currentPlayer == 2 else 2
                # Check for KEYDOWN event
                if event.type == KEYDOWN:
                    # If the Esc key is pressed, then exit the main loop
                    if event.key == K_ESCAPE:
                        running = False
                        pygame.quit()
                        import sys;sys.exit()
                # Check for QUIT event. If QUIT, then set running to false.
                elif event.type == QUIT:
                    running = False
                    pygame.quit()
                    import sys;sys.exit()
            pressed_keys = pygame.key.get_pressed()
            screen.fill((200,200,200))
            screen.blit(boardImage, [0, 0])
            for button in buttons:
                screen.blit(button.image,button.pos)
            screen.blit(text,textRect)
            for sprite,pos,alpha in otherSprites:
                if not alpha[0]:
                    screen.blit(sprite,pos)
                else:
                    blit_alpha(screen, sprite, pos, alpha[1])
            pygame.display.flip()
        pygame.quit()
    if gameType == 'player vs computer':
        player1 = 1 if choicePopup(["o","x"],"x or o") == "o" else 2
        currentPlayer = player1
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')
        font = pygame.font.Font('freesansbold.ttf', 40)
        font2 = pygame.font.Font('freesansbold.ttf', 100)
        font3 = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render('Turn '+("X" if player1 == 2 else "O"), True, (0,0,0))
        textRect = pygame.Rect(373, 5, 200, 50)
        otherSprites = []
        again = againOrQuit([150,500],[300,300],"Again")
        quitProgram = againOrQuit([550,500],[300,300],"Quit")
        done = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if again.rect.collidepoint(x,y) and done:
                        running = False
                        startAgain = True
                        return
                    elif quitProgram.rect.collidepoint(x,y) and done:
                        running = False
                        pygame.quit()
                        import sys;sys.exit()
                    for button in buttons:
                        if button.rect.collidepoint(x,y) and not button.set:
                            button.set = True
                            button.image = oxImages[currentPlayer-1]
                            text=font.render('Turn '+("X" if currentPlayer == 1 else "O"), True, (0,0,0))
                            symbolScreen = move(symbolScreen, button.numpadPos, currentPlayer)
                            winner = checkWinner(symbolScreen)
                            if winner != 0:
                                if winner == 3:
                                    for button2 in buttons:
                                        button2.set = True
                                    surf = pygame.Surface((1000,1000))
                                    surf.fill((255,255,255,100))
                                    surf.set_colorkey(-1, RLEACCEL)
                                    otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                                    text = font2.render('It was a tie', True, (0,0,0))
                                    textRect = text.get_rect()
                                    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-20)
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([again.image,again.rect,[False]])
                                    text = font3.render(again.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = again.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                                    text = font3.render(quitProgram.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = quitProgram.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    done = True
                                else:
                                    for button2 in buttons:
                                        button2.set = True
                                    surf = pygame.Surface((1000,1000))
                                    surf.fill((255,255,255,100))
                                    surf.set_colorkey(-1, RLEACCEL)
                                    otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                                    if winner == 1 if player1 == 2 else 2:
                                        text = font2.render('Computer has won.', True, (0,0,0))
                                    else:
                                        text = font2.render('Player has won!',True, (0,0,0))
                                    textRect = text.get_rect()
                                    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-80)
                                    otherSprites.append([text,textRect,[False]])
                                    if winner == 1 if player1 == 2 else 2:
                                        text = font2.render('You lose.', True, (0,0,0))
                                    textRect = text.get_rect()
                                    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2+10)
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([again.image,again.rect,[False]])
                                    text = font3.render(again.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = again.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                                    text = font3.render(quitProgram.text, True, (10,10,10))
                                    textRect = text.get_rect()
                                    textRect.center = quitProgram.rect.center
                                    otherSprites.append([text,textRect,[False]])
                                    done = True
                            currentPlayer = 1 if currentPlayer == 2 else 2
                            
                            if not done:
                                #computer move
                                computeMove = computerMove(symbolScreen,currentPlayer)
                                symbolScreen = move(symbolScreen,computeMove,currentPlayer)
                                if computeMove != None:
                                    buttons[computeMove].image = oxImages[currentPlayer-1]
                                winner = checkWinner(symbolScreen)
                                if winner != 0:
                                    if winner == 3:
                                        for button2 in buttons:
                                            button2.set = True
                                        surf = pygame.Surface((1000,1000))
                                        surf.fill((255,255,255,100))
                                        surf.set_colorkey(-1, RLEACCEL)
                                        otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                                        text = font2.render('It was a tie', True, (0,0,0))
                                        textRect = text.get_rect()
                                        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-20)
                                        otherSprites.append([text,textRect,[False]])
                                        otherSprites.append([again.image,again.rect,[False]])
                                        text = font3.render(again.text, True, (10,10,10))
                                        textRect = text.get_rect()
                                        textRect.center = again.rect.center
                                        otherSprites.append([text,textRect,[False]])
                                        otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                                        text = font3.render(quitProgram.text, True, (10,10,10))
                                        textRect = text.get_rect()
                                        textRect.center = quitProgram.rect.center
                                        otherSprites.append([text,textRect,[False]])
                                        done = True
                                    else:
                                        for button2 in buttons:
                                            button2.set = True
                                        surf = pygame.Surface((1000,1000))
                                        surf.fill((255,255,255,100))
                                        surf.set_colorkey(-1, RLEACCEL)
                                        otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                                        if winner == 1 if player1 == 2 else 2:
                                            text = font2.render('Computer has won.', True, (0,0,0))
                                        else:
                                            text = font2.render('Player has won!',True, (0,0,0))
                                        textRect = text.get_rect()
                                        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-80)
                                        otherSprites.append([text,textRect,[False]])
                                        if winner == 1 if player1 == 2 else 2:
                                            text = font2.render('You lose.', True, (0,0,0))
                                        textRect = text.get_rect()
                                        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2+10)
                                        otherSprites.append([text,textRect,[False]])
                                        otherSprites.append([again.image,again.rect,[False]])
                                        text = font3.render(again.text, True, (10,10,10))
                                        textRect = text.get_rect()
                                        textRect.center = again.rect.center
                                        otherSprites.append([text,textRect,[False]])
                                        otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                                        text = font3.render(quitProgram.text, True, (10,10,10))
                                        textRect = text.get_rect()
                                        textRect.center = quitProgram.rect.center
                                        otherSprites.append([text,textRect,[False]])
                                        done = True
                                currentPlayer = 1 if currentPlayer == 2 else 2
            
            screen.fill((200,200,200))
            screen.blit(boardImage, [0, 0])
            for button in buttons:
                screen.blit(button.image,button.pos)
            screen.blit(text,textRect)
            for sprite,pos,alpha in otherSprites:
                if not alpha[0]:
                    screen.blit(sprite,pos)
                else:
                    blit_alpha(screen, sprite, pos, alpha[1])
            pygame.display.flip()
        pygame.quit()

    if gameType == 'computer vs computer':
        player1 = 2
        currentPlayer = player1
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')
        font = pygame.font.Font('freesansbold.ttf', 40)
        font2 = pygame.font.Font('freesansbold.ttf', 80)
        font3 = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render('Turn '+("X" if player1 == 2 else "O"), True, (0,0,0))
        textRect = pygame.Rect(373, 5, 200, 50)
        otherSprites = []
        again = againOrQuit([150,500],[300,300],"Again")
        quitProgram = againOrQuit([550,500],[300,300],"Quit")
        done = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if again.rect.collidepoint(x,y) and done:
                        running = False
                        startAgain = True
                        return
                    elif quitProgram.rect.collidepoint(x,y) and done:
                        running = False
                        pygame.quit()
                        import sys;sys.exit()
                            
                # Check for KEYDOWN event
                if event.type == KEYDOWN:
                    # If the Esc key is pressed, then exit the main loop
                    if event.key == K_ESCAPE:
                        running = False
                        pygame.quit()
                        import sys;sys.exit()
                # Check for QUIT event. If QUIT, then set running to false.
                elif event.type == QUIT:
                    running = False
                    pygame.quit()
                    import sys;sys.exit()
            pressed_keys = pygame.key.get_pressed()
            computeMove = computerMove(symbolScreen,currentPlayer)
            symbolScreen = move(symbolScreen,computeMove, currentPlayer)
            if computeMove != None:
                buttons[computeMove].image=oxImages[currentPlayer-1]
            
            winner = checkWinner(symbolScreen)
            if winner != 0 and not done:
                done = True
                if winner == 3:
                    for button2 in buttons:
                        button2.set = True
                    surf = pygame.Surface((1000,1000))
                    surf.fill((255,255,255,100))
                    surf.set_colorkey(-1, RLEACCEL)
                    otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                    text = font2.render('It was a tie', True, (0,0,0))
                    textRect = text.get_rect()
                    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-20)
                    otherSprites.append([text,textRect,[False]])
                    otherSprites.append([again.image,again.rect,[False]])
                    text = font3.render(again.text, True, (10,10,10))
                    textRect = text.get_rect()
                    textRect.center = again.rect.center
                    otherSprites.append([text,textRect,[False]])
                    otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                    text = font3.render(quitProgram.text, True, (10,10,10))
                    textRect = text.get_rect()
                    textRect.center = quitProgram.rect.center
                    otherSprites.append([text,textRect,[False]])
                    done = True
                else:
                    for button2 in buttons:
                        button2.set = True
                    surf = pygame.Surface((1000,1000))
                    surf.fill((255,255,255,100))
                    surf.set_colorkey(-1, RLEACCEL)
                    otherSprites.append([surf,pygame.Rect(0, 0, 10000, 1000),[True,200]])
                    if winner == 2:
                        text = font2.render('Computer X has won!', True, (0,0,0))
                    else:
                        text = font2.render('Computer O has won!',True, (0,0,0))
                    textRect = text.get_rect()
                    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-20)
                    otherSprites.append([text,textRect,[False]])
                    otherSprites.append([again.image,again.rect,[False]])
                    text = font3.render(again.text, True, (10,10,10))
                    textRect = text.get_rect()
                    textRect.center = again.rect.center
                    otherSprites.append([text,textRect,[False]])
                    otherSprites.append([quitProgram.image,quitProgram.rect,[False]])
                    text = font3.render(quitProgram.text, True, (10,10,10))
                    textRect = text.get_rect()
                    textRect.center = quitProgram.rect.center
                    otherSprites.append([text,textRect,[False]])
                    done = True
            currentPlayer = 1 if currentPlayer == 2 else 2
            screen.fill((200,200,200))
            screen.blit(boardImage, [0, 0])
            for button in buttons:
                screen.blit(button.image,button.pos)
            screen.blit(text,textRect)
            for sprite,pos,alpha in otherSprites:
                if not alpha[0]:
                    screen.blit(sprite,pos)
                else:
                    blit_alpha(screen, sprite, pos, alpha[1])
            pygame.display.flip()
        pygame.quit()

while True:
    screen =[[0,0,0],
             [0,0,0],
             [0,0,0]]
    playGUI()