import tkinter as tk
from random import randint

ROW = 100
COL = 100
assert ROW == COL
LIST_LENGTH = ROW * COL
SIZE = 5
WINDOW_SIZE = '%dx%d' % (COL * SIZE + 5, ROW * SIZE + 5)
PLACEMENT_SIZE = 5

# Each cell: (state, box_id)
cells = [(0, None) for _ in range(LIST_LENGTH)]
future_cells = [(0, None) for _ in range(LIST_LENGTH)]

placing = False
placing_job = None

def place_box(e):
    x = int(e.x / SIZE) - PLACEMENT_SIZE // 2
    y = int(e.y / SIZE) - PLACEMENT_SIZE // 2

    for dy in range(PLACEMENT_SIZE):
        for dx in range(PLACEMENT_SIZE):
            xi = x + dx
            yi = y + dy
            if 0 <= xi < COL and 0 <= yi < ROW:
                idx = yi * COL + xi
                state, box_id = cells[idx]
                if state == 0:
                    # Draw new box
                    x0, y0 = xi * SIZE, yi * SIZE
                    new_id = canvas.create_rectangle(x0, y0, x0 + SIZE, y0 + SIZE, fill='white', outline='white')
                    cells[idx] = (1, new_id)

def update_states():
    # Copy current states to future_cells
    for i in range(LIST_LENGTH):
        state, box_id = cells[i]
        future_cells[i] = (state, box_id)

    for i in range(LIST_LENGTH):
        state, box_id = cells[i]
        if state == 1:
            UNDER = i + COL
            LEFT = i + COL - 1
            RIGHT = i + COL + 1

            moved = False
            if UNDER < LIST_LENGTH and cells[UNDER][0] == 0:
                move_cell(i, UNDER)
                moved = True
            elif (i % COL != COL - 1 and i % COL != 0 and
                  RIGHT < LIST_LENGTH and LEFT < LIST_LENGTH and
                  cells[RIGHT][0] == 0 and cells[LEFT][0] == 0):
                if randint(0, 1) == 0:
                    move_cell(i, RIGHT)
                else:
                    move_cell(i, LEFT)
                moved = True
            elif i % COL != COL - 1 and RIGHT < LIST_LENGTH and cells[RIGHT][0] == 0:
                move_cell(i, RIGHT)
                moved = True
            elif i % COL != 0 and LEFT < LIST_LENGTH and cells[LEFT][0] == 0:
                move_cell(i, LEFT)
                moved = True
            if not moved:
                future_cells[i] = (1, box_id)

    # Apply changes and update canvas
    for i in range(LIST_LENGTH):
        curr_state, curr_id = cells[i]
        next_state, next_id = future_cells[i]
        if curr_state != next_state:
            xi, yi = i % COL, i // COL
            if next_state == 1:
                # Draw new box
                x0, y0 = xi * SIZE, yi * SIZE
                new_id = canvas.create_rectangle(x0, y0, x0 + SIZE, y0 + SIZE, fill='white', outline='white')
                cells[i] = (1, new_id)
            else:
                # Remove box
                if curr_id is not None:
                    canvas.delete(curr_id)
                cells[i] = (0, None)
        else:
            cells[i] = (next_state, next_id)

    canvas.after(5, update_states)

def move_cell(src, dst):
    # Move state and box_id from src to dst in future_cells
    state, box_id = cells[src]
    future_cells[src] = (0, None)
    future_cells[dst] = (1, box_id)

def start_placing(event):
    global placing, placing_job
    placing = True
    place_box(event)
    placing_job = canvas.after(20, lambda: continuous_place(event))

def continuous_place(event):
    global placing, placing_job
    if placing:
        place_box(event)
        placing_job = canvas.after(20, lambda: continuous_place(event))

# Stop placing when mouse move and button is released
def stop_placing(event):
    global placing, placing_job
    placing = False
    if placing_job is not None:
        canvas.after_cancel(placing_job)
        placing_job = None

def motion_place(event):
    stop_placing(event)
    place_box(event)

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Falling Sand')
    window.geometry(WINDOW_SIZE)

    canvas = tk.Canvas(
        window,
        width=COL * SIZE,
        height=ROW * SIZE,
        background='black'
    )

    canvas.bind('<ButtonPress-1>', start_placing)
    canvas.bind('<B1-Motion>', motion_place)
    canvas.bind('<ButtonRelease-1>', stop_placing)
    canvas.pack(anchor='center', expand=True)
    update_states()

    window.mainloop()