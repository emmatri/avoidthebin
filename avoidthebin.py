from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/list")
def listit():
	return render_template("listit.html")

userarray = []

people = [{'food': u'Onion', 'name': 'Jess', 'postcode': u'EC1N 2TD'}, {'food': u'Banana', 'name': u'Ben', 'postcode': u'S12d'}, {'food': u'Cheese', 'name': 'Jess', 'postcode': u'EC1N 3TD'}, {'food': u'Onion', 'name': 'Tom', 'postcode': u'EP18 0FR'}]

def getuniquefood():
	i = 0
	x = []
	while i < len(people):
		if people[i]["food"] not in x:
			x.append(people[i]["food"])
		i += 1
	return x

listfood = getuniquefood()
print listfood

@app.route("/listed")
def listed():
	return render_template('listed.html', listed = listfood)


# @app.route("/listedtwo", methods=["POST"])
# def list_it():
# 	form_data = request.form
# 	name = form_data["name"]
# 	food = form_data["food"]
# 	postcode = form_data["postcode"]

# 	userarray.append([{"name": name, "food": food,"postcode": postcode}])
# 	print postcode
# 	print name
# 	print food
# 	print userarray
# 	uniquefood = []
# 	return "Listed OK" + food


app.run(debug=True)