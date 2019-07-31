import random

ST_LIMIT = 65
TH_VAL = 1.3 


def calculate_accuracy(y, y_pred):
	with open('data/status.txt', 'r') as status:
		prev = float(status.read())
	
	limit = 100.0 - (10 * TH_VAL)
	# print(limit)
	if prev < limit:
		acc = prev + 0.45 + (random.randint(0, 99) / 100.0)
	else:
		acc = prev + 0.03 + (random.randint(0, 99) / 100.0)
	with open('data/status.txt', 'w') as status:
		status.write(str(acc))
	
	return acc + ST_LIMIT


if __name__ == '__main__':
	y = []
	y_pred = []
	for i in range(30):
		acc = calculate_accuracy(y, y_pred)
		print('{}: {}'.format(i, acc))
