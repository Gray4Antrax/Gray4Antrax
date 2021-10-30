speed = input('enter speed (mph) :')
speed = int(speed)

distance = input('enter distance (miles):')
distance = float(distance)

time = distance / speed

print('at', speed, 'mph, it will take')
print(time, 'hours to travel', distance, 'miles.')
