import turtle
import random
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X ,SIZE_Y)

turtle.penup()

SQUARE_SIZE =20
START_LENGTH=6

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake =turtle.clone()
snake.shape('square')

turtle.hideturtle()

for i in range (START_LENGTH):
    x_pos=snake.pos() [0]
    y_pos=snake.pos() [1]

    x_pos+=SQUARE_SIZE
    snake.goto(x_pos,y_pos)
    my_pos=(x_pos,y_pos)
    pos_list.append(my_pos)

    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

UP_ARROW='Up'
LEFT_ARROW='left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
TIME_STEP=100

SPACEBAR = 'space'

direction=UP

UP= 0
DOWN=1
LEFT=2
RIGHT=3

def up ():
     global direction
     direction=UP
     move_snake()
     print('you pressed the up key!')
def down ():
    global direction
    direction=DOWN
    move_snake()
    print('you pressed the  down key!')

def left ():
    global direction
    direction = LEFT
    move_snake()
    print ('you pressed the left key!')

def right():
    global direction
    direction = RIGHT
    move_snake()
    print('you pressed the right key!')

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()

                
    
     
















