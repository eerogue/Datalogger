from tkinter import *
import random
import time
from threading import Thread

master = Tk()

w = Canvas(master, width=1400, height=400)
w.pack()

x = []
y = [0]*151

for i in range (len(y)):
	x.append(10*i)

def piirustus():
	global x, y
	while True:
		yy = 0
		y.append(random.randint (0, 400))
		if (len(y) > 21):
			y.pop(0)
		xx = 0
		
		for i in range (len(x)):
						
			
			x1 = xx
			y1 = yy

			xx = x[i]
			yy = y[i]

			x2 = xx
			y2 = yy
			
			#print (x1, y1, x2, y2, i)
			w.create_line(x1, y1, x2, y2)
			
			x1 = x2
			y1 = y2

		time.sleep(0.05)
		w.delete('all')

def runit():
	master.mainloop()

t = Thread(target=piirustus, args=())
t.start()

runit()

