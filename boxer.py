# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 20:30:03 2025

@author: george burton
"""
#imports random to change outcomes and have multiple beginnings
import random 
#creates a charecter object as a base for each boxer 
class character:
    def __init__(self, name, health):
        self.name = name 
        self.health = health
        
    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name
    
    def set_health(self, health):
        self.health = health
        
    def set_name(self, name):
        self.name = name
        
    def get_char(self):
        return f"name {self.name}, health {self.health}"

#creates main loop with intro 
print('Welcome to boxer showdown!')  
while True:
    #sets up the player character
    name = input("what name do you want your character to be? ")
    char1 = character(name, 100)
    #sets up a loop to ask what difficulty is desired and handle if a difficulty entered is not valid
    while True:
        difficulty = input("What difficulty? (Easy, medium or hard): ").lower()
        if difficulty == "easy":
            comp = character("jerry", 20)
            break
        elif difficulty == "medium":
            comp = character("Jim", 60)
            break
        elif difficulty == "hard":
            comp = character("phil", 100)
            break
        else:
            print(f"difficulty cannot be {difficulty} must be easy, medium or hard")
    #prints stats to show player their health and their opponents starting health
    print(f"\nopponent's stats: {comp.get_char()}")
    print(f"your stats: {char1.get_char()}\n")
    print("controls:")
    print("1 = jab \n2 = cross \n3 = lead hook \n4 = rear hook \n5 = lead uppercut \n6 = rear uppercut\n")
    #uses conditional statements to start the match in a different way based on difficulty
    x = 0
    if difficulty == "hard":
        #uses random module to switch up the start so it isn't the same every time
        x = random.randint(1, 3)
        if x == 1:
            print(f"You stand in the corner waiting for the match to start, heart racing. You look at {comp.get_name()} holding his knuckles. Your trainer standing next to you on to the side of the ring. Crowd noise rises to a level you can't hear you're self think, the match is about to start. The ref enters the ring and heads to the middle, calls you and {comp.get_name()} to the center of the ring. the ref then says a few instructions that are mostly muffled out by the noises of the crowd, then you go to fist bump {comp.get_name()} and his arms are so stiff and strong that his arms don't move")
        elif x == 2:
            print(f"Sweat is dripping down your face the anticipation is so high, the crowd going wild, over the speakers you hear 'welcome to the arena today is a match against {char1.get_name()} in the right corner, and {comp.get_name()} in the left corner', the crowd gets louder, the ref looks at you and tels you to come to the middle of the rink along with {comp.get_name()} to get instructions. while you are there it is so loud you can barely hear the ref. You go for a the beginning fist bump while {comp.get_name()} just sits and stairs menicingly.")
        else:
            print(f'You stand in the hall way waiting to enter the arena, your hands shaking in anticipation, mind racing you hear the anouncer blair over the radio, entering on the east side of the arena {char1.get_name()} your trainer trailing behind you while you lightly jog in and hear loud metal over the speakers, and the crowd yelling out your name "{char1.get_name().upper()}, {char1.get_name().upper()}, {char1.get_name().upper()}", you finally feel a sense of normality and calmness unti the music shifts and the anouncer yells over the speakers again, "Entering on the west side of the ring is {comp.get_name().upper()}" The crowd goes wild and seems to shift fully the other way chanting "{comp.get_name().upper()}, {comp.get_name().upper()}, {comp.get_name().upper()}", once everything settles down a little the ref calls you over for the rules and instruction, after he describes the rules you go for the the fist bump and {comp.get_name()} hits your hands so hard your arms launch downward')
    if difficulty == "medium":
        x = random.randint(1, 3)
        