# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:06:16 2015

@author:    Murmer The Code Ninja
Desc:       The game is to guess a string of x digits. Fewest attempts 
            is a better score.
Example:        
            secret = 1234
            1> 1222
            **
            2> 1232
            ***
            3> 1234
            Congratz you won in 3 attempts!
                
"""
import sys

# Main...
def main()
              
    secret = '1234'
    score = play(secret)
    checkHighscore(score)

# Functions 
def play(secret):
    '''Play the game and return the number of attempts (score)'''
    attempt = 1
    while True:
        
        print attempt, ">",    
        guess = raw_input()
        
        feedback = 0
        for idx, num in enumerate(guess):
            assert len(guess) == 4
            if num == secret[idx]: feedback += 1
        
        if feedback == 4:
            print "Congratz you won in %s attempts!" % (attempt)
            return attempt
        else:
            print feedback * '*'        
            
        attempt += 1
    
def checkHighscore(score):
    '''
    Check current score against highscores.txt and see if a new highscore 
    has been achieved
    '''
    # open highscores.txt
    # compare score to top three scores
    prompt =    'Zomg you\'ve achieved a new highscore! What would you like' 
                + ' the heralds to know you as? '    
    gamer_tag = raw_input(prompt)
    #write new highscore to document
    #save highscore


###############################
if __name__ == '__main__':
    main()