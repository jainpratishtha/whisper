from flask import Flask, render_template,request
import run
import time
import json
import os
app = Flask(__name__)
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/demo")
def demo():
	return render_template("index2.html")

@app.route("/demofinal")
def demofinal():
	time.sleep(0.5)
	if run.run():
		with open('text.json', 'r') as f:
    			distros_dict = json.load(f)
		label = distros_dict['_text']
		return render_template('index3.html', label=label)
		
	else:
		return "Nhi Huva!!"


if __name__ == "__main__":
	app.run(debug=True)
