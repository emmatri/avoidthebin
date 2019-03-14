from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello_someone():
	return render_template("listit.html")

postcodearray = []


@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	postcode = form_data["postcode"]
	postcodearray.append(postcode)
	print postcode
	return "All OK"
	

app.run(debug=True)