import time 

def mergesort(data,low,high,Getdata,sp):

	if low < high:
			
		mid = (high +low)// 2
		
		mergesort(data,low,mid,Getdata,sp)

		mergesort(data,mid+1,high,Getdata,sp)

		merge(data,low,mid,high,Getdata,sp)


def merge(data,low,mid,high,Getdata,sp):

	Getdata(data,Color(len(data),low,mid,high))
	time.sleep(sp)
	la = data[low:mid+1]
	ra = data[mid+1:high+1]

	l = r = 0
	for i in range(low,high+1):
		if l < len(la) and r < len(ra):
			if la[l] < ra[r]:
				data[i] = la[l]
				l += 1
			else:
				data[i] = ra[r]
				r += 1
		elif l < len(la):
			data[i] = la[l]
			l += 1
		elif r < len(ra):
			data[i] = ra[r]
			r += 1
	Getdata(data,['green' if k >= low and k <= high else 'gray' for k in range(len(data))])
	time.sleep(sp)

def Color(len,low,mid,high):
	color = []
	for i in range(len):
		if i >= low and i <= high:
			if i <= mid:
				color.append('yellow')
			else:
				color.append('blue')
		else:
			color.append('gray')
	return color