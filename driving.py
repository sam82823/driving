country = input('What is your contury: ')
age = input('How old are you: ')
age = int(age)
if country == 'Taiwan' or country == 'taiwan':
	if age >= 18:
		print('you can drive')
	else:
		print('No drive')
elif country == 'US':
	if age >= 16:
		print('you can drive')
	else:
		print('NO drive')
else:
	print('only Taiwan or US')