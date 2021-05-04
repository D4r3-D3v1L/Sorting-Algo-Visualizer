import time
def bubbleSort(data,Getdata,sp):
	for i in range(len(data)):
		for j in range(len(data)-1):
			if data[j] > data[j+1]:
				data[j],data[j+1] = data[j+1],data[j]
				Getdata(data,['red' if i == j or i == j+1 else 'green' for i in range(len(data))])
				time.sleep(sp)
	Getdata(data,['red' for i in range(len(data))])
