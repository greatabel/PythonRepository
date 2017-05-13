def CelsiusToFahrenheit(c):
	#保留2位小数
	return "%.2f" %(c * 1.8 + 32)

for i  in range(100):
	print("Cel=",i+1,"F=",CelsiusToFahrenheit(i+1))