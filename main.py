import tkinter as tk

sands = {}

def place_sand(e):
    global sands
    x = e.x - (e.x % 10)
    y = e.y - (e.y % 10)
    sand_id = canvas.create_rectangle(x, y, x + 10, y + 10, fill = 'white')
    sands[sand_id] = [x, y, x+10, y+10]

def update_sand():
    global sands
    if len(sands) >= 1:
        for sand_id in sands:
            # canvas.coords(sand_id, (sands[sand_id][0], sands[sand_id][1] + 10), (sands[sand_id][2], sands[sand_id][3] + 10))
            sands[sand_id][1] += 10
            sands[sand_id][3] += 10
            canvas.coords(sand_id, sands[sand_id][0], sands[sand_id][1], sands[sand_id][2], sands[sand_id][3])

    canvas.after(500, update_sand)

root = tk.Tk()
root.geometry('800x600')
root.title('Falling Sands')

canvas = tk.Canvas(root, width = 750, height = 500, bg = 'black')
canvas.pack(anchor = tk.CENTER, expand = True)

canvas.bind('<Button>', place_sand)

root.after(500, update_sand)

root.mainloop()