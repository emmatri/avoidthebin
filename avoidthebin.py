from flask import Flask, render_template, request
from flask_navigation import Navigation

app = Flask("AvoidTheBin")
nav = Navigation(app)

nav.Bar('top', [
	nav.Item('Home', 'home'),
    nav.Item('List It', 'listit'),
    nav.Item('Listed', 'listed'),
])

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/listit")
def listit():
	return render_template("listit.html")

users = []

def getuniquefood():
	i = 0
	x = []
	print len(users)
	while i < len(users):
		if users[i]["food"] not in x:
			x.append(users[i]["food"])
		i += 1
	return x

@app.route("/listed")
def listed():
	return render_template('listed.html', listed = getuniquefood())


@app.route("/added", methods=["POST"])
def list_it():
	form_data = request.form
	name = form_data["name"]
	food = form_data["food"]
	postcode = form_data["postcode"]
	users.append({"name": name, "food": food,"postcode": postcode})
	return render_template('itemadded.html',  user = form_data)

@app.route("/Login")
def Login():return render_template('Login.html')

@app.route('/Login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('Login.html', error=error)



app.run(debug=True)
