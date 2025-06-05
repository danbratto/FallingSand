import tkinter as tk
from array import array
from random import randint

ROW : int = 80
COL : int = 80
assert ROW == COL
LIST_LENGTH = ROW * COL
SIZE : int = 10
GRID_SIZE : int = ROW * COL
WINDOW_SIZE : str = '%dx%d' % (COL * SIZE + 5, ROW * SIZE + 5)
PLACEMENT_SIZE : int = 2

# Lets try a 1D array
# 0 to 1599
current_states = array('B', [0] * LIST_LENGTH)
future_states = array('B', [0] * LIST_LENGTH)

def place_box(e, current_states):
    x = int(e.x / SIZE) - PLACEMENT_SIZE // 2
    y = int(e.y / SIZE) - PLACEMENT_SIZE // 2

    for dy in range(PLACEMENT_SIZE):
        for dx in range(PLACEMENT_SIZE):
            xi = x + dx
            yi = y + dy
            if 0 <= xi < COL and 0 <= yi < ROW:
                idx = yi * COL + xi
                current_states[idx] = 1

    draw(current_states)


def draw(current_states):
    canvas.delete('all')
    for i, state in enumerate(current_states):
        if state == 1:
            canvas.create_rectangle(i % COL * SIZE, int(i / ROW) * SIZE, i % COL * SIZE + SIZE, int(i / ROW) * SIZE + SIZE, fill = 'white', outline = 'white')

def update_states(current_states, future_states):
    draw(current_states)

    for i in range(LIST_LENGTH):
        if current_states[i] == 1:
            UNDER = i + COL
            LEFT = i + COL - 1
            RIGHT = i + COL + 1
            
            if i + COL < LIST_LENGTH and current_states[UNDER] == 0:
                future_states[i] = 0
                future_states[UNDER] = 1
            elif i % COL != COL - 1 and i + COL + 1 < LIST_LENGTH and current_states[RIGHT] == 0:
                future_states[i] = 0
                future_states[RIGHT] = 1
            elif i % COL != 0 and i + COL - 1 < LIST_LENGTH and current_states[LEFT] == 0:
                future_states[i] = 0
                future_states[LEFT] = 1
            else:
                future_states[i] = 1
        
        
    for i in range(LIST_LENGTH):
        current_states[i] = future_states[i]

    canvas.after(15, update_states, current_states, future_states)

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Falling Sand')
    window.geometry(WINDOW_SIZE)

    canvas = tk.Canvas(
        window,
        width = COL * SIZE,
        height = ROW * SIZE,
        background = 'black'
    )

    canvas.bind('<Button-1>', lambda e: place_box(e, current_states))
    canvas.bind('<B1-Motion>', lambda e: place_box(e, current_states))
    canvas.pack(anchor = 'center', expand = True)
    update_states(current_states, future_states)

    window.mainloop()