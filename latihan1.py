import random
a = 0
jumlah = int(input("Masukan jumlah n : "))
for x in range (0,jumlah):
	i = random.uniform(0.0, 0.5)
	a+=1
	print("Data Ke-",a,"=>",i)
