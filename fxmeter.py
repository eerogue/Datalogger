# fxmeter.py
# class to show a gauge or panel meter
# by Jeff Salvo
# inspired by meter.py from Roger Woollett
import tkinter as tk
import tkinter.font as tkf
    
import math

class MeterTemp(tk.Canvas):
    def __init__(self,master,*args,**kwargs):
        tk.Canvas.__init__(self,master,*args,**kwargs)
        
        self.layoutparams()
        self.graphics()
        self.createhand()
        self.setrange()
        
    def layoutparams(self):
        # set parameters that control the layout
        height = int(self['height'])
        width = int(self['width'])
        
        # find a square that fits in the window
        if(height*2 > width):
            side = width
        else:
            side = height*2
        
        # set axis for hand
        self.centrex = side/2
        self.centrey = side/2
        
        # standard with of lines
        self.linewidth = 2
        
        # outer radius for dial
        self.radius = int(0.40*float(side))
        
        # set width of bezel
        self.bezel = self.radius/15
        self.bezelcolour1 = '#c0c0c0'
        self.bezelcolour2 = '#808080'
    
        # set lengths of ticks and hand
        self.majortick = self.radius/8
        self.minortick = self.majortick/2
        self.handlen = self.radius - self.majortick - self.bezel - 1
        self.blobrad = self.handlen/6
             
    def graphics(self):
        """ create the static components """
        self.create_oval(self.centrex-self.radius
        ,self.centrey-self.radius
        ,self.centrex+self.radius
        ,self.centrey+self.radius
        ,width = self.bezel
        ,outline = self.bezelcolour2)
        
        self.create_oval(self.centrex-self.radius - self.bezel
        ,self.centrey-self.radius - self.bezel
        ,self.centrex+self.radius + self.bezel
        ,self.centrey+self.radius + self.bezel
        ,width = self.bezel
        ,outline = self.bezelcolour1)
        # create the graduations
        for deg in range(-60,40,6):
            self.createtick(deg, self.minortick, 'blue')
        for deg in range(41,140,6):
            self.createtick(deg,self.minortick, 'green')
        for deg in range(141,241,6):
            self.createtick(deg,self.minortick, 'red')
        for deg in range(-60,241,30):
            self.createtick(deg,self.majortick, 'black')
        
    def createhand(self):
        # create text display
        self.textid = self.create_text(self.centrex
        ,self.centrey + 3*self.blobrad
        ,fill = 'red'
        ,font = tkf.Font(size = -int(2*self.majortick)))
        
        # create moving and changeable bits (needle)
        self.handidOil = self.create_line(self.centrex,self.centrey
        ,self.centrex - self.handlen,self.centrey
        ,width = 2*self.linewidth
        ,fill = 'red')
        
        # create the blob (center of the meter)
        self.blobid = self.create_oval(self.centrex - self.blobrad
        ,self.centrey - self.blobrad
        ,self.centrex + self.blobrad
        ,self.centrey + self.blobrad
        ,outline = 'black', fill = 'black')
        
    def createtick(self,angle,length, color = 'black'):
        # helper function to create one tick
        rad = math.radians(angle)
        cos = math.cos(rad)
        sin = math.sin(rad)
        radius = self.radius - self.bezel
        self.create_line(self.centrex - radius*cos
        ,self.centrey - radius*sin
        ,self.centrex - (radius - length)*cos
        ,self.centrey - (radius - length)*sin
        ,width = self.linewidth, fill = color)
        
    def setrange(self,start = 0, end=100):
        self.start = start
        self.range = end - start
        
    def set(self,valueOil):
        # call this to set the hand
        # convert value to range 0,100
        degOil = 300*(valueOil - self.start)/self.range - 240
        
        self.itemconfigure(self.textid,text = str(valueOil))
        radOil = math.radians(degOil)
        # reposition hands
        self.coords(self.handidOil,self.centrex,self.centrey
        ,self.centrex+self.handlen*math.cos(radOil), self.centrey+self.handlen*math.sin(radOil))
        
    def blob(self,colour):
        # call this to change the colour of the blob
        self.itemconfigure(self.blobid,fill = colour,outline = colour)

class Meterframe(tk.Frame):
    """Create the meter frame"""
    #define global variables.
    valueOil = 0
    
    """Create the frame object"""
    def __init__(self,master,text = '',scale=(0,100),*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)

        width = kwargs.get('width',100)
        self.meter = MeterTemp(self,height = width,width = width)
        self.meter.setrange(scale[0],scale[1])
        self.meter.pack()
        self.scalemin = scale[0]
        self.scalemax = scale[1]
                
        tk.Label(self,text=text).pack()
        self.setmeter(0)

        """tk.Scale(self,length = width,from_ = scale[0], to = scale[1]
        ,orient = tk.HORIZONTAL
        ,command = self.setmeter).pack()"""

    def setmeter(self,valueOil):
        #Modify the value, change the blob color depend on the value.
        '''valueOil = int(valueOil)'''
        self.meter.set(valueOil)
        plage = self.scalemax - self.scalemin
        #Debug print
        #print('min %s ; max %s ; value %s ; plage %s' % (self.scalemin, self.scalemax, value, plage))
        
        if (valueOil < (plage)/3 + self.scalemin):
            self.meter.blob('blue')

        # create a timer function to update the values with self.meter.set.
    def updateMeterTimer(self):
        #Fade over time
        self.var.set(self.var.get())
        self.after(20, self.updateMeterTimer)

