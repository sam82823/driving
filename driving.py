country = input('What is your contury: ')
age = input('How old are you: ')
age = int(age)
if country == 'Taiwan' or 'taiwan':
	if age >= 18:
		print('you can drive')
	else:
		print('No drive')
