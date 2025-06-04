import tkinter as tk

print('Loading Game.')
grid = list()
for i in range(160):
    grid.append([])
    for j in range(160):
        grid[i].append(0)
print('Load Done.')
    
# if grid[x][y - 1] == 0:
#     grid[x][y] = 0
#     grid[x][y] = 1

# limits x: 800, y: 800


def draw_sand(x, y):
    #.append(canvas.create_rectangle(x, y, x + 5, y + 5, fill = 'white'))
    pass
    

def get_point(mouse, grid):
    grid_x = int( (mouse.x - (mouse.x % 5)) / 5 )
    grid_y = int( (mouse.y - (mouse.y % 5)) / 5 )
    can_x = (mouse.x - (mouse.x % 5))
    can_y = (mouse.y - (mouse.y % 5))
    if grid[grid_x][grid_y] == 0:
        grid[grid_x][grid_y] = canvas.create_rectangle(can_x, can_y, can_x+5, can_y+5, fill = 'white')

def update_sand(bunch_of_sand, grid):
    for i in range(160):
        for j in range(160):
            if grid[i][j] == 1 and grid[i][j + 1] == 0:
                grid[i][j] = 0
                grid[i][j + 1] = 1


window = tk.Tk()
window.title('Falling Sand')
window.geometry('900x900')

canvas = tk.Canvas(
    window,
    width = 800,
    height = 800,
    background = 'black'
)

canvas.pack(
    anchor = tk.CENTER,
    expand = True
)

canvas.bind('<B1-Motion>', lambda e: get_point(e, grid))
canvas.bind('<Button-1>', lambda e: get_point(e, grid))

window.mainloop()

# def create_grid(n):
#     grid = list()
#     for i in range(n):
#         grid.append([])
#         for j in range(n):
#             grid[i].append(0)
#     return grid

# x = None
# y = None
# grid = create_grid(100)

# def place_sand(mouse):
#     t0 = time.time_ns()
#     global x, y, grid
#     x = int((mouse.x - (mouse.x % 10)) / 10)
#     y = int((mouse.y - (mouse.y % 10)) / 10)

#     if x < 100 and y < 100 or x >= 0 and y >= 0:
#         grid[y][x] = 1
#     draw_sand()
#     print(f'{(time.time_ns() - t0)/1000000} ms')

# def draw_sand():
#     global grid, x, y
#     for row in range(100):
#         for col in range(100):
#             if grid[row][col] == 1:
#                 canvas.create_rectangle(x*10, y*10, (x*10)+10, (y*10)+10, fill = 'white')


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.geometry('1000x1000')
#     root.title('Falling Sand')

#     canvas = tk.Canvas(
#         root,
#         width = 1000,
#         height = 1000,
#         bg = 'black')

#     canvas.pack(
#         anchor = tk.CENTER,
#         expand = True)
    
#     canvas.bind('<B1-Motion>', place_sand)

#     root.mainloop()


# def place_sand(e):
#     global sands
#     x = e.x - (e.x % 10)
#     y = e.y - (e.y % 10)
#     sand_id = canvas.create_rectangle(x, y, x + 10, y + 10, fill = 'white')
#     sands[sand_id] = [x, y, x+10, y+10]

# def update_sand():
#     global sands
#     if len(sands) >= 1:
#         for sand_id in sands:
#             # canvas.coords(sand_id, (sands[sand_id][0], sands[sand_id][1] + 10), (sands[sand_id][2], sands[sand_id][3] + 10))
#             sands[sand_id][1] += 10
#             sands[sand_id][3] += 10
#             canvas.coords(sand_id, sands[sand_id][0], sands[sand_id][1], sands[sand_id][2], sands[sand_id][3])

#     canvas.after(500, update_sand)

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Falling Sands')

# canvas = tk.Canvas(root, width = 750, height = 500, bg = 'black')
# canvas.pack(anchor = tk.CENTER, expand = True)

# canvas.bind('<Button>', place_sand)

# root.after(500, update_sand)

# root.mainloop()