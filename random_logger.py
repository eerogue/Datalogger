import threading
import time
import sys
#import redis
from datetime import datetime
import random

print ("ErskaLogger 2020-1")

start_time = datetime.now()
def millis():
    dt = datetime.now()-start_time
    ms = (dt.days*24*60*60 + dt.seconds)*1000+dt.microseconds / 1000.0  
    return ms

#r = redis.StrictRedis(host='localhost', port=6379, db=0)  

#interval between readings
interval = 200

#Name of lists
#from LOGGER
sensor1 = "boostpressureHPT1"
sensor2 = "boostpressureLPT2"
sensor3 = "drivepressureHPT1"
sensor4 = "drivepressureLPT2"
sensor5 = "egtcylinder1"
sensor6 = "egtcylinder2"
sensor7 = "egtcylinder3"
sensor8 = "egtcylinder4"
sensor9 = "egtcylinder5"
sensor10 = "egtcylinder6"
sensor11 = "egtHPT1"
sensor12 = "egtLPT2"
sensor13 = "boosttemperature1"
sensor14 = "boosttemperature2"
sensor15 = "boosttemperature3"
sensor16 = "oilpressure"
sensor17 = "oiltemperature"
sensor18 = 'wg1pwm'
sensor19 = 'wg2pwm'
sensor20 = "AFC position"

#from ATC
sensor21 = "carspeed"
sensor22 = "enginerpm"
sensor23 = "tps"
sensor24 = "gear"
sensor25 = "watertemp"
sensor26 = "atftemp"
sensor27 = "load"
sensor28 = "boost"
#drive presssure (included in datastream from atc, not used)
#boostlimit (included in datastream from atc, not used)
#pressure difference (included in datastream from atc, not used)
sensor29 = "n2speed"
sensor30 = "n3speed"
sensor31 = "evalgear"
sensor32 = "ratio"
sensor33 = "tcslip"
sensor34 = "battery"
#boost pwm (included in datastream from atc, not used)
#egt (included in datastream from atc, not used)

dataa1 = []
dataa2 = []


class Database:
	def __init__(self):
		self.value = 0

	def update(self):		

		print("start")

		dataa1 = [
		0,
		round(random.triangular(0, 1020, 550),1),
		round(random.triangular(0, 1020, 150),1),
		round(random.triangular(0, 1020, 400),1),
		round(random.triangular(0, 1020, 100),1),
		round(random.triangular(200, 1200, 700),1),
		round(random.triangular(200, 1200, 700),1),
		round(random.triangular(200, 1200, 700),1),
		round(random.triangular(200, 1200, 700),1),
		round(random.triangular(200, 1200, 700),1),
		round(random.triangular(200, 1200, 700),1),
		round(random.triangular(200, 1200, 850),1),
		round(random.triangular(200, 1200, 500),1),
		round(random.triangular(30, 400, 300),1),
		round(random.triangular(30, 400, 200),1),
		round(random.triangular(30, 400, 100),1),
		round(random.triangular(0, 1020, 550),1),
		round(random.triangular(50, 120, 90)),
		round(random.triangular(0, 100, 80)),
		0,
		0
		]
		dataa2 = [
		0,
		round(random.triangular(0, 300, 120)),
		round(random.triangular(500, 6500, 3500)),
		round(random.triangular(0, 100, 75)),
		round(random.triangular(0, 5, 4)),
		round(random.triangular(40, 120, 80)),
		round(random.triangular(0, 100, 50)),
		round(random.triangular(0, 1020, 550),1),
		round(random.triangular(0, 6000, 2500)),
		round(random.triangular(0, 6000, 2300)),
		round(random.triangular(0, 5, 4)),
		round(random.triangular(0, 10, 7)),
		round(random.triangular(0, 100, 50)),
		round(random.triangular(11000, 15000, 13000)),
		0
		]
		
		self.dataa1 = dataa1
		self.dataa2 = dataa2
		
		#print (dataa1[17])

		keyms = float(time.time())
		print (keyms)
		
		try:
			csvdata1 = str(dataa1[1])
			csvdata2 = str(dataa1[2])
			csvdata3 = str(dataa1[3])
			csvdata4 = str(dataa1[4])
			csvdata5 = str(dataa1[5])
			csvdata6 = str(dataa1[6])
			csvdata7 = str(dataa1[7])
			csvdata8 = str(dataa1[8])
			csvdata9 = str(dataa1[9])
			csvdata10 = str(dataa1[10])
			csvdata11 = str(dataa1[11])
			csvdata12 = str(dataa1[12])
			csvdata13 = str(dataa1[13])
			csvdata14 = str(dataa1[14])
			csvdata15 = str(dataa1[15])
			csvdata16 = str(dataa1[16])
			csvdata17 = str(dataa1[17])
			csvdata18 = str(dataa1[18])
			csvdata19 = str(dataa1[19])
			csvdata20 = str(dataa1[20])

			csvdata21 = str(dataa2[1])
			csvdata22 = str(dataa2[2])
			csvdata23 = str(dataa2[3])
			csvdata24 = str(dataa2[4])
			csvdata25 = str(dataa2[5])
			csvdata26 = str(dataa2[6])
			csvdata27 = str(dataa2[7])
			csvdata28 = str(dataa2[8])
			csvdata29 = str(dataa2[9])
			csvdata30 = str(dataa2[10])
			csvdata31 = str(dataa2[11])
			csvdata32 = str(dataa2[12])
			csvdata33 = str(dataa2[13])
			csvdata34 = str(dataa2[14])
		except:
			print (":(")

		#read main boost pressure 1)
		try:
			value = float(csvdata1)
			#r.zadd(sensor1, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor1, {keyms: value})


		#read secondary boost pressure T2
		try:
			value = float(csvdata2)
			#r.zadd(sensor2, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor2, {keyms: value})


		#read main drive pressure T1
		try:
			value = float(csvdata3)
		except:
			##print('sensor read failed')
			value = -999

		#r.zadd(sensor3, {keyms: value})


		#read secondary drive pressure T2
		try:
			value = float(csvdata4)
			#r.zadd(sensor4, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor4, {keyms: value})


		#read EGT cyl 1
		try:
			value = float(csvdata5)
			#r.zadd(sensor5, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor5, {keyms: value})


		#read EGT cyl 2
		try:
			value = float(csvdata6)
			#r.zadd(sensor6, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor6, {keyms: value})


		#read EGT cyl 3
		try:
			value = float(csvdata7)
			#r.zadd(sensor7, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor7, {keyms: value})


		#read EGT cyl 4
		try:
			value = float(csvdata8)
			#r.zadd(sensor8, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor8, {keyms: value})


		#read EGT cyl 5
		try:
			value = float(csvdata9)
			#r.zadd(sensor9, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor9, {keyms: value})


		#read EGT cyl 6
		try:
			value = float(csvdata10)
			#r.zadd(sensor10, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor10, {keyms: value})


		#read EGT hpturbo t1
		try:
			value = float(csvdata11)
			#r.zadd(sensor11, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor11, {keyms: value})


		#read EGT lpturbo t2
		try:
			value = float(csvdata12)
			#r.zadd(sensor12, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor12, {keyms: value})


		#read boost temperature 1
		try:
			value = float(csvdata13)
			#r.zadd(sensor13, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor13, {keyms: value})


		#read boost temperature 2
		try:
			value = float(csvdata14)
			#r.zadd(sensor14, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor14, {keyms: value})
		
		
		#read boost temperature 3
		try:
			value = float(csvdata15)
			#r.zadd(sensor15, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor15, {keyms: value})


		#read oil pressure
		try:
			value = float(csvdata16)
			#r.zadd(sensor16, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor16, {keyms: value})
		
		
		#read oil temperature
		try:
			value = float(csvdata17)
			#r.zadd(sensor17, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor17, {keyms: value})
		
		
		#read wg1 pwm
		try:
			value = float(csvdata18)
			#r.zadd(sensor18, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor18, {keyms: value})
		
		
		#read wg2 pwm
		try:
			value = float(csvdata19)
			#r.zadd(sensor19, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor19, {keyms: value})

		
		#read AFC position
		try:
			value = float(csvdata20)
			#r.zadd(sensor20, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor20, {keyms: value})


#------------------------------------------------------------------------------

		#read car speed
		try:
			value = float(csvdata21)
			#r.zadd(sensor21, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor21, {keyms: value})


		#read engine speed
		try:
			value = float(csvdata22)
			#r.zadd(sensor22, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor22, {keyms: value})


		#read tps
		try:
			value = float(csvdata23)
			#r.zadd(sensor23, {keyms: value})
			#print value
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor23, {keyms: value})


		#read gear
		try:
			value = float(csvdata24)
			#r.zadd(sensor24, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor24, {keyms: value})


		#read water temperature
		try:
			value = float(csvdata25)
			#r.zadd(sensor25, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor25, {keyms: value})


		#read atf temperature
		try:
			value = float(csvdata26)
			#r.zadd(sensor26, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor26, {keyms: value})


		#read load
		try:
			value = float(csvdata27)
			#r.zadd(sensor27, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor27, {keyms: value})


		#read boost pressure from atc
		try:
			value = float(csvdata28)
			#r.zadd(sensor28, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor28, {keyms: value})


		#read n2 speed
		try:
			value = float(csvdata29)
			#r.zadd(sensor29, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor29, {keyms: value})


		#read n3 speed
		try:
			value = float(csvdata30)
			#r.zadd(sensor30, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor30, {keyms: value})


		#read eval gear
		try:
			value = float(csvdata31)
			#r.zadd(sensor31, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor31, {keyms: value})


		#read gear ratio
		try:
			value = float(csvdata32)
			#r.zadd(sensor32, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor32, {keyms: value})


		#read tc slip
		try:
			value = float(csvdata33)
			#r.zadd(sensor33, {keyms: value})
		except:
			##print('sensor read failed')
			value = -999
			#r.zadd(sensor33, {keyms: value})


		#read battery voltage
		try:
			value = float(csvdata34)
			#r.zadd(sensor34, {keyms: value})
		except:
			#print('sensor read failed')
			value = -999
			#r.zadd(sensor34, {keyms: value})


		time.sleep(0.01)


if __name__ == "__main__":
	print ("start main")
	while (True):
		database = Database()
		database.update()



