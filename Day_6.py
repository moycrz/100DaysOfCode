#REEBORG'S WORLD

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

### Maze ###

## Funciones ## 
# The functions were defined on the website.

## Codigo ##
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def left_is_clear():
    turn_left()
    front_is_clear()
    

while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_right()
            
    elif wall_in_front():
        if wall_on_right():
            turn_left()
        elif right_is_clear():
            turn_right()
            
    else:
        move()