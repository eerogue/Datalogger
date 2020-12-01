import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from serial import Serial
import threading
import time
import sys
import redis
from datetime import datetime

print ("ErskaLogger 2020-1")

#port = '/dev/ttyACM0'
#ser = Serial(port , baudrate=115200, timeout=3)

start_time = datetime.now()
def millis():
    dt = datetime.now()-start_time
    ms = (dt.days*24*60*60 + dt.seconds)*1000+dt.microseconds / 1000.0  
    return ms

r = redis.StrictRedis(host='localhost', port=6379, db=1)  

#ser.reset_input_buffer()
#ser.readlines(5)

SPI0_PORT   = 0
SPI0_DEVICE = 0
mcp0 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI0_PORT, SPI0_DEVICE))

SPI1_PORT   = 0
SPI1_DEVICE = 1
mcp1 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI1_PORT, SPI1_DEVICE))

SPI2_PORT   = 1
SPI2_DEVICE = 0
mcp2 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI2_PORT, SPI2_DEVICE))

SPI3_PORT   = 1
SPI3_DEVICE = 1
mcp3 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI3_PORT, SPI3_DEVICE))

# Read all the ADC channel values in a list.
values0 = [0]*8
values1 = [0]*8
values2 = [0]*8
values3 = [0]*8

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


class Database:
    def __init__(self):
        self.value = 0

    def update(self):	
        print ("Start")
        #serdata = str(ser.readlines(1))
        #print(serdata1)

        #dataa1 = serdata.split(";")
        dataa2 = values0+values1+values2+values3
        
        #self.dataa1 = dataa1
        self.dataa2 = dataa2
        
        #print ("dataa1")
        
        keyms = float(time.time())
        #print ("%.3f" % keyms)
            
        try:
            # different for loop for same spi port devices because it is only way it works fast enough
            for i in range(8):
                # read channels = i
                values0[i] = mcp0.read_adc(i)
                values2[i] = mcp2.read_adc(i)
                
            for i in range(8):
                values1[i] = mcp1.read_adc(i)
                values3[i] = mcp3.read_adc(i)
            
            print(dataa2)
            
            csvdata1 = str(values0[0])
            csvdata2 = str(values0[1])
            csvdata3 = str(values0[2])
            csvdata4 = str(values0[3])
            csvdata5 = str(values0[4])
            csvdata6 = str(values0[5])
            csvdata7 = str(values0[6])
            csvdata8 = str(values0[7])
            csvdata9 = str(values1[0])
            csvdata10 = str(values1[1])
            csvdata11 = str(values1[2])
            csvdata12 = str(values1[3])
            csvdata13 = str(values1[4])
            csvdata14 = str(values1[5])
            csvdata15 = str(values1[6])
            csvdata16 = str(values1[7])
            csvdata17 = str(values2[0])
            csvdata18 = str(values2[1])
            csvdata19 = str(values2[2])
            csvdata20 = str(values2[3])
            """
            csvdata21 = str(dataa2[1])
            csvdata22 = str(dataa2[2])
            csvdata23 = str(dataa2[3])
            csvdata24 = str(dataa2[4])
            csvdata25 = str(dataa2[5])
            csvdata26 = str(dataa2[6])
            csvdata27 = str(dataa2[7])
            csvdata28 = str(dataa2[8])
            csvdata29 = str(dataa2[12])
            csvdata30 = str(dataa2[13])
            csvdata31 = str(dataa2[14])
            csvdata32 = str(dataa2[15])
            csvdata33 = str(dataa2[16])
            csvdata34 = str(dataa2[17])'
            """
        except:
            print ("When Shit hits the fan")    
        
        
        #read main boost pressure T1
        try:
            value = float(csvdata1)
            r.zadd(sensor1, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor1, {keyms: value})


        #read secondary boost pressure T2
        try:
            value = float(csvdata2)
            r.zadd(sensor2, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor2, {keyms: value})


        #read main drive pressure T1
        try:
            value = float(csvdata3)
        except:
            #print('sensor read failed')
            value = -999

        r.zadd(sensor3, {keyms: value})


        #read secondary drive pressure T2
        try:
            value = float(csvdata4)
            r.zadd(sensor4, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor4, {keyms: value})


        #read EGT cyl 1
        try:
            value = float(csvdata5)
            r.zadd(sensor5, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor5, {keyms: value})


        #read EGT cyl 2
        try:
            value = float(csvdata6)
            r.zadd(sensor6, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor6, {keyms: value})


        #read EGT cyl 3
        try:
            value = float(csvdata7)
            r.zadd(sensor7, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor7, {keyms: value})


        #read EGT cyl 4
        try:
            value = float(csvdata8)
            r.zadd(sensor8, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor8, {keyms: value})


        #read EGT cyl 5
        try:
            value = float(csvdata9)
            r.zadd(sensor9, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor9, {keyms: value})


        #read EGT cyl 6
        try:
            value = float(csvdata10)
            r.zadd(sensor10, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor10, {keyms: value})


        #read EGT hpturbo t1
        try:
            value = float(csvdata11)
            r.zadd(sensor11, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor11, {keyms: value})


        #read EGT lpturbo t2
        try:
            value = float(csvdata12)
            r.zadd(sensor12, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor12, {keyms: value})


        #read boost temperature 1
        try:
            value = float(csvdata13)
            r.zadd(sensor13, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor13, {keyms: value})


        #read boost temperature 2
        try:
            value = float(csvdata14)
            r.zadd(sensor14, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor14, {keyms: value})
        
        
        #read boost temperature 3
        try:
            value = float(csvdata15)
            r.zadd(sensor15, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor15, {keyms: value})


        #read oil pressure
        try:
            value = float(csvdata16)
            r.zadd(sensor16, {keyms: value})
        except:
            print('sensor read failed')
            value = -999
            r.zadd(sensor16, {keyms: value})
        
        
        #read oil temperature
        try:
            value = float(csvdata17)
            r.zadd(sensor17, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor17, {keyms: value})
        
        
        #read wg1 pwm
        try:
            value = float(csvdata18)
            r.zadd(sensor18, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor18, {keyms: value})
        
        
        #read wg2 pwm
        try:
            value = float(csvdata19)
            r.zadd(sensor19, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor19, {keyms: value})

        
        #read AFC position
        try:
            value = float(csvdata20)
            r.zadd(sensor20, {keyms: value})
        except:
            #print('sensor read failed')
            value = -999
            r.zadd(sensor20, {keyms: value})


        #print(values0,values1,values2,values3)
        time.sleep(0.01)



if __name__ == "__main__":
	print ("start main")
	while (True):
		database = Database()
		database.update()

