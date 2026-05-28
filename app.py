from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_email
app = Flask(__name__)

ENV = 'dev'

# 1. Setup Configurations First
if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:asimkhan7890@localhost:5432/lexus'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. Initialize Database with Configurations Ready
db = SQLAlchemy(app)

# 3. Define Models
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer  = db.Column(db.String(200), unique = True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments
# 4. Run the App at the Very End
if __name__ == '__main__':
    if ENV == 'dev':
        app.run(debug=True)
    else:
        app.run(debug=False)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '' or rating == '' or comments == '':
            return render_template('index.html' , message = "Please enter the required information")
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_email(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message="You have already submitted your feedback")


if __name__ == '__main__':
    app.run()
