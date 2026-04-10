import time
import tkinter as tk
canvas = tk.Canvas(width=500, height=500)

canvas.pack()

canvas.create_rectangle(2,2,200,100)
canvas.create_rectangle(2,2,66,100, fill="green")
canvas.create_rectangle(133,2,200,100, fill="orange")
# canvas.create_rectangle(125,155,275,205, fill="orange")
# canvas.create_rectangle(150,105,250,155, fill="yellow")


canvas.create_rectangle(2,150,200,280, fill="gray")

canvas.create_rectangle(12,160,22,270,fill="blue")
canvas.create_rectangle(12,160,190,170, fill="red")
canvas.create_rectangle(190,160,180,270,fill="blue")
canvas.create_rectangle(22,260,190,270, fill="red")

canvas.create_rectangle(2,350,202,460,fill="gray")
canvas.create_rectangle(27,370,67,410,fill="red")
canvas.create_rectangle(37,380,77,420,fill="yellow")
canvas.create_rectangle(47,390,87,430,fill="blue")
canvas.create_rectangle(57,400,97,440,fill="green")


x=250
y=2

j=100
d=20
t=80
c=40
p=60
canvas.create_rectangle(x,y,x+j,y+j,fill="red")
canvas.create_rectangle(x+d,y+d,x+t,y+t,fill="blue")
canvas.create_rectangle(x+c,y+c,x+p,y+p,fill="white")


# , outline=""
canvas.create_rectangle(250,200,400,290,fill="red")
canvas.create_rectangle(250,230,400,260,fill="white")

canvas.create_rectangle(280,200,310,290,fill="white")
canvas.create_rectangle(251,231,400,260,fill="white", outline="")

canvas.create_rectangle(251,237,400,253,fill="blue", outline="")
canvas.create_rectangle(287,201,303,290,fill="blue", outline="")


tk.mainloop()