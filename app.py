from flask import Flask, render_template, url_for, request
import re
import functions.spell_correction as spell
import functions.text_classifier as classifier

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("spell.html")

@app.route('/classifier')
def classify():
	return render_template("classifier.html")

@app.route('/spell', methods=['POST'])
def process():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		results = spell.correct(raw_text)
	return render_template("spell.html", results=results,raw_text=raw_text)

@app.route('/classifier', methods=['POST'])
def classify2():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		results = classifier.BigClassifier(raw_text)
	return render_template("classifier.html", results=results,raw_text=raw_text)

if __name__ == '__main__':
	app.run(debug=True)	