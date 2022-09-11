score = input("Enter Score: ")

try:
	s= float(score)
except Exception as e:
	print(e)

if s>1.00:
	print('Bigger than 1.0')
elif s<0.0:
	print('smaller than 0.0')
elif s>=0.9:
	print('A')
elif s>=0.8:
	print('B')
elif s>=0.7:
	print('C')
elif s>=0.6:
	print('D')
else:
	print('F')