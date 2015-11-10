# jiujitsugame
Interactive JiuJitsu Sparring Project

Goal
Build an interactive JiuJitsu sparring session

Progression:
Simple sparring situations between white belts
Rolling log of console output for training and debugging purposes
Weighted likelyhood of completion of move
Advanced belts with more options and weighted likelyhood of completion of moves with a higher complexity score
2 parts: Engine to do work and UI to take user input and output engine response
Website to host gameplay


Example situation during game play
# closed guard, I sit up on my opponent and now my options are
# 1) Hip-bump sweep 2) Kimura or 3) Guillotine
# difficulty of move may impact success - weighted against experience level
action = input("What do you do?")

#based on option

#state machine

#each opponant may be in a different state

#computer opponent does random with weighted preferences
#humans success is weighted

#provide an engine to do the work and a user interface that tells engine what user is doing
#rolling log of console output
