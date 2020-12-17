from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150), nullable=False)
	email = db.Column(db.String(150), nullable=False)
	question = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Comment %r>' % self.id


@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html")


@app.route('/face-masks')
def mask():
	return render_template("mask.html")


@app.route('/physical-distancing')
def distancing():
	return render_template("distance.html")


@app.route('/hand-hygiene')
def hand():
	return render_template("hand.html")


@app.route('/daily-health-check')
def check():
	return render_template("check.html")

@app.route('/daily')
def daily():
	return render_template("daily.html")

@app.route('/testing')
def testing():
	return render_template("testing.html")


@app.route('/comment', methods=['POST', 'GET'])
def comment():
	if request.method == "POST":
		name = request.form['name']
		email = request.form['email']
		question = request.form['question']

		comment = Comment(name=name, email=email, question=question)

		try:
			db.session.add(comment)
			db.session.commit()
			return redirect('/')
		except:
			return "During process of sending your question there was an error!"
	else:
		return render_template("comment.html")


if __name__ == "__main__":
	app.run(debug=True)