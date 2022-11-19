import sys

name = input('Name: ')
sex = input('Sex: ')
hour_of_day = input('Hour of day (0-23): ')

hour_of_day = int(hour_of_day)

text = ''

if 0 <= hour_of_day <= 9:
    text += 'Good morning, '
elif hour_of_day >= 10 and hour_of_day <= 17:
    text += "Good day, "
elif hour_of_day in range(18, 24):
    text += "Good evening, "
else:
    print('geh weg!')
    sys.exit(1)

if sex == 'm':
    text += 'Mr.'
elif sex == 'w':
    text += 'Mrs.'
else:
    print('geh weg!')
    sys.exit(1)

text += name
    
print(text)
