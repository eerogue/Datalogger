import tkinter as tk
import fxmeter as m
import random
from threading import Thread
import time
import random_logger as te


class Mainframe(tk.Frame):
	def __init__(self,master,*args,**kwargs):
		tk.Frame.__init__(self,master,*args,**kwargs)
		print("initializing")
		#gauge setup 
		self.tempframe1 = m.Meterframe(self,text = 'EGT T1 C',width = 200,scale = (0,1200))
		self.tempframe1.grid(row = 0,column = 0)

		self.tempframe2 = m.Meterframe(self,text = 'EGT T2 C',width = 200,scale = (0,1200))
		self.tempframe2.grid(row = 0,column = 1)

		self.tempframe3 = m.Meterframe(self,text = 'EGT Cyl Avg C',width = 200,scale = (0,1200))
		self.tempframe3.grid(row = 1,column = 0)


		
		self.pressframe1 = m.Meterframe(self,text = 'Boost T1 Kpa',width = 200,scale = (0,1020))
		self.pressframe1.grid(row = 0,column = 3)

		self.pressframe2 = m.Meterframe(self,text = 'Boost T2 Kpa',width = 200,scale = (0,1020))
		self.pressframe2.grid(row = 0,column = 4)

		self.pressframe3 = m.Meterframe(self,text = 'Drive T1 Kpa',width = 200,scale = (0,1020))
		self.pressframe3.grid(row = 1,column = 3)

		self.pressframe4 = m.Meterframe(self,text = 'Drive T2 Kpa',width = 200,scale = (0,1020))
		self.pressframe4.grid(row = 1,column = 4)
		
		self.pressframe5 = m.Meterframe(self,text = 'Oil Press Kpa',width = 200,scale = (0,1020))
		self.pressframe5.grid(row = 1,column = 1)

		

		#self.speedframe1 = m.Meterframe(self,text = 'Engine RPM',width = 300,scale = (0,6500))
		#self.speedframe1.grid(row = 0,column = 2)

		#self.speedframe2 = m.Meterframe(self,text = 'Speed KM/H',width = 300,scale = (0,300))
		#self.speedframe2.grid(row = 1,column = 2)

		#button setup
		tk.Button(self,text = 'Quit',width = 15,command = self.stop) \
		.grid(row = 3,column = 0)


		self._thread = Thread(target = self.updateValues)
		self._thread.start()
	
	

	#gauge value update
	def updateValues(self):
		self._active = True
		while(self._active):
			database = te.Database()
			database.update()
			dataa1 = database.dataa1
			dataa2 = database.dataa2
			
			c1 = float(dataa1[5])
			c2 = float(dataa1[6])
			c3 = float(dataa1[7])
			c4 = float(dataa1[8])
			c5 = float(dataa1[9])
			c6 = float(dataa1[10])
			avec = (c1+c2+c3+c4+c5+c6)/6

			data1 = float(dataa1[11])
			data2 = float(dataa1[12])
			data3 = avec

			self.tempframe1.setmeter(data1)
			self.tempframe2.setmeter(data2)
			self.tempframe3.setmeter(int (data3))
			
			data4 = float(dataa1[17])
			data5 = float(dataa2[5])
			data6 = float(dataa1[3])
			data7 = float(dataa1[4])
			data8 = float(dataa1[16])

			self.pressframe1.setmeter(data4)
			self.pressframe2.setmeter(data5)
			self.pressframe3.setmeter(data6)
			self.pressframe4.setmeter(data7)
			self.pressframe5.setmeter(data8)
			
			#data9 = float(dataa2[2])
			#data10 = float(dataa2[1])

			#self.speedframe1.setmeter(data9)
			#self.speedframe2.setmeter(data10)

			#print raw_data1
			time.sleep(0.02)   

	def stop(self):
		print('bye bye')
		self._active = False
		self.master.destroy()

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title('Try fxMeter')
		Mainframe(self).pack()
		
App().mainloop()
