cm = 170

# calculate the number of feet
feet = int(cm // 30.48)

# calculate the remaining inches
inches = int((cm % 30.48) / 2.54)

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
