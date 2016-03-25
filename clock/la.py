from canvas import *

#create_oval(10, 10, 50, 50, fill="#00ffff")
#create_oval(40, 10, 50, 50, fill="#ff0000")

for i in range(1, 10):
    create_oval(20+(i*5), 20+(i*30), 50+(i*5), 50+(i*30), fill='red')

complete()
