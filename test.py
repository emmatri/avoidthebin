people = [{'food': u'Onion', 'name': 'Jess', 'postcode': u'EC1N 2TD'}, {'food': u'Banana', 'name': u'Ben', 'postcode': u'S12d'}, {'food': u'Cheese', 'name': 'Jess', 'postcode': u'EC1N 3TD'}, {'food': u'Onion', 'name': 'Tom', 'postcode': u'EP18 0FR'}]

def getuniquefood():
	i = 0
	x = []
	while i < len(people):
		if people[i]["food"] not in x:
			x.append(people[i]["food"])
		i += 1
	print x
	
getuniquefood()



# def getfood(food):
# 	i = 0
# 	while 

# getfood("food")



# def tryingone(food, people):
# 	y = [element for element in people if element['food'] == food]
# 	print y
# 	x = y[0]["food"]
# 	print x


# tryingone('Cheese', people)
