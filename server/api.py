from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.Text, primary_key=True)
    shares = db.Column(db.Integer, nullable=False)
    price =  db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f'{self.name} {self.shares} {self.price}'
    
def user_serializer(self):
     return {
            'name': self.name,
            'shares': self.shares,
            'price': self.price
        }

@app.route('/api', methods=['GET'])
def index():
   return jsonify([*map(user_serializer, User.query.all())])

@app.route('/api/buy_or_sell', methods=['POST'])
def buy_or_sell():
    request_data = json.loads(request.data)
    print(request_data)
    print(request_data['amount'])
    user = User.query.filter_by(name = 'init_user').first()
    user.shares -= request_data['amount']
    db.session.commit()
    return {200: "OK"}
   

if __name__ == '__main__':
    app.run(debug=True)
    if not (db.engine.has_table('user')):
        db.create_all()
        test = User(name='test',shares=100 , price=50)
        db.session.add(test)
        db.session.commit()