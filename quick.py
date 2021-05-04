import time

def partition(data ,low, high, Getdata, sp):
	i = low
	pivot = data[high]

	Getdata(data, Color(len(data),low,high,i,i))
	time.sleep(sp)
	for j in range(low,high):
		if data[j] < pivot:
			Getdata(data, Color(len(data),low,high,i,j,True))
			time.sleep(sp)
			data[j],data[i] = data[i],data[j]
			i += 1
		Getdata(data, Color(len(data),low,high,i,j))
		time.sleep(sp)

	Getdata(data, Color(len(data),low,high,i,high,True))
	time.sleep(sp)
	data[i],data[high] = data[high], data[i]	

	return i



def quciksort(data, low, high, Getdata, sp):

	if low < high :

		midpt = partition(data,low,high,Getdata,sp)

		quciksort(data,low,midpt -1,Getdata,sp)

		quciksort(data,midpt+1,high,Getdata,sp)
	return data

def Color(len,low,high,i,cur,swapp = False):
	color = []

	for k in range(len):
		if k >=low and k <= high:
			color.append('gray')
		else:
			color.append('orange')
		if k == high:
			color[k] = 'blue'
		elif k == i:
			color[k] = 'pink'
		elif k == cur:
			color[k] = 'yellow'
	if swapp:
		if k == i or k == cur:
			color[k] = 'black'

	return color