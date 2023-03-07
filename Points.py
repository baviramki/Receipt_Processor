import json
import re
import datetime
import math


def Calculate_points(receipt):

	points = 0
	name = receipt['retailer']
	total = receipt['total']
	items = receipt['items']
	
	points += len(re.sub(r'\W+',"",name))
	if int(total.split(".")[1]) == 0:
		points +=50
	if float(total) % .25 == 0:
		points +=25
	date = datetime.datetime.strptime(receipt['purchaseDate'], "%Y-%m-%d")
	if (date.day) % 2 == 1:
		points += 6
	time = datetime.datetime.strptime(receipt['purchaseTime'], "%H:%M").time()
	if time >= datetime.time(14,0) and  time <= datetime.time(16,0):
		points += 10
	points += (len(items)//2)*5
	for each_item in receipt['items']:
		if len(each_item['shortDescription'].strip()) % 3 == 0:
			points += math.ceil(float(each_item['price'])*0.2)
	return points

	
	

	

	
	












