# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:45:41 2015

@author: mike
"""

rooms = {
            1 : {'name' : 'Hall',
                 'east' : 2,
                 'south': 3}, 
            2 : {'name' : 'Bedroom',
                 'west' : 1,
                 'south': 4},
            3 : {'name' : 'Tower',
                 'north': 1},
            4 : {'name' : 'Dressing Room',
                 'north': 2}
        }

currentRoom = 1
print("You are in room: ", currentRoom)
print("This is the ", rooms[currentRoom]['name'])
move = input(">")
currentRoom = rooms[currentRoom][move]
print("you are now in room : ", currentRoom)
print("This is the ", rooms[currentRoom]['name'])

