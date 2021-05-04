import time 

def selection(data,Getdata,sp):
	for i in range(len(data)):
		min_ind = i
		Getdata(data,['green' for i in range(len(data))])
		for j in range(i+1,len(data)):
			if data[min_ind] > data[j]:
				min_ind = j
				Getdata(data,['yellow' if x == min_ind else 'green' for x in range(len(data))])
				time.sleep(sp)

			
		data[i],data[min_ind] = data[min_ind] , data[i]
		Getdata(data,['blue' if x <= i  else 'green' for x in range(len(data))])
		time.sleep(sp)