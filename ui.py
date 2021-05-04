from tkinter import *
from tkinter import ttk
from bubble import bubbleSort
import random
from merge import mergesort
from quick import quciksort
from insertion import insertion_sort
from select_sort import selection

app = Tk()

app.title("AlgoVizualizer")

app.maxsize(1200,900)
app.config(bg="black")

algo = StringVar()

data = []

def Getdata(data,colors):
	canvas.delete('all')
	canvas_height = 600
	canvas_width = 900
	bar_width = canvas_width / (len(data)+1)
	offset = 30
	space = 10
	mod_data = [i/max(data) for i in data]

	for i,height in enumerate(mod_data):
		x0 = i * bar_width + offset + space
		y0 = canvas_height - height*550

		x1 = (i+1) * bar_width + offset 
		y1 = canvas_height

		canvas.create_rectangle(x0,y0,x1,y1,fill=colors[i])
		canvas.create_text(x0+2,y0,anchor=SW,text = str(data[i]))
	app.update_idletasks()
def Create():
	global data

	# print("Selected one "+ algo.get())
	minval = int(min_inp.get())
	maxval = int(max_inp.get())
	size = int(size_inp.get())

	data = []
	for i in range(size):
		data.append(random.randrange(minval,maxval+1))
	Getdata(data,['green' for i in range(len(data))])
def StartAlgo():
	global data
	sp = float(speed.get())

	a = algo.get()

	if a == 'Merge Sort':
		mergesort(data,0,len(data)-1,Getdata,sp)
	elif a == 'Quick Sort':
		quciksort(data,0,len(data)-1,Getdata,sp)
	elif a == 'Bubble Sort':
		bubbleSort(data,Getdata,sp)
	elif a == 'Selection Sort':
		selection(data,Getdata,sp)
	elif a == 'Insertion Sort':
		insertion_sort(data,Getdata,sp)
	
	Getdata(data,['blue' for i in range(len(data))])

header = Frame(app , width = 900 , height = 300, bg = "grey")
header.grid(row=0, column=0, padx=10 , pady=5)

canvas = Canvas(app, width = 900, height = 600, bg = 'white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(header, text = "Sort type :",bg = 'grey').grid(row=0,column=0,padx=10,pady=5,sticky=W)
menu = ttk.Combobox(header, textvariable=algo,values=['Selection Sort','Bubble Sort','Merge Sort','Insertion Sort','Quick Sort'])
menu.grid(row=0,column=1,padx=5,pady=5)
menu.current(0)

speed = Scale(header,from_= 0.1, to=2.0,length=200,digits=2,resolution=0.1,orient=HORIZONTAL,label="Select Speed")
speed.grid(row=0,column=2,padx=5,pady=5)

Button(header,text='Start',bg='red',command=StartAlgo).grid(row=0,column=3,padx=5,pady=5)

size_inp =  Scale(header,from_= 3, to=30,length=200,resolution=1,orient=HORIZONTAL,label="Size")
size_inp.grid(row=1,column=0,padx=5,pady=5)

min_inp =   Scale(header,from_= 0, to=10,length=200,resolution=1,orient=HORIZONTAL,label="Minimum")
min_inp.grid(row=1,column=1,padx=5,pady=5)

max_inp =  Scale(header,from_= 10, to=100,length=200,resolution=1,orient=HORIZONTAL,label="Maximum")
max_inp.grid(row=1,column=2,padx=5,pady=5)

Button(header,text='Create',bg='orange',command=Create).grid(row=1,column=3,padx=5,pady=5)

app.mainloop()