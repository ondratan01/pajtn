
import time
import tkinter as tk
canvas = tk.Canvas(width=500, height=500)
canvas.pack()

xn=3
yn=3
xj=52
yj=52

# canvas.create_rectangle(3,3,52,52)
# canvas.create_rectangle(xn+17,yn+17,xj-47,yj-47)
# canvas.create_rectangle(xn+62,yn,xj+64,yj)
# canvas.create_rectangle(xn+62+17,yn+17,xj+64-47,yj-47)
# canvas.create_rectangle(200,20,200,250)

canvas.create_rectangle(100,205,300,255, fill="red")
canvas.create_rectangle(125,155,275,205, fill="orange")
canvas.create_rectangle(150,105,250,155, fill="yellow")


canvas.create_rectangle(125,55,275,105, fill="orange")
canvas.create_rectangle(100,5,300,55, fill="red")


canvas.create_rectangle(115,75,110,185,fill="black")
canvas.create_rectangle(285,75,290,185,fill="black")

canvas.create_rectangle(115,120,285,140,fill="black")




canvas.create_rectangle(100,300,280,400)
canvas.create_rectangle(145,300,175,400,fill="blue")
canvas.create_rectangle(100,335,280,365,fill="blue")

tk.mainloop()





