#! /usr/bin/env python3
#Jiu Jitsu Game

import random
import position_lists

position = ()

offense = {
    "takedowns": ["single leg", "double leg", "judo throw", "pull guard"],
    "closedguardbottom": ["hip-bump sweep", "kimura", "guillotine"],
    "closedguardtop": ["arm lock", "key lock", "cross choke"],
    "backmount": ["rear naked choke"]
}

defense = {
    "takedowns": ["sprawl", "pull guard"], 
    "closedguardbottom": ["shrimp", "cross arms by neck"],
    "closedguardtop": ["posture up and defend","stand up guard pass"],
    "backmount": ["rear naked choke defense", "turtle"],
    "tap": ["tap out"]
    
}

print("""
Welcome to the JiuJitsu Trainer. You are a white belt who is rolling with another white belt.
You will need to make decisions on how to attack and how to defend yourself. Since you are new, 
your options are limited and there is a good chance you may notbe able to accomplish the move that you 
decide to do. As you advance, you will be more successful.
""")

if input("Shall we begin?").lower() in ["y", "yes"]:
    print("Good! You bow as you enter the mat and you bow and shake your training partners hand.")
    print(position_lists.play_pos_top["a"] + " and " + position_lists.opp_pos_bot["a"])
    print("You both begin circling...")
    print
else:
    print("Oh, keep watching youtube and come back when you are ready.")
    exit
    
for description, move in offense.items():
    print(range("takedowns"))
    action = input("What do you do?") 
    

position = position_lists.play_pos_bot["a"] + " and " + position_lists.opp_pos_top["a"]
print(position)



# closed guard, I sit up on my opponent and now my options are
# 1) Hip-bump sweep 2) Kimura or 3) Guillotine
# difficulty of move may impact success - weighted against experience level

