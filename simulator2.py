import time

coins = 0
max = 10
point = 0

while True:
	print('')
	print('[1]: faire des point ',point,'/',max,'  [2]: ajouter max','[',max,']','  [3]: échange [argents: ',coins,']')
	print('')
	chois = input('Choisis: ')
	print('')
	if chois == '1':
			while point < max :
				point += 1
				print('point =',point)
				time.sleep(0.1)
	print('')
	if chois == '1':
		if point == max:
			print('coins max')
	if chois == '2':
		if coins == max:
			coins -= max
			max += 5
	if chois == '2':
		if coins > max:
			coins -= max
			max += 5
	if chois == '3':
			coins += point
			point = 0