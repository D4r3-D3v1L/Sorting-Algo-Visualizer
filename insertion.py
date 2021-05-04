import  time

def insertion_sort(data, Getdata, sp):
	for i in range(1,len(data)):
		key = data[i]
		j = i - 1
		while j >=0 and key < data[j]:
			data[j+1] = data[j]
			j -= 1
			Getdata(data,['red' if k == j or k == j+1 else 'green' for k in range(len(data))])
			time.sleep(sp)
		data[j+1] = key