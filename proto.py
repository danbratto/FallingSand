import tkinter as tk
from random import randint

width = 400
height = 400
box_size = 10

row = int(height / box_size)
col = int(width / box_size)

window = tk.Tk()
window.title('Falling Sand')
window.geometry(f'{width + 5}x{height + 4}')

canvas = tk.Canvas(
    window,
    width = width,
    height = height,
    background = 'black'
)

canvas.pack(
    anchor = tk.CENTER,
    expand = True
)

grid = list()
another_grid = list()
for i in range(row):
    grid.append([])
    another_grid.append([])
    for j in range(col):
        grid[i].append(0)
        another_grid[i].append(0)

def place_box(mouse, grid, box_size):
    x = int((mouse.x - (mouse.x % box_size)) / box_size)
    y = int((mouse.y - (mouse.y % box_size)) / box_size)
    grid[y][x] = 1

def draw_box(x, y, box_size):
    canvas.create_rectangle( x * box_size, y * box_size, x * box_size + box_size, y * box_size + box_size, fill = 'white' )


def update_grid(grid, another_grid, row, col, box_size):
    # Clear canvas
    canvas.delete('all')

    # Search grid and draw square
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                draw_box(j, i, box_size)
            if i < 39 and grid[i][j] == 1 and grid[i + 1][j] == 0:
                another_grid[i+1][j] = 1
                another_grid[i][j] = 0
            elif j < 39 and j > 0 and i < 39 and grid[i][j] == 1 and grid[i + 1][j + 1] == 0 and grid[i + 1][j - 1] == 0:
                coin = randint(0,1)
                if coin == 1:
                    another_grid[i + 1][j + 1] = 1
                    another_grid[i][j] = 0
                else:
                    another_grid[i + 1][j - 1] = 1
                    another_grid[i][j] = 0
            elif j < 39 and j > 0 and i < 39 and grid[i][j] == 1 and grid[i + 1][j + 1] == 0:
                another_grid[i + 1][j + 1] = 1
                another_grid[i][j] = 0
            elif j < 39 and j > 0 and i < 39 and grid[i][j] == 1 and grid[i + 1][j - 1] == 0:
                another_grid[i + 1][j - 1] = 1
                another_grid[i][j] = 0
            grid[i][j] = another_grid[i][j]
            

    window.after(50, update_grid, grid, another_grid, row, col, box_size)

canvas.bind('<B1-Motion>', lambda mouse: place_box(mouse, grid, box_size))
canvas.bind('<Button-1>', lambda mouse: place_box(mouse, grid, box_size))
canvas.bind('<ButtonRelease-1>', lambda mouse: print('Rleased'))

# Start the sycle
update_grid(grid, another_grid, row, col, box_size)

window.mainloop()