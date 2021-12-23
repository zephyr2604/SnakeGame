import curses
from random import randint

#setup
curses.initscr()
win = curses.newwin(20,60,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#Snake and Food
snake = [(4,10),(4,9),(4,8)]
food = (10,20)

win.addch(food[0], food[1], '#')

#Logic
score = 0
ESC = 27
key = curses.KEY_RIGHT


while key != ESC:
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) //5 + len(snake) //10 % 120) #increase speed formula

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
        key = prev_key
 
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_RIGHT and prev_key != curses.KEY_LEFT:
        x = (x+1) % 58
        if x == 0: x = 1
    elif key == curses.KEY_LEFT and prev_key != curses.KEY_RIGHT:
        x -= 1
        if x == 0: x = 58
    elif key == curses.KEY_DOWN and prev_key != curses.KEY_UP:
        y = (y+1) % 18
        if y == 0: y = 1
    elif key == curses.KEY_UP and prev_key != curses.KEY_DOWN:
        y -= 1
        if y == 0: y = 18
    else:
        key = prev_key
        if key == curses.KEY_RIGHT:
            x = (x+1) % 58
            if x == 0: x = 1
        elif key == curses.KEY_LEFT:
            x -= 1
            if x == 0: x = 58
        elif key == curses.KEY_DOWN:
            y = (y+1) % 18
            if y == 0: y = 1
        elif key == curses.KEY_UP:
            y -= 1
            if y == 0: y = 18

    snake.insert(0,(y,x)) 

    #Check whether snake got the food
    if y == food[0] and x == food[1]:
        score += 1
        food = ()
        while food==():
            food = (randint(1,18),randint(1,58)) 
            for body in snake:
                if food == body:
                    food = ()
            if food == (): 
                continue
        win.addch(food[0], food[1], '#')
    else:
        last = snake.pop()
        win.addch(last[0],last[1],' ')

    #Check if Snake bit itself
    bite_ind = False
    for l in snake[1:]:
        if snake[0] == l:
            bite_ind = True
            break
    if bite_ind: break

    #Draw snake
    for c in snake:
        win.addch(c[0],c[1],'*')

curses.endwin
print(f"Final Score = {score}")