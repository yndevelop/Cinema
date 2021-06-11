#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:07:54 2021

@author: user
"""

#create a database
films= {
        #film, age limit, tickets remaining
        "Dust of the earth":[3,5],
        "Ten Words":[18,5],
        "When the king was born":[5,2],
        "300 men to War":[20, 12]
        }


while True:
   
    choice = input("What film would you liked to watch? ").strip().title()
    
    if choice in films:
        
        #age input
        age = int(input("How old are you? ").strip())
        
        #check user age 
        if age >= films[choice][0]:
            
            #check the number of seats
            nums_seats = films[choice][1]
            
            if nums_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Salah, we are sold out!")
        else:
        
            print("You are too young to see the film")
        
    else:
        print("We don't have that film.... ")
    