import random
import tkinter as tk
import time as v
m = tk.Tk()
r = tk.Tk()
r.title('Counting Seconds')
x=0
while x<9:
    button = tk.Button(r, text=random.randint(1,9), width=25, command=r.destroy)
    x=+1
    v.sleep(8)

button.pack()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )

   
m.mainloop()


