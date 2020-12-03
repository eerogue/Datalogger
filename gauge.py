import tkinter as tk
import tk_tools
import random_logger as rl

root = tk.Tk()

# Typical one-sided gauge that you might be expecting for a
# speedometer or tachometer.  Starts at zero and goes to
# max_value when full-scale.
speed_gauge = tk_tools.Gauge(root, height=180, width=320,
                             max_value=300,
                             label='speed', unit=' km/h',
                             bg='grey')
speed_gauge.grid(row=0, column=0, sticky='news')

tach_gauge = tk_tools.Gauge(root, height=180, width=320,
                            max_value=8000,
                            label='Taco Metri', unit=' RPM',
                            divisions=10)
tach_gauge.grid(row=1, column=0, sticky='news')

strange_gauge = tk_tools.Gauge(root, height=180, width=320,
                               max_value=10.2,
                               label='boost', unit=' Bar',
                               divisions=10, red=90, yellow=60)
strange_gauge.grid(row=2, column=0, sticky='news')

# The battery voltage gauge has a lower voltage limit and an
# upper voltage limit.  These are automatically created when
# one imposes values on red_low and yellow_low along with
# using the min_value.
batV_gauge = tk_tools.Gauge(root, height=180, width=320,
                            max_value=16, min_value=8,
                            label='Bat voltage', unit='V',
                            divisions=8, yellow=60, red=75, red_low=30, yellow_low=40)
batV_gauge.grid(row=0, column=1, sticky='news')

# Similar to the previous gauge with bi-directional, but shows an
# imbalanced configuration along with support for negative numbers.
batI_gauge = tk_tools.Gauge(root, height=180, width=300,
                            max_value=100, min_value=0,
                            label='Tps', unit='%',
                            divisions=14, yellow=80, red=90, red_low=20, yellow_low=30)
batI_gauge.grid(row=1, column=1, sticky='news')

# create the graph
graph0 = tk_tools.Graph(root, height=180, width=300,
                        x_min=0.0, x_max=100.0, x_tick=10.0,
                        y_min=0, y_max=1020, y_tick=200.0)
graph0.grid(row=0, column=2, sticky='news')

graph1 = tk_tools.Graph(root, height=180, width=300,
                        x_min=0.0, x_max=100.0, x_tick=10.0,
                        y_min=0, y_max=1020, y_tick=200.0)
graph1.grid(row=1, column=2, sticky='news')


x0 = []
x1 = []
y0 = [0]*10
y1 = [0]*10

for o in range(11):
    x0.append(o*10)
for o in range(11):
    x1.append(o*10)

line_0 = [(0,0)]*10
line_1 = [(0,0)]*10

def update_gauge():
    global rl, line_0, line_1, x0, y0, x1, y1

    graph0.draw_axes()
    graph1.draw_axes()

    database = rl.Database()
    database.update()
    dataa1 = database.dataa1
    dataa2 = database.dataa2

    y0.append(dataa1[1])

    if (len(y0) > 11):
        y0.pop(0)
    
    line_0 = [(x0[0],y0[0]), (x0[1],y0[1]), (x0[2],y0[2]), (x0[3],y0[3]), (x0[4],y0[4]), (x0[5],y0[5]), (x0[6],y0[6]), (x0[7],y0[7]), (x0[8],y0[8]), (x0[9],y0[9]), (x0[10],y0[10])]

    graph0.plot_line(line_0, color='blue')
    graph1.plot_line(line_0, color='blue')


    y1.append(dataa1[2])

    if (len(y1) > 11):
        y1.pop(0)
    
    line_1 = [(x1[0],y1[0]), (x1[1],y1[1]), (x1[2],y1[2]), (x1[3],y1[3]), (x1[4],y1[4]), (x1[5],y1[5]), (x1[6],y1[6]), (x1[7],y1[7]), (x1[8],y1[8]), (x1[9],y1[9]), (x1[10],y1[10])]

    graph1.plot_line(line_1, color='red')
    graph0.plot_line(line_1, color='red')


    # update the gauges according to their value
    speed_gauge.set_value(dataa2[1])
    tach_gauge.set_value(dataa2[2])
    strange_gauge.set_value(dataa1[1]/100)
    batV_gauge.set_value(dataa2[13]/1000)
    batI_gauge.set_value(dataa2[12])

    root.after(50, update_gauge)

if __name__ == '__main__':
    root.after(100, update_gauge)

    root.mainloop()
